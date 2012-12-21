#!/usr/bin/env python

# This program is licensed under the GPL; see LICENSE for details.

# Server that demonstrates shared memory between threads.  The server will
# accept requests for one of several names, which it returns to a client.
# The list of names is shared among all client threads.  Each request also
# returns the numbers of times that client has requested a name; this
# information is *not* shared among threads.

import optparse
import select
import socket
import string
import sys
import threading
import time

# For this import to work, you need to put this line
#
# export PYTHONPATH=/home/zappala/Web
#
# in your .bashrc and then login again
from shared import *

class Server(threading.Thread):
    """ Server thread

    The server accepts clients, which can then send requests using
    the message:

          lookup <i>

    where <i> is some number greater than 1.  If the server has a name
    corresponding to that number, it returns the name using the message:

          name <mytotal> <sharedtotal> <name>

    where <mytotal> is the number of times this client has requested a
    name during this session, <sharedtotal> is the number of times all
    clients have requested a name, and <name> is the name (may have
    spaces).  If there is no name matching the requested number, the
    server returns:

          error

    All messages are terminated by a newline.

    The server exits whenever any input is entered on standard input.
    The server will wait for any client threads to terminate before
    exiting.
    """
    def __init__(self):
        """ Initialize the server thread.  Default hostname is this machine's
        hostname.
        """
        threading.Thread.__init__(self)
        self.host = socket.gethostname()
        self.port = 0
        self.backlog = 5
        self.size = 1024
        self.server = None

    def run(self):
        """ Run the server thread.  This thread will accept new client
        connections and spawn a client thread for each one.
        """
        self.do_options()
        self.open_socket()
        input = [self.server,sys.stdin]
        running = 1
        while running:
            try:
                # Listen to both standard input and the server socket.  If
                # any input is received on standard input (triggered by
                # the enter key), ignore it and quit the server.
                inputready,outputready,exceptready = select.select(input,[],[])
            except socket.error, (value,reason):
                if self.server:
                    self.server.close()
                print "Socket Error: " + reason
                sys.exit(1)
            except KeyboardInterrupt:
                # handle a keyboard interrupt (control-c) by killing server
                # gracefully
                if self.server:
                    self.server.close()
                print "Killing Server"
                sys.exit(1)

            for s in inputready:

                if s == self.server:
                    # handle the server socket
                    w = Worker(self.server.accept())
                    w.start()

                elif s == sys.stdin:
                    # handle standard input
                    junk = sys.stdin.readline()
                    running = 0 

        # close all threads
        self.server.close()
        for c in threading.enumerate():
            if c != threading.currentThread():
                c.join()

    def parse_options(self):
        """ Parse options.  User can use '-p' to specify a port to
        listen on.  Use the '-d' option to print debugging information.
        """
        parser = optparse.OptionParser(usage = "%prog [options]",
                                       version = "%prog 0.1")
        parser.add_option("-p", "--port", type="int",dest="port",
                          metavar="PORT",default=0,
                          help="port number for the server")
        parser.add_option("-d","--debug",action="store_true",dest="debug",
                          default=False,
                          help="print debugging information")

        return parser.parse_args()

    def do_options(self):
        """ Parse options.  See above for valid options.
        """
        (options, args) = self.parse_options()

        self.port = options.port
        shared.verbose = options.debug

    def open_socket(self):
        """ Open the server socket, binding it to the given host and
        port.  Check for socket exceptions and exit if one occurs.
        """
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            self.server.bind((self.host,self.port))
            if self.port == 0:
                host,port = self.server.getsockname()
                print "Server was assigned port %d" % (port)
            self.server.listen(5)
        except socket.error, (value,reason):
            if self.server:
                self.server.close()
            print "Could not open socket: " + reason
            sys.exit(1)

class Worker(threading.Thread):
    """ Client thread.  Initialized with a socket.  Handles any input
    from a client and exits when socket is closed.
    """
    def __init__(self,(client,address)):
        """ Initialize client thread with a socket. """
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024
        self.data = ""
        self.running = True
        self.count = 0

    def run(self):
        """ Run the client thread, parsing any messages and returning
        appropriate responses.
        """
        while self.running:
            try:
                data = self.client.recv(self.size)
            except socket.error, (value,reason):
                data = None
            if data:
                self.parse_data(data)
            else:
                self.running = False
        self.client.close()

    def parse_data(self,data):
        """ Parse data to see if we have received a complete message.
        Handle any complete messages and save the rest of the data
        for next time.
        """
        # get cached data
        data = self.data + data
        self.data = ""

        # find end of message
        end = string.find(data,"\n")
        if (end < 0):
            # cache the data we have
            self.data = data
        else:
            # parse the message
            self.parse_message(data[:end])
            if self.running:
                start = end + 1
                if start < len(data):
                    self.parse_data(data[start:])

    def parse_message(self,message):
        """ Parse a complete message """
        string.rstrip(message)
        parts = string.split(message)
        if parts == []:
            return
        if parts[0] == "lookup":
            if len(parts) >=2:
                # validate ID
                try:
                    id = int(parts[1])
                except:
                    print "Couldn't convert ",parts[1]
                    return self.error()

                self.count += 1
                count,name = shared.lookup(id)
                if count == "":
                    print "Lookup error"
                    return self.error()
                # send name message
                message = "name " + str(self.count) + " " + str(count) + " " + name + "\n"
                return self.send(message)

        else:
            print "Didn't understand ", parts[0]
            self.error()


    def error(self):
        """ Return an error message to the client """
        return self.send("error\n")

    def send(self,message):
        """ Send a message to the client """
        try:
            self.client.send(message)
        except socket.error, (value,reason):
            self.running = False

if __name__ == "__main__":
    # Variables declared here are visible to all client threads. I put all
    # shared memory within a single class.  This way, any other class
    # can access the variables of the shared class without creating separate
    # instances of those variables

    # An alternative is to declare variables within the server class and
    # then pass these by reference to each new client thread that is created.
    # This would allow the server to choose which variables are visible to
    # each thread.  Of course, all variables would still be visible through
    # the server instance.

    s = Server()
    s.start()

#!/usr/bin/env python

# This program is licensed under the GPL; see LICENSE for details.

# Client that demonstrates shared memory between threads.  The client
# can send requests for one of several names.

import optparse
import socket
import string
import sys
import time

# For this import to work, you need to put this line
#
# export PYTHONPATH=/home/zappala/Web
#
# in your .bashrc and then login again
from shared import *

class Client:
    """ The client can send requests using the message:

          lookup <i>

    where <i> is some number greater than 1.  If the server has a name
    corresponding to that number, it returns the name using the message:

          name <number> <name>

    where <number> is the number of times this client has requested a
    name during this session, and <name> is the name (a string with no
    spaces).  If there is no name matching the requested number, the
    server returns:

          error

    All messages are terminated by a newline.

    The client exits when the user enters:

          quit

    """
    def __init__(self):
        """ Initialize the client with default values """
        self.host = socket.gethostname()
        self.port = 0
        self.debugging = False
        self.size = 1024
        self.data = ""
        self.running = True

    def run(self):
        """ Run the client """
        self.do_options()
        self.open_socket()
        self.prompt()
        while self.running:
            # read from keyboard
            line = sys.stdin.readline()
            self.parse_command(line)
        self.client.close()


    def parse_options(self):
        """ Parse options.  User can use '-s' to specify the server name
        and '-p' to specify the server port.  Use '-d' to print debugging
        information.
        """
        parser = optparse.OptionParser(usage = "%prog [options]",
                                       version = "%prog 0.1")
        parser.add_option("-p", "--port", type="int",dest="port",
                          metavar="PORT",default=0,
                          help="port number for the server")
        parser.add_option("-s", "--server", type="string", dest="host",
                          metavar="SERVER",default=socket.gethostname(),
                          help="host name for the server")
        parser.add_option("-d","--debug",action="store_true",dest="debug",
                          default=False,
                          help="print debugging information")

        return parser.parse_args()

    def do_options(self):
        """ Parse options.  See above for valid options.
        """
        (options, args) = self.parse_options()

        self.port = options.port
        self.host = options.host
        self.debugging = options.debug

    def open_socket(self):
        """ Open a socket and connect to the server.  Check for socket
        exceptions and exit if one occurs.
        """
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print self.host, self.port
            self.client.connect((self.host,self.port))
        except socket.error, (value,reason):
            if self.client:
                self.client.close()
            print "Could not open socket: " + reason
            sys.exit(1)

    def prompt(self):
        """ Display a prompt.  Note we flush standard output to be sure
        it prints immediately.
        """
        sys.stdout.write('%')
        sys.stdout.flush()

    def parse_command(self,line):
        """ Parse a command the user has entered """
        line = string.strip(line)
        parts = string.split(line)
        if parts == []:
            self.prompt()
            return
        command = parts[0]
        if command == "lookup":
            if len(parts) >= 2:
                try:
                    value = int(parts[1])
                except:
                    sys.stdout.write("Huh?\n")
                    self.prompt()
                    self.running = False
                    return
                self.send(command + " " + parts[1] + "\n")
                self.parse_response()
        elif command == "quit":
            self.running = False
        else:
            sys.stdout.write("Huh?\n")
            
        if self.running:
            self.prompt()

    def parse_response(self):
        """ Parse a response from the server. Handle partial messages. """
        if not self.running:
            return
        done = False
        while not done:
            try:
                data = self.client.recv(self.size)
            except socket.error, (value,reason):
                print "Connection to server is closed: ", reason
                self.running = False
                return

            if not data:
                print "Server has closed the connection"
                self.running = False
                return
            # get cached data
            data = self.data + data
            self.data = ""

            # find end of message
            end = string.find(data,"\n")
            if (end < 0):
                # cache the data we have
                self.data = data
                shared.debug(["Caching:",self.data])
            else:
                # parse the message
                sys.stdout.write(data[:end+1])
                done = True
                start = end + 1
                if start < len(data):
                    self.data = data[start:]
                    shared.debug(["Caching:",self.data])


    def send(self,message):
        """ Send a message to the server """
        try:
            self.client.send(message)
        except socket.error, (value,reason):
            print "Connection to server has closed: ", reason
            self.running = False


if __name__ == "__main__":
    c = Client()
    c.run()

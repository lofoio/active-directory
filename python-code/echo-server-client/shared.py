# This program is licensed under the GPL; see LICENSE for details.

# An example of shared memory for threads

import sys
import threading
import time

# These are the items this file exports.  Note that we include both
# the Shared class and the shared variable pointing to an instance of
# this class.  See other files in this program for how to use the
# shared memory.

__all__ = ['Shared','shared']

class Shared:
    """ Shared memory structure.  Currently holds command line options
    and seeds the random number generator.
    """
    def __init__(self):
        self.verbose = False
        self.debug_semaphore = threading.Semaphore()
        self.count = 0
        self.names = ['Caesar','Groucho Marx','Tony Martinez',
                      'Santa Claus','Sherlock Holmes','Ralph Waldo Emerson']


    def lookup(self,id):
        """ Lookup a name given a string that should correspond to an integer
        """
        
        # get corresponding name if one exists
        try:
            name = self.names[id-1]
        except:
            return "",""
        # increment count
        self.debug_semaphore.acquire()
        self.count += 1
        count = self.count
        self.debug_semaphore.release()
        # return count and name
        return count,name

    def debug(self,list):
        """ Debugging function.  Pass in a list of items to print.  They
        will each be converted to a string and printed with the current time.
        """
        if not self.verbose:
            return
        data = "[" + time.asctime() + "]"
        for item in list:
            if item == None:
                continue
            data += " "
            data += str(item)
        if len(list) > 0:
            if type(list[-1]) != str or len(list[-1]) <= 0 or list[-1][-1] != '\n':
                data += "\n"

        self.debug_semaphore.acquire()
        sys.stdout.write(data)
        sys.stdout.flush()
        self.debug_semaphore.release()


# An instance of the shared memory class.  Any python code that imports
# this module can reference shared memory through this instance.
shared = Shared()

#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 7 - launcelot_tests.py
# Test suite that can be run against the Launcelot servers.
from funkload.FunkLoadTestCase import FunkLoadTestCase
import socket, os, unittest, launcelot
SERVER_HOST = os.environ.get('LAUNCELOT_SERVER', 'localhost')
class TestLauncelot(FunkLoadTestCase):
    def test_dialog(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((SERVER_HOST, launcelot.PORT))
        for i in range(10):
            question, answer = launcelot.qa[i % len(launcelot.qa)]
            sock.sendall(question)
            reply = launcelot.recv_until(sock, '.')
            self.assertEqual(reply, answer)
        sock.close()
if __name__ == '__main__':
    unittest.main()

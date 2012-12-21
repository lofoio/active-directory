import IN, socket, sys
tskt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535
PORT = 1060
if len(sys.argv) != 2:
    print >> sys.stderr, 'usage: big_sender.py host'
    sys.exit(2)
hostname = sys.argv[1]
tskt.connect((hostname, PORT))
tskt.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
try:
    tskt.send('#' * 65000)
except socket.error:
    print 'The message did not make it'
else:
    print 'The big message was sent! Your network supports really big packets!'
option = getattr(IN, 'IP_MTU', 14) # constant taken from <linux/in.h>
print option
print 'MTU:', tskt.getsockopt(socket.IPPROTO_IP, option)

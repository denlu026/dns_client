import socket
from packs.BaseHeader import BaseHeader
from packs.BaseQuestion import BaseQuestion
from packs.EncodeResponse import EncodeResponse

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = b'biubiu' + b'whoami'
address = ('127.0.0.1', 53)
s.sendto(data, address)

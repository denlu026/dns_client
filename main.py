import socket
from packs.BaseHeader import BaseHeader
from packs.BaseQuestion import BaseQuestion


def dns_client(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = BaseHeader().get_header() + BaseQuestion('www.bbb.com').get_question()
    addr = ('127.0.0.1', 53)
    s.sendto(data, addr)
    rel_data, rel_addr = s.recvfrom(2048)
    print(rel_data)


dns_client(1, 1)


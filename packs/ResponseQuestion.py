import struct


class EncodeResponse:
    def __init__(self, data, addr):
        temp1 = data[:12]
        for t in temp1:
            print(t)

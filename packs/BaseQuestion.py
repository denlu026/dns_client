import struct


class BaseQuestion:
    def __init__(self, data):
        temp = b''
        for d in data.split('.'):
            temp = temp + struct.pack('B', len(d)) + bytes(d, encoding='utf-8')
        self.q_name = temp + b'\x00'
        self.q_type = 1
        self.q_class = 1

    def get_question(self):
        question = self.q_name + struct.pack(
            '>HH',
            self.q_type,
            self.q_class
        )
        return question

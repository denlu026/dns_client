import struct
import random


class BaseHeader:
    def __init__(self):
        self.tid = random.randint(1, 65535)
        self.flags = 256
        self.quests = 1
        self.answers = 0
        self.author = 0
        self.addition = 0

    def get_header(self):
        header = struct.pack(
            '>HHHHHH',
            self.tid,
            self.flags,
            self.quests,
            self.answers,
            self.author,
            self.addition
        )
        return header

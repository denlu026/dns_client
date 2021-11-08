import struct


class EncodeResponse:
    def __init__(self, data, address):
        self.data = data
        self.address = address
        self.len = 0
        self.header = self.get_header()
        self.question = self.get_question()
        self.answer = self.get_answer()
        self.additional = self.get_additional()

    def get_header(self):
        header = (
            tid,
            flags,
            quests,
            answers,
            author,
            addition
        ) = struct.unpack('>HHHHHH', self.data[:12])
        return {'header': header, 'bytes header': self.data[:12]}

    def get_question(self):
        i = 0
        domain = ''
        for q in self.data[12:]:
            if q == 0:
                break
            if q < 32:
                domain = domain + '.'
            else:
                domain = domain + chr(q)
            i += 1
        domain = domain[1:]
        length = i + 12 + 1
        q_name = self.data[12:length]
        q_type = self.data[length:length + 2]
        q_class = self.data[length + 2: length + 4]

        self.len = length + 4

        question = {
            'question': (q_name, q_type, q_class),
            'bytes_question': (domain,) + struct.unpack('>HH', self.data[length:length + 4])
        }
        return question

    def get_answer(self):
        answer = struct.unpack(
            '>HHHLHBBBB',
            self.data[self.len:self.len + 16]
        )

        bytes_answer = (
            self.data[self.len:self.len + 2],
            self.data[self.len + 2:self.len + 4],
            self.data[self.len + 4:self.len + 6],
            self.data[self.len + 6:self.len + 10],
            self.data[self.len + 10:self.len + 12],
            self.data[self.len + 12:self.len + 13],
            self.data[self.len + 13:self.len + 14],
            self.data[self.len + 14:self.len + 15],
            self.data[self.len + 15:self.len + 16],
        )

        self.len = self.len + 16
        return {
            'answer': answer,
            'bytes_answer': bytes_answer
        }

    def get_additional(self):
        return self.data[self.len:]



from enum import Enum, auto


class J1939_PDU(Enum):
    PDU1 = auto()
    PDU2 = auto()


class J1939_ID:

    _id = None

    def __init__(self, id=None, pgn=None):

        if id is not None:
            self._id = id
        elif pgn is not None:
            self._id = pgn << 8

    @property
    def p(self):
        return (self._id >> 26) & 0x3

    @property
    def r(self):
        return (self._id >> 25) & 0x1

    @property
    def dp(self):
        return (self._id >> 24) & 0x1

    @property
    def dp(self):
        return (self._id >> 24) & 0x1

    @property
    def pf(self):
        return (self._id >> 16) & 0xFF

    @property
    def ps(self):
        return (self._id >> 8) & 0xFF

    @property
    def sa(self):
        return self._id & 0xFF

    @property
    def pdu(self):
        if self.pf < 240:
            return J1939_PDU.PDU1
        else:
            return J1939_PDU.PDU2

    @property
    def id(self):
        return self._id

    @property
    def pgn(self):
        if self.pdu is J1939_PDU.PDU1:
            # Clear target address
            return (self._id >> 8) & 0x3FF00
        else:
            return (self._id >> 8) & 0x3FFFF

    def __str__(self):
        return f"ID: 0x{self.id:08X} ({self.id:>9}), " \
               f"P: 0x{self.p:01X}, " \
               f"DP: 0x{self.dp:01X}, " \
               f"PF: 0x{self.pf:02X} ({self.pf:>3}), " \
               f"PS: 0x{self.ps:02X} ({self.ps:>3}), " \
               f"SA: 0x{self.sa:02X} ({self.sa:>3}), " \
               f"PGN: 0x{self.pgn:05X} ({self.pgn:>6})"

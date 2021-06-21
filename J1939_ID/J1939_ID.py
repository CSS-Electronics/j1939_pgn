from enum import Enum, auto


class J1939_PDU(Enum):
    """
    J1939 PDU type
    """
    PDU1 = auto()
    PDU2 = auto()


class J1939_ID:
    """
    J1939 class
    """
    _id = None

    def __init__(self, msg_id: int = None, msg_pgn: int = None):
        """
        Takes either a message ID or PGN
        :param msg_id: CAN-bus message ID
        :param msg_pgn: CAN-bus message J1939 PGN
        """

        if msg_id is not None:
            self._id = msg_id
        elif msg_pgn is not None:
            self._id = msg_pgn << 8

    @property
    def p(self) -> int:
        """
        Priority
        :return: J1939 priority value
        """
        return (self._id >> 26) & 0x7

    @property
    def r(self) -> int:
        """
        Reserved bit
        :return: Reserved bit value
        """
        return (self._id >> 25) & 0x1

    @property
    def dp(self) -> int:
        """
        Data Page
        :return: Data Page value
        """
        return (self._id >> 24) & 0x1

    @property
    def pf(self) -> int:
        """
        PDU format
        :return: PDU format value
        """
        return (self._id >> 16) & 0xFF

    @property
    def ps(self) -> int:
        """
        PDU Specific
        :return: PDU specific value
        """
        return (self._id >> 8) & 0xFF

    @property
    def sa(self) -> int:
        """
        Source Address
        :return: Source Address value
        """
        return self._id & 0xFF

    @property
    def pdu(self) -> J1939_PDU:
        """
        PDU type
        :return: PDU type as J1939_PDU
        """
        if self.pf < 240:
            return J1939_PDU.PDU1
        else:
            return J1939_PDU.PDU2

    @property
    def id(self) -> int:
        """
        Message ID
        :return: Message ID value
        """
        return self._id

    @property
    def pgn(self):
        """
        Message PGN
        :return: Message PGN value
        """
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

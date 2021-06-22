from J1939_PGN import J1939_PGN, J1939_PDU


class TestJ1939PGN(object):

    def test_id_to_pgn(self):
        
        sa = 0xFF
        ps = 0xAA
        for priority in range(0, 8):
            for pf in range(0, 256):

                msg_id = priority << 26 | 0 << 25 | 0 << 24 | pf << 16 | ps << 8 | sa << 0

                j1939 = J1939_PGN(msg_id=msg_id)

                assert j1939.p == priority
                assert j1939.ps == 0xAA

                if pf < 240:
                    # With PF < 240, the PS field is target address and set to zero in the PGN
                    assert j1939.pdu == J1939_PDU.PDU1, f"{j1939}"
                    assert j1939.pgn == (msg_id >> 8) & 0x3FF00

                else:
                    # With PF >= 240, the PS field is group extension and part of the PGN
                    assert j1939.pdu == J1939_PDU.PDU2, f"{j1939}"
                    assert j1939.pgn == (msg_id >> 8) & 0x3FFFF

                    pass

    def test_pgn_to_id(self):

        ps = 0xAA
        for pf in range(0, 256):

            msg_pgn = 0 << 17 | 0 << 16 | pf << 8 | ps << 0

            j1939 = J1939_PGN(msg_pgn=msg_pgn)

            # Assume that SA is set to zero
            assert j1939.sa == 0

            assert j1939.id == (msg_pgn << 8)

            if pf < 240:
                assert j1939.pdu == J1939_PDU.PDU1, f"{j1939}"
            else:
                assert j1939.pdu == J1939_PDU.PDU2, f"{j1939}"

    def test_fields(self):

        p = 2
        r = 0
        dp = 0
        pf = 255
        ps = 100
        sa = 200
        msg_id = p << 26 | r << 25 | dp << 24 | pf << 16 | ps << 8 | sa << 0

        j1939 = J1939_PGN(msg_id=msg_id)

        assert j1939.p == p
        assert j1939.r == r
        assert j1939.dp == dp
        assert j1939.pf == pf
        assert j1939.ps == ps
        assert j1939.sa == sa

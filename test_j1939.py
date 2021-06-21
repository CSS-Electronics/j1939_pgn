from J1939 import J1939, J1939_PDU

if __name__ == "__main__":

    # Init by PGN
    j1939 = J1939(pgn=60928)
    print(j1939)

    # Init by id
    j1939 = J1939(id=16704256)
    print(j1939)

    # Compact use
    print(f"ID: {J1939(pgn=60928).id}")
    print(f"PGN: {J1939(id=16704256).pgn}")

    # Access elements
    j1939 = J1939(id=16704256)
    print(f"P:  {j1939.p}")
    print(f"DP: {j1939.dp}")
    print(f"PF: {j1939.pf}")
    print(f"PS: {j1939.ps}")
    print(f"SA: {j1939.sa}")

    # Access specific elements
    j1939 = J1939(pgn=60928)
    if j1939.pdu is J1939_PDU.PDU1:
        print(f"Target address: {j1939.ps:02X}")

# Python SAE J1939 PGN

Python module for working with SAE J1939 PGNs.

## Installation
```
pip install j1939_pgn
```
## Dependencies
None

## Usage examples

```
from J1939_PGN import J1939_PGN, J1939_PDU

# Init from PGN
j1939 = J1939_PGN(msg_pgn=60928)
print(j1939)

# Init from ID
j1939 = J1939_PGN(msg_id=16704256)
print(j1939)

# Compact use
print(f"ID: {J1939_PGN(msg_pgn=60928).id}")
print(f"PGN: {J1939_PGN(msg_id=16704256).pgn}")

# Access elements
j1939 = J1939_PGN(msg_id=16704256)
print(f"P:  {j1939.p}")
print(f"DP: {j1939.dp}")
print(f"PF: {j1939.pf}")
print(f"PS: {j1939.ps}")
print(f"SA: {j1939.sa}")

# Access specific elements
j1939 = J1939_PGN(msg_pgn=60928)
if j1939.pdu is J1939_PDU.PDU1:
    print(f"Target address: {j1939.ps:02X}")
```
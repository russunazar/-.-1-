dup = "mother father"
dup1 = str()
for char in dup:
    a = int(0)
    if char == chr(32):
        dup1 += char
    else:
        dup1 += char + char
print(dup1)

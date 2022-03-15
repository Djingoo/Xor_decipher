# data

normal_gif = [b"\x47", b"\x49", b"\x46", b"\x38", b"\x39", b"\x61", b"\x90", b"\x01", b"\x2C", b"\x01"]

exo1_gif = [b"\x4e", b"\x76", b"\xe0", b"\x82", b"\xc2", b"\xa6", b"\x7d", b"\xd7", b"\x0c", b"\x90"]

order = []

#functions

def xor(byte = bytes, key = int):
    for bit in byte:
        return bytes([bit ^ key])

def rate(byte, target):
    for i in range(0,255):
        rank = xor(byte, i)
        if rank == target:
            return i

for index, bt in enumerate(normal_gif):
    order.append(rate(bt, exo1_gif[index]))

with open("output.gif.WIN.gif", "wb") as output:
    with open("the_force_400x300.gif.enc","rb") as input:
        while True:
            chunk = input.read(10)
            if chunk:
                for index,bt in enumerate(chunk):
                    output.write(xor(bt.to_bytes(1,'big'), int(order[index])))
            else:
                break
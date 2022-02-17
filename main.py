import math


def add_padding(msg) -> str:
    msg.append('10000000')
    while len(msg) % 64 != 56:
        msg.append('00000000')
    return msg


def append_length(msg_arr, length: str):
    i = 0
    while i < len(length):
        byte = ''
        for j in range(0, 8):
            byte = byte + length[i]
            i += 1
        msg_arr.append(byte)
    return msg_arr


def make_byte_arr(msg: str):
    m_arr_b = bytearray(msg, "utf8")
    m_arr = []
    for x in m_arr_b:
        if x != 194:
            b = format(x, "08b")
            m_arr.append(b)
    return m_arr


# F(X,Y,Z) = XY v not(X) Z
def F(x, y, z):
    return (x & y) | ((not x) & z)


# G(X,Y,Z) = XZ v Y not(Z)
def G(x, y, z):
    return (x & z) | (y & (not z))


# H(X,Y,Z) = X xor Y xor Z
def H(x, y, z):
    return x ^ y ^ z


# I(X,Y,Z) = Y xor (X v not(Z))
def I(x, y, z):
    return y ^ (x | (not z))


def main():
    # getting the input text
    or_m = input("give me a text to hash:\t")

    # making an array of msg's chars in binary(utf8)
    m_arr = make_byte_arr(or_m)

    # adding padding
    or_m = add_padding(m_arr)

    # appending the length
    m_arr = append_length(m_arr, format(len(or_m), "064b"))

    # initial MD buffers
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    # generate the table of constants
    k = []
    for i in range(0, 64):
        k.append(hex(math.floor(int(2**32 * abs(math.sin(i + 1))))))

    # define the shift values table
    s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
         5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
         4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
         6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]


if __name__ == '__main__':
    main()

def dec_to_bin(dec):
    b = ''
    while dec > 0:
        ost = dec % 2
        dec = dec // 2
        b = str(ost) + b
    return b

m = 17028546
print(dec_to_bin(m))
print(bin(m))
print(oct(m))
print(hex(m))


10011100001111
18446744073709551616
11111011000111000010
1000000111101010111000010

9999
4294967296


"""
ABCDEFUKGVKUGVKUJ
int32 => 
int64

19(10) => X(2)

"""
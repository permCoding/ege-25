def dec_to_base(dec, base=2):
    b = ''
    while dec > 0:
        ost = dec % base
        dec = dec // base
        b = str(ost) + b
    return b


m = 152  # 10
print(dec_to_base(m, 8))  # 230





# print(bin(m))
# print(oct(m))
# print(hex(m))


"""
ABCDEFUKGVKUGVKUJ
int32 => 
int64

19(10) => X(2)

"""
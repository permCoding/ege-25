def dec_to_seven(dec):
    result = ''
    while dec > 0:
        ost = dec % 7
        dec = dec // 7
        result = str(ost) + result
    return result


for n in range(1000, 0, -1):
    s = dec_to_seven(n)
    if n%2 == 0:
        s = '52' + s + '1'
    else:
        s = s[-1] + s[1:-1] + s[0] + '15'
    if len( dec_to_seven(int(s, 7)) ) == 4:
        print(n, s)  # 09999
        break


# s = '0006'  # 7
# s = '0010'  # 7
# s = '000000000006666'  # 7
# dec = int(s, 7)
# s = dec_to_seven(dec)
# print( s )

# s = 'abcdefgh'  # 8

# print(s[-1] + s[0])

# print(s[len(s)-1] + s[0])

# print(s[-1] + s[0])


# 10  7
# 0  0
# 1  1
# 2  2
# 3  3
# 4  4
# 5  5
# 6  6(7)+1
# 7

# _9
# +
# _1

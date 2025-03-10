n = 1024099
s = str(n)

# sm = ''
# for e in s:
#     # print(e, type(e))
#     sm += e
# print(sm, type(sm))

# sm = 0
# for e in s:
#     sm += int(e)
# print(sm)

# sm = 0
# for i in 0,1,2,3:
#     sm += int(s[i])
# print(sm)

# sm = 0
# for i in range(len(s)):
#     sm += int(s[i])
# print(sm)

# print(sum(int(e) for e in s))

sm = 0
i = 0
while i < len(s):
    sm += int(s[i])
    i += 1
print(sm)
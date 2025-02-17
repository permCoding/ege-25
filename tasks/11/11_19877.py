n = 65

_id = 20  # bit
ops = 770  # bit
dop = n   # bit

obj = _id + ops + dop  # 192 byte


amount = 131_072
weight_all_obj = 24 * 1024 * 1024  # byte
print(weight_all_obj / amount)  # 192 byte
print(790 / 8)
print(192 - 99)

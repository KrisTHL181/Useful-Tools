import itertools

not_quite_id = input("前位号码(未知用*号代替,必须给校验码):")
if len(not_quite_id) != 18: raise BaseException("给出的号码不是18位!")

print("正在开始计算...")

count = 0
for try_number in itertools.product("0123456789", repeat=not_quite_id.count('*') ):
    verify=(12 - (sum(((1 << (17 - i)) % 11) * int(not_quite_id.replace(not_quite_id.count('*') * "*", str().join(try_number))[:17][i]) for i in range(0, 17)) % 11)) % 11
    verify_code=str(verify) if verify < 10 else 'X'
    if verify_code ==  not_quite_id.replace(not_quite_id.count('*') * "*", str().join(try_number))[-1]:
        print(f"可能搭配:{not_quite_id.replace(not_quite_id.count('*') * '*', str().join(try_number))+verify_code}\n缺失位是:{str().join(try_number)}")
        count += 1
print(f"一共有{count}种可能!")


user_input = int(input())
for n in range(2,user_input):
    for x in range(2,n):
        if n%x == 0:
            print(f'number {n} is not primary number, it be can expressed as {n} = {x} * {n//x}')
            break
    else:
        print(f'number {20n} is primary number')
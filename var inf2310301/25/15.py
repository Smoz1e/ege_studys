for x in range(1000):
    for y in range(10):
        if int(f'1{x}4022{y}9') % 1987 ==0:
            print(int('1'+ str(x) +'4022' + str(y) + '9'))
        if x < 100 and int(f'10{x}4022{y}9') % 1987 ==0:
            print(int(f'10{x}4022{y}9'))
        if x < 10 and int(f'100{x}4022{y}9') % 1987 ==0:
            print(int(f'100{x}4022{y}9'))

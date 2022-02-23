def liftoff(num):
    for i in range(num, -1, -1):
        if i == 0:
            print('liftoff!')
        else:
            print(i)

liftoff(10)

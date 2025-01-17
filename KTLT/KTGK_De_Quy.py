def move(n, x, y, z):
    if n == 1:
        print(f"Move {z} => {y}")
    else:
        move(n - 1, z,x,y)
        print(f"Move {z} => {x}")
        move(n - 1, x,z,y)

n = 4
move(n, 't1', 't2', 't3')

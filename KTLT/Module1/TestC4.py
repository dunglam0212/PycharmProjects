x=5
def fnX():
    global x
    x=9
    x+=2
    print(f'x={x}')
fnX()
print(f'x={x}')

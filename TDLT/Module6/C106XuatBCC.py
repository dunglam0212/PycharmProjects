'''def print_bcc():
    for i in range (1,10):
        print(f'Bảng cửu chương {i} là:')
        for j in range(1,10):
            print(f'{i}*{j}={i*j}')'''

def print_bcc():
    for i in range(1,11):
        for j in range(2,10):
            print(f'{j}*{i}={i*j}', end = '\t')
        print()
print_bcc()
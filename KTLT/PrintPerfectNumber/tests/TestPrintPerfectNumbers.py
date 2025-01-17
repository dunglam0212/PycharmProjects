from PrintPerfectNumber.ProcessPrintPerfectNumbers import print_perfect_numbers, print_perfect_numbers_from_1_to_N

n=int(input('Please enter an interger: '))
rs = print_perfect_numbers(n)
if rs==None:
    print(f'{n} is not a perfect number!')
else:
    print(f'{n} is a perfect number!')

print(print_perfect_numbers_from_1_to_N(10000))
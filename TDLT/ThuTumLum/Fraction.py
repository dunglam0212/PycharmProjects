class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def toString(self):
        return str(self.numerator) + "/" + str(self.denominator)

class Operator:
    def __init__(self, fraction1, fraction2):
        self.fraction1 = fraction1
        self.fraction2 = fraction2

    def GCD(self, a, b):
        numerator = a
        denominator = b
        if numerator < 0 or denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
        while numerator != denominator:
            if numerator > denominator:
                numerator = numerator - denominator
            else:
                denominator = denominator - numerator
        return numerator

    def shorten(self, fraction):
        gcd = self.GCD(fraction.numerator, fraction.denominator)
        fraction.numerator = fraction.numerator / gcd
        fraction.denominator = fraction.denominator / gcd

    def addition(self):
        result = Fraction(
            self.fraction1.numerator * self.fraction2.denominator + self.fraction2.numerator * self.fraction1.denominator,
            self.fraction1.denominator * self.fraction2.denominator)
        self.shorten(result)
        print("Result: ", result.toString())

    def substration(self):
        result = Fraction(
            self.fraction1.numerator * self.fraction2.denominator - self.fraction2.numerator * self.fraction1.denominator,
            self.fraction1.denominator * self.fraction2.denominator)
        self.shorten(result)
        print("Result: ", result.toString())

    def multiplication(self):
        result = Fraction(self.fraction1.numerator * self.fraction2.numerator,
                          self.fraction1.denominator * self.fraction2.denominator)
        self.shorten(result)
        print("Result: ", result.toString())

    def division(self):
        if self.fraction1.numerator == 0 or self.fraction2.numerator == 0:
            print("Result: 0")
        else:
            result = Fraction(self.fraction1.numerator * self.fraction2.denominator,
                              self.fraction1.denominator * self.fraction2.numerator)
            self.shorten(result)
            print("Result: ", result.toString())


def input_number_numerator(str):
    flag = False
    while not flag:
        try:
            number = int(input(f"Enter {str} : "))
            flag = True
        except ValueError:
            print("Invalid value !!!")
    return number

def input_number_denominator(str):
    flag = False
    while not flag:
        try:
            number = int(input(f"Enter {str} : "))
            if number != 0:
                flag = True
            else:
                print("You must enter the denominator not equal to 0 !!!")
        except ValueError:
            print("Invalid value !!!")
    return number


numerator1 = input_number_numerator("first numerator")
denominator1 = input_number_denominator("first denominator")
fraction1 = Fraction(numerator1, denominator1)
numerator2 = input_number_numerator("second numerator")
denominator2 = input_number_denominator("second denominator")
fraction2 = Fraction(numerator2, denominator2)
op = Operator(fraction1, fraction2)
flag = True
print("=" * 100)
print("1. Addition ")
print("2. Substraction ")
print("3. Multiplication")
print("4. Division ")
print("5. Exit ")
print("=" * 100)
while flag:
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            op.addition()
        case 2:
            op.substration()
        case 3:
            op.multiplication()
        case 4:
            op.division()
        case 5:
            answer = input("Do you want to continue (Y/y or N/n)?")
            if answer == "N" or answer == "n":
                print(f'Thank you for using!')
                print('See you later!')
                flag = False
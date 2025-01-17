from Module2.C29Sort_Negative_Number_in_String.Process import NegativeNumberInString

string = "abc-556756756xyz-172k9l--p"
print(string[0])

rs = NegativeNumberInString(string)
for i in rs:
    print(i)

# if int(string[4])%1==0 and string[4-1]=='-':
#     print("True")
# else:
#     print("False")
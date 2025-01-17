from Module2.C28StatisticsOfNumbersInAString.Process import statistic_numbers, statistic_even_numbers, \
    statistic_negative_numbers, statistic_prime_numbers, avg, check_prime_number

string = "5;7;8;-2;8;11;13;9;10"
rs = statistic_numbers(string)

rs1 = statistic_even_numbers(string)
print(f"Thống kê chữ số chẵn trong chuỗi trên là: {rs1}")

rs2 = statistic_negative_numbers(string)
print(f"Thống kê chữ số âm trong chuỗi trên là: {rs2}")

rs3 = statistic_prime_numbers(string)
print(f"Thống kê các số nguyên tố trong chuỗi trên là: {rs3}")

print(check_prime_number(-2))

rs4 = avg(string)
print(f"Giá trị trung bình của chuỗi trên là: {rs4}")
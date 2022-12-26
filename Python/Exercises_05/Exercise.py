


def divisible(numerator: int, denominator: int)->boolean:
 return numerator % denominator == 0
print(divisible(30,4))



def find_num(number_list: list, number: int)->boolean:
 for iterate_number in number_list:
 if iterate_number == number:
 return True
 else:
 pass
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)

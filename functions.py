
# def calculate_gross_salary(tax:int,netsal:int):
#     '''
#     calculates the gross salary
#     '''
#     if type(tax) == type(netsal) == type(int):
#         return netsal - (netsal*tax)
#     else:
#         return "Only integers are allowed as part of arguments."

# calculate_gross_salary("2","200000")

# def calculate_gross_salary(tax:int,netsal:int):
#     '''
#     calculates the gross salary
#     '''
#     if type(tax) == type(netsal) == type(int):
#         return netsal - (netsal*tax)
#     else:
#         return "Only integers are allowed as part of arguments."

# calculate_gross_salary("2","200000")

# print("gross salary {}".format(calculate_gross_salary(.3,100000)))


# print("gross salary {}".format(calculate_gross_salary(.3,100000)))


l = [1,2,3,4,5,6]

# def even_bool(num):
#     return num % 2 == 0


even = filter(lambda num: num%2 == 0,l)

print(list(even))
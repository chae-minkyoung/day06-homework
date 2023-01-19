class Oopsexception(Exception):
    pass

try:
    raise Oopsexception("Caught an oops")
except Oopsexception as abc:
    print(abc)



# # try:
# #     numbers=input(f"숫자 두개를 입력하세요:")
# #     number=numbers.split()
# #     a=int(number[0])
# #     b=int(number[1])
# #     print(a+b)
# # except IndexError as OopsException:
# #     print(f'Caught an oops')
# #
# #
# def sud(a):
#     return a**2
#
# print(sud(3))
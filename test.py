# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# words=['auto','cat','win111111']
# for i in words[:]:
#     if len(i)>5:
#         words.insert(1,i)
# print(words,len(words))
# range(5,10)
#
# for n in range(2,10):
#     for x in range(2,n):
#         if n % x == 0:
#             print(n,'equls',x,'*',n//x)
#             break
#     else:
#         print(n,'is a prime')

# def fib(n):
#     a,b=0,1
#     while a<n:
#         print(a,end=' ')
#         a,b=b,b+a
#     print()
# fib(2000)
#
# def fib2(n):
#     result = []
#     a,b=0,1
#     while a<n:
#         result.append(a)
#         a,b=b,a+b
#     return result
# print(fib2(100))
#
# def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise OSError('uncooperative user')
#         print(complaint)
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
#
# i=5
# def f(arg=i):
#     print(arg)
# i=6
# f()
#
# a = "hello"
# l = len(a)
# print(l)
#
# def main():
#     a = "hello"
#     c = len(a)
#     print c
# if __name__ = '__main__':
#     main()
from fibo import *
fib(500)
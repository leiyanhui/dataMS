# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 10:31 下午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : test.py
# @Software : PyCharm


def outer(func):
    print("outer")
    def inner(*args,**kwargs):
        print("inner",args)
        func(*args)
    return inner

def outer2(a):
    print("outer2",a)
    def outer(func):
        print("outer")
        def inner(*args,**kwargs):
            print("inner",args)
            func(*args)
        return inner
    return outer
@outer2(123)
def main(*args):
    print("this is main",args)

# main(90)  outer(main)(90)==inner(90) print("outer")
# outer(main)(*args)  inner(*args)  print("inner")
# inner(*args)  print("inner")

if __name__ == '__main__':
    main(90)
# -*- coding: UTF-8 -*-  
#decorator
def log(func):
    def inner(*args,**kwargs):
            print"log is:%s%s"%(args,kwargs)
            return func(*args,**kwargs)
    return inner
    
@log
def func1(x,y):
    print(x+y)
@log
def func2(x,y):
    print(x*y)
def main():
    func1(5,2)
    func2(3,4)
main()
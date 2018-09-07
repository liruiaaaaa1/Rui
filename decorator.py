#装饰器
def log（func）
    def inner（*args,**kwargs）:
	    print"log is：%s%s"%（args，kwargs）
		return func（*args，**kwargs）
	return inner
	
@log
def func1(x,y)
    return x+y
@log
def func2(x,y)
    return x*y
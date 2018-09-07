from collections import Iterable
                  
class List(object):
    def __init__(self):
        self.items = []
                  
    def add(self,val):
        self.items.append(val)
                  
    def __iter__(self):
                  
        iterator = Iterator1(self)
        return iterator
                  
class Iterator1(object):
                  
    def __init__(self,list):
        self.list = list
        self.current= 0
                  
    def __next__(self):
        if self.current < len(self.list.items):
            item = self.list.items[self.current]
            self.current += 1
            return item
        else:    
            raise StopIteration
    def __iter__(self):
        return self                                                                                                                                                           
                  
if __name__ == '__main__':
    list = List()
    list.add(1)
    list.add(2)
    list.add(3)
    list.add(4)
    list.add(5)
    for num in list:
        print(num)
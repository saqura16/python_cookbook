# class Data_test2(object):
#     day=0
#     month=0
#     year=0
#     def __init__(self,year=0,month=0,day=0):
#         self.day=day
#         self.month=month
#         self.year=year
#     @classmethod
#     def get_date(cls,data_as_string):
 
#         #这里第一个参数是cls， 表示调用当前的类名
 
#         year,month,day=map(int,data_as_string.split('-'))
#         date1=cls(year,month,day)     #返回的是一个初始化后的类
#         return date1
 
#     def out_date(self):
#         print("year :",self.year)
#         print("month :",self.month)
#         print("day :",self.day)
        
# r=Data_test2.get_date("2020-1-1")
# print(r)

# r.out_date()


# class A:
    
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
        
#     def add(self,x,y):
#         return x+y
    
#     def __repr__(self):
#         return '{}+{}={}'.format(self.x,self.y,self.add(self.x,self.y))
    
# a=A(2,3)
# print(a)




# class Person:
#     def __init__(self, first_name=10):
#         self._first_name = first_name
#     # Getter function
#     @property
#     def first_name(self):
#         return self._first_name
#     # Setter function
#     @first_name.setter
#     def first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._first_name = value
#     # Deleter function (optional)
#     @first_name.deleter
#     def first_name(self):
#         raise AttributeError("Can't delete attribute")
       
# a=Person('dyd')
# print(a.first_name)
# a.first_name='gbd'
# print(a.first_name)


# class A:
#     def __init__(self):
#         self.x = 0
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.y = 1 
#     @property
#     def p(self):
#         print(self.x,self.y)
            
# b=B()
# b.p



# class Person:
#     def __init__(self, name):
#         self.name = name


#     # Getter function
#     @property
#     def name(self):
#         return self._name
#     # Setter function
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._name = value
#     # Deleter function
#     @name.deleter
#     def name(self):
#         raise AttributeError("Can't delete attribute")

# class SubPerson(Person):
#     @property
#     def name(self):
#         print('Getting name')
#         return super().name
#     @name.setter
#     def name(self, value):
#         print('Setting name to', value)
#         super(SubPerson, SubPerson).name.__set__(self, value)
#     @name.deleter
#     def name(self):
#         print('Deleting name')
#         super(SubPerson, SubPerson).name.__delete__(self) 
        
# s=SubPerson('dyd')
# print(s.name)
# s.name='gbd'
# print(s.name)

# class lazyproperty:
#     def __init__(self, func):
#         self.func = func

#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             value = self.func(instance)
#             setattr(instance, self.func.__name__, value) #setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的。
#             return value

# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     @lazyproperty
#     def area(self):
#         print('Computing area')
#         return math.pi * self.radius ** 2 
#     @lazyproperty
#     def perimeter(self):
#         print('Computing perimeter')
#         return 2 * math.pi * self.radius
    
# c=Circle(4)
# print(c.area)
# print(c.perimeter)

# print(c.area)
# print(c.perimeter)


# def lazyproperty(func):
#     name = '_lazy_' + func.__name__
#     @property
#     def lazy(self):
#         if hasattr(self, name):  #hasattr()函数用于判断对象是否包含对应的属性
#             return getattr(self, name)
#         else:
#             print(type(func))
#             value = func(self)
#             setattr(self, name, value) #setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的。
#             return value
#     return lazy

# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     @lazyproperty
#     def area(self):
#         print('Computing area')
#         return math.pi * self.radius ** 2 
#     @lazyproperty
#     def perimeter(self):
#         print('Computing perimeter')
#         return 2 * math.pi * self.radius 

# c = Circle(4.0) 
# print(c.area )
# print(c.area )


# import math
# class Structure:
#     # Class variable that specifies expected fields
#     _fields= []
#     def __init__(self, *args):
#         # len(args)指的是列表中元素的个数
#         if len(args) != len(self._fields): 
#             raise TypeError('Expected {} arguments'.format(len(self._fields)))
#         # Set the arguments
#         for name, value in zip(self._fields, args):
#             setattr(self, name, value)
# # Example class definitions
# if __name__ == '__main__':
#     class Stock(Structure):
#         _fields = ['name', 'shares', 'price']  #在类外修改类的属性
#     class Point(Structure):
#         _fields = ['x','y']
#     class Circle(Structure):
#         _fields = ['radius']
#         def area(self):
#             return math.pi * self.radius ** 2

#     s = Stock('ACME', 50, 91.1)

# class Structure:
#     _fields= []
#     def __init__(self, *args, **kwargs):
#         if len(args) > len(self._fields):
#             raise TypeError('Expected {} arguments'.format(len(self._fields)))
#         # Set all of the positional arguments
#         for name, value in zip(self._fields, args):
#             setattr(self, name, value) #设置属性并设置属性名
#         # Set the remaining keyword arguments
#         for name in self._fields[len(args):]:
#             setattr(self, name, kwargs.pop(name))
#             print(name)
#         # Check for any remaining unknown arguments
#         if kwargs:
#              raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))
# # Example use
# if __name__ == '__main__':
#     class Stock(Structure):
#         _fields = ['name', 'shares', 'price'] 
#     #s1 = Stock('ACME', 50, 91.1)
#     #s2 = Stock('ACME', 50, price=91.1)
#     s3 = Stock('ACME', price=91.1, shares=50) 
#     print(1)

# from abc import ABCMeta, abstractmethod
# class IStream(metaclass=ABCMeta):
#     @abstractmethod
#     def read(self, maxbytes=-1):
#         pass
#     @abstractmethod
#     def write(self, data):
#         pass 


# Base class. Uses a descriptor to set a value
# class Descriptor: 
#     def __init__(self, name=None, **opts):
#         self.name = name
#         for key, value in opts.items():
#             setattr(self, key, value)
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value
        
# # Descriptor for enforcing types
# class Typed(Descriptor):
#     expected_type = type(None) 
#     def __set__(self, instance, value):
#         if not isinstance(value, self.expected_type):
#             raise TypeError('expected ' + str(self.expected_type))
#         super().__set__(instance, value)
        
# # Descriptor for enforcing values
# class Unsigned(Descriptor):
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Expected >= 0')
#         super().__set__(instance, value)
        
# class MaxSized(Descriptor):
#     def __init__(self, name=None, **opts):
#         if 'size' not in opts:  #opts是个字典！size是key,判断是否传入了size的大小
#             raise TypeError('missing size option')
#         super().__init__(name, **opts)
#     def __set__(self, instance, value):   #set方法
#         if len(value) >= self.size:
#             raise ValueError('size must be < ' + str(self.size))
#         super().__set__(instance, value)
        
# class Integer(Typed):
#     expected_type = int
# class UnsignedInteger(Integer, Unsigned):
#      pass
# class Float(Typed):
#     expected_type = float
# class UnsignedFloat(Float, Unsigned):
#     pass
# class String(Typed):
#     expected_type = str
# class SizedString(String, MaxSized):
#     pass 

# class Stock:
#     # Specify constraints
#     name = SizedString('name',size=8)
#     shares = UnsignedInteger('shares')
#     price = UnsignedFloat('price')
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price
    
# if __name__ == "__main__":    
#     s = Stock('ACME', 50, 91.1)
#     print( s.name )
#     s.shares = 75
#     # s.shares = -10


# class Proxy:
#     def __init__(self, obj):
#         self._obj = obj
#     # Delegate attribute lookup to internal obj
#     def __getattr__(self, name):
#         print('getattr:', name)
#         return getattr(self._obj, name)
#     # Delegate attribute assignment
#     def __setattr__(self, name, value):
#         if name.startswith('_'):
#             super().__setattr__(name, value)
#         else:
#             print('setattr:', name, value)
#             setattr(self._obj, name, value)
#     # Delegate attribute deletion
#     def __delattr__(self, name):
#         if name.startswith('_'):
#             super().__delattr__(name)
#         else:
#             print('delattr:', name)
#             delattr(self._obj, name)
            
# class Spam:
#     def __init__(self, x):
#         self.x = x
#     def bar(self, y):
#         print('Spam.bar:', self.x, y)
# # Create an instance
# s = Spam(2)
# # Create a proxy around it
# p = Proxy(s)
# # Access the proxy
# print(p.x) # Outputs 2
# p.bar(3) # Outputs "Spam.bar: 2 3"
# p.x = 37 # Changes s.x to 37

# class Connection:
#     def __init__(self):
#         self.new_state(ClosedConnectionState)  #此处传入一个类的地址
#     def new_state(self, newstate):
#         self._state = newstate  #类似实例化一个类
#     # Delegate to the state class
#     def read(self):
#         return self._state.read(self)
#     def write(self, data):
#         return self._state.write(self, data)
#     def open(self):
#         return self._state.open(self)
#     def close(self):
#         return self._state.close(self)

# # Connection state base class
# class ConnectionState:                          #基类
#     @staticmethod
#     def read(conn):
#         raise NotImplementedError()
#     @staticmethod
#     def write(conn, data):
#         raise NotImplementedError()
#     @staticmethod
#     def open(conn):
#         raise NotImplementedError()
#     @staticmethod
#     def close(conn):
#         raise NotImplementedError()
        
# # Implementation of different states        
# class ClosedConnectionState(ConnectionState):   #close类
#     @staticmethod
#     def read(conn):
#         raise RuntimeError('Not open')
#     @staticmethod
#     def write(conn, data):
#         raise RuntimeError('Not open')
#     @staticmethod
#     def open(conn):
#         conn.new_state(OpenConnectionState)   #切换为open类
#     @staticmethod
#     def close(conn):
#         raise RuntimeError('Already closed')

# class OpenConnectionState(ConnectionState):     #open类  
#     @staticmethod
#     def read(conn):
#         print('reading')
#     @staticmethod
#     def write(conn, data):
#         print('writing')
#     @staticmethod
#     def open(conn):
#         raise RuntimeError('Already open')
#     @staticmethod
#     def close(conn):
#         conn.new_state(ClosedConnectionState) 

# c = Connection()
# print(c._state)
# c.open()
# print(c._state)
# c.read()
# c.write('hello')
# c.close()
# print(c._state) 


# class Connection:
#     def __init__(self):
#         self.new_state(ClosedConnection)
#     def new_state(self, newstate):
#         self.__class__ = newstate
#     def read(self):
#         raise NotImplementedError()
#     def write(self, data):
#         raise NotImplementedError()
#     def open(self):
#         raise NotImplementedError()
#     def close(self):
#         raise NotImplementedError()

# class ClosedConnection(Connection):
#     def read(self):
#         raise RuntimeError('Not open')
#     def write(self, data):
#         raise RuntimeError('Not open')
#     def open(self):
#         self.new_state(OpenConnection)
#     def close(self):
#         raise RuntimeError('Already closed')
      
#     def _state(self):
#         return self.__class__
# class OpenConnection(Connection):
#     def read(self):
#         print('reading')
#     def write(self, data):
#         print('writing')
#     def open(self):
#         raise RuntimeError('Already open')  
#     def close(self):
#         self.new_state(ClosedConnection)
#     def _state(self):
#         return self.__class__
    


# c=Connection()
# print(c._state())
# c.open()
# c.write('hello')
# print(c._state())
# c.close()
# print(c._state())

# int('as')


# class Node:
#     pass

# class UnaryOperator(Node):
#     def __init__(self, operand):
#         self.operand = operand

# class BinaryOperator(Node):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right

# class Add(BinaryOperator):
#     pass

# class Sub(BinaryOperator):
#     pass

# class Mul(BinaryOperator):
#     pass

# class Div(BinaryOperator):
#     pass

# class Negate(UnaryOperator):
#     pass

# class Number(Node):
#     def __init__(self, value):
#         self.value = value

# class NodeVisitor:
#     def visit(self, node):
#         methname = 'visit_' + type(node).__name__
#         meth = getattr(self, methname, None)
#         if meth is None:
#             meth = self.generic_visit
#         return meth(node)
#     def generic_visit(self, node):
#         raise RuntimeError('No {} method'.format('visit_' + type(node).__name__)) 
# class Evaluator(NodeVisitor):
#     def visit_Number(self, node):
#         return node.value
#     def visit_Add(self, node):
#         return self.visit(node.left) + self.visit(node.right)
#     def visit_Sub(self, node):
#         return self.visit(node.left) - self.visit(node.right)
#     def visit_Mul(self, node):
#         return self.visit(node.left) * self.visit(node.right)
#     def visit_Div(self, node):
#         return self.visit(node.left) / self.visit(node.right)
#     def visit_Negate(self, node):
#         return -node.operand
    
    

# # Representation of 1 + 2 * (3 - 4) / 5
# t1 = Sub(Number(3), Number(4))
# t2 = Mul(Number(2), t1)
# t3 = Div(t2, Number(5))
# t4 = Add(Number(1), t3)
# e = Evaluator()
# print(e.visit(t4))


# class A(object):
#     bar=1
# a = A()
# getattr(a, 'bar')        # 获取属性 bar 值

# c=getattr(a, 'bar2', 3)    # 属性 bar2 不存在，但设置了默认值

# print(a.bar,c)
# print(a.__dict__)   
# import types


# class Node:
#     pass


# class NodeVisitor:
#     def visit(self, node):
#         stack = [node]
#         last_result = None
#         while stack:
#             try:
#                 last = stack[-1]
#                 if isinstance(last, types.GeneratorType):
#                     stack.append(last.send(last_result))
#                     last_result = None
#                 elif isinstance(last, Node):
#                     stack.append(self._visit(stack.pop()))
#                 else:
#                     last_result = stack.pop()
#             except StopIteration:
#                 stack.pop()
#         return last_result

#     def _visit(self, node):
#         methname = 'visit_' + type(node).__name__
#         meth = getattr(self, methname, None)
#         if meth is None:
#             meth = self.generic_visit
#         return meth(node)

#     def generic_visit(self, node):
#         raise RuntimeError('No {} method'.format(
#             'visit_' + type(node).__name__))


# class UnaryOperator(Node):
#     def __init__(self, operand):
#         self.operand = operand


# class BinaryOperator(Node):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right


# class Add(BinaryOperator):
#     pass


# class Sub(BinaryOperator):
#     pass


# class Mul(BinaryOperator):
#     pass


# class Div(BinaryOperator):
#     pass


# class Negate(UnaryOperator):
#     pass


# class Number(Node):
#     def __init__(self, value):
#         self.value = value

# # A sample visitor class that evaluates expressions


# class Evaluator(NodeVisitor):
#     def visit_Number(self, node):
#         return node.value

#     def visit_Add(self, node):
#         return self.visit(node.left) + self.visit(node.right)

#     def visit_Sub(self, node):
#         return self.visit(node.left) - self.visit(node.right)

#     def visit_Mul(self, node):
#         return self.visit(node.left) * self.visit(node.right)

#     def visit_Div(self, node):
#         return self.visit(node.left) / self.visit(node.right)

#     def visit_Negate(self, node):
#         return -self.visit(node.operand)


# if __name__ == '__main__':
#     # 1 + 2*(3-4) / 5
#     t1 = Sub(Number(3), Number(4))
#     t2 = Mul(Number(2), t1)
#     t3 = Div(t2, Number(5))
#     t4 = Add(Number(1), t3)
#     # Evaluate it
#     e = Evaluator()
#     print(e.visit(t4))  # Outputs 0.6




# import types
# class Node:
#     pass
# class NodeVisitor:
#     def visit(self, node):
#         stack = [node]
#         last_result = None
#         while stack:
#             try:
#                 last = stack[-1]
#                 if isinstance(last, types.GeneratorType):
#                     stack.append(last.send(last_result))
#                     last_result = None
#                 elif isinstance(last, Node):
#                     stack.append(self._visit(stack.pop()))
#                 else:
#                     last_result = stack.pop()
#             except StopIteration:
#                 stack.pop()
#         return last_result

#     def _visit(self, node):
#         methname = 'visit_' + type(node).__name__
#         meth = getattr(self, methname, None)
#         if meth is None:
#             meth = self.generic_visit
#         return meth(node)

#     def generic_visit(self, node):
#         raise RuntimeError('No {} method'.format(
#             'visit_' + type(node).__name__))
# class UnaryOperator(Node):
#     def __init__(self, operand):
#         self.operand = operand


# class BinaryOperator(Node):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right


# class Add(BinaryOperator):
#     pass


# class Sub(BinaryOperator):
#     pass


# class Mul(BinaryOperator):
#     pass


# class Div(BinaryOperator):
#     pass


# class Negate(UnaryOperator):
#     pass


# class Number(Node):
#     def __init__(self, value):
#         self.value = value

# class Evaluator(NodeVisitor):
#     def visit_Number(self, node):
#         return node.value
#     def visit_Add(self, node):
#         yield (yield node.left) + (yield node.right)
#     def visit_Sub(self, node):
#         yield (yield node.left) - (yield node.right)
#     def visit_Mul(self, node):
#         yield (yield node.left) * (yield node.right)
#     def visit_Div(self, node):
#         yield (yield node.left) / (yield node.right)
#     def visit_Negate(self, node):
#         yield -(yield node.operand)

# a = Number(0)
# for n in range(1,100000):
#     a = Add(a, Number(n))
# e = Evaluator() 
# print(e.visit(a))




# # Class just to illustrate when deletion occurs
# class Data:
#     def __del__(self):
#         print('Data.__del__')
# # Node class involving a cycle
# class Node:
#     def __init__(self):
#         self.data = Data()
#         self.parent = None
#         self.children = []

#     # NEVER DEFINE LIKE THIS.
#     # Only here to illustrate pathological behavior
#     def __del__(self):
#         del self.data
#         print(1)


#     def add_child(self, child):
#         self.children.append(child)
#         child.parent = self 


# a = Node()
# a.add_child(Node())
# print(a)
# import gc
# gc.collect()
# print(a)


# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')
# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        
a = Node()
a.add_child(Node())
print(a)
del a                   # Not deleted (no message)#但是如果打印a会被告知a未定义,我的理解是:a是Node类型,因为删除了部分(Data)但未完全删除a,导致a不完整,无法访问。
print(11)

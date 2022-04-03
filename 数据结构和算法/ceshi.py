# def k(items):
#     seen=set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)

# if __name__ == "__main__":
#     a = [1, 5, 2, 1, 9, 1, 5, 10] 
#     list = (k(a))
#     for i in list:
#         print(i,end=" ")
# def dedupe(items, key=None):
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)#不理解
#         if val not in seen:
#             yield item
#             seen.add(val) 
# if __name__ == "__main__":
#     a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}] 
#     print(list(dedupe(a, key=lambda d: (d['x'],d['y']))) )


# from collections import namedtuple
# S = namedtuple('Subscriber', ['addr', 'joined'])
# sub1 = S('jonesy@example.com', '2012-10-19')
# sub2 = S('jonesy', '2012-10-19')
# print(sub1)#Subscriber(addr='jonesy@example.com', joined='2012-10-19')
# print(sub2)#Subscriber(addr='jonesy', joined='2012-10-19')
# print(sub1.addr)
# # 'jonesy@example.com'
# print( sub1.joined)
# # '2012-10-19'


from collections import ChainMap


values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()#new_child()的作用是添加一个新的空白字典，然后像普通字典一样操作添加数据。
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)


values = values.parents 
print(values)

values = values.parents 
print(values)
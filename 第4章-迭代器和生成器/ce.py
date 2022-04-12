# # 子生成器
# def average_gen():
#     total = 0
#     count = 0
#     average = 0
#     while True:
#         new_num = yield average
#         count += 1
#         total += new_num
#         average = total/count

# # 委托生成器
# def proxy_gen():
#     while True:
#         yield from average_gen()

# # 调用方
# def main():
#     calc_average = proxy_gen()
#     next(calc_average)            # 预激下生成器
#     print(calc_average.send(10))  # 打印：10.0
#     print(calc_average.send(20))  # 打印：15.0
#     print(calc_average.send(30))  # 打印：20.0

# if __name__ == '__main__':
#     main()



# from collections import deque 
# class linehistory:     
#     def __init__(self, lines, histlen=3):
#         self.lines = lines
#         self.history = deque(maxlen=histlen)
#     def __iter__(self):
#         for lineno, line in enumerate(self.lines,1):
#
# self.history.append((lineno, line))
#
# yield line     
#     def clear(self):
#         self.history.clear()
        
        
# with open('4.1.txt') as f:
#     lines = linehistory(f)
#     for line in lines:
#         if 'python' in line:
#
# for lineno, hline in lines.history:
#
#     print('{}:{}'.format(lineno, hline), end='')




from collections.abc import Iterable
# def flatten(items, ignore_types=(str, bytes)):   
#     for x in items:         
#         if isinstance(x, Iterable) and not isinstance(x, ignore_types):
#             yield from flatten(x)        
#         else:
#             yield x 
                
# items = [1, 2, [3, 4, [5, 6], 7], 8] 
# # Produces 1 2 3 4 5 6 7 8 
# for x in flatten(items):
#     print(x)


# def flatten1(items, ignore_types=(str, bytes)): 
#     for x in items: 
#         if isinstance(x, Iterable) and not isinstance(x, ignore_types):
#             for i in flatten1(x):
#                 yield i 
#         else: 
#             yield x 

# items = [1, 2, [3, 4, [5, 6], 7], 8] 

# for i in flatten1(items):
#     print(i)


# import heapq 
# a = [11, 10, 7, 1] 
# b = [41, 11, 6, 2] 
# for c in heapq.merge(a, b): 
#     print(c)
    
    

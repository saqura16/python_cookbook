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
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)#不理解
        if val not in seen:
            yield item
            seen.add(val) 
if __name__ == "__main__":
    a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}] 
    print(list(dedupe(a, key=lambda d: (d['x'],d['y']))) )
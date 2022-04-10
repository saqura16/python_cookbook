# from fnmatch import fnmatch, fnmatchcase
# print(fnmatch('foo.txt', '*.TXT'))


# def func1(f):
#     for i in range(10):
#         print(i,1)
#     f()


# def func2():
#     for i in range(10):
#         print(i,2)
        
        
# func1(func2)
# for i in range(10):
#     print(i, 3)

# from calendar import month_abbr 
# import re
# def change_date(m):
#     mon_name = month_abbr[int(m.group(1))]
#     print(mon_name)
#     return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

# datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# text = 'Today is 11/27/2012. PyCon starts 3/13/2013.' 



# print(datepat.sub(change_date, text))


# import re

# def matchcase(word):
#     def replace(m):
#         text = m.group()
#         if text.isupper():
#             return word.upper()
#         elif text.islower():
#             return word.lower()
#         elif text[0].isupper():
#             return word.capitalize()
#         else:
#             return word  
#     return replace


# text = 'UPPER PYTHON, lower python, Mixed Python'
# a=re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
# print(a)



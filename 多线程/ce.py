
#daima1

# from multiprocessing import Process
# import os
# import time

# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     time.sleep(2)
#     p.join()
#     print('Child process end.')


#daima2
# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')




# #daima3

# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)







# import time
# from threading import Thread, Event
# import random
# items = []
# event = Event()

# class consumer(Thread):
#     def __init__(self, items, event):
#         Thread.__init__(self)
#         self.items = items
#         self.event = event

#     def run(self):
#         while True:
#             time.sleep(2)
#             self.event.wait()
#             item = self.items.pop()
#             print('Consumer notify : %d popped from list by %s' % (item, self.name))

# class producer(Thread):
#     def __init__(self, items, event):
#         Thread.__init__(self)
#         self.items = items
#         self.event = event

#     def run(self):
#         global item
#         for i in range(100):
#             time.sleep(2)
#             item = random.randint(0, 256)
#             self.items.append(item)
#             print('Producer notify : item N° %d appended to list by %s' % (item, self.name))
#             print('Producer notify : event set by %s' % self.name)
#             self.event.set()
#             print('Produce notify : event cleared by %s '% self.name)
#             self.event.clear()

# if __name__ == '__main__':
#     t1 = producer(items, event)
#     t2 = consumer(items, event)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

# import threading
# import logging
# logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

# def threading_with(statement):
#     with statement:
#         logging.debug('%s acquired via with' % statement) #去掉with的输出结果见最下，去掉with会使unlocked

# def threading_not_with(statement):
#     statement.acquire()
#     try:
#         logging.debug('%s acquired directly' % statement )
#     finally:
#         statement.release()

# if __name__ == '__main__':
#     # let's create a test battery
#     lock = threading.Lock()
#     rlock = threading.RLock()
#     condition = threading.Condition()
#     mutex = threading.Semaphore(1)
#     threading_synchronization_list = [lock, rlock, condition, mutex]
#     # in the for cycle we call the threading_with e threading_no_with function
#     for statement in threading_synchronization_list :
#        t1 = threading.Thread(target=threading_with, args=(statement,))
#        t2 = threading.Thread(target=threading_not_with, args=(statement,))
#        t1.start()
#        t2.start()
#        t1.join()
#        t2.join()
       
       
       
'''
(Thread-7  ) <locked _thread.lock object at 0x000001A04BCA15D0> acquired via with
(Thread-8  ) <locked _thread.lock object at 0x000001A04BCA15D0> acquired directly
(Thread-9  ) <locked _thread.RLock object owner=7092 count=1 at 0x000001A04BCA11B0> acquired via with
(Thread-10 ) <locked _thread.RLock object owner=17816 count=1 at 0x000001A04BCA11B0> acquired directly
(Thread-11 ) <Condition(<locked _thread.RLock object owner=17364 count=1 at 0x000001A04BCA10F0>, 0)> acquired via with
(Thread-12 ) <Condition(<locked _thread.RLock object owner=19476 count=1 at 0x000001A04BCA10F0>, 0)> acquired directly
(Thread-13 ) <threading.Semaphore object at 0x000001A04BCA1970> acquired via with
(Thread-14 ) <threading.Semaphore object at 0x000001A04BCA1970> acquired directly
       
'''
       
'''
(Thread-7  ) <unlocked _thread.lock object at 0x0000022C841515D0> acquired via with
(Thread-8  ) <locked _thread.lock object at 0x0000022C841515D0> acquired directly
(Thread-9  ) <unlocked _thread.RLock object owner=0 count=0 at 0x0000022C841511B0> acquired via with
(Thread-10 ) <locked _thread.RLock object owner=18440 count=1 at 0x0000022C841511B0> acquired directly
(Thread-11 ) <Condition(<unlocked _thread.RLock object owner=0 count=0 at 0x0000022C841510F0>, 0)> acquired via with 
(Thread-12 ) <Condition(<locked _thread.RLock object owner=9884 count=1 at 0x0000022C841510F0>, 0)> acquired directly
(Thread-13 ) <threading.Semaphore object at 0x0000022C84151970> acquired via with
(Thread-14 ) <threading.Semaphore object at 0x0000022C84151970> acquired directly
    
    
    
'''
        
# from threading import Thread
# from queue import Queue
# import time
# import random
# class producer(Thread):
#     def __init__(self, queue):
#         Thread.__init__(self)
#         self.queue = queue

#     def run(self) :
#         for i in range(10):
#             item = random.randint(0, 256)
#             self.queue.put(item)
#             print('Producer notify: item N° %d appended to queue by %s' % (item, self.name))
#             time.sleep(1)

# class consumer(Thread):
#     def __init__(self, queue):
#         Thread.__init__(self)
#         self.queue = queue

#     def run(self):
#         while True:
#             item = self.queue.get() #内置阻塞
#             print('Consumer notify : %d popped from queue by %s' % (item, self.name))
#             self.queue.task_done()

# if __name__ == '__main__':
#     queue = Queue()
#     t1 = producer(queue)
#     t2 = consumer(queue)
#     t3 = consumer(queue)
#     t4 = consumer(queue)
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     t4.join()
        

from threading import Thread

class threads_object(Thread):
    def run(self):
        function_to_run()

class nothreads_object(object):
    def run(self):
        function_to_run()

def non_threaded(num_iter):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(nothreads_object())
    for i in funcs:
        i.run()

def threaded(num_threads):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(threads_object())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()

def function_to_run():
    a, b = 0, 1
    for i in range(10000):
        a, b = b, a + b
def show_results(func_name, results):
    print("%-23s %4.6f seconds" % (func_name, results))

if __name__ == "__main__":
    import sys
    from timeit import Timer
    repeat = 100
    number = 1
    num_threads = [1, 2, 4, 8]
    print('Starting tests')
    for i in num_threads:
        t = Timer("non_threaded(%s)" % i, "from __main__ import non_threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("non_threaded (%s iters)" % i, best_result)
        t = Timer("threaded(%s)" % i, "from __main__ import threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("threaded (%s threads)" % i, best_result)
        print('Iterations complete')
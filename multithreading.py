from threading import Thread,current_thread
import os
#method 1
def func():
    print("Process ID: {}".format(os.getpid()))
    for x in range(10):
        print("Child Executing...", current_thread().getName())
        

t1 = Thread(target=func)
print(current_thread().getName())
t1.start()
t1.join()
print("Bye", current_thread().getName())

#method 2
class A(Thread):
    def run(self):
        for x in range(7):
            print("Child = ", current_thread().getName())
obj = A()
obj.start()
obj.join()
print("Control returned to ", current_thread().getName())

#method 3
class ex:
    def B(self):
        lst = [2,1,1,2,"hello"]
        for x in lst:
            print("Child printing",x)
myobj = ex()
t1= Thread(target=myobj.B)
t1.start()
t1.join()
print('done')

import threading
import time
class FooBar(threading.Thread):
	def __init__(self, n ,txt):
		super().__init__()
		self.n = n
		self.txt = txt
	def foo(self):
		for i in range(self.n):
			print("foo",end ='')
			time.sleep(1)

	def bar(self):
		for i in range(self.n):
			print("bar",end ='')
			time.sleep(1)

	def yeah(self):
		for i in range(self.n):
			print("yeah")
			time.sleep(1)

	def run(self):
		if self.txt == 'foo':
			self.foo()
		if self.txt == 'bar':
			self.bar()
		if self.txt == 'yeah':
			self.yeah()
n = int(input('input n:'))			
t1 = FooBar(n,'foo')
t2 = FooBar(n,'bar')
t3 = FooBar(n,'yeah')
t_list = []
t_list.append(t1)
t_list.append(t2)
t_list.append(t3)
t1.start()
t2.start()
t3.start()
for thread in t_list:
    thread.join()
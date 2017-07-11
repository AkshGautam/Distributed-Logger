import psutil
import subprocess
import datetime as dt
import time
import numpy as np
fw=open("output.txt","a")
class processes():
	def cpu_time(self):
		self.cpu_statistics=psutil.cpu_times()
		fw.write(str(self.cpu_statistics.idle))
		fw.write(",")
	def virtual_memory(self):
		self.memory_statistics=psutil.virtual_memory()
		fw.write(str(self.memory_statistics.available))
		fw.write(",")
	def net_io(self):
		self.network_statistics=psutil.net_io_counters()
		fw.write(str(self.network_statistics.bytes_recv-self.network_statistics.bytes_sent))

obj=processes()
for x in range(5):
	dateconv=np.vectorize(dt.datetime.fromtimestamp)
	date=dateconv(time.time())
	fw.write(str(date)+",")
	obj.cpu_time()
	obj.virtual_memory()
	obj.net_io()
	fw.write("\n")

import psutil
import subprocess
import datetime
import time
import sqlite3
user=system=idle=usedmem=availablemem=0
conn=sqlite3.connect('process.db')
cur=conn.cursor()
def create_table():
	cur.execute('CREATE TABLE IF NOT EXISTS cpulogs(user text,system text,idle text,usedmem text,availablemem text)')
def insert_into_table(user,system,idle,usedmem,availablemem):
	cur.execute("INSERT INTO cpulogs(user,system,idle,usedmem,availablemem)VALUES(?,?,?,?,?)",(user,system,idle,usedmem,availablemem))
	conn.commit()
class processes():
	def cpu_time(self):
		global user,sytem,idle
		self.cpu_statistics=psutil.cpu_times()
		user=self.cpu_statistics[0]
		system=self.cpu_statistics[2]
		idle=self.cpu_statistics[3]
	def virtual_memory(self):
		global usedmem,availablemem
		self.memory_statistics=psutil.virtual_memory()
		availablemem=self.memory_statistics[1]
		usedmem=self.memory_statistics[3]
	def disk_space(self):
		self.disk_use=psutil.disk_usage('/')
		

create_table()
obj=processes()
obj.virtual_memory()
obj.cpu_time()
print "user %s system %s idle %s usedmem %s availablemem %s" %(user,system,idle,usedmem,availablemem)
insert_into_table(user,system,idle,usedmem,availablemem)

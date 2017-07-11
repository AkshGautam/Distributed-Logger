import paramiko
import os.path
import sys
import subprocess
import time
import matplotlib.pyplot as plt
import csv
import numpy as np
import datetime as dt
import matplotlib.dates as md

import dateutil
# Add the device IP here comma separated
ip=["ip"]
# Add the device root password here,comma separated
passwd=["password"]
for x,y in zip(ip,passwd):
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	# ADD username
	ssh.connect(x,port=22,username='username',password=y)
	current_iter=0
	req_iter=3
	while(current_iter<req_iter):
		time.sleep(2)
		# Place the script.py in the desired location of remote computer
		stdin,stdout,stderr=ssh.exec_command("cd Desktop;python script.py")
		# replace username and output file path
		subprocess.call("sshpass -p "+y+" scp username@"+x+":/home/aksh/Desktop/output.txt .",shell=True)
		current_iter=current_iter+1
	if os.path.isfile("output.txt"):
		os.rename("output.txt",x+".txt")
# Plotting Graphs
for i in range(2):
	fig=plt.figure()
	x=[]
	y=[]
	z=[]
	w=[]
	with open('/home/aksh/web_app/Logger/'+ip[i]+'.txt','r') as csvfile:
		plots=csv.reader(csvfile,delimiter=',')
		for row in plots:
			x.append(dateutil.parser.parse(row[0]))
			y.append(float(row[1]))
			z.append(float(row[2]))
			w.append(float(row[3]))
	for i in x:
		print i
	ax1=fig.add_subplot(221)
	ax2=fig.add_subplot(222)
	ax3=fig.add_subplot(212)
	ax1.plot(x,y,label='bytes')
	ax2.plot(x,z,label="idl")
	ax3.plot(x,w,label="memory")
	plt.legend()
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Graph')
	plt.show()
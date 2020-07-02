#!/usr/bin/python3

import socket
import time
import threading
import sys
from queue import Queue
from datetime import datetime

socket.setdefaulttimeout(0.55)
print_lock = threading.Lock()
 
#Welcome
print("-" * 50)
print("Python Port Scanner 3000")
print("A project by The Mayor/Dievus")
print("-" * 50)
time.sleep(1)
target = input("Enter your target IP address or URL here: ")
error = ("Invalid Input!")

try:
	t_ip = socket.gethostbyname(target)
except Exception:
	print("\n\033[91m{}\033[00m".format(error))
	sys.exit()

#Banner
print("-" * 50)
print("Scanning target " + t_ip)
print("Time started: " + str(datetime.now()))
print("-" * 50)
t1 = datetime.now()

def portscan(port):

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
   try:
      conx = s.connect((t_ip, port))
      with print_lock:
         print("Port {} is open".format(port))
      conx.close()

   except:
      pass

def threader():
   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
  
q = Queue()
 
startTime = time.time()
 
for x in range(200):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()

for worker in range(1, 65535):
   q.put(worker)

q.join()

t2 = datetime.now()
total = t2 - t1
print("Port scan completed in "+str(total))
print("-" * 50)

print("Press the Enter button to exit...")
input()

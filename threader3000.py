#!/usr/bin/python3
# Threader3000 - Multi-threader Port Scanner
# A project by The Mayor
# v1.0.2
# https://github.com/dievus/threader3000
# Licensed under GNU GPLv3 Standards.  https://www.gnu.org/licenses/gpl-3.0.en.html


import socket
import signal
import time
import threading
import sys
import subprocess
from queue import Queue
from datetime import datetime

# Start Threader3000 with clear terminal
subprocess.call('clear', shell=True)

# Main Function
def main():
    socket.setdefaulttimeout(0.30)
    print_lock = threading.Lock()

# Welcome Banner
    print("-" * 60)
    print("        Threader 3000 - Multi-threaded Port Scanner          ")
    print("                       Version 1.0.2                    ")
    print("                   A project by The Mayor               ")
    print("-" * 60)
    time.sleep(1)
    target = input("Enter your target IP address or URL here: ")
    error = ("Invalid Input")
    try:
        t_ip = socket.gethostbyname(target)
    except Exception:
        print("\n[-]Invalid format. Please use a correct IP or web address[-]\n")
        sys.exit()
    #Banner
    print("-" * 60)
    print("Scanning target "+ t_ip)
    print("Time started: "+ str(datetime.now()))
    print("-" * 60)
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
    print("-" * 60)

    print("Press Enter to exit...")
    input()

if __name__ == '__main__':
    main()

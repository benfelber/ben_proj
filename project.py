import time
import subprocess
import multiprocessing

def run_sever():
    while True:
        try:
            subprocess.call("D:\server.py",shell=True)
        except:
            pass
#run_sever()

def run_client():
    while True:
        try:
            subprocess.call("D:\client.py",shell=True)
        except:
            pass
#run_client()

if __name__ =='__main__':
    p = multiprocessing.Process(target=run_sever, args=())
    p.start()
    p2 = multiprocessing.Process(target=run_client, args=())
    p2.start()
    raw_input("yyy")
from socket import socket,AF_INET,SOCK_STREAM
from sys import argv,exit
from threading import Thread
from time import sleep
from signal import signal , SIGINT

def handel(sig,frame):
    print("\nStop Program\n")
    exit()

class PortScanner:

    def __init__(self) -> None:
        self.args = argv[1:]
    
    def __Scanner(self,ip,port):
        try:
            Connection = socket(AF_INET,SOCK_STREAM)
            Connection.connect((ip,port))
            print("Open Port ",port)
            Connection.close()
        except Exception:
            print(f" {port}\r\r\r\r\r\r\r\r",end='\r')
    
    
    def _args(self):
        if self.args[0].strip() == '-h':
            print(f"""\nPortscanner Usage:\n\n-i,--ip    for ipaddress\n-p,--port  for port range\n-d,-delay  for delay between probes\n-h,--help  for usage help""")
            quit()
        args = {
            '-i':self.args[1],
            '--ip':self.args[1],
            '-p':int(self.args[3]),
            '--port':int(self.args[3]),
            '-d':float(self.args[5]),
            '--delay':float(self.args[5])
        }
        
        if not self.args[0] in ['-i','--ip']:
            quit(f"Invalid args {self.args[0]}")
        if not self.args[2] in ['-p','--port']:
            quit(f"Invalid args {self.args[2]}")
        if not self.args[4] in ['-d','--delay']:
            quit(f"Invalid args {self.args[4]}")
        
        for port in range(args.get('-p')):
            signal(SIGINT,handel)
            th = Thread(target=self.__Scanner,args=(args.get('-i'),port))
            th.start()
            sleep(args.get('-d'))



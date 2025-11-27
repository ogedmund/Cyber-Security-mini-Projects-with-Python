#importing modules
import sys
import socket
import pyfiglet


ascii_banner = pyfiglet.figlet_format("Python 4 Pentesters \nPort Scanner")
print(ascii_banner)


ip = '192.168.1.6'   #specifying the target
open_ports =[]   #An empty “open_ports” array that will be populated later with the detected open ports

ports = range(1, 65535) # Ports that will be probed 


def probe_port(ip, port, result = 1):   #Tries to connect to the port
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result


for port in ports:   #for loop that iterates through the specified port list
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    

if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("Looks like no ports are open :(")



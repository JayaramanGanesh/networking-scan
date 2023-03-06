#import nmap
import requests
import networkscan
import socket
import sys
import os
#import dns.resolver
import nmap 
import os
from time import *
from datetime import datetime
import random
from time import sleep



class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'
    
print("""\033[92m
    
███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗██████╗ ██╗██╗  ██╗
████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██╔══██╗██║╚██╗██╔╝
██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ██████╔╝██║ ╚███╔╝ 
██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██╔═══╝ ██║ ██╔██╗ 
██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗██║     ██║██╔╝ ██╗
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
                                                                                 \033[0m """)
print("====================================================================================")
print("""
  1.local network scan   
  2.Ip address open port scan    
  3.Ping Local Network Ip Address
  4.Ping Target ip Address 
  5.Domain DNS Lookup
      """)

userchoose = str(input("kindly mention scaning number:"))

if userchoose == "1":
    print("thank you for chooseing local network scan")
    print("ex : 192.168.?.0/24")
    my_network = str(input("kindly adreess the network ip range"))
    my_scan = networkscan.Networkscan(my_network)
    print("Network to scan: " + str(my_scan.network))
    print("Prefix to scan: " + str(my_scan.network.prefixlen))
    print("Number of hosts to scan: " + str(my_scan.nbr_host))
    print("Scanning hosts...")
    my_scan.run()
    print("List of hosts found:")
    for i in my_scan.list_of_hosts_found:
        print(i)
    print("Number of hosts found: " + str(my_scan.nbr_host_found))
    res = my_scan.write_file()
    if res:
        print("Write error with file " + my_scan.filename)
    else:
        print("Data saved into file " + my_scan.filename)

elif userchoose == "2":
    print("thank you for choosing ip open port scaning")
    target= str(input("kindly mention ip address : "))
    try:
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            if result == 0:
                print("port{} is open".format(port))
            s.close()
            
    except KeyboardInterrupt:
        print("\n Exiting Program !!!")
        
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!")
        sys.exit()
        
    except socket.error:
        print("\n Server Not Responding !!!")
        

elif userchoose == "3":
    print("thank you for chooseing Ping Local Network Ip Address")
    print("ex : 192.168.?.0/24")
    my_network = str(input("kindly adreess the network ip range :"))
    my_scan = networkscan.Networkscan(my_network)
    my_scan.run()
    adr = []
    for i in my_scan.list_of_hosts_found:
       adr.append(i)
    up =[] 
    down =[]    
    for i in adr:
        response = os.popen(f"ping -c 4 {i} ").read()
        if("Request timed out." or "unreachable") in response:
            print(response)
            down.append(i)
        else:
            print(response)
            up.append(i)
    print("sumarry of up devices")
    print(up)
    print("sumarry of down devices")
    print(down)
    
elif userchoose == "4":
    print("Thank you for choosing ping the target")
    target = str(input("mention the target ip address :"))
    my_scan = networkscan.Networkscan(target)
    my_scan.run()
    adr = []
    for i in my_scan.list_of_hosts_found:
      adr.append(i)    
    for i in adr:
        response = os.popen(f"ping -c 6 {i} ").read()
        if("Request timed out." or "unreachable") in response:
            print(response)
            print("target address is down or offline")
        else:
            print(response)
            print("target address is online and up")
            
elif userchoose == "5":
    print("thank you for choosing dns lookup we are try to find domain ip address ")
    target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
    try:
        print("\033[34m[~] Scanning Nmap Port Scan: \033[0m" + target)
        scanner = nmap.PortScanner()
        command = ("nmap - " + target)
        process = os.popen(command)
        results = str(process.read())
        logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        print(results + command + logPath)
        print("\033[34mNmap Version: \033[0m", scanner.nmap_version())

    except KeyboardInterrupt:
        print("\n")
        print("[-] User Interruption Detected..!")
        time.sleep(1)
        
elif userchoose == "6":
    print("thank you for choosing the whois domain")
    try:
        target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
        os.system("reset")
        print("\033[34m[~] Searching for Whois Lookup: \033[0m".format(target) + target)
        time.sleep(1.5)
        command = ("whois " + target)
        proces = os.popen(command)
        results = str(proces.read())
        print(results + command)

    except Exception:
        print("kindly once verified the domain address")
        pass


 
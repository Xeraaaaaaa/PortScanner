import PortScanner

ip = '192.168.140.129 , 127.0.0.1 , 192.168.140.255'
firstPort = 1
lastPort = 100

if ',' in ip:
    for ipAddr in ip.split(","):
        PortScanner.scan(ipAddr.strip(" "), firstPort, lastPort)

else:
    PortScanner.scan(ip, firstPort, lastPort)

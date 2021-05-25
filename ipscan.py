import PortScanner

ip = 'www.google.com' # Can be written as IP Address or website. Websites will be converted into their IP Address.
firstPort = 1
lastPort = 100

if ',' in ip:
    for ipAddr in ip.split(","):
        PortScanner.scan(ipAddr.strip(" "), firstPort, lastPort)

else:
    PortScanner.scan(ip, firstPort, lastPort)

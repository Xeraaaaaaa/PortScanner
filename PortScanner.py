import socket
from IPy import IP

# Port 80 is assigned to HTTP
# port = input('[+] Enter Port Number')

def scanPort(ipaddress, port):
    try:
        openCount = 0
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = getBanner(sock)
            print('[+] Port ' + str(port) + ' Is Open. Banner: ' + str(banner))
            openCount += 1


        except:
            print('[+] Port ' + str(port) + ' Is Open.')
            openCount += 1

    except:
        pass



def checkIP(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scan(target,firstPort,lastPort):
    convertedIP = checkIP(target)
    print("\n" + '[Scanning Target] ' + str(target))

    for port in range(int(firstPort),int(lastPort)):
        scanPort(convertedIP, port)


def getBanner(s):
    return s.recv(1024).decode().strip('\r').strip('\n')

if __name__ == "__main__":
    targets = input('[+] Enter IP Address/es To Scan. Syntax: xxx.xxx.xxx.xxx,xxx.xxx.xxx.xxx ')
    portNumStart = input('[+] First Port Number: ')
    portNumEnd = input('[-] Last Port Number: ')


    if ',' in targets:
        for ipAddr in targets.split(","):
            scan(ipAddr.strip(" "),portNumStart,portNumEnd)

    else:
        scan(targets,portNumStart,portNumEnd)

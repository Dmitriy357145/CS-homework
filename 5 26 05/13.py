from ipaddress import *
c=0
ip_net = ip_network('122.14.129.32/255.255.128.0',0)
for ip in ip_net:
    x = str(ip).split('.')[-1]
##    print(x,ip)
    if x=='255':
        c+=1
print(c)

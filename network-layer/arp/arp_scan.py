#email:dazhuang_python@sina.com
#date:20190421


from concurrent.futures.thread import ThreadPoolExecutor
from scapy.all import srp,Ether,ARP,conf
conf.verb=0

def handle_arp_address(ip_address):
    ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address),timeout=2)
    for snd,rcv in ans:
        print (rcv.sprintf(r"%Ether.src% & %ARP.psrc%"))

ip_list = ["192.168.0."+str(i) for i in range(1,254)]
t = ThreadPoolExecutor()
thread_list = []
for ip in ip_list:
    thread = t.submit(handle_arp_address,ip)
    thread_list.append(thread)
t.shutdown()

from concurrent.futures.thread import ThreadPoolExecutor
from scapy.all import sr,IP,ICMP,conf


conf.verb = 0
def detect_alive_hosts(scan_hosts):
    ans, unans = sr(IP(dst=scan_hosts) / ICMP(), retry=0, timeout=2)
    for snd,rcv in ans:
        print(rcv.sprintf(r"%IP.src% is alive"))


if __name__ == '__main__':
    ip_list = ["192.168.0."+str(i) for i in range(1,255)]
    t = ThreadPoolExecutor(50)
    thread_list = []
    for ip in ip_list:
        thread = t.submit(detect_alive_hosts,ip)
        thread_list.append(thread)
    t.shutdown()

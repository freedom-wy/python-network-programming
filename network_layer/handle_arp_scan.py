from multiprocessing.pool import ThreadPool
from scapy.all import *


def arp_request(ip_address, ifname='ens33'):
    # 获取本机IP地址
    localip = get_ip_address(ifname)
    # 获取本机MAC地址
    localmac = get_mac_address(ifname)
    try:  # 发送ARP请求并等待响应!
        result_raw = sr1(ARP(op=1,
                             hwsrc=localmac, hwdst='00:00:00:00:00:00',
                             psrc=localip, pdst=ip_address),
                             iface=scapy_iface(ifname),
                             timeout=1,
                             verbose=False)

        return ip_address, result_raw.getlayer(ARP).fields['hwsrc']

    except AttributeError:
        return ip_address, None


# if __name__ == "__main__":
#     # Windows Linux均可使用
#     arp_result = arp_request('10.1.1.252', "Net1")
#     print("IP地址:", arp_result[0], "MAC地址:", arp_result[1])


def scapy_arp_scan(network,ifname):
    net = ipaddress.ip_network(network)
    ip_list = []
    for ip_add in net:
        ip_list.append(str(ip_add))  # 把IP地址放入ip_list的清单
    pool = ThreadPool(processes=100)  # 创建多进程的进程池（并发为100）
    result = []
    for i in ip_list:
        result.append(pool.apply_async(arp_request,args=(i,ifname))) # 关联函数与参数，并且添加结果到result
    pool.close()  # 关闭pool，不在加入新的进程
    pool.join()  # 等待每一个进程结束
    scan_list = []  # 扫描结果IP地址的清单
    for r in result:
        if r.get()[1] is None:  # 如果没有获得MAC，就continue进入下一次循环
            continue
        scan_list.append(r.get()[0])  # 如果获得了MAC，就把IP地址放入scan_list清单
    return sort_ip(scan_list)  # 排序并且返回清单


if __name__ == '__main__':
    # Windows Linux均可使用
    import time

    t1 = time.time()
    print('活动IP地址如下:')
    for ip in scapy_arp_scan("10.1.1.0/24", 'Net1'):
        print(str(ip))
    t2 = time.time()
    print('本次扫描时间: %.2f' % (t2 - t1))  # 计算并且打印扫描时间
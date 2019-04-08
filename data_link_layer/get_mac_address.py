import psutil

network_info = psutil.net_if_addrs()
#获取所有网络信息
print(network_info)
#获取有线网卡的MAC地址
print(network_info['以太网'][0].address)

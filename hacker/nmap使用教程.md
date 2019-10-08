# python-network-programming
### nmap教程
1、-A 全面扫描，nmap -A 192.168.1.1  
2、扫描地址段，nmap 192.168.1.1-200  
3、-sP ping扫描，nmap -sP 192.168.1.1  
4、-P0 无ping扫描，nmap -P0 192.168.1.1输出比ping扫描多一点，无ping扫描可以在目标主机禁ping的情况下使用  
5、-PS TCP SYN Ping扫描，nmap -PS -v 192.168.1.1  
6、-PA TCP ACK Ping扫描，这种方式扫描可以探测阻止SYN包或ICMP请求的主机，nmap -PA -v 192.168.1.1  
7、-PU UDP Ping扫描，nmap -PU -v 192.168.1.1  
8、-PR ARP Ping扫描，nmap -PR 192.168.1.1，也可以直接扫一个段，nmap -PR 192.168.1.0/24  
9、-n 禁止DNS反向解析  
10、-R反向解析域名  
11、-6 扫描IPv6地址，nmap -6 2408:8207:7842:8100:15e1:dfd:958e:7b3c  
12、-PY SCTP INIT Ping扫描  
13、nmap --traceroute -v www.163.com，路由跟踪
14、TCP协议编号为6，UDP协议编号为17，ICMP协议编号为1，IGMP协议编号为2  
15、nmap -T0和-T1 非常慢的扫描，用于IDS逃避  
16、nmap -sS 192.168.1.1 使用syn发包方式探测  
17、nmap -sT 192.168.1.1 使用TCP三次握手方式发包探测  
18、nmap -sU 192.168.1.1 使用Udp方式发包探测，速度非常慢，建议使用-p 限定端口  
19、nmap -sN 192.168.1.1 是Null扫描，是通过发送非常规的TCP通信数据包对计算机进行探测的  
20、nmap -sF 192.168.1.1 发送FIN数据包进行探测，可以很好的穿透防火墙  
21、nmap -sW 使用TCP的窗口进行扫描  
22、nmap -sI www.0day.co:80 192.168.1.1 利用僵尸主机www.0day.co的主机对192.168.1.1进行空闲扫描，如果有IDS，IDS会把www.0day.co当做扫描者。  
23、nmap -sV 192.168.1.1 启用版本探测，可以联合-A使用  
24、nmap -sV --allports 192.168.1.1 全端口探测  
25、nmap -sV --version-trace 192.168.1.1 获取详细版本信息  
26、nmap -f -v 192.168.1.1 使用报文分段方式进行扫描  
27、nmap -D RND:11 192.168.1.1 伪造11个源地址进行扫描，注意在版本检测和TCP扫描的时候，伪造的源地址是无效的,并且伪造的源IP地址必须是工作的  
28、nmap --source-port 53 192.168.1.1 伪造源端口扫描  
29、nmap --script ip-geolocation-* www.baidu.com ip地址信息搜集  
30、nmap -A -oN test.txt 192.168.1.1 保存结果到text.txt  
31、nmap -A -oX test.xml 192.168.1.1 保存结果到text.xml

***
不定期分享一些python开发,逆向破解、渗透测试相关文章,欢迎大家关注.  
![微信公众号](gongzhonghao.jpg)
***
BUG:dazhuang_python@sina.com
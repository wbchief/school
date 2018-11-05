import requests
from pyquery import PyQuery as pq

url = 'http://jwgl.cust.edu.cn/teachwebsl/login.aspx'
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
username = '2016002028'
passwoed = '076710'

response = requests.get(url, headers=header)
html = response.text
doc = pq(html)

VIEWSTATE = doc('#__VIEWSTATE[value]').attr['value']
EVENTVALIDATION = doc('#__EVENTVALIDATION[value]').attr['value']

s = requests.session()
datas = {'__VIEWSTATE': VIEWSTATE, '__EVENTVALIDATION': EVENTVALIDATION,
                                    'txtUserName': username, 'txtPassWord': passwoed, 'Button1': '登录'}
login = s.post(url, headers=header, data=datas)

response = s.get('http://jwgl.cust.edu.cn/teachweb/index1.aspx', headers=header)
print(response.text)
# response = requests.get('http://jwgl.cust.edu.cn/teachweb/index1.aspx', headers=header, cookies=login.cookies)
# print(response.text)
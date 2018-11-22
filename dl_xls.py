import requests
from PIL import Image
import os,sys,datetime
sys.path.append('C:\\Users\\quiet_wang\\Desktop\\python')
from chaojiying import *

os.chdir('C:\\Users\\quiet_wang\\Desktop\\python')
cjy_username = 'wdpanjing'
cjy_password = 'wdp1008'
cjy_soft_id = 897341
cjy_style = 1006
vcode_header = {
'Accept':'image/webp,image/*,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,pt;q=0.4',
'Connection':'keep-alive',
'Host':'investorservice.cfmmc.com',
'Referer':'https://investorservice.cfmmc.com/login.do',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,pt;q=0.4',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'141',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'investorservice.cfmmc.com',
'Origin':'https://investorservice.cfmmc.com',
'Referer':'https://investorservice.cfmmc.com/login.do',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
data = {'org.apache.struts.taglib.html.TOKEN': '50e9e4f8161c52fae5f5e291b3835f59',
        'showSaveCookies': '',
        'userID': '017888000079',
        'password': '123456cyqh',
        'vericode':''
        }
codeurl = 'https://investorservice.cfmmc.com/veriCode.do'
logurl = 'https://investorservice.cfmmc.com/login.do'
downloadurl = 'https://investorservice.cfmmc.com/customer/setupViewCustomerDetailFromCompanyWithExcel.do'

success = 0
try_num = 0
while success == 0 & try_num < 3:
    s = requests.session()
    try_resp = s.post(logurl)
    vcode = s.get(codeurl)
    f=open('vcode.png','wb')
    f.write(vcode.content)
    f.close()
    f=open('vcode.png','rb')
    cjy = Chaojiying_Client(cjy_username,cjy_password,cjy_soft_id)
    result = cjy.PostPic(f,cjy_style)
    data['vericode'] = result['pic_str']
    resp = s.post(logurl,headers=headers,data=data)
    ok_resp = s.get(downloadurl)
    filename = str(datetime.date.today())
    f = open(filename+'.xls','wb')
    f.write(ok_resp.content)
    f.close()
    filesize = os.path.getsize(filename+'.xls')/float(1024)
    if filesize < 100:
        print('Downlaod fail')
        cjy.ReportError(result['pic_id'])
        try_num = try_num + 1
    else:
        print('Download OK')
        success = 1

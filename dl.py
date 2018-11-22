#!/usr/bin/python
import requests, re
import time, sys, os, optparse
from requests_toolbelt import MultipartEncoder

def download():
    data = {
        'Name': 'S1060',
        'Pass': 'Wdp1008',
        'ACTION': 'LOGIN',
        'Send': 'Submit'
    }
    url = "http://dtdinfo.realtek.com.tw:8080/cgi-bin/cgiwrap/bk_adm/download_cad2.pl"
    s = requests.session()
    resp = s.post(url, data=data)
    r = re.compile("ID=.*\d")
    m = r.search(str(resp.text))
    id_me = m.group().split("=")[1]
    dl_data = {
        'ACTION': 'LIST',
        'ID': id_me
    }
    dl_list = s.get(url, params=dl_data)
    file_list = re.findall("option value=\"(.*)\"", dl_list.text)
    for f in file_list:
        print(str(file_list.index(f)) + "\t" + f)
    num = input("Please input download number:")
    num = str(num)
    if not num.isdigit():
        print("You input wrong number")
    else:
        file_name = file_list[int(num)]
        dl_data = {
            "ID": id_me,
            "ACTION": "GET",
            "FILE": file_name,
            ".submit": "Download",
            ".cgifields": "FILE"
        }
        with open(file_name, "wb") as f:
            dl = s.post(url, dl_data)
            f.write(dl.content)
            f.close()

def upload(user, filename):
    url = "http://dtdinfo.realtek.com.tw:8080/cgi-bin/cgiwrap/bk_adm/upload_cad-2.pl"
    data = {
        'Name': 'S1060',
        'Pass': 'Wdp1008',
        'ACTION': 'LOGIN',
        'Send': 'Submit'
    }
    s = requests.session()
    resp = s.post(url, data=data)
    r = re.compile("value=\"(.*\d)")
    m = r.search(str(resp.text))
    id_me = m.group(1)
    m = MultipartEncoder(fields={
        "RECEIVER": user,
        "upload_file": (filename, open(filename, 'rb'), "image/png"),
        "ACTION": "UPLOAD",
        "ID": id_me,
        "Send": "Submit"
    })
    s.post(url, data=m, headers={"Content-type": m.content_type})

def_user = os.popen("whoami").read().rstrip("\n")
user_msg = """
    %prog [options] arg1 arg2
    Example:
        dl.py -u S10XX test.txt
        dl.py -d
"""
parser = optparse.OptionParser(usage=user_msg)
parser.add_option("-d","--download",action="store_true",dest="download",default=False,help="Download file from cadinfo")
parser.add_option("-u","--user",action="store",dest="user",default=def_user,help="Enter the upload user,exp S1060")
opts,args = parser.parse_args()
if opts.download:
    print("Download file begin...")
    download()
elif opts.user:
    user = opts.user
    if args:
        for f in args:
            upload(user,f)
            print("Upload file: %s successfully !"%f)
    else:
        msg = "Must have a file for uploading, ex."+os.path.basename(sys.argv[0]) +" -u S10XX filename \n"
        print(msg)
        parser.print_help()

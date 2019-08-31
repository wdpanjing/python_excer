import struct
'''
JPEG (jpg) FFD8FF
PNG (png) 89504E47
GIF (gif) 47494638
TIFF (tif) 49492A00
Windows Bitmap (bmp) 424D
CAD (dwg) 41433130
Adobe Photoshop (psd) 38425053
Rich Text Format (rtf) 7B5C727466
XML (xml) 3C3F786D6C
HTML (html) 68746D6C3E
Email [thorough only] (eml) 44656C69766572792D646174653A
Outlook Express (dbx) CFAD12FEC5FD746F
Outlook (pst) 2142444E
MS Word/Excel (xls.or.doc) D0CF11E0
MS Access (mdb) 5374616E64617264204A
'''
def typeList():
    return {
        "68746D6C3E": "html",
        "D0CF11E0": "xls",
        "89504E47":"png",
        "FFD8FF":"jpg"}

def bytes2hex(bytes):
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()


# 获取文件类型
def fileguess(filename):
    binfile = open(filename, 'rb')  # 必需二制字读取
    tl = typeList()
    ftype = 'unknown'
    for hcode in tl.keys():
        numOfBytes = int(len(hcode) / 2)  # 需要读多少字节
        binfile.seek(0)  # 每次读取都要回到文件头，不然会一直往后读取
        hbytes = struct.unpack_from("B" * numOfBytes, binfile.read(numOfBytes))  # 一个 "B"表示一个字节
        f_hcode = bytes2hex(hbytes)
        if f_hcode == hcode:
            ftype = tl[hcode]
            break
    binfile.close()
    return ftype

if __name__ == '__main__':
    print(fileguess('1.xls'))

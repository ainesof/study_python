import os, urllib
from urllib import request
from urllib.error import URLError


def ipchk(ip):
    """IP접속가능여부 체크"""
    try:
        req = request.urlopen(ip, timeout=0.5)
        return ip
    except URLError:
        pass

if __name__ == '__main__':
    try:
        ip=[]
        ip.append('http://192.168.123.3:5000')
        ip.append('http://192.168.123.4:5000')
        ip.append('http://192.168.123.5:5000')
        ip.append('http://11.10.5.34:5000')
        req=''

        print('업데이트 시작')
        for i,val in enumerate(ip):
            req=ipchk(val)
            if req:
                break
        if req:
            print("접속지:",req)
            url = req+'/static/file/main.exe'
            urllib.request.urlretrieve(url, "main.exe")
            print("다운 완료\n프로그램이 재시작됩니다.")
            os.startfile('main.exe')
        else:
            print("접속 불가")
            os.system('pause')

    except:
        print('에러 발생')
        os.system('pause')




import os, urllib
from urllib import request
from urllib.error import URLError
import time


def ipchk(ip):
    """IP접속가능여부 체크"""
    try:
        req = request.urlopen(ip, timeout=0.5)
        return ip
    except URLError:
        pass

if __name__ == '__main__':
    try:
        version='2021-12-31'
        ip=[]
        ip.append('http://192.168.123.3:5000')
        ip.append('http://11.10.5.34:5000')
        req=''

        print('애드온 버전:'+version+'\n프로그램 업데이트 시작')
        for i,val in enumerate(ip):
            req=ipchk(val)
            if req:
                break
        if req:
            print("접속지:",req)
            url = req+'/static/file/main.exe'
            urllib.request.urlretrieve(url, "main.exe")
            if os.path.exists('main.exe'):
                print("다운 완료\n 몇초 뒤 프로그램이 재시작됩니다.")
                time.sleep(2)
                os.startfile('main.exe')
            else:
                print("파일이 생성되지 않았습니다.")
        else:
            print("서버에 접속할 수 없습니다")
            os.system('pause')

    except:
        print('알 수 없는 에러로 패치가 중단되었습니다')
        os.system('pause')




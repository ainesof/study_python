import os
import traceback, datetime
import ftplib,logging,logging.handlers

def kfr_getfile():
    """ftp에서 특정파일 받음"""
    try:
        path = 'D://kfr_data//imsi//'
        files=['KFRFV42','KFRFV34','KFRFV33','KFRFV30','KFRFV29',
                        'KFRCV25','KFRCV24','KFRCV23','KFRCV22','KFRCV21',
                        'KFRCV20','KFRCV19','KFRCM99','KFRCM32','KFRFV28',
                        'KFRFV26','KFRFV18','KFRFV17','KFRFV16','KFRFV15',
                        'KFRFV14','KFRFV13','KFRFV12','KFRFV11','KFRCM10',
                        'KFRCM09','KFRCM08','KFRCM07','KFRCM06','KFRCM05',
                        'KFRCM04','KFRCM02','KFRCM01']

        def findfile(filename,cnt):
            timediff = datetime.timedelta(days=cnt)
            days = (today + timediff).strftime('%Y%m%d')
            downfile = filename + '.' + days
            folder = path + downfile

            if downfile in ftp.nlst():
                if os.path.exists(folder):
                    print(downfile+' 이미 존재')
                else:
                    with open(folder, 'wb') as file:
                        ftp.retrbinary('RETR %s' % downfile, file.write)
                        print(downfile + ' 다운로드')
                        logger.debug(downfile + ' 다운로드')
            elif cnt>-7:
                findfile(filename,cnt-1)
            else:
                print(filename+' 다운로드 실패')
                logger.debug(filename+' 다운로드 실패')

        if os.path.exists(path):
            logger, logfile = setlog(path)
            user={'id':'heungkuk', 'password': 'gmdrnr!@'}
            ftp=ftplib.FTP('211.62.79.4',user['id'],user['password'])
            # ftp.retrlines('LIST')

            today=datetime.date.today()
            cnt=-1
            logger.debug('다운로드 시작 '+str(files))
            for i in files:
                findfile(i,cnt)
            print('끝')
            logger.debug('종료')
            logger.removeHandler(logfile)
        else:
            print('저장경로가 존재하지 않습니다 ' + path)

        # https://jinisbonusbook.tistory.com/62
        # https://kgu0724.tistory.com/49
        return '0'

    except:
        print(traceback.format_exc())
        logger.debug(traceback.format_exc())

def setlog(path):
    """로그파일 세팅"""
    logger = logging.getLogger('root')
    filename='log_test.log'
    logfile = logging.handlers.RotatingFileHandler(path+filename, maxBytes=1024 * 1024 * 10,backupCount=10)
    formatter = logging.Formatter(' %(asctime)s %(message)s')
    logfile.setFormatter(formatter)
    logger.addHandler(logfile)
    logger.setLevel(logging.DEBUG)
    return logger, logfile

if __name__ == '__main__':
    kfr_getfile();



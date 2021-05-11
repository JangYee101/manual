
import signal
import time


def CtrlCFunc(signo, unkown):
    """
    可以再这里写关闭后的操作
    """
    print 'you had Ctrl+C!'
    print signo
    print unkown
    exit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, CtrlCFunc)
    while True:
        print "hello world!"
        time.sleep(1)

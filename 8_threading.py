import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for ii in xrange(5):
            print 'thread - {0} - sleeping for a second'.format(ii)
            time.sleep(1)

thr = MyThread()
thr.start()

for ii in xrange(5):
    print 'main thread - {0} - sleeping for a second'.format(ii)
    time.sleep(1)

thr.join()

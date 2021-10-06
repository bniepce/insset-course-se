import threading, time


class SimpleThread(threading.Thread):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def run(self):
        for i in range(0, 10):
            print('Thread {} is at {}'.format(self.name, i))
            time.sleep(0.1)

T1 = SimpleThread("T1")
T1.start()

T2 = SimpleThread("T2")
T2.start()
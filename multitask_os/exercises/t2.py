import threading, time


class WaitThread(threading.Thread):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.state = False
    
    def run(self):
        self.state = True
        for i in range(0, 10):
            print('Thread {} is at {}'.format(self.name, i))
            time.sleep(0.1)
        self.state = False

T1 = WaitThread('T1')
T1.start()


print('Début')

while T1.state == False:
    time.sleep(0.1)

while T1.state == True:
    print('l')
    time.sleep(0.1)

print('Fin')
    
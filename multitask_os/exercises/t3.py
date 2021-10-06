import threading, time

class EventThread(threading.Thread):
    
    def __init__(self, name, event):
        super().__init__()
        self.name = name
        self.event = event
    
    def run(self):
        for i in range(0, 10):
            print('Thread {} is at {}'.format(self.name, i))
            time.sleep(0.1)
        self.event.set()
        

E = threading.Event()
E.clear()

T1 = EventThread('T1', E)
T1.start()
E.wait()

print('Event done.')
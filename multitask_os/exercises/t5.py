from threading import Semaphore, Thread
import time
S = Semaphore(3)

def talk(person_name):
    S.acquire()
    for i in range(3):
        print("{} est en train de parler ...".format(person_name))
        time.sleep(1)
    print('{} part'.format(person_name))
    S.release()

names = [chr(x) for x in range(ord('a'), ord('z') + 1)][:6]
threads = [Thread(target=talk, args=(i, )) for i in names]
for t in threads:
    t.start()
    
    
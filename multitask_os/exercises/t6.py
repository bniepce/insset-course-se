from threading import Lock, Thread
import time


def talk(person_name, mutex):
    mutex.acquire(1)
    for i in range(3):
        print("{} est en train de parler ...".format(person_name))
        time.sleep(1)
    print('{} part'.format(person_name))
    mutex.release()
    
mutex = Lock()
names = [chr(x) for x in range(ord('a'), ord('z') + 1)][:6]
threads = [Thread(target=talk, args=(i, mutex)) for i in names]
for t in threads:
    t.start()
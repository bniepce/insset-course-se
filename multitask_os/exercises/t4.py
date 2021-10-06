from threading import Thread, Event
import time



event = Event()


def set_list(num_list, q_in, q_out):
    while True:
        if not q.empty():
            q_in = q.get()
            for i in range(len(d)):
                d[i] += 1
            q_out.put(d)
        if event.is_set():
            break
        time.sleep(0.1)

n = [1, 2, 3, 4, 5]
Q = Queue()
Q.put(n)

T1 = Thread(target=set_list, args=(n, Q))
T2 = Thread(target=set_list, args=(n, Q))

T1.start()
T2.start()

while True:
    try:
        print(n)
        time.sleep(1)
    except KeyboardInterrupt:
        event.set()
        break

event.set()
T1.join()
T2.join()

print(n)
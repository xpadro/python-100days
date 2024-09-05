import threading


class Timer:

    def __init__(self, fun):
        self.event = threading.Event()
        self.event.set()
        self.t = threading.Thread(target=fun, args=(self.event,))
        self.t.start()

    def stop(self):
        self.event.clear()

import threading

class IntervalScheduler:
    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.stop_event = threading.Event()
        self.thread = None

    def start(self):
        if not self.thread or not self.thread.is_alive():
            self.stop_event.clear()
            self.thread = threading.Thread(target=self._run)
            self.thread.daemon = True
            self.thread.start()

    def _run(self):
        while not self.stop_event.wait(self.interval):
            self.function(*self.args, **self.kwargs)

    def stop(self):
        self.stop_event.set()
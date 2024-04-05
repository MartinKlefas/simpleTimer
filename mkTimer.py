import time

class Timer:
    def __init__(self):
        self.start_times = {}
        self.stop_times = {}
        self.loop_times = {}

    def start(self, event_name):
        self.start_times[event_name] = time.time()

    def stop(self, event_name):
        self.stop_times[event_name] = time.time()
        
    def start_looped(self, event_name):
        if event_name not in self.loop_times:
            self.loop_times[event_name] = []
        self.loop_times[event_name].append(time.time())

    def stop_looped(self, event_name):
        if event_name in self.loop_times:
            self.loop_times[event_name][-1] = time.time() - self.loop_times[event_name][-1]


    def get_elapsed_time(self, event_name):
        start = self.start_times.get(event_name)
        stop = self.stop_times.get(event_name)

        if start is None or stop is None:
            return None

        return stop - start

    def report(self):
        retval = ""
        for event_name in self.start_times:
            elapsed_time = self.get_elapsed_time(event_name)
            if elapsed_time is not None:
                retval+=f'Elapsed time for {event_name}: {elapsed_time} seconds\n'
                
        for event_name in self.loop_times:
            times = self.loop_times.get(event_name)
            if times:
                avg_time = sum(times) / len(times)
                retval+=f'There were {len(times)} repeats of {event_name}, average duration was: {avg_time} seconds\n'
        return retval
import time, io, csv


class Timer:
    def __init__(self):
        self.start_times = {}
        self.stop_times = {}
        self.loop_times = {}
        self.event_stack = []

    def start(self, event_name):
        self.start_times[event_name] = time.time()
        self.current_event_name = event_name
        self.event_stack.append(event_name)
        return self

    def stop(self, event_name=None):
        if event_name is None:
            if self.event_stack:
                event_name = (
                    self.event_stack.pop()
                )  # Pop the last event name from the stack
            else:
                raise ValueError("No event name provided and no event names in stack.")
        else:
            if event_name in self.event_stack:
                self.event_stack.remove(
                    event_name
                )  # Remove the specified event name from the stack
            else:
                raise ValueError("Event name provided not found in stack.")

        self.stop_times[event_name] = time.time()

    def lap(self, new_event_name):
        # Stops the last started timer and starts a new one
        self.stop()
        return self.start(new_event_name)

    def lap_looped(self, new_event_name):
        # Stops the last started timer and starts a new one
        self.stop_looped()
        return self.start_looped(new_event_name)

    def start_looped(self, event_name):
        if event_name not in self.loop_times:
            self.loop_times[event_name] = []
        self.loop_times[event_name].append(time.time())
        self.event_stack.append(event_name)
        return self

    def stop_looped(self, event_name=None):
        if not event_name:
            event_name = self.event_stack.pop()
        else:
            self.event_stack.remove(event_name)

        if event_name in self.loop_times:
            self.loop_times[event_name][-1] = (
                time.time() - self.loop_times[event_name][-1]
            )

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
                retval += f"Elapsed time for {event_name}: {elapsed_time} seconds\n"

        for event_name in self.loop_times:
            times = self.loop_times.get(event_name)
            if times:
                avg_time = sum(times) / len(times)
                retval += f"There were {len(times)} repeats of {event_name}, average duration was: {avg_time} seconds\n"
        return retval

    def reportCSV(self):
        listdictresults = []
        for event_name in self.start_times:
            elapsed_time = self.get_elapsed_time(event_name)
            listdictresults.append(
                {"event_name": event_name, "repeats": 1, "Time": elapsed_time}
            )

        for event_name in self.loop_times:
            times = self.loop_times.get(event_name)
            if times:
                avg_time = sum(times) / len(times)
                listdictresults.append(
                    {"event_name": event_name, "repeats": len(times), "Time": avg_time}
                )

        output = io.StringIO()
        fieldnames = ["Event", "Repeats", "(avg) Duration"]
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        for row in listdictresults:
            writer.writerow(
                {
                    "Event": row["event_name"],
                    "Repeats": row["repeats"],
                    "(avg) Duration": row["Time"],
                }
            )

        csv_string = output.getvalue()

        output.close()

        return csv_string

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

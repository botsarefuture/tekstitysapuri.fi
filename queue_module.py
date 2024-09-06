import threading


class Queue:
    def __init__(self, runners):
        self.runners = runners
        self.task_queue = []

    def add_task(self, task):
        self.task_queue.append(task)
        self.run_queue()

    def run_queue(self):
        while self.task_queue:
            task = self.task_queue.pop(0)  # Get the first task in the queue
            runner = self.get_free_runner()

            if runner:
                threading.Thread(target=runner.run_task, args=(task,)).start()

    def get_free_runner(self):
        for runner in self.runners:
            if not runner.is_busy():
                return runner
        return None

# python3

from collections import namedtuple
# from test import test

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
Thread = namedtuple("Thread", ["number", "next_free_time"])


class Threads:
    def __init__(self, n_threads):
        self.threads = [Thread(number, 0) for number in range(n_threads)]
        self.size = len(self.threads)


    def shift_down(self, index):
        while True:
            min_index = index
            left_index = 2*index + 1
            right_index = 2*index + 2
            left_child = self.threads[left_index] if left_index < self.size else None
            right_child = self.threads[right_index] if right_index < self.size else None

            if left_child and left_child.next_free_time < self.threads[min_index].next_free_time:
                min_index = left_index
            elif left_child and left_child.next_free_time == self.threads[min_index].next_free_time:
                if left_child.number < self.threads[min_index].number:
                    min_index = left_index
 
            if right_child and right_child.next_free_time < self.threads[min_index].next_free_time:
                min_index = right_index
            elif right_child and right_child.next_free_time == self.threads[min_index].next_free_time:
                if right_child.number < self.threads[min_index].number:
                    min_index = right_index
            
            if index != min_index:
                self.threads[index], self.threads[min_index] = self.threads[min_index], self.threads[index]
                index = min_index
            else:
                break


    def assign_job(self, duration):
        new_thread = self.threads[0]
        self.threads[0] = Thread(new_thread.number, new_thread.next_free_time + duration)
        self.shift_down(0)
        return new_thread


def assign_jobs(n_workers, jobs):
    result = []
    threads = Threads(n_workers)
    for job in jobs:
        next_worker = threads.assign_job(job)
        result.append(AssignedJob(next_worker.number, next_worker.next_free_time))

    return result


def main():
    # test(assign_jobs)
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()

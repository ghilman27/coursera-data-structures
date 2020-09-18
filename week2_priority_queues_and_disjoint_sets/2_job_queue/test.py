import random
import gc
from collections import namedtuple


MIN_THREADS = 1
MAX_THREADS = 100000
MIN_JOBS = 1
MAX_JOBS = 1000_000_000
MIN_DURATION = 0
MAX_DURATION = 1000_000_000
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def test(myfunc):
    while True:
        n_workers = random.randint(MIN_THREADS, MAX_THREADS)
        n_jobs = random.randint(MIN_JOBS, MAX_JOBS)
        jobs = []
        for _ in range(n_jobs):
            jobs.append(random.randint(MIN_DURATION, MAX_DURATION))
        assert len(jobs) == n_jobs

        ref_solution = assign_jobs(n_workers, jobs)
        my_solution = myfunc(n_workers, jobs)

        print("INPUT:")
        print(n_workers, n_jobs)
        print(jobs)
        if ref_solution == my_solution:
            print("OK")
        else:
            print("ERROR")
            print("REF SOLUTION")
            for job in ref_solution:
                print(job.worker, job.started_at)
            print("------------------------------------")
            print("MY SOLUTION")
            for job in my_solution:
                print(job.worker, job.started_at)
            break

        gc.collect()
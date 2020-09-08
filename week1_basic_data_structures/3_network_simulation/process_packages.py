# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, request):
        # write your code here
        # 1. Check finished processes
        while len(self.finish_time) > 0 and self.finish_time[0] <= request.arrived_at:
            self.finish_time.popleft()

        # 2. Check buffer availability
        start_time = request.arrived_at if len(self.finish_time) == 0 else self.finish_time[-1]
        if len(self.finish_time) < self.size:
            finish_time = start_time + request.time_to_process
            self.finish_time.append(finish_time)
            return Response(was_dropped=False, started_at=start_time)
        
        return Response(was_dropped=True, started_at=start_time)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()

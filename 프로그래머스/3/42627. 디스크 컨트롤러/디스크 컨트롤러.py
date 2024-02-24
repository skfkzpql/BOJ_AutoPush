import heapq

def solution(jobs):
    answer = 0
    length = len(jobs)
    heap = []
    jobs.sort()  # 요청 시점을 기준으로 정렬

    current_time, total_time = 0, 0
    while jobs or heap:
        # 현재 시간 이전에 요청이 들어온 작업들을 heap에 추가
        while jobs and jobs[0][0] <= current_time:
            request_time, processing_time = jobs.pop(0)
            heapq.heappush(heap, (processing_time, request_time))

        if heap:
            processing_time, request_time = heapq.heappop(heap)
            current_time += processing_time
            total_time += (current_time - request_time)
        else:
            # 현재 시간에 요청이 들어온 작업이 없다면 가장 먼저 들어오는 작업을 수행
            request_time, processing_time = jobs.pop(0)
            current_time = request_time + processing_time
            total_time += processing_time

    answer = total_time // length
    return answer


def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True) 
    n = len(jobs)
    max_deadline = max(job[1] for job in jobs)
    slots = [False] * max_deadline
    job_order = [None] * max_deadline
    total_profit = 0
    for job in jobs:
        for j in range(min(max_deadline, job[1]) - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                job_order[j] = job[0]
                total_profit += job[2]
                break
    return [job for job in job_order if job is not None], total_profit

def activity_selection(activities):
    activities.sort(key=lambda x: x[1]) 
    n = len(activities)
    selected = [activities[0]]
    last_finish = activities[0][1]
    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]
    return selected

if __name__ == "__main__":
    jobs = [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
    order, profit = job_scheduling(jobs)
    print("Job Scheduling:")
    print(f"Order: {order}")
    print(f"Total Profit: {profit}\n")

    activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
    selected = activity_selection(activities)
    print("Activity Selection:")
    print(f"Selected activities: {selected}")

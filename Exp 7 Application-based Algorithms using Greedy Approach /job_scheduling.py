class Job:
    """Job class to store deadline and profit"""
    def __init__(self, deadline=0, profit=0):
        self.deadline = deadline
        self.profit = profit


def main():
    size = int(input("Enter total job count: "))
    jobs = []
    max_deadline = 0
    
    print("Enter job details:")
    for i in range(size):
        deadline = int(input(f"- Enter job {i + 1} deadline: "))
        profit = int(input(f"  Enter job {i + 1} profit: "))
        jobs.append(Job(deadline, profit))
        if i == 0:
            max_deadline = deadline
        else:
            if max_deadline < deadline:
                max_deadline = deadline
    
    # Sort by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    slots = [0] * max_deadline
    selected_jobs = [Job()] * max_deadline
    
    total_profit = 0
    for i in range(size):
        s = jobs[i].deadline
        for k in range(s - 1, -1, -1):
            if slots[k] == 0:
                slots[k] = 1
                total_profit += jobs[i].profit
                selected_jobs[k] = jobs[i]
                break
    
    print(f"Total profit: {total_profit}")
    print("Selected jobs:")
    for i in range(max_deadline):
        if selected_jobs[i].deadline > 0:
            print(f"{selected_jobs[i].profit}({selected_jobs[i].deadline})")


if __name__ == "__main__":
    main()

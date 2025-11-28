MAX = 100


def activity_selection(start, finish, n):
    """Activity Selection using greedy approach"""
    # Selection sort
    for i in range(n - 1):
        min_pos = i
        for j in range(i + 1, n):
            if finish[j] < finish[min_pos]:
                min_pos = j
        # Swap finish
        finish[i], finish[min_pos] = finish[min_pos], finish[i]
        # Swap start
        start[i], start[min_pos] = start[min_pos], start[i]
    
    print("\nSelected activities: ", end="")
    last_finish = finish[0]
    print("1 ", end="")  # first activity
    
    for i in range(1, n):
        if start[i] >= last_finish:
            print(f"{i + 1} ", end="")
            last_finish = finish[i]
    print()


def main():
    n = int(input("Enter number of activities: "))
    
    start = []
    finish = []
    
    print("Enter start and finish times:")
    for i in range(n):
        times = input(f"Activity {i + 1}: ").split()
        start.append(int(times[0]))
        finish.append(int(times[1]))
    
    activity_selection(start, finish, n)


if __name__ == "__main__":
    main()

def greedy_job_scheduling(jobs):
    # Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    schedule = [None] * max_deadline

    for job in jobs:
        for slot in range(job[1] - 1, -1, -1):
            if schedule[slot] is None:
                schedule[slot] = job
                break

    scheduled_jobs = [job[0] for job in schedule if job]
    total_profit = sum(job[2] for job in schedule if job)
    
    return scheduled_jobs, total_profit


if __name__ == "__main__":
    n = int(input("Enter number of jobs: "))
    jobs = []
    for _ in range(n):
        name, deadline, profit = input("Enter job name, deadline, profit: ").split()
        jobs.append((name, int(deadline), int(profit)))

    result, profit = greedy_job_scheduling(jobs)

    print("\nScheduled Jobs in order:", result)
    print("Total Profit:", profit)

# # OUTPUT
# PS C:\Users\Asus\OneDrive\Desktop\LP2> python 3rd.py               
# Enter number of jobs: 4
# Enter job name, deadline, profit: a 4 20
# Enter job name, deadline, profit: b 1 20
# Enter job name, deadline, profit: c 1 30
# Enter job name, deadline, profit: d 1 22 

# Scheduled Jobs in order: ['c', 'a']
# Total Profit: 50
# PS C:\Users\Asus\OneDrive\Desktop\LP2> 

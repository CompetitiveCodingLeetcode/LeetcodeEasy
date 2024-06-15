def decimat_to_binary(num):
    temp_num=num
    binary = ""
    while temp_num/2 != 0:
        d = temp_num%2
        d = str(d)
        binary = d + binary
        temp_num=temp_num//2
    return binary

def check_for_consecutive1s(s:str):
    for i in range(len(s)-1):
        ch1 = s[i]
        ch2 = s[i+1]
        if ch1 == '1' and ch2 == '1':
            return True
    return False

num = 2
count=0
for i in range(num+1):
    binary = decimat_to_binary(i)
    if check_for_consecutive1s(binary):
        count+=1

print(num+1 - count)
# print("binary=",decimat_to_binary(3))



"""
G Question PS round:

Let's say that we have an OS for scheduling user jobs and we have different algos that the OS uses for scheduling. For this question, let's say
that the OS uses a FCFS algorithm - the OS prioitizes the job that was submitted earlier. 

We are given a list of jobs, the time they were submitted at and the time they take to finish the job. We want to print the start time and the end time
of each job in the order that the OS would schedule them. 

Include a priority value. 
[10,4,p1][12,8,p2][10,1,p3][15,4,p4]
single job 



[10,1][10,2][15,4]
[10,11][11,13][15,19]

[10,5] --> [10,15]
[10,2] --> [15,17]
[12,8] ---> [17,25]

node:
  start_time
  time_taken
  priority_value

def get_job_time(job_schedule):
  n = len(job_schedule)
  job_start_end_time = []
  start_time = job_schedule[0][0]
  end_time = start_time + job_schedule[0][1]
  job_start_end_time.append([start_time,end_time])
  for i in range(1,n):
    prev_job_end_time = job_start_end_time[i-1][1]
    start_time = job_schedule[i][0]
    if start_time <= prev_job_end_time:
      start_time = prev_job_end_time
    end_time = start_time + job_schedule[i][1]
    
    job_start_end_time.append([start_time,end_time])
   
  return job_start_end_time

def get_sorted_job_schedule(jobs):
  jobs = jobs.sort(key = lambda x:x[0])
  get_job_time(job_schedule)
"""
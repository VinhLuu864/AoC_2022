monkeyNumbers = {}
jobs = {}

file21 = open('Inputs/input21')
for line in file21:
    line = line.strip().split()
    if len(line) == 4: #This would mean it is a job.
        jobs[line[0][:-1]] = line[1:]
    else:
        monkeyNumbers[line[0][:-1]] = eval(line[1])


deleteThis = []
while 'root' not in monkeyNumbers:
    for job in jobs.keys():
        if jobs[job][0] in monkeyNumbers and jobs[job][2] in monkeyNumbers:
            #Operations
            if jobs[job][1] == '+':
                monkeyNumbers[job] = monkeyNumbers[jobs[job][0]] + monkeyNumbers[jobs[job][2]]
            if jobs[job][1] == '-':
                monkeyNumbers[job] = monkeyNumbers[jobs[job][0]] - monkeyNumbers[jobs[job][2]]
            if jobs[job][1] == '*':
                monkeyNumbers[job] = monkeyNumbers[jobs[job][0]] * monkeyNumbers[jobs[job][2]]
            if jobs[job][1] == '/':
                monkeyNumbers[job] = int(monkeyNumbers[jobs[job][0]] / monkeyNumbers[jobs[job][2]])
            deleteThis.append(job)

    for delete in deleteThis:
        if delete in jobs.keys():
            del jobs[delete]

print(monkeyNumbers['root'])
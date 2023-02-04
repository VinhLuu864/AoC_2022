import numpy as np
from sklearn.linear_model import LinearRegression

monkeyNumbers = {}
jobs = {}

file21 = open('Inputs/input21')
for line in file21:
    line = line.strip().split()
    if len(line) == 4: #This would mean it is a job.
        jobs[line[0][:-1]] = line[1:]
    else:
        monkeyNumbers[line[0][:-1]] = eval(line[1])

#Part 2 specific stuff
del monkeyNumbers['humn']
jobs['root'] = [jobs['root'][0], '-', jobs['root'][2]]

def fitFunc(jobs, monkeyNumbers, humnNum):
    monkeyNumbers['humn'] = humnNum
    deleteThis = []
    canDelete = True
    while canDelete:
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
                    monkeyNumbers[job] = monkeyNumbers[jobs[job][0]] / monkeyNumbers[jobs[job][2]]
                deleteThis.append(job)

        for delete in deleteThis:
            if delete in jobs.keys():
                del jobs[delete]
        if len(deleteThis) == 0:
            canDelete = False
        deleteThis = []
    return monkeyNumbers['root']


model = LinearRegression()
x = np.linspace(1, 10e12, 101).reshape(-1, 1)
print(x)
y = fitFunc(jobs, monkeyNumbers, x)
model.fit(x, y)

print(min(-model.intercept_ / model.coef_)[0])
#We get 3769668716708.9985. Answer was correct when rounded up.
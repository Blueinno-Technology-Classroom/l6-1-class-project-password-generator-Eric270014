import random

head_tail = random.randint(0, 1) # 0 ~ 1

if (head_tail == 0):
    print('tail')
else:
    print('head')


rps =  random.randint(0, 2)
if (rps == 0):
    print('rock')
elif (rps == 1):
    print('paper')
elif (rps == 2):
    print(sizzors)

options = ['rock', 'paper', 'sizzors']
rps = random.choice(options)
print(rps)




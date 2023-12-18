import numpy as np
player=3
size=1000
inputs = [[0 for _ in range(size)] for _ in range(player*3)]

for i in range(player):
    for s in range(3):
        for j in range(size):
            inputs[3*i+s][j]=np.random.randint(0,1000,1)[0]

result=[0 for _ in range(player)]
# Calculate the Maximum
for i in range(player):
    for s in range(3):
        for j in range(size):
            if int(inputs[3*i+s][j])>int(result[i]):
                result[i]=inputs[3*i+s][j]
print(result)
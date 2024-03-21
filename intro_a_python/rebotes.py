

def throwBall(times):
    height = 100
    height = height * (3/5) ** times
    return height

times = 10

for time in range(1, times + 1):
    print(round(throwBall(time), 2))


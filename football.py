def pointcout(results):
    points = 0
    for match in results:
        if int(match[0])>int(match[2]):
            points+=3
        elif int(match[0]) == int(match[2]):
            points+=1
    return points


import random
game_results = []
for i in range (0,10):
    game_results.append(str(random.randint(0,4))+";"+str(random.randint(0,4)))
print(game_results)
print(pointcout(game_results))

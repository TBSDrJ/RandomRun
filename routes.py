import networkx as nx
import random

map = nx.Graph()
map.add_nodes_from(range(1,21))
map.add_weighted_edges_from([
    (1,2,0.07),
    (2,2,0.15),
    (2,3,0.04),
    (2,4,0.06),
    (4,4,0.15),
    (3,6,0.03),
    (3,12,0.16),
    (11,11,0.06),
    (12,12,0.06),
    (6,11,0.05),
    (6,9,0.07),
    (9,14,0.05),
    (9,13,0.10),
    (14,20,0.05),
    (13,10,0.06),
    (20,20,0.06),
    (19,19,0.06),
    (18,18,0.06),
    (20,19,0.06),
    (18,19,0.06),
    (17,18,0.04),
    (4,5,0.05),
    (5,7,0.05),
    (7,8,0.05),
    (8,10,0.05),
    (10,16,0.08),
    (10,15,0.05),
    (15,16,0.12),
    (15,17,0.05)
])

currentNode = 2
history = [1,2]
historyIndex = 0
stepNum = 0
totalDistance = 0
# targetDistance = int(input("Roughly how many miles do you want to go? "))
targetDistance = 4
minDistance = targetDistance * 0.75
while totalDistance < minDistance:
    possibleNodes = map[currentNode]
    choices = list(possibleNodes.keys())
    choices.remove(history[historyIndex])
    historyIndex += 1
    print(history[historyIndex], choices)
    currentNode = random.choice(choices)
    history.append(currentNode)
    # print(currentNode, possibleNodes[currentNode]['weight'])
    if currentNode == 1:
        break

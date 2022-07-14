import math

opp = input('Enter the opposite side value: ')
adj = input('Enter the adjecent side value: ')

div_of_adj_and_opp = int(opp) / int(adj)

print(div_of_adj_and_opp)

result = math.tan(div_of_adj_and_opp)

print(result)
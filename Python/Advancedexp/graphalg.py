
################################## SIMPLE GRAPH ALGORITHMS ###########################

first_graph_vertex = ['London','Brisbane','Paris']

first_graph_edge = [['London','Paris'],['Paris','London'],['Brisbane','Brisbane']]

# How many unique flights can I go on around my 'world'?

print(len(first_graph_edge))

# Can I go one-way from Brisbane to Paris?

for i in range(len(first_graph_edge)):
    if first_graph_edge[i] == ['Brisbane','Paris']:
        print('Yes, you can')
    else:
        print('No, you can\'t')

# Are there any return flights?

print(range(len(first_graph_edge)))


'''
for i in range(len(first_graph_edge)):
    for j in range(len(first_graph_edge[1])):
        if first_graph_edge[i][j] == [[j],[i]]:
            print('Found a return flight!')
'''


################################## SIMPLE GRAPH ALGORITHMS ###########################

places = ['London','Brisbane','Paris','Milan','NYC']

flights = [['London','Paris'],['Paris','London'],['Brisbane','Paris'],['Milan','London'],['NYC','Milan']]

# How many unique flights can I go on around my 'world'?

print(len(flights))

# Can I go one-way from Brisbane to Paris? (Flight availability checker)

found = 0
for i in range(len(flights)):
    if flights[i] == ['Brisbane','Paris']:
        found = 1
        print('Yes, you can')

if found == 0:
    print('No, you can\'t')


# Are there any return flights?

# For each departure and arrival combination, see if the flipped version exists



'''
for i in range(len(flights)):
    for j in range(0,1):
        if ( (flights[i][0] == flights[i][1])
        and (flights[j][0] == flights[j][1]) ):
            print('Found a return flight!')

print(flights[0][1])
'''

'''
for i in range(len(first_graph_edge)):
    for j in range(len(first_graph_edge)):
        if (first_graph_edge[i][1] == first_graph_edge[i][2])
        and (first_graph_edge[j][1] == first_graph_edge[j][2]):
            print('Found a return flight!')

'''

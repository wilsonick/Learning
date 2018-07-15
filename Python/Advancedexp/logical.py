pa = pb = pc = True

# not / and or ( iff implies )

# Generate all possible logical statements from five connectives and three propositions. 

# Loop through all 8 combinations of truth values. 

for i in range(8)



not pa and pb == pa or pb
pa or pb and not pc == True



# Store and evaluate whether not not a is a:

# Evaluate LHS and RHS of the logical connective

LHS = not not not pa 
RHS = pa

if LHS == RHS:
    print('Yes!')

propa = not pa

LHS = not not not pa
RHS = pa

if LHS == RHS:
    print('Yes, both!')




with open("05_update_input.txt", "r") as file:
    lines = [line.strip().split(",") for line in file]

updates = [[int(num) for num in line] for line in lines]

with open("05_rule_input.txt", "r") as file:
    lhs = []
    rhs = []
    
    for line in file:
        left, right = line.strip().split("|")

        lhs.append(int(left))
        rhs.append(int(right))

validUpdates = []
invalidUpdates = []

for update in updates:
    valid = True
    processed = []
    for num in update:
        if valid == False:
            break

        #loop through rhs, if num exists here, there is a number that has to be before it
        for i,j in enumerate(rhs):
            #if num exists on rhs, there is a rule that a number needs to be before it
            #if that number exists in the update and hasn't already been processed, this update is invalid
            if rhs[i] == num and lhs[i] in update and lhs[i] not in processed:
                valid = False
        
        processed.append(num)
    
    if valid:
        validUpdates.append(update)
    else:
        invalidUpdates.append(update)

#reorder invalidupdates, doing this in a seperate loop just to simplify logic, not caring about speed
reorderedInvalidUpdates = []
for invalidUpdate in invalidUpdates:
    is_changed = True
    while is_changed:
        is_changed = False
        for i in range(len(lhs)):
            if lhs[i] in invalidUpdate and rhs[i] in invalidUpdate:
                lhs_index = invalidUpdate.index(lhs[i])
                rhs_index = invalidUpdate.index(rhs[i])
                
                if rhs_index < lhs_index:
                    invalidUpdate[lhs_index], invalidUpdate[rhs_index] = invalidUpdate[rhs_index], invalidUpdate[lhs_index]
                    is_changed = True

    reorderedInvalidUpdates.append(invalidUpdate)



#sum of middle elements
total_middle_sum = 0
for sub_array in validUpdates:
    middle_element = sub_array[len(sub_array) // 2]
    total_middle_sum += middle_element

print("Sum of middle elements:", total_middle_sum)

#sum of middle elements for reordered ones
total_middle_sum_reordered = 0
for sub_array in reorderedInvalidUpdates:
    middle_element = sub_array[len(sub_array) // 2]
    total_middle_sum_reordered += middle_element

print("Sum of middle elements:", total_middle_sum_reordered)
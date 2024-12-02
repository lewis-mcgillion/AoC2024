import numpy as np
data = np.loadtxt("./01_input.txt")


#pt1 total difference after ordering
col1 = data[:, 0]
col2 = data[:, 1]

col1_sorted = np.sort(col1)
col2_sorted = np.sort(col2)

difference_absolute = np.abs(col1_sorted - col2_sorted)
difference_total = np.sum(difference_absolute)

print(difference_total)


#pt2 similarity score

global_similarity = 0
for x in col1:
    occurences = np.count_nonzero(col2 == x)
    local_similarity = occurences * x
    global_similarity += local_similarity

print(global_similarity)
    


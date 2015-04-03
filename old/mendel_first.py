input = raw_input().split()
k,m,n = int(input[0]), int(input[1]), int(input[2])

total_dominant = (k * 2.0) + m
total_recessive = (n * 2.0) + m

population = total_dominant + total_recessive

prob = (total_recessive/population) * total_dominant/(population - 1.0) + (total_dominant/population)  

print prob

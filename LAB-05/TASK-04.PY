def compute_ratios(values):
    results=[]
    for i in range(len(values)):
        for j in range(i,len(values)):
            ratio=values[i]/(values[j]-values[i])
            results.append((i,j,ratio))
    return results
nums=[5,10,15,20,25]
try:
    print(compute_ratios(nums))
except ZeroDivisionError as e:
    print("Error: Division by zero occurred in compute_ratios.")
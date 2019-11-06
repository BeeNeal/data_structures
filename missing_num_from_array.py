def missing_num_optimized(lst):
    if lst:
        summ = sum(x for x in range(1, len(lst)+2))
        return  summ - sum(lst)
    else:
        return 0

print(missing_num_optimized([1,2,3,5]))
print(missing_num_optimized([]))
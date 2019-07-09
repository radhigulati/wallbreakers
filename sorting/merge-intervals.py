def merge(intervals):
    if len(intervals) < 1:
        return []
    sortedIntervals = sorted(intervals)
    res = [sortedIntervals[0]]
    for first_time, last_time in sortedIntervals[1:]:
        last_merged_start, last_merged_end = res[-1]
        if first_time <= last_merged_end:
            res[-1] = (last_merged_start, max(last_time, last_merged_end))
        else:
            res.append([first_time, last_time])
    return res


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [4, 5]]))

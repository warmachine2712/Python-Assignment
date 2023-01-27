def temp(list, target):
    l = len(list)
    for i in range(l-1):
        for j in range(l-1):
            if (list[i] + list[j+1]) == target:
               return [list[i],list[j+1]]

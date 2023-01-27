def temp(s1,s2):
    m = len(s1)
    n = len(s2)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    temp_set =set()
    for i in range(m):
        for j in range(n):
            if s1[i]==s2[j]:
                c = counter[i][j]+1
                counter[i+1][j+1] =c
                if c > longest:
                    temp_set = set()
                    longest = c
                    temp_set.add(s1[i-c+1:i+1])
                elif c == longest:
                    temp_set.add(s2[i-c+1:i+1])
    return temp_set

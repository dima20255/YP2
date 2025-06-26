def comb(cand, target):
    cand.sort()
    res = []
    def backtrack(i, path, t):
        if t == 0:
            res.append(path)
            return
        if t < 0:
            return
        for j in range(i, len(cand)):
            if j > i and cand[j] == cand[j-1]:
                continue
            backtrack(j+1, path + [cand[j]], t - cand[j])
    backtrack(0, [], target)
    return res

print(comb([2,5,2,1,2], 5))
print(comb([10,1,2,7,6,1,5], 8))

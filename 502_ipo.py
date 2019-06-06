class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):

        projects = sorted([[i, j ] for i, j in zip(Profits, Capital)])

        if k == 0 and min(Capital) > 0: return 0
        if k > len(projects): k = len(projects)

        count = 0
        for i in range(k):
            for j in range(len(projects) - 1, -1, -1):
                if projects[j][1] <= W:
                    W += projects[j][0]
                    del projects[j]
                    count += 1
                    break
        return W

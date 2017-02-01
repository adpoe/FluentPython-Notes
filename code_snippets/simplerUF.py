# From: https://github.com/UmassJin/Leetcode/


class UnionFind:
    def __init__(self, n):
        self.father = [i for i in xrange(n)]
        self.ranks = [0 for i in xrange(n)]

    def find(self, x):
        if self.father[x] == x:
            return x
        return find(self.father[x])

    def do_union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.ranks[x] < self.ranks[y]:
            self.father[x] = y
        else:
            self.father[y] = x
            if self.ranks[x] == self.ranks[y]:
                self.ranks[x] += 1

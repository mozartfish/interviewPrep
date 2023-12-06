class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1
    
    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        # map email to accounts 
        emailToAccount = {} 

        for index, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccount:
                    uf.union(index, emailToAccount[email])
                else:
                    emailToAccount[email] = index 
        # print(emailToAccount)

        emailGroup = collections.defaultdict(list)
        for email, index in emailToAccount.items():
            leader = uf.find(index)
            emailGroup[leader].append(email)
        
        # print(emailGroup)

        result = []
        for index, email in emailGroup.items():
            name = accounts[index][0]
            result.append([name] + sorted(emailGroup[index]))
        
        return result
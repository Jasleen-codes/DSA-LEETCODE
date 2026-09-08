class Solution:
    def findPrimePairs(self, n):
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False

        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        result = []

        for x in range(2, n // 2 + 1):
            y = n - x

            if prime[x] and prime[y]:
                result.append([x, y])

        return result
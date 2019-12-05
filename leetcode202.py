def isHappy(self, n: int) -> bool:
        while n >= 9:
            n = sum(map(lambda k : k * k, [int(d) for d in str(n)]))
        if n == 7:
            return True
        return n == 1
        

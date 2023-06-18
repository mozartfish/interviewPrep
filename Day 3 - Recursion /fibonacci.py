# runtime - O(2^n)
# space - O(n) additional space because we are using additional stack space for every recursive call 
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n 
        return self.fib(n - 1) + self.fib(n - 2)
        
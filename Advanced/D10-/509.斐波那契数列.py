
class Solution:
    def fib(self, n: int) -> int:

        self.memory = {0: 0, 1: 1}

        return self.sub_fib(n)

    def sub_fib(self, n: int) -> int:
        if n in self.memory:
            return self.memory[n]
        else:
            result = self.sub_fib(n-2) + self.sub_fib(n-1)
            self.memory[n] = result
            return result

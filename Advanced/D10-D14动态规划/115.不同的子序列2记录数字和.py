
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        self.s, self.t = s, t 

        self.str_dict = {}

        self.N = len(self.t)

        for index, i in enumerate(s):
            if i in self.t:
                if i in self.str_dict:
                    self.str_dict[i].append(index)
                else:
                    self.str_dict[i] = [index]

        for i in self.t:
            if i not in self.str_dict:
                return 0
        
        self.records = {}
        def explode_path(position_on_target, position_on_s):
            """
            返回后面有多少个正确路径
            """

            if (position_on_target, position_on_s) in self.records:
                return self.records[(position_on_target, position_on_s)]

            if position_on_target > self.N:
                self.records[(position_on_target, position_on_s)] = 0
                return self.records[(position_on_target, position_on_s)]
            elif position_on_target == self.N:
                self.records[(position_on_target, position_on_s)] = 1
                return self.records[(position_on_target, position_on_s)]

            target_char = self.t[position_on_target]
            next_positions = self.str_dict[target_char]

            result = 0
            for pos in next_positions:
                if pos > position_on_s:
                    result += explode_path(position_on_target + 1, pos)

            self.records[(position_on_target, position_on_s)] = result
            return result
                    
        result = explode_path(0,-1)
        return result

if __name__ == '__main__':
    solu = Solution()
    s = "rabbbit"
    t = "rabbit"

    s = "babgbag"
    t = "bag"
    result = solu.numDistinct(s,t)
    print(result)


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        self.s, self.t = s, t 

        self.str_dict = {}

        for index, i in enumerate(s):
            if i in self.t:
                if i in self.str_dict:
                    self.str_dict[i].append(index)
                else:
                    self.str_dict[i] = [index]

        for i in self.t:
            if i not in self.str_dict:
                return 0


        self.end_pos = len(t)

        self.final_counts = 0


        def explore_path(current_pos_on_target, pos):

            if current_pos_on_target >= self.end_pos:
                self.final_counts += 1
                return 0
            
            target_key = self.t[current_pos_on_target]
            next_pathes = self.str_dict[target_key]

            for next_pos in next_pathes:
                if next_pos <= pos:
                    continue
                explore_path(current_pos_on_target +1, next_pos)

        explore_path(0,-1)
        return self.final_counts

if __name__ == '__main__':
    solu = Solution()
    s = "rabbbit"
    t = "rabbit"

    s = "babgbag"
    t = "bag"
    result = solu.numDistinct(s,t)
    print(result)

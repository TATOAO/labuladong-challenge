class Solution:

    def largest_substring(self, s1, s2):
        
        return




    def minDistance(self, word1: str, word2: str) -> int:

        self.global_max = abs(len(word1) - len(word2)) + len(word2)
        self.records = {}
        self.records[word2] = 0

        self.char_maps = {}
        for i,var in enumerate(word1):
            if var in self.char_maps:
                self.char_maps[var].append(i)
            else:
                self.char_maps[var] = [i]

        for i in word2:
            pass

        all_possible_one_action = []

        return 1

    def minDistance_two_same_size(self, word1, word2):

        if len(word1) != len(word2):
            return -1

        
        for i in range(len(word1)):
            pass


    


    def sub_minDistance(self, word1, word2, previous_path_len):
        if previous_path_len + 1 > self.global_max:
            self.records[word1] = previous_path_len + 1
            return previous_path_len 
        if word1 in self.records:
            return self.records
            
        

if __name__ == '__main__':
    solu = Solution()
    word1 = "horse"
    word2 = "ros"
    result = solu.minDistance(word1, word2)

    print(result)

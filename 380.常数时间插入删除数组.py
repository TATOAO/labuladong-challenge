
import random
class ChainNode:
    def __init__(self, val, last = None, next=None):
        """TODO: Docstring for function.

        :arg1: TODO
        :returns: TODO

        """
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        node_chain = []

        while self != None:
            node_chain.append(self.val)
            self = self.next

        return str(node_chain)



class RandomizedSet:
    def __init__(self):
        self.chain = None
        self.chainSearch = {}
        self.indexSearch = {}
    


    def insert(self, val: int) -> bool:
        newNode = ChainNode(val, None)
    # the set is empty
        if self.chain == None:
            self.chain = newNode
            self.chainSearch[val] = newNode
            return True
        # val is already taken
        elif val in self.chainSearch:
            return False

        else:
            self.chainSearch[val] =newNode
            self.chain.next = newNode
            self.chain = newNode
            
            return True



    def remove(self, val: int) -> bool:
        if val in self.chainSearch:

    #
    #
    # def getRandom(self) -> int:
    #



rset = RandomizedSet()
rset.insert(1)


rset.chain
rset.chainSearch

rset.insert(2)
rset.insert(2)




##############################################################
# chain node won't work
##############################################################




class RandomizedSet:
    def __init__(self):
        self.store_list = []
        self.search_dict = {}
        self.length = 0

    def insert(self, val) -> bool:
        if val in self.search_dict:
            return False
        else:
            
            self.store_list.append(val)
            self.search_dict[val] = self.length
            self.length += 1
            return True

    def remove(self, val) -> bool:
        if val in self.search_dict:
            old_position = self.search_dict[val]
            last_position = self.length - 1
            last_value = self.store_list[last_position]



            self.store_list[last_position], self.store_list[old_position] =\
                self.store_list[old_position], self.store_list[last_position]

            self.search_dict[last_value] = old_position
            self.store_list.pop()

            self.search_dict.pop(val)
            self.length -= 1
            return True
        else:
            return False

    def getRandom(self):
        random_index = random.randint(0, self.length - 1)
        return self.store_list[random_index]
        





rset = RandomizedSet()
rset.insert(1)


rset.store_list
rset.search_dict

rset.insert(2)
rset.insert(2)
rset.insert(5)

rset.getRandom()

rset.remove(1)



[random.randint(1,5) for _ in range(10)]
[ rset.getRandom() for _ in range(10)]













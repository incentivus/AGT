<<<<<<< HEAD
import numpy as np


# chains = {'canonical': {}, 'forks': {1: {}, 2: {}}}


class Agents:
    agents = []
    agents_dic = []
    id = 1

    def __init__(self, user_name, hash_power=0, hash_effective=None):
        self.id = Agents.id
        self.user_name = user_name
        self.hash_power = hash_power
        self.hash_effective = hash_effective
        self.block_id_visible = []
        self.matrix_visible = []
        self.strategy = []
        self.blocks_for_mine = []
        self.agent_visible = []
        Agents.agents.append(self)
        Agents.agents_dic.append(self.__dict__)
        Agents.id += 1

    def createMatrixVisible(self, main_block_matrix, new_block_id):
        """
        create matrix of block.
        if chain of new block exist , add block end of it, else we add chain to matrix.
        :param main_block_matrix: Every element is a list af triple block_id,owner_id and fee.
        :param new_block_id: a triple (block_id,owner_id,fee) for new block is mine.
        :return: updated matrix_visible.
        """
        if new_block_id in self.block_id_visible:
            for ch in main_block_matrix:
                if new_block_id in ch:
                    row = [j for j in ch if j != new_block_id]
                    if row not in self.matrix_visible:
                        self.matrix_visible.append(ch)
                        return self.matrix_visible
                    else:
                        index = self.matrix_visible.index(row)
                        self.matrix_visible[index].append(new_block_id)
                        return self.matrix_visible
        else:
            return self.matrix_visible

    def policy(self):
        """
                #7
        #1#2#3#4#5
          #6
            This function writes by students!POLICY
        [{1:10,2:20}]
        :return: {'block':[hash for each block that they can mine it this is a
         dictionary of id block father and amount of hash],'strategy':[honest or DDos],
        'visibility':[if block is mined which agents can see it]}
        """
        pass

    def action(self, e, *args):
        """This function for DDos attack!"""
        args = np.array(args)
        sTilda = (1 + e * (1 - np.sum(args))) * self.hash_power
        return sTilda

    def callPolicy(self):
        """
        for each agent call policy and return vector of block
        """
        context = self.policy(self.hash_power, self.matrix_visible)
        self.blocks_for_mine = context['block']  ### همین جا باید کدوم بلاک چقدره رو جدا کنی!!!
        self.strategy = context['strategy']
        self.agent_visible = context['visibility']

    def checkOutputPolicy(self):
        """
        check sum of hash for each strategy and block be hash power.
        :return:
        """
        sum_strategy = sum(self.strategy)
        block = list(self.blocks_for_mine.key())
        sum_block = sum(block)
        if sum_block + sum_strategy != self.hash_power:
            self.strategy = 0
            self.blocks_for_mine = 0

    def hashOfEachBlockAfterAttack(self):
        """
        :return: a dictionary of block_id : hash after attack
        """
        hash_block = self.blocks_for_mine
        attack = self.hash_power - self.hash_effective
        for i in hash_block:
            j = hash_block[i] - attack
            hash_block[i] = j
        return hash_block

    def blocksAgentWantToMine(self):
        """
        Determine which blocks are wanted to mine!
        :return:list of id of blocks
        """
        block_and_hash = self.hashOfEachBlockAfterAttack()
        blocks = list(block_and_hash.keys())
        return blocks

    def __str__(self):
        return self.user, self.hash_power

    @staticmethod
    def createMatrixOfBlocksAgentsWantsToMine():
        """
        step 1: determine which blocks may be mine!
        :return: a matrix !
        """
        agents = Agents.agents
        matrix = [0] * len(agents)
        set_block = []
        agent_block = []
        for i in agents:
            v = {}
            b = i.blocksAgentWantToMine()
            set_block.append(b)
            v[i.id] = b
            agent_block.append(v)
        set_block.sort()
        set_block = set(set_block)
        k = 0
        for i in agents:
            for j in set_block:
                if j in agent_block[k][i.id]:
                    matrix[i.id][j] = i.hashOfEachBlockAfterAttack()[j]
                else:
                    matrix[i.id][j] = 0
                k += 1
        return matrix
=======
import numpy as np


# chains = {'canonical': {}, 'forks': {1: {}, 2: {}}}


class Agents:
    agents = []
    agents_dic = []
    id = 1

    def __init__(self, user_name, hash_power=0, hash_effective=None):
        self.id = Agents.id
        self.user_name = user_name
        self.hash_power = hash_power
        self.hash_effective = hash_effective
        self.block_id_visible = []
        self.matrix_visible = []
        self.strategy = []
        self.blocks_for_mine = []
        self.agent_visible = []
        Agents.agents.append(self)
        Agents.agents_dic.append(self.__dict__)
        Agents.id += 1

    def createMatrixVisible(self, main_block_matrix, new_block_id):
        """
        create matrix of block.
        if chain of new block exist , add block end of it, else we add chain to matrix.
        :param main_block_matrix: Every element is a list af triple block_id,owner_id and fee.
        :param new_block_id: a triple (block_id,owner_id,fee) for new block is mine.
        :return: updated matrix_visible.
        """
        if new_block_id in self.block_id_visible:
            for ch in main_block_matrix:
                if new_block_id in ch:
                    row = [j for j in ch if j != new_block_id]
                    if row not in self.matrix_visible:
                        self.matrix_visible.append(ch)
                        return self.matrix_visible
                    else:
                        index = self.matrix_visible.index(row)
                        self.matrix_visible[index].append(new_block_id)
                        return self.matrix_visible

        else:
            return self.matrix_visible

    def createMatrixForPolicy(self,fee):
        """
        this function create matrix for policy
        :return:
        """
        martix_visible_temp=self.matrix_visible
        list_len_row = []
        for row in self.matrix_visible:
            len_row = len(row)
            list_len_row.append(len_row)
        max_row = max(list_len_row)
        martix_visible_temp[max_row].append((0, 0, fee))
        return martix_visible_temp, fee
    def policy(self):
        """
                #7
        #1#2#3#4#5
          #6
            This function writes by students!POLICY
        [{1:10,2:20}]
        :return: {'block':[hash for each block that they can mine it this is a
         dictionary of id block father and amount of hash],'strategy':[honest or DDos],
        'visibility':[if block is mined which agents can see it]}
        """
        pass

    def action(self, e, *args):
        """This function for DDos attack!"""
        args = np.array(args)
        sTilda = (1 + e * (1 - np.sum(args))) * self.hash_power
        return sTilda

    def callPolicy(self,fee):
        """
        for each agent call policy and return vector of block
        """
        matrix_visible_temp=self.createMatrixForPolicy(fee)
        context = self.policy(self.hash_power, matrix_visible_temp)
        self.blocks_for_mine = context['block']  ### همین جا باید کدوم بلاک چقدره رو جدا کنی!!!
        self.strategy = context['strategy']
        self.agent_visible = context['visibility']

    def checkOutputPolicy(self):
        """
        check sum of hash for each strategy and block be hash power.
        :return:
        """
        sum_strategy = sum(self.strategy)
        block = list(self.blocks_for_mine.key())
        sum_block = sum(block)
        if sum_block + sum_strategy != self.hash_power:
            self.strategy = 0
            self.blocks_for_mine = 0

    def hashOfEachBlockAfterAttack(self):
        """
        :return: a dictionary of block_id : hash after attack
        """
        hash_block = self.blocks_for_mine
        attack = self.hash_power - self.hash_effective
        for i in hash_block:
            j = hash_block[i] - attack
            hash_block[i] = j
        return hash_block

    def blocksAgentWantToMine(self):
        """
        Determine which blocks are wanted to mine!
        :return:list of id of blocks
        """
        block_and_hash = self.hashOfEachBlockAfterAttack()
        blocks = list(block_and_hash.keys())
        return blocks

    def __str__(self):
        return self.user, self.hash_power

    @staticmethod
    def createMatrixOfBlocksAgentsWantsToMine():
        """
        step 1: determine which blocks may be mine!
        :return: a matrix !
        """
        agents = Agents.agents
        matrix = [0] * len(agents)
        set_block = []
        agent_block = []
        for i in agents:
            v = {}
            b = i.blocksAgentWantToMine()
            set_block.append(b)
            v[i.id] = b
            agent_block.append(v)
        set_block.sort()
        set_block = set(set_block)
        k = 0
        for i in agents:
            for j in set_block:
                if j in agent_block[k][i.id]:
                    matrix[i.id][j] = i.hashOfEachBlockAfterAttack()[j]
                else:
                    matrix[i.id][j] = 0
                k += 1
        return matrix
>>>>>>> a8487a6afdd8848fe4f3c9b8275da37f54a8021a
#!/usr/bin/env python
# coding: utf-8

# ## Bi Directional BFS

# In[1]:


from collections import deque as dq
 
# class for queue
class node :
    def __init__(self, w, l):
        self.word=w
        self.len=l
 
 
# Function that returns true if a and b
# differ in only a single character
def isAdj(a, b):
    count = 0
    for i in range(len(a)):
        if (a[i] != b[i]):
            count+=1
     
    if (count == 1):
        return True
    return False
 
 
# Function to return the length of the shortest
# chain from ‘beginWord’ to ‘endWord’
def ladderLength(beginWord, endWord, wordList):
 
    # q1 is used to traverse the graph from beginWord
    # and q2 is used to traverse the graph from endWord.
    # vis1 and vis2 are used to keep track of the
    # visited states from respective directions
    q1=dq([])
    q2=dq([])
    vis1=dict()
    vis2=dict()
 
    start = node(beginWord, 1)
    end = node(endWord, 1)
 
    vis1[beginWord] = 1
    q1.append(start)
    vis2[endWord] = 1
    q2.append(end)
 
    while (q1 and q2):
 
        # Fetch the current node
        # from the source queue
        curr1 = q1.popleft()
 
        # Fetch the current node from
        # the destination queue
        curr2 = q2.popleft()
 
        # Check all the neighbors of curr1
        for it in wordList:
 
            # If any one of them is adjacent to curr1
            # and is not present in vis1
            # then push it in the queue
            if (isAdj(curr1.word, it) and it not in vis1) :
 
                temp = node(it, curr1.len + 1)
                q1.append(temp)
                
                vis1[it] = curr1.len + 1
                print(vis1)
 
                # If temp is the destination node
                # then return the answer
                if (temp.word == endWord) :
                    return temp.len
                    print(vis1)
                 
 
                # If temp is present in vis2 i.e. distance from
                # temp and the destination is already calculated
                if temp.word in vis2 :
                    return temp.len + vis2[temp.word] - 1
                 
             
         
 
        # Check all the neighbors of curr2
        for it in wordList:
 
            # If any one of them is adjacent to curr2
            # and is not present in vis1 then push it in the queue.
            if (isAdj(curr2.word, it) and it not in vis2) :
 
                temp = node(it, curr2.len + 1)
                q2.append(temp)
                vis2[it] = curr2.len + 1
 
                # If temp is the destination node
                # then return the answer
                if (temp.word == beginWord) :
                    return temp.len
                    print(temp)
                 
 
                # If temp is present in vis1 i.e. distance from
                # temp and the source is already calculated
                if temp.word in vis1:
                    return temp.len + vis1[temp.word] - 1         
 
    return 0
 
 
# Driver code
if __name__=='__main__':
 
    wordList = ["fool", "pool", "foil", "foul", "cool", "poll", "fail", "pole",
            "pall", "pope", "pale", "page", "sale", "sage", "pipe", "doll", "soil",
            "soul", "nail", "jail", "tail", "bail", "fall"]
 
    start = "pole"
    target = "soul"
 
    print(ladderLength(start, target, wordList))


# ## BFS

# In[2]:


import collections
from collections import deque 

class Solution(object):
    # method that will help find the path
    def ladderLength(self, beginWord, 
                        endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :returntype: int
        """

        # Queue for BFS
        queue = deque()

        # start by adding begin word
        queue.append((beginWord, [beginWord]))

        while queue:
            print('Current queue:',queue)

            # get the current node and 
            # path how it came
            node, path = queue.popleft()

            # let's keep track of path length 
            # traversed so far
            print('Current transformation count:',
                                        len(path))

            # find possible next set of 
            # child nodes, 1 diff
            for next in self.next_nodes(node, 
                            wordList) - set(path):
                # traversing through all child nodes to find match              
                if next == endWord:
                    print('found endword at path:',
                                            path)
                    return len(path)
                else:
                    # keep record of next 
                    # possible paths
                    queue.append((next, 
                                path + [next]))
        return 0

    def next_nodes(self, word, word_list):
        # start with empty collection
        possiblenodes = set()

        # all the words are of fixed length
        wl_word_length = len(word)

        # loop through all the words in 
        # the word list
        for wl_word in word_list:
            mismatch_count = 0

            # find all the words that are 
            # only a letter different from 
            # current word those are the 
            # possible next child nodes
            for i in range(wl_word_length):
                if wl_word[i] != word[i]:
                    mismatch_count += 1
            if mismatch_count == 1:
                # only one alphabet different-yes
                possiblenodes.add(wl_word)
        
        # lets see the set of next possible nodes 
        print('possible next nodes:',possiblenodes)
        return possiblenodes

# Setup
beginWord = "pole"
endWord = "soul"
wordList = ["fool", "pool", "foil", "foul", "cool", "poll", "fail", "pole",
            "pall", "pope", "pale", "page", "sale", "sage", "pipe", "doll", "soil",
            "soul", "nail", "jail", "tail", "bail", "fall"]

# Call
print('Transformations needed: ',
    Solution().ladderLength(beginWord, 
                            endWord, wordList))


# ## recursive back-tracking

# In[5]:



def is_diff_one(str1, str2):
    if len(str1) != len(str2):
        return False

    count = 0
    
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            count = count + 1

    if count == 1:
        return True

    return False


potential_ans = []


def transform(wordlist, start, end, count):
    global potential_ans
    if count == 0:
        count = count + 1
        
        potential_ans = [start]
    

    if start == end:
        print (potential_ans)
        
        return potential_ans
    
    for w in wordlist:
        if is_diff_one(w, start) and w not in potential_ans:
            potential_ans.append(w)
            transform(wordlist, w, end, count)
           
            potential_ans[:-1]
    return None



wordlist = set(["fool", "pool", "foil", "foul", "cool", "poll", "fail", "pole",
            "pall", "pope", "pale", "page", "sale", "sage", "pipe", "doll", "soil",
            "soul", "nail", "jail", "tail", "bail", "fall"])
transform(wordlist, 'pole', 'soul', 0)


# In[ ]:





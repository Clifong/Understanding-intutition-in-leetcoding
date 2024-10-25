"""
Intuition:

|********************************************************|
|  You should have an understanding of trie preferably   |
|                    to solve this                       |
|********************************************************|

We are dealing with string prefixes here because of the
definition of subfolders

"A folder[i] is a subfolder of folder[j] if 
folder[j] must start with folder[j], followed by a "/". 
For example, "/a/b" is a sub-folder of "/a", 
but "/b" is not a sub-folder of "/a/b/c"."

When it comes to string prefixes, the most ideal data structure
to use for efficiency is a trie.

We first determine how a trie is constructured. The most natural
approach is that if we split the "/" (i.e remove all "/".  
Each partitioned component is allocated into a list. See python's
.split() method for more information), each partitioned file name
will be stored in the node. For example,

"a/b/cd/ef".split() => ["a", "b", "cd", "ef"]

Then the trie will be:
    a
    |
    b
    |
    cd
    |
    ef*

We denote node with a * as the end node, meaning they mark the
end of the string. Then store this information into the node.

Afterwards, all operations are as per usual. We will only need two
more operation

Insertion:

Rationale: Build the trie

Using the same trie as above, suppose we want to insert a 
new node "a/b/e". Then the new trie is:
    a
    |
    b ___
    |    \ 
    cd    e*
    |
    ef*

Explore until the first * in each branch is encountered:

Rationale: The main folder is the first node we encounter in a branch
that is an end node. We define branch as the sequence of edges from
a node to any end node. We will use a DFS traversal.

E.g
"a/b/c, a/b, a/c, a/c/d/e"

    a __
    |   \ 
    b*  c*
    |    \ 
    c*    d
           \ 
            e*

Branches:
a - b
a - b - c
a - c
a - c - d- e

We expect this to return [/a/b, /a/c]. This correspond to the bramches
a - b and a - c which occurs when the end node we first encounter 
uss the shortest number of traversal (aka shortest branch).
"""

class node:
    def __init__(self, name):
        self.name = name
        self.end = False
        self.children = {}

    def insert(self, node):
        if node.name not in self.children:
            self.children[node.name] = node
        return self.children[node.name]

    def explore_till_end(self):

        def explore(node, temp):
            if node.end:
                return [temp]
            else:
                ans = []
                for c in node.children.keys():
                    ans.extend(explore(node.children[c], temp + "/" + node.children[c].name))
                return ans
        return explore(self, "/" + self.name)

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        all_folder = {}

        #This is impt if the folders are not given
        #In terms of ascending length. Without this property,
        #it becomes a bit complex to handle
        folder.sort(key=lambda a: len(a))

        for f in folder:
            remove_slash = f.split("/")
            temp = None
            for c in range(1, len(remove_slash)):

                new_node = node(remove_slash[c])

                #THe last letter. Make the new node an end node
                if c == len(remove_slash) - 1:
                    new_node.end = True
                    
                if c == 1:
                    if remove_slash[c] not in all_folder:
                        all_folder[remove_slash[c]] = new_node 
                    temp = all_folder[remove_slash[c]]
                else:
                    temp = temp.insert(new_node)

        answer = []
        for top in all_folder.keys():
            answer.extend(all_folder[top].explore_till_end())
        return answer
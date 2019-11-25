


# 一种现成bst node

class Node:
    """BST node containing value and and smallest index that has that value."""

    def __init__(self, val, index, parent=None):
        self.val = val
        self.index = index
        self.left = None
        self.right = None
        self.parent = parent

    def insert(self, val, index):
        """Inserts new value.

        If val doesn't exist, we create a new node. If val exists, we instead
        just replace the index.

        Returns the index of predecessor and successor, if any.
        """
        if val < self.val:
            if not self.left:
                self.left = Node(val, index, self)
                return self.left.predecessor(), self.left.successor()
            else:
                return self.left.insert(val, index)
        elif val > self.val:
            if not self.right:
                self.right = Node(val, index, self)
                return self.right.predecessor(), self.right.successor()
            else:
                return self.right.insert(val, index)
        else:
            current_index = self.index
            self.index = index
            return current_index, current_index

    def smallest(self):
        if self.left:
            return self.left.smallest()
        return self.index

    def largest(self):
        if self.right:
            return self.right.largest()
        return self.index
    #
    def predecessor(self, visit_left_subtree=True):
        """Index of the in-order predecessor."""
        if visit_left_subtree and self.left:
            return self.left.largest()
        if self.parent is not None:
            if self == self.parent.right:
                return self.parent.index
            return self.parent.predecessor(visit_left_subtree=False)
        return 0

    def successor(self, visit_right_subtree=True):
        """Index of the in-order successor."""
        if visit_right_subtree and self.right:
            return self.right.smallest()
        if self.parent is not None:
            if self == self.parent.left:
                return self.parent.index
            return self.parent.successor(visit_right_subtree=False)
        return 0




###################### BST ########
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                return res.payload
           else:
                return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    # def spliceOut(self):
    #    if self.isLeaf():
    #        if self.isLeftChild():
    #               self.parent.leftChild = None
    #        else:
    #               self.parent.rightChild = None
    #    elif self.hasAnyChildren():
    #        if self.hasLeftChild():
    #               if self.isLeftChild():
    #                  self.parent.leftChild = self.leftChild
    #               else:
    #                  self.parent.rightChild = self.leftChild
    #               self.leftChild.parent = self.parent
    #        else:
    #               if self.isLeftChild():
    #                  self.parent.leftChild = self.rightChild
    #               else:
    #                  self.parent.rightChild = self.rightChild
    #               self.rightChild.parent = self.parent

    def findSuccessor(self, node):
      succ = node
      if node.hasRightChild():
          succ = node.rightChild.findMin()
      else:
          if node.parent:
                 if node.isLeftChild():
                     succ = node.parent
                 else:
                     node.parent.rightChild = None
                     succ = node.parent.findSuccessor()
                     node.parent.rightChild = self
      return succ
###
    def findpredecessor(self, node):
      succ = node
      if node.hasLeftChild():
          succ = node.leftChild.findMax()
      else:
          if node.parent:
                 if node.isRightChild():
                     succ = node.parent
                 else:
                     node.parent.leftChild = None
                     succ = node.parent.findpredecessor()
                     node.parent.leftChild = self
      return succ
    def findMin(self):
      current = self
      while current.hasLeftChild():
          current = current.leftChild
      return current

    def findMax(self):
      current = self
      while current.hasRightChild():
          current = current.rightChild
      return current
    def remove(self,currentNode):
         if currentNode.isLeaf(): #leaf
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): #interior
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: # this node has one child
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)


###########################
# 最后结果
    
class Solution1:
    def oddEvenJumps(self, A):
        n = len(A)
        odd_jump = [False] * n
        even_jump = [False] * n
        bst = SortedArray()
        # base case
        odd_jump[n - 1] = True
        even_jump[n - 1] = True       
        bst.put(A[n - 1], n - 1)
        # general case
        for i in range(n - 2, -1, -1):
            # odd跳的结果 （比它大的里面找最小的）
            next_node = bst.find_next(A[i])
            odd_jump[i] = next_node[0] != -1 and even_jump[next_node[1]]
            # even跳的结果（比它小的里面找最大的）
            pre_node = bst.find_prev(A[i])
            even_jump[i] = pre_node[0] != -1 and odd_jump[pre_node[1]]
            # 把cur加入当前bst
            bst.put(A[i], i)
        result = 0
        # 看每个起点的odd跳的结果
        for i in range(0, n):
            if odd_jump[i]:
                result += 1
        return result



class SortedArray:
    def __init__(self):
        self.array = []

    def put(self, val, index):
        i = 0
        while i < len(self.array):
            if val <= self.array[i][0]:
                break
            i += 1
        self.array.insert(i, [val, index])

    def find_prev(self, val):
        i = 0
        while i < len(self.array):
            if val <= self.array[i][0]:
                if val == self.array[i][0]:
                    return self.array[i]
                i -= 1
                break
            i += 1
        if i == len(self.array):
            i -= 1
        if i < 0:
            return [-1, -1]
        while i > 0:
            if self.array[i][0] != self.array[i-1][0]:
                break
            i -= 1
        return self.array[i]

    def find_next(self, val):
        i = 0
        while i < len(self.array):
            if val <= self.array[i][0]:
                if val == self.array[i][0]:
                    return self.array[i]
                break
            i += 1

        if i > len(self.array) - 1:
            return -1, -1
        return self.array[i]

s = Solution1()
a = [2,3,1,1,4] # 3
print(s.oddEvenJumps(a))
a = [10,13,12,14,15] # 2
print(s.oddEvenJumps(a))
a = [5,1,3,4,2] # 3
print(s.oddEvenJumps(a))
a = [1,2,3,2,1,4,4,5] # 6
print(s.oddEvenJumps(a))
a = [5,1,3,4,2] #3
print(s.oddEvenJumps(a))





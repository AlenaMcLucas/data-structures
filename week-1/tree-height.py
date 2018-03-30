# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.root = 0
                self.new_tree = {}

                # set indexes
                for i in range(self.n):
                        self.new_tree[i] = []

                # set values
                for j in self.new_tree:
                        if self.parent[j] != -1:
                                self.new_tree[self.parent[j]].append(j)
                        else:
                                self.root = j


        def compute_height(self):
                new_queue = [self.root]
                depth = 1

                while new_queue != []:
                        depth += 1
                        new_queue = self.get_children(new_queue)

                return (depth - 1)

                
        def get_children(self, new_queue):
                children = []
                for k in new_queue:
                        if self.new_tree[k] != []:
                                for l in self.new_tree[k]:
                                        children.append(l)
                return children


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()

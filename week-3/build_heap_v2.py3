# python3

class HeapBuilder:
  def __init__(self):
    #self._swaps = []
    self._swaps = ""
    self._data = []
    self._n = 0
    self._count = 0

  def ReadData(self):
    self._n = int(input())
    self._data = [int(s) for s in input().split()]
    assert self._n == len(self._data)

  def WriteResponse(self):
    print(str(self._count) + self._swaps)
    #print(len(self._swaps))
    #for swap in self._swaps:
    #  print(swap[0], swap[1])

  def BuildHeap(self):
    for i in range(self._n // 2 + 1, -1, -1):
      self.SiftDown(i)

  def SiftDown(self,i):
    #leftChild = 2 * i + 1
    #rightChild = 2 * i + 2
    #i_temp = i

    leftChild, rightChild = 0, 0

    if (2 * i + 1) <= (self._n - 1):
      leftChild =  self._data[(2 * i + 1)] - self._data[i]
    if (2 * i + 2) <= (self._n - 1):
      rightChild =  self._data[(2 * i + 2)] - self._data[i]

    if leftChild < 0 or rightChild < 0:

      if leftChild <= rightChild:
        # SiftUp left
        #self._swaps.extend([[i,(2 * i + 1)]])
        self._swaps += "\n" + str(i) + " " + str(2 * i + 1)
        i_temp = self._data[(2 * i + 1)]
        self._data[(2 * i + 1)] = self._data[i]
        self._data[i] = i_temp
        self._count += 1
        self.SiftDown(2 * i + 1)

      else:   # leftChild > rightChild
        # SiftUp right
        #self._swaps.extend([[i,(2 * i + 2)]])
        self._swaps += "\n" + str(i) + " " + str(2 * i + 2)
        i_temp = self._data[(2 * i + 2)]
        self._data[(2 * i + 2)] = self._data[i]
        self._data[i] = i_temp
        self._count += 1
        self.SiftDown(2 * i + 2)

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]

  def Solve(self):
    self.ReadData()
    self.BuildHeap()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

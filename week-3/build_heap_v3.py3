# python3

class HeapBuilder:
  def __init__(self):
    #self._swaps = ""
    self._swaps = []
    self._data = []
    self._n = 0
    #self._count = 0

  def ReadData(self):
    self._n = int(input())
    self._data = [int(s) for s in input().split()]
    assert self._n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])


  def BuildHeap(self):
    for i in range(self._n // 2 + 1, -1, -1):
      self.SiftDown(i)

  def SiftDown(self,i):
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2
    i_temp = i

    if (leftChild <= self._n - 1) and (self._data[leftChild] < self._data[i_temp]):
      i_temp = leftChild
    if (rightChild <= self._n - 1) and (self._data[rightChild] < self._data[i_temp]):
      i_temp = rightChild

    if i_temp == leftChild:
      self._swaps.append((i, leftChild))
      self._data[i], self._data[leftChild] = self._data[leftChild], self._data[i]
      self.SiftDown(leftChild)

    if i_temp == rightChild:
      self._swaps.append((i, rightChild))
      self._data[i], self._data[rightChild] = self._data[rightChild], self._data[i]
      self.SiftDown(rightChild)


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

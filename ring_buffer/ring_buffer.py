class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.list = []

  def append(self, item):
        # print(self.current)
        if self.current == self.capacity:
              self.current = 0
        if len( self.list) < self.capacity:
            self.list.append(item)
        else:
            self.list[self.current] = item
        self.current += 1   

  def get(self):
    return self.list


buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())   # should return ['d', 'e', 'f']
from solution_template import Heap

def print_heap(myheap):
   print myheap.heap
h = Heap(int)
print_heap(h)
for i in range(10):
  h.insert(i)
  print_heap(h)




class Heap:
    
    def init(self):
        self.heap = [0]
    
    def push(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1 
        
        #percolate up
    
        while self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap [i // 2] = tmp    
            i = i // 2
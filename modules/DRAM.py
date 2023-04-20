DRAM_SIZE = 1024*1024
DRAM_BASE = 0x80000000

class DRAM:

    def __init__(self):
        self.mem = [0 for _ in range(DRAM_SIZE)] 
    
    def load(self, addr, size) -> int:
        return -1

    def store(self, addr, size, value):
        pass

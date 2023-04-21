DRAM_SIZE = 1024*1024
DRAM_BASE = 0

class DRAM:

    def __init__(self):
        self.mem = [0 for _ in range(DRAM_SIZE)]
    
    def load(self, addr, size) -> int:
                
        if size == 8:
            return self._load_8(addr)
        if size == 16:
            return self._load_16(addr)
        if size == 32:
            return self._load_32(addr)
        if size == 64:
            return self._load_64(addr)

        raise Exception("Invalid load size")

    def store(self, addr, size, value):
        if size == 8:
            return self._store_8(addr, value)
        if size == 16:
            return self._store_16(addr, value)
        if size == 32:
            return self._store_32(addr, value)
        if size == 64:
            return self._store_64(addr, value)

        raise Exception("Invalid store size")

#### Private functions

    def _load_8(self, addr) -> int:
        return self.mem[addr - DRAM_BASE]

    def _load_16(self, addr) -> int:
        return self.mem[addr - DRAM_BASE] \
            | self.mem[addr - DRAM_BASE + 1] << 8 

    def _load_32(self, addr) -> int:
        return self.mem[addr - DRAM_BASE] \
            | self.mem[addr - DRAM_BASE + 1] << 8 \
            | self.mem[addr - DRAM_BASE + 2] << 16 \
            | self.mem[addr - DRAM_BASE + 3] << 24

    def _load_64(self, addr) -> int:
        return self.mem[addr - DRAM_BASE] \
            | self.mem[addr - DRAM_BASE + 1] << 8 \
            | self.mem[addr - DRAM_BASE + 2] << 16 \
            | self.mem[addr - DRAM_BASE + 3] << 24 \
            | self.mem[addr - DRAM_BASE + 4] << 32 \
            | self.mem[addr - DRAM_BASE + 5] << 40 \
            | self.mem[addr - DRAM_BASE + 6] << 48 \
            | self.mem[addr - DRAM_BASE + 7] << 56

    def _store_8(self, addr, value):
        self.mem[addr - DRAM_BASE] = (value & 0xff)

    def _store_16(self, addr, value):
        self.mem[addr - DRAM_BASE] = (value & 0xff)
        self.mem[addr - DRAM_BASE + 1] = ((value >> 8) & 0xff)

    def _store_32(self, addr, value):
        self.mem[addr - DRAM_BASE] = (value & 0xff)
        self.mem[addr - DRAM_BASE + 1] = ((value >> 8) & 0xff)
        self.mem[addr - DRAM_BASE + 2] = ((value >> 16) & 0xff)
        self.mem[addr - DRAM_BASE + 3] = ((value >> 24) & 0xff)

    def _store_64(self, addr, value):
        self.mem[addr - DRAM_BASE] = (value & 0xff)
        self.mem[addr - DRAM_BASE + 1] = ((value >> 8) & 0xff)
        self.mem[addr - DRAM_BASE + 2] = ((value >> 16) & 0xff)
        self.mem[addr - DRAM_BASE + 3] = ((value >> 24) & 0xff)
        self.mem[addr - DRAM_BASE + 4] = ((value >> 32) & 0xff)
        self.mem[addr - DRAM_BASE + 5] = ((value >> 40) & 0xff)
        self.mem[addr - DRAM_BASE + 6] = ((value >> 48) & 0xff)
        self.mem[addr - DRAM_BASE + 7] = ((value >> 56) & 0xff)
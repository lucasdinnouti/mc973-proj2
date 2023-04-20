from modules.DRAM import DRAM

class BUS:

    def __init__(self):
        self.dram = DRAM()

    def load(self, addr, size) -> int:
        return self.dram.load(addr, size)

    def storre(self, addr, size, value):
        self.dram.store(addr, size, value)


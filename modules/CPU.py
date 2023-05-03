from modules.BUS import BUS
from utils.Logger import LogInfo
from services.Decoder import Decoder
from utils.Binary import Binary as bin

class CPU:

    def __init__(self):
        self.regs = [0 for _ in range(32)]
        self.pc = 0
        self.bus = BUS()

    def fetch(self) -> int:
        return self.bus.load(self.pc, 32)
    
    def store_program(self, program):
        for i, instr in enumerate(program):
            self.bus.store(i * 4, 32, instr)

    def enrich_registers(self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)

        log_info.set_rd(rd, self.get(rd))
        log_info.set_rs1(rs1, self.get(rs1))
        log_info.set_rs2(rs2, self.get(rs2))
            
    def get(self, register, unsigned=False) -> int:
        val = self.regs[register]

        return bin.twos_comp(val, 32) if unsigned else val
    
    def set(self, register, value) -> None:
        self.regs[register] = value
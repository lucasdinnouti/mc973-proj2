from services.executors.ExecutionStrategy import ExecutionStrategy
from utils.Logger import LogInfo
from services.Decoder import Decoder

class LUIStrategy(ExecutionStrategy):
    def execute(self, instr, log_info: LogInfo) -> int:
        self.exec_LUI(instr, log_info)
        
    def exec_LUI(self, instr, log_info: LogInfo):
        imm = Decoder.imm_U(instr)
        rd = Decoder.rd(instr)

        self.cpu.set(rd, (imm & 0xfffff000))

        if imm < 0:
            imm += 2**32

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_disassembly(f'lui x{rd}, {hex(imm << 12)}')
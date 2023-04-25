from services.executors.ExecutionStrategy import ExecutionStrategy
from utils.Logger import LogInfo
from services.Decoder import Decoder

class AUIPCStrategy(ExecutionStrategy):
    def execute(self, instr, log_info: LogInfo) -> int:
        self.exec_AUIPC(instr, log_info)
        
    def exec_AUIPC(self, instr, log_info: LogInfo):
        imm = Decoder.imm_U(instr)
        rd = Decoder.rd(instr)

        self.set(rd, self.cpu.pc + (imm & 0xfffff000))

        if imm < 0:
            imm += 2**32

        log_info.set_rd(rd, self.get(rd))
        log_info.set_disassembly(f'auipc x{rd}, {hex(imm << 12)}')
from services.executors.ExecutionStrategy import ExecutionStrategy
from utils.Logger import LogInfo
from services.Decoder import Decoder
import utils.Constants as const

class STypeStrategy(ExecutionStrategy):
    def execute(self, instr, log_info: LogInfo) -> int:
        funct3 = Decoder.funct3(instr)

        if funct3 == const.SB:
            self.exec_SB(instr, log_info)
        elif funct3 == const.SH:
            self.exec_SH(instr, log_info)
        elif funct3 == const.SW:
            self.exec_SW(instr, log_info)
        else:
            raise Exception('Cannot decode S_TYPE instruction')
        
    def store(self, instr, log_info: LogInfo, size, acronym):
        rs1 = Decoder.rs1(instr)
        rs2 = Decoder.rs2(instr)
        offset = Decoder.imm_S(instr)

        addr = self.cpu.get(rs1) + offset

        self.cpu.bus.store(addr, size, self.cpu.get(rs2))

        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_rs2(rs2, self.cpu.get(rs2))
        log_info.set_disassembly(f'{acronym} x{rs2}, {offset}(x{rs1})')

    def exec_SB(self, instr, log_info: LogInfo):
        self.store(instr, log_info, 8, 'sb')

    def exec_SH(self, instr, log_info: LogInfo):
        self.store(instr, log_info, 16, 'sh')

    def exec_SW(self, instr, log_info: LogInfo):
        self.store(instr, log_info, 32, 'sw')

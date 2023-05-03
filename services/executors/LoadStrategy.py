from services.executors.ExecutionStrategy import ExecutionStrategy
from utils.Logger import LogInfo
from services.Decoder import Decoder
import utils.Constants as const

class LoadStrategy(ExecutionStrategy):
    def execute(self, instr, log_info: LogInfo) -> int:
        funct3 = Decoder.funct3(instr)

        if funct3 == const.LB:
            self.exec_LB(instr, log_info)
        elif funct3 == const.LH:
            self.exec_LH(instr, log_info)
        elif funct3 == const.LW:
            self.exec_LW(instr, log_info)
        elif funct3 == const.LBU:
            self.exec_LBU(instr, log_info)
        elif funct3 == const.LHU:
            self.exec_LHU(instr, log_info)
        else:
            raise Exception('Cannot decode LOAD instruction')
        
    def load(self, instr, log_info: LogInfo, size, acronym):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        offset = Decoder.imm_LOAD(instr)

        addr = self.cpu.get(rs1) + offset

        loaded_value = self.cpu.bus.load(addr, size)
        self.cpu.set(rd, loaded_value)

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_disassembly(f'{acronym} x{rd}, {offset}(x{rs1})')

    def exec_LB(self, instr, log_info: LogInfo):
        self.load(instr, log_info, 8, 'lb')

    def exec_LH(self, instr, log_info: LogInfo):
        self.load(instr, log_info, 16, 'lh')

    def exec_LW(self, instr, log_info: LogInfo):
        self.load(instr, log_info, 32, 'lw')

    def exec_LBU(self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        offset = Decoder.imm_LOAD(instr)

        addr = self.cpu.get(rs1) + offset

        value = self.cpu.bus.load(addr, 8) & 0xFF
        self.cpu.set(rd, value)

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_disassembly(f'lbu x{rd}, {offset}(x{rs1})')

    def exec_LHU(self, instr, log_info: LogInfo):
        rd = Decoder.rd(instr)
        rs1 = Decoder.rs1(instr)
        offset = Decoder.imm_LOAD(instr)

        addr = self.cpu.get(rs1) + offset

        value = self.cpu.bus.load(addr, 16) & 0xFFFF
        self.cpu.set(rd, value)

        log_info.set_rd(rd, self.cpu.get(rd))
        log_info.set_rs1(rs1, self.cpu.get(rs1))
        log_info.set_disassembly(f'lhu x{rd}, {offset}(x{rs1})')
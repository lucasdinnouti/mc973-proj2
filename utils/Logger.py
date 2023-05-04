from utils.Binary import Binary as bin
from utils.Constants import REGISTER_NAMES

class LogInfo:

    def __init__(self) -> None:
        self.pc = ''
        self.instr = ''
        
        self.rd = ''
        self.rd_value = ''
        
        self.rs1 = ''
        self.rs1_value = ''
        
        self.rs2 = ''
        self.rs2_value = ''
        
        self.disassembly = ''

    def set_pc(self, pc): 
        self.pc = self.to_hex(pc)

    def set_instr(self, instr): 
        self.instr = self.to_hex(instr)

    def set_rd(self, rd, rd_value):
        self.rd = rd
        self.rd_value = self.to_hex(rd_value)

    def set_rs1(self, rs1, rs1_value):
        self.rs1 = rs1
        self.rs1_value = self.to_hex(rs1_value)

    def set_rs2(self, rs2, rs2_value):
        self.rs2 = rs2
        self.rs2_value = self.to_hex(rs2_value)

    def set_disassembly(self, disassembly):
        for (register, name) in REGISTER_NAMES:
            disassembly = disassembly.replace(register, name)

        # pad instructions for them to line up
        disassembly = disassembly.split(' ')[0].ljust(7) + ' ' + ' '.join(disassembly.split(' ')[1:])

        self.disassembly = disassembly

    def to_hex(self, value):
        if value < 0:
            value = value + 2**32

        return hex(value).split('x')[1].zfill(8)
    
    def rd_to_string(self):
        if self.rd != '':
            return f'x{str(self.rd).zfill(2)}={self.rd_value} '
        
        return ''

    def rs1_to_string(self):
        if self.rs1 != '':
            return f'x{str(self.rs1).zfill(2)}={self.rs1_value} '
        
        return ''

    def rs2_to_string(self):
        if self.rs2 != '':
            return f'x{str(self.rs2).zfill(2)}={self.rs2_value} '
        
        return ''

    def to_string(self):
        return f'PC={self.pc} {self.instr} {self.rd_to_string()}{self.rs1_to_string()}{self.rs2_to_string()}{self.disassembly}'

class Logger:

    def __init__(self, log_file) -> None:
        log_file = log_file.replace('.riscv', '')
        log_file = log_file.replace('.bin', '')

        self.file = log_file + '.log'

    def log(self, message: str):
        file = open(self.file, mode='a')
        file.write(message)
        file.write('\n')
        file.close()


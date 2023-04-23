from utils.Binary import Binary as bin

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
        self.disassembly = disassembly

    def to_hex(self, value):
        if value < 0:
            value = value + 2**32

        return hex(value).split('x')[1].zfill(8)
    
    def rd_to_string(self):
        if self.rd != '':
            return f'x{self.rd}={self.rd_value} '
        
        return ''

    def rs1_to_string(self):
        if self.rs1 != '':
            return f'x{self.rs1}={self.rs1_value} '
        
        return ''

    def rs2_to_string(self):
        if self.rs2 != '':
            return f'x{self.rs2}={self.rs2_value} '
        
        return ''

    def to_string(self):
        return f'{self.pc} {self.instr} {self.rd_to_string()}{self.rs1_to_string()}{self.rs2_to_string()}{self.disassembly}'

class Logger:

    def __init__(self) -> None:
        pass

    def log(self, message: str):
        print(message)


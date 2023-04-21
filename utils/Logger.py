
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
        return hex(value).split('x')[1]
    
    def to_string(self):
        return f'{self.pc} {self.instr} \
                {self.rd}={self.rd_value} \
                {self.rs1}={self.rs1_value} \
                {self.rs2}={self.rs2_value} \
                {self.disassembly}'

class Logger:

    def __init__(self) -> None:
        pass

    def log(self, message: str):
        print(message)


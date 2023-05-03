from utils.Binary import Binary as bin

register_names = {
    'x0': 'zero',
    'x1': 'ra',
    'x2': 'sp',
    'x3': 'gp',
    'x4': 'tp',
    'x5': 't0',
    'x6': 't1',
    'x7': 't2',
    'x8': 's0',
    'x9': 's1',
    'x10': 'a0',
    'x11': 'a1',
    'x12': 'a2',
    'x13': 'a3',
    'x14': 'a4',
    'x15': 'a5',
    'x16': 'a6',
    'x17': 'a7',
    'x18': 's2',
    'x19': 's3',
    'x20': 's4',
    'x21': 's5',
    'x22': 's6',
    'x23': 's7',
    'x24': 's8',
    'x25': 's9',
    'x26': 's10',
    'x27': 's11',
    'x28': 't3',
    'x29': 't4',
    'x30': 't5',
    'x31': 't6'
}

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
        renamed = self.disassembly

        for register in register_names:
            renamed = renamed.replace(register, register_names[register])

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

    def __init__(self) -> None:
        pass

    def log(self, message: str):
        print(message)


class Decoder:
    @staticmethod
    def opcode(instr) -> int:
        return instr & 0x7f

    @staticmethod
    def funct3(instr) -> int:
        return (instr >> 12) & 0x7

    @staticmethod
    def funct7(instr) -> int:
        return (instr >> 25) & 0x7f

    @staticmethod
    def rd(instr) -> int:
        return (instr >> 7) & 0x1f
        
    @staticmethod
    def rs1(instr) -> int:
        return (instr >> 15) & 0x1f 

    @staticmethod
    def rs2(instr) -> int:
        return (instr >> 20) & 0x1f 

    @staticmethod
    def imm_I(instr) -> int:
        return (instr & 0xfff00000) >> 20 

    @staticmethod
    def imm_S(instr) -> int:
        return ((instr & 0xfe000000) >> 20) | (instr >> 7) & 0x1f

    @staticmethod
    def imm_B(instr) -> int:
        return ((instr & 0x80000000) >> 19) \
            | ((instr & 0x80) << 4) \
            | ((instr >> 20) & 0x7e0) \
            | ((instr >> 7) & 0x1e)

    @staticmethod
    def imm_U(instr) -> int:
        return instr & 0xfffff999

    @staticmethod
    def imm_J(instr) -> int:
        return ((instr & 0x80000000) >> 11) \
            | (instr & 0xff000) \
            | ((instr >> 9) & 0x800) \
            | ((instr >> 20) & 0x7fe)

    @staticmethod
    def shamt(instr) -> int:
        return (Decoder.imm_I(instr) & 0x1f) 

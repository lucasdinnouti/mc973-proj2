LUI    = 0b0110111
AUIPC  = 0b0010111 
JAL    = 0b1101111 
JALR   = 0b1100111 
LOAD   = 0b0000011
FENCE  = 0b0001111

B_TYPE = 0b1100011
R_TYPE = 0b0110011
I_TYPE = 0b0010011
S_TYPE = 0b0100011
E_TYPE = 0b1110011

# LOAD
LB  = 0b000
LH  = 0b001
LW  = 0b010
LBU = 0b100
LHU = 0b101

# B_TYPE
BEQ   = 0b000
BNE   = 0b001
BLT   = 0b100
BGE   = 0b101
BLTU  = 0b110
BGEU  = 0b111

# R_TYPE
ADD_SUB = 0b000
ADD  = 0b0000000
SUB  = 0b0100000
SLL  = 0b001
SLT  = 0b010
SLTU = 0b011
XOR  = 0b100
SR   = 0b101
SRL  = 0b0000000
SRA  = 0b0100000
OR   = 0b110
AND  = 0b111

# I_TYPE
ADDI  = 0b000
SLTI  = 0b010
SLTIU = 0b011
XORI  = 0b100
ORI   = 0b110
ANDI  = 0b111
SLLI  = 0b001
SRI   = 0b101
SRLI  = 0b0000000
SRAI  = 0b0100000

# S_TYPE
SB = 0b000
SH = 0b001
SW = 0b010

# E_TYPE
ECALL = 0b000000000000
EBREAK = 0b000000000001

REGISTER_NAMES = [
    ('x31', 't6'),
    ('x30', 't5'),
    ('x29', 't4'),
    ('x28', 't3'),
    ('x27', 's11'),
    ('x26', 's10'),
    ('x25', 's9'),
    ('x24', 's8'),
    ('x23', 's7'),
    ('x22', 's6'),
    ('x21', 's5'),
    ('x20', 's4'),
    ('x19', 's3'),
    ('x18', 's2'),
    ('x17', 'a7'),
    ('x16', 'a6'),
    ('x15', 'a5'),
    ('x14', 'a4'),
    ('x13', 'a3'),
    ('x12', 'a2'),
    ('x11', 'a1'),
    ('x10', 'a0'),
    ('x9', 's1'),
    ('x8', 's0'),
    ('x7', 't2'),
    ('x6', 't1'),
    ('x5', 't0'),
    ('x4', 'tp'),
    ('x3', 'gp'),
    ('x2', 'sp'),
    ('x1', 'ra'),
    ('x0', 'zero')
]
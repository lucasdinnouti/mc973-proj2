from modules.CPU import CPU 
from services.Executor import Executor 
from services.Executor import Executor 
from utils.Logger import Logger, LogInfo

import sys

def read_program(path):
    content = []
    with open(path, mode='rb') as file:
        bytes = file.read(4)
        while bytes:
            int_from_bytes = int.from_bytes(bytes, 'little')
            content.append(int_from_bytes)
            bytes = file.read(4)
        
        file.close()

    return content

def main():
    cpu = CPU()
    executor = Executor(cpu)

    logger = Logger()

    program_path = sys.argv[1]
    # program = [
    #     0b00000000111111111111000110110111, # lui x3, 0xfffff000
    #     0b00000000111111111111000010110111, # lui x1, 0xfffff000
    #     0b00000000001100011000000110010011, # addi x3, x0, 3
    #     0b00000000000100001000000010010011, # addi x1, x1, 1
    #     0b00000000001100001101110001100011, # bge  x1, x3, 24
    #     0b11111111100111111111000101101111, # jal  x2, -8
    #     0b00000000001100001000000010100011, # sb x3, 1(x1)
    #     0b00000000001000000000001000000011, # lb x4, 2(x0)
    #     0b11111111111111111111000100010111, # auipc x2, 0xffffffff000
    #     0b00000000001100001101000001100011  # bge  x1, x3, 0
    # ]
    program = read_program(program_path)
    cpu.store_program(program)
    
    while True:
        log_info = LogInfo()
        log_info.set_pc(cpu.pc)

        instr = cpu.fetch()
        log_info.set_instr(instr)

        cpu.pc += 4

        if not executor.execute(instr, log_info):
            break
        
        cpu.enrich_registers(instr, log_info)
        
        logger.log(log_info.to_string())
        
        if cpu.pc == 0:
            break


if __name__ == "__main__":
    sys.exit(main())
from modules.CPU import CPU 
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

    program_path = sys.argv[0]
    program = [
        0b00000000001100000000000110010011, # addi x3, x0, 3
        0b00000000000100001000000010010011, # addi x1, x1, 1
        0b00000000001100001100001001100011, # blt  x1, x3, 4
        0b00000000001100001101000001100011  # bge  x1, x3, 0
    ]
    #program = read_program(program_path)
    cpu.store_program(program)
    
    while True:
        log_info = LogInfo()
        log_info.set_pc(cpu.pc)

        instr = cpu.fetch()
        log_info.set_instr(instr)

        cpu.pc += 4

        if not executor.execute(instr, log_info):
            break
        
        if cpu.pc == 0:
            break

        logger.log(log_info.to_string())

if __name__ == "__main__":
    sys.exit(main())
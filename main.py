from modules.CPU import CPU 
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
    logger = Logger()

    program_path = sys.argv[0]
    program = read_program(program_path)
    cpu.store_program(program)
    
    while True:
        log_info = LogInfo()
        log_info.set_pc(cpu.pc)

        instr = cpu.fetch()
        log_info.set_instr(instr)

        cpu.pc += 4

        if not cpu.execute(instr, log_info):
            break
        
        if cpu.pc == 0:
            break

        logger.log(log_info.to_string())

if __name__ == "__main__":
    sys.exit(main())
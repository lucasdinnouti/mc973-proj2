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
    total_cicles = 0

    cpu = CPU()
    executor = Executor(cpu)
    program_path = sys.argv[1]
    program = read_program(program_path)
    cpu.store_program(program)
    
    logger = Logger(program_path)
    while True:
        log_info = LogInfo()
        log_info.set_pc(cpu.pc)

        instr = cpu.fetch()
        log_info.set_instr(instr)

        cpu.pc += 4

        cpu.enrich_rs(instr, log_info)
        
        cicles = executor.execute(instr, log_info)
        
        cpu.enrich_rd(instr, log_info)
        
        logger.log(log_info.to_string())
        
        if cicles < 0:
            break
        else:
            total_cicles += cicles

    print('Total cicles:', total_cicles)


if __name__ == "__main__":
    sys.exit(main())
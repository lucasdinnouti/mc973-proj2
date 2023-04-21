from modules.CPU import CPU 

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

    program_path = sys.argv[0]
    program = read_program(program_path)
    cpu.store_program(program)
    
    while True:
        instr = cpu.fetch()

        cpu.pc += 4

        if not cpu.execute(instr):
            break
        
        if cpu.pc == 0:
            break

if __name__ == "__main__":
    sys.exit(main())
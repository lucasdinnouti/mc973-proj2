from modules.CPU import CPU 

import sys

def main():
    cpu = CPU()

    while True:
        instr = cpu.fetch()

        cpu.pc += 4

        if not cpu.execute(instr):
            break
        
        if cpu.pc == 0:
            break

if __name__ == "__main__":
    sys.exit(main())
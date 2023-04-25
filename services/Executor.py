import utils.Constants as const
from services.Decoder import Decoder
from services.executors.LUIStrategy import LUIStrategy
from services.executors.JALStrategy import JALStrategy
from services.executors.BTypeStrategy import BTypeStrategy
from services.executors.RTypeStrategy import RTypeStrategy
from services.executors.ITypeStrategy import ITypeStrategy
from services.executors.CTypeStrategy import CTypeStrategy
from services.executors.STypeStrategy import STypeStrategy
from services.executors.LoadStrategy import LoadStrategy

class Executor:
    def __init__(self, cpu) -> None:
        self.LUI = LUIStrategy(cpu)
        self.JAL = JALStrategy(cpu)

        self.B_type = BTypeStrategy(cpu)
        self.R_type = RTypeStrategy(cpu)
        self.I_type = ITypeStrategy(cpu)
        self.C_type = CTypeStrategy(cpu)
        self.S_TYPE = STypeStrategy(cpu)
        self.LOAD   = LoadStrategy(cpu)

    def execute(self, instr, log_info) -> int:
        opcode = Decoder.opcode(instr)

        if opcode == const.LUI:
            self.LUI.execute(instr, log_info)
        elif opcode == const.AUIPC:
            self.AUIPC.execute(instr, log_info)
        elif opcode == const.JAL:
            self.JAL.execute(instr, log_info)
        elif opcode == const.JALR:
            self.JALR.execute(instr, log_info)
        elif opcode == const.LOAD:
            self.LOAD.execute(instr, log_info)
        elif opcode == const.FENCE:
            self.FENCE.execute(instr, log_info)
        elif opcode == const.B_TYPE:
            self.B_type.execute(instr, log_info)
        elif opcode == const.R_TYPE:
            self.R_type.execute(instr, log_info)
        elif opcode == const.I_TYPE:
            self.I_type.execute(instr, log_info)
        elif opcode == const.C_TYPE:
            self.C_type.execute(instr, log_info)
        elif opcode == const.S_TYPE:
            self.S_TYPE.execute(instr, log_info)
        else:
            raise Exception('Cannot decode instruction type')
        
        return 1
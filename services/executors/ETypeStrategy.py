from services.executors.ExecutionStrategy import ExecutionStrategy
from utils.Logger import LogInfo
from services.Decoder import Decoder
import utils.Constants as const

class ETypeStrategy(ExecutionStrategy):
    def execute(self, instr, log_info: LogInfo) -> int:
        imm = Decoder.imm_I(instr)

        if imm == const.ECALL:
            return self.exec_ECALL(instr, log_info)
        elif imm == const.EBREAK:
            return self.exec_EBREAK(instr, log_info)
        else:
            raise Exception('Cannot decode E_TYPE instruction')

    def exec_ECALL(self, instr, log_info: LogInfo):
        print('* ecall not implemented. *')


    def exec_EBREAK(self, instr, log_info: LogInfo):
        log_info.set_disassembly('ebreak')
        return -1

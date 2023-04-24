from services.executors.ExecutionStrategy import ExecutionStrategy
from utils.Logger import LogInfo

class CTypeStrategy(ExecutionStrategy):
    def execute(self, instr, log_info: LogInfo) -> int:
        raise Exception('Cannot decode C_TYPE instruction')

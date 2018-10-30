import time
import random
from pathlib import Path
from SMWinservice import SMWinservice

class PythonServiceExample(SMWinservice):
    _svc_name_ = "PythonServiceExample"
    _svc_display_name_ = "Python Service Example"
    _svc_description_ = "Winservice with Python..."

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        # i = 0
        while self.isrunning:
            random.seed()
            x = random.randint(1, 1000000)
            Path(f'D:\log\{x}.txt').touch()
            time.sleep(5)

if __name__ == '__main__':
    PythonServiceExample.parse_command_line()
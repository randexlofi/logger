from datetime import datetime
import traceback, os

class Logger():
    LEVELS = {
        "INFO": 10, 
        "WARNING": 20, 
        "ERROR": 30
    }

    # initialize logger
    def __init__(self, filename, level="INFO", console=False):
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        self.file = open(filename, 'a')
        self.level = self.LEVELS[level]
        self.console = console

    def close(self):
        self.file.close()

    # General log method with timestamp to be used by other log methods. (info, warn, error)
    def log(self, level_name, message):
        if self.LEVELS[level_name] < self.level:
            return

        timestamp = datetime.now().strftime('%d-%b-%Y %H:%M:%S.%f')
        log_message = f"[{timestamp}] [{level_name:<8}] {message}"

        self.file.write(log_message + '\n')
        self.file.flush()

        if self.console:
            print(log_message)

    # Normal log method
    def info(self, message):
        self.log("INFO", message)

    # Warning log method
    def warning(self, message):
        self.log("WARNING", message)

    # Error log method
    def error(self, message):
        self.log("ERROR", message)

    def exception(self, message):
        tb = traceback.format_exc()
        self.log("ERROR", f"{message}\n{tb}")

    def separator(self, char='=', length=60):
        self.file.write(char * length + '\n')

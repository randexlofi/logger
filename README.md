# Logger

You can use this logger for anything you want.

## Usage

```python
import logger

# initialize logger
## assign your folder/filename.log
## default the level for the logs
## console = True (will print the logs into your console as they are being logged.)
logger = Logger('logs/logfile.log', level="INFO", console=True)

# log examples:
logger.info("This is an info message.")       # Log an info message
logger.warning("This is a warning message.")  # Log a warning message
logger.error("This is an error message.")     # Log an error message

try:
    1 / 0 # Example to raise an exception
except Exception:
    logger.exception("An exception occurred.") # Log the exception with traceback

logger.separator(char='=', length=60) # Log a separator line (can add custom character and length)


# close the logger file at the end of usage.
logger.close()
```
## Output
```
[17-Dec-2025 10:46:10.504841] [INFO    ] This is an info message.
[17-Dec-2025 10:46:10.505400] [WARNING ] This is a warning message.
[17-Dec-2025 10:46:10.505605] [ERROR   ] This is an error message.
[17-Dec-2025 10:46:10.522572] [ERROR   ] An exception occurred.
Traceback (most recent call last):
  File "c:\logger.py", line 65, in main
    1 / 0 # Example to raise an exception
    ~~^~~
ZeroDivisionError: division by zero

============================================================
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

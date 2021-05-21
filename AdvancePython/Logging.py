"""
logging levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s", filename="logs.txt")

logger = logging.getLogger('logger')

logger.info("information")
logger.warning("show")
print('test')

print('test')
print('test')
# calculator.py
import logging
from custom_logger import *

logger = logging.getLogger('my_app.calculator')

@log_function(logger)
def calculate_average(numbers):
    logger.info("Starting average calculation")
    
    if not numbers:
        logger.warning("Empty list provided, returning 0")
        return 0
    
    try:
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        logger.debug(f"Total: {total}, Count: {count}, Average: {average}")
        logger.info("Finished average calculation")
        return average
    except TypeError as e:
        logger.error(f"Error calculating average: {e}")
        return 0
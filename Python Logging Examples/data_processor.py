# data_processor.py
import logging
from custom_logger import *

logger = logging.getLogger('my_app.data_processor')

@log_function(custom_logger)
def process_data(data):
    logger.info("Starting data processing")
    
    cleaned_data = []
    for item in data:
        try:
            logger.debug(f"Processing item: {item}")
            cleaned_data.append(float(item))
            logger.debug(f"Converted {item} to {float(item)}")
        except (ValueError, TypeError) as e:
            logger.error(f"Failed to process {item}: {e}")
    
    logger.info("Finished data processing")
    return cleaned_data

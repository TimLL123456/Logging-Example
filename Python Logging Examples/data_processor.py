# data_processor.py
import logging
from custom_logger import *

custom_logger = logging.getLogger('my_app.data_processor')

@log_function(custom_logger)
def process_data(data):
    custom_logger.info("Starting data processing")
    
    cleaned_data = []
    for item in data:
        try:
            custom_logger.debug(f"Processing item: {item}")
            cleaned_data.append(float(item))
            custom_logger.debug(f"Converted {item} to {float(item)}")
        except (ValueError, TypeError) as e:
            custom_logger.error(f"Failed to process {item}: {e}")
    
    custom_logger.info("Finished data processing")
    return cleaned_data
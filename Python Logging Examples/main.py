# main.py
import logging
from custom_logger import logger_setup
from data_processor import process_data
from calculator import calculate_average

# Main logic
logger = logger_setup(logger_name="my_app", logger_filename="app.log")
logger = logging.getLogger('my_app.main')
logger.info("Starting the application")

data = [1, 2, 3, "four", 5]
processed_data = process_data(data)
average = calculate_average(processed_data)
logger.info(f"Average of processed data: {average}")

logger.info("Application finished")
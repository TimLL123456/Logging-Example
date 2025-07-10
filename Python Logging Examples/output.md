# Console Output

```bash
>>> INFO - main.py:10 - Starting the application
>>> INFO - data_processor.py:9 - Starting data processing
>>> ERROR - data_processor.py:18 - Failed to process four: could not convert string to float: 'four'
>>> INFO - data_processor.py:20 - Finished data processing
>>> INFO - calculator.py:9 - Starting average calculation
>>> INFO - calculator.py:20 - Finished average calculation
>>> INFO - main.py:15 - Average of processed data: 2.75
>>> INFO - main.py:17 - Application finished
```

# app.log

```bash
2025-07-10 11:47:29,369 - my_app.main - INFO - main.py:10 - Starting the application
2025-07-10 11:47:29,369 - my_app.data_processor - DEBUG - custom_logger.py:38 - Entering function 'process_data' with args=([1, 2, 3, 'four', 5],), kwargs={}
2025-07-10 11:47:29,369 - my_app.data_processor - INFO - data_processor.py:9 - Starting data processing
2025-07-10 11:47:29,369 - my_app.data_processor - DEBUG - data_processor.py:14 - Processing item: 1
2025-07-10 11:47:29,369 - my_app.data_processor - DEBUG - data_processor.py:16 - Converted 1 to 1.0
2025-07-10 11:47:29,369 - my_app.data_processor - DEBUG - data_processor.py:14 - Processing item: 2
2025-07-10 11:47:29,369 - my_app.data_processor - DEBUG - data_processor.py:16 - Converted 2 to 2.0
2025-07-10 11:47:29,369 - my_app.data_processor - DEBUG - data_processor.py:14 - Processing item: 3
2025-07-10 11:47:29,369 - my_app.data_processor - DEBUG - data_processor.py:16 - Converted 3 to 3.0
2025-07-10 11:47:29,369 - my_app.data_processor - DEBUG - data_processor.py:14 - Processing item: four
2025-07-10 11:47:29,369 - my_app.data_processor - ERROR - data_processor.py:18 - Failed to process four: could not convert string to float: 'four'
2025-07-10 11:47:29,369 - my_app.data_processor - DEBUG - data_processor.py:14 - Processing item: 5
2025-07-10 11:47:29,369 - my_app.data_processor - DEBUG - data_processor.py:16 - Converted 5 to 5.0
2025-07-10 11:47:29,369 - my_app.data_processor - INFO - data_processor.py:20 - Finished data processing
2025-07-10 11:47:29,369 - my_app.data_processor - DEBUG - custom_logger.py:40 - Exiting function 'process_data' with result=[1.0, 2.0, 3.0, 5.0]
2025-07-10 11:47:29,369 - my_app.calculator - DEBUG - custom_logger.py:38 - Entering function 'calculate_average' with args=([1.0, 2.0, 3.0, 5.0],), kwargs={}
2025-07-10 11:47:29,369 - my_app.calculator - INFO - calculator.py:9 - Starting average calculation
2025-07-10 11:47:29,369 - my_app.calculator - DEBUG - calculator.py:19 - Total: 11.0, Count: 4, Average: 2.75
2025-07-10 11:47:29,370 - my_app.calculator - INFO - calculator.py:20 - Finished average calculation
2025-07-10 11:47:29,370 - my_app.calculator - DEBUG - custom_logger.py:40 - Exiting function 'calculate_average' with result=2.75
2025-07-10 11:47:29,370 - my_app.main - INFO - main.py:15 - Average of processed data: 2.75
2025-07-10 11:47:29,370 - my_app.main - INFO - main.py:17 - Application finished
```

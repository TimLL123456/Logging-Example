# Logging-Example

1. **logging_config.yml**
<details>
  <summary>Click to expand code</summary>

```YAML
version: 1
formatters:
  detailed:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: detailed
  main_file:
    class: logging.FileHandler
    filename: main.log
    encoding: utf-8
    level: INFO
    formatter: detailed
  db_file:
    class: logging.FileHandler
    filename: database.log
    encoding: utf-8
    level: ERROR
    formatter: detailed
loggers:
  my_app.main:
    level: DEBUG
    handlers: [console, main_file]
    propagate: no
  my_app.database:
    level: DEBUG
    handlers: [console, db_file]
    propagate: no
root:
  level: WARNING
  handlers: [console]
```
</details>

2. **main.py**
<details>
  <summary>Click to expand code</summary>

```Python
import logging
import logging.config
import yaml
import database

# 載入 YAML 配置
with open(r"C:\Users\tllam\Desktop\Remark\Python\Test\logging_config.yml", "r") as f:
    config = yaml.safe_load(f)
logging.config.dictConfig(config)

# 為主模組創建日誌器
main_logger = logging.getLogger("my_app.main")

def main():
    main_logger.debug("來自主模組的除錯訊息")
    main_logger.info("啟動應用程式")
    main_logger.info("Starting the application")
    
    # 呼叫資料庫模組
    database.process_data()
    
    main_logger.info("應用程式完成")
    main_logger.info("Application finished")

if __name__ == "__main__":
    main()
```
</details>

3. **database.py**
<details>
  <summary>Click to expand code</summary>

```Python
import logging

# 為資料庫模組創建日誌器
db_logger = logging.getLogger("my_app.database")

def process_data():
    db_logger.debug("除錯資料庫操作")
    db_logger.info("在資料庫中處理數據")
    db_logger.info("Processing data in database")
    try:
        result = 1 / 0  # 模擬錯誤
    except ZeroDivisionError:
        db_logger.exception("資料庫操作錯誤")
        db_logger.exception("Error in database operation")
```
</details>

# Output

```Bash
2025-07-09 15:45:53,444 - my_app.main - DEBUG - 來自主模組的除錯訊息
2025-07-09 15:45:53,445 - my_app.main - INFO - 啟動應用程式
2025-07-09 15:45:53,445 - my_app.main - INFO - Starting the application
2025-07-09 15:45:53,445 - my_app.database - DEBUG - 除錯資料庫操作
2025-07-09 15:45:53,446 - my_app.database - INFO - 在資料庫中處理數據
2025-07-09 15:45:53,446 - my_app.database - INFO - Processing data in database
2025-07-09 15:45:53,446 - my_app.database - ERROR - 資料庫操作錯誤
Traceback (most recent call last):
  File "c:\Users\tllam\Desktop\Remark\Python\Test\database.py", line 11, in process_data
    result = 1 / 0  # 模擬錯誤
ZeroDivisionError: division by zero
2025-07-09 15:45:53,447 - my_app.database - ERROR - Error in database operation
Traceback (most recent call last):
  File "c:\Users\tllam\Desktop\Remark\Python\Test\database.py", line 11, in process_data
    result = 1 / 0  # 模擬錯誤
ZeroDivisionError: division by zero
2025-07-09 15:45:53,448 - my_app.main - INFO - 應用程式完成
2025-07-09 15:45:53,448 - my_app.main - INFO - Application finished
```

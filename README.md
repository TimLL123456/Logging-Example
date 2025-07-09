# Logging-Example

`logging_config.yml`
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

`main.py`
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

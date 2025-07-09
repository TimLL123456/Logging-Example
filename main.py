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
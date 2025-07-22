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
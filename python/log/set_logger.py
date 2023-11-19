import logging

def get_logger():
    # ロガーを作成
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # ファイルハンドラを作成し、ファイルにログを書き込む
    file_handler = logging.FileHandler('log\\history.log')
    file_handler.setLevel(logging.DEBUG)

    # コンソールハンドラを作成し、コンソールにログを表示
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # ログのフォーマットを設定
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(log_format)

    # ハンドラにフォーマッタを設定
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # ロガーにハンドラを追加
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

# ログメッセージを記録
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

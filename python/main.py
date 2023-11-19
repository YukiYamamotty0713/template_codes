from utils import test
from utils import operate_os
from config import setting
from log import set_logger
from error import logging_error
from utils import read_csv

#================================================================
#ロガーの設定
#================================================================
logger = set_logger.get_logger()

#================================================================
#メイン関数
#================================================================
def main():
    try:
        #write code below
        #↓example
        print('hello') 
        print(test.add_one(setting.BIRTHYEAR))


    except Exception as e:
        logger.error('Error occured')
        logging_error.error_logging(e,exe_print = True)

if __name__ == '__main__':
    main()

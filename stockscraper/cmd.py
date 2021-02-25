import os
import schedule
import time

def crawling():
    os.system('cd {}'.format(os.getcwd()))
    os.system('conda activate my_python_env')
    output = os.popen('scrapy crawl my_stock_bots').read()
    print(output)

schedule.every(10).minutes.do(crawling)
while True:
    schedule.run_pending()
    time.sleep(1)

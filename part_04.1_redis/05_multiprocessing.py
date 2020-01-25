import redis
import time
import random
from multiprocessing import Process


class Spider:
    def __init__(self):
        self.r = redis.Redis()

    # 生产者进程的事件函数
    def product(self):
        # 生产者生成url
        for page in range(67):
            url = 'http://app.mi.com/category/2#page={}'.format(page)
            self.r.lpush('xiaomi:spider', url)
            time.sleep(random.randint(1, 3))

    # 消费者 - 进程的事件函数
    def consumer(self):
        while True:
            url = self.r.brpop('xiaomi:spider', 4)
            # brpop 返回的是元组

            if url:
                print("我正在抓取:", url[1].decode())
            else:
                print("抓取结束")
                break

    # 主函数
    def run(self):
        # 创建两个进程
        p1 = Process(target=self.product)
        p2 = Process(target=self.consumer)
        p1.start()
        p2.start()
        p1.join()
        p2.join()


if __name__ == "__main__":
    spider = Spider()
    spider.run()

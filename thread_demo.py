"""
Created on 2018/3/6
@Author: Jeff Yang
"""
import requests
import time
# multiprocessing这个module有一个dummy的sub module，它是基于multithread实现了multiprocessing的API。
from multiprocessing import Pool  # 多进程实现了concurrency
from multiprocessing.dummy import Pool as TheadPool  # 多线程实现concurrency

urls = ['http://python.jobbole.com/all-posts/page/' + str(i) for i in range(1, 101)]


def get_page(url):
    html = requests.get(url).text


def use_none():
    time1 = time.time()
    for url in urls:
        get_page(url)
    time2 = time.time()
    print("不使用multiprocessing耗时：", time2 - time1)


def use_pool():
    pool = Pool(4)
    time3 = time.time()
    pool.map(get_page, [url for url in urls])
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    time4 = time.time()
    print("使用pool耗时：", time4 - time3)


def use_thread_pool():
    pool = TheadPool(4)
    time5 = time.time()
    pool.map(get_page, [url for url in urls])
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    time6 = time.time()
    print("使用thread pool耗时：", time6 - time5)


if __name__ == '__main__':
    use_none()
    use_pool()
    use_thread_pool()

# multiprocessing_comparison

多进程与多线程模拟爬虫的对比

使用三种方法获取伯乐在线100页文章的运行时间，几次运行的时间大致一样，类似：

```
不使用multiprocessing耗时： 48.05367946624756
使用pool耗时： 15.402552843093872
使用thread pool耗时： 14.417507648468018
```

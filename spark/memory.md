# memory management
spark 内存4个区域
![img_13.png](img_13.png)
* reserved memory 300m
  * 存储内部对象，not configurable
* User memory
  * developer自定义数据结构
* Execution memory
  * task执行过程中用于算子计算
* Storage memory
  * 缓存RDD
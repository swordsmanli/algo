# 分布式数仓


## spark with hive
![img_34.png](img_34.png)
spark利用hive提供的metastore，加载元信息，spark sql自行读取数据

## hive on spark
![img_35.png](img_35.png)
hive的engine是可以插拔的，利用spark作为分布式执行引擎。SQL解析，执行计划，优化都是hive负责

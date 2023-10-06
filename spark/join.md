# dataframe join

## join types
![img_21.png](img_21.png)

example
![img_22.png](img_22.png)
* inner
  * ![img_27.png](img_27.png)
* leftouter
  * ![img_24.png](img_24.png)
* rightouter
  * ![img_25.png](img_25.png)
* fullouter
  * ![img_26.png](img_26.png)
* leftsemi
  * ![img_28.png](img_28.png)
* leftanti
  * ![img_29.png](img_29.png)

## join mechanism
![img_33.png](img_33.png)
* nlj nested loop join
左表，驱动表，右表，基表， 2层for循环进行匹配
![img_30.png](img_30.png)
O(mxn)
* smj sort merge join
先排序，后归并
![img_31.png](img_31.png)
O(m+n)
* hj hash join
build + probe
![img_32.png](img_32.png)


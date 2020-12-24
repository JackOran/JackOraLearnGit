### 为何`Vue`采用异步渲染



视图更新的时候有个**update**方法，来进行视图更新，将**watcher放入队列**中，通过**nextTick**来刷新**watcher队列**


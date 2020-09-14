![image-20200909164747332](/Users/apple/Library/Application%20Support/typora-user-images/image-20200909164747332.png)

### 核心概念

- #### State: this.$store.state.xxx取值

- #### Getter:this.$store.getters.xxx取值

- #### Mutation:this.$store.commit('xxx')赋值

- #### Action: this.$store.dispatch('xxx')赋值

- #### Module

  - 开启命名空间：**namespaces:true**
  - 嵌套模块不要过深，尽量扁平化
  - 灵活应用**createNamespacedHelpers**



### 底层原理

- #### State:提供一个响应式的数据

- #### Getter:借助Vue计算属性Computed来进行缓存

- #### Mutation:触发state方法

- #### Action:yellow_heart:触发mutation方法

- #### Module:Vue.set动态添加state到响应式数据中


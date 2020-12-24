## Vuex

Vuex 是一个专为 Vue.js 应用程序开发的**状态管理模式**。

**状态管理**到底是什么？
状态管理模式、集中式存储管理这些名词听起来就非常高大上，让人捉摸不透。
其实，你可以简单的将其看成把需要多个组件共享的变量全部存储在一个对象里面。
然后，将这个对象放在顶层的Vue实例中，让其他组件可以使用。
那么，多个组件是不是就可以共享这个对象中的所有变量属性了呢？

不用怀疑，Vuex就是为了提供这样一个在多个组件间共享状态的插件，用它就可以了

#### 单页面的状态管理

![image-20200922133129777](/Users/apple/Library/Application%20Support/typora-user-images/image-20200922133129777.png)

State：状态

View：视图层

Actions：用户的各种行为

<img src="/Users/apple/Library/Application%20Support/typora-user-images/image-20200922133319872.png" alt="image-20200922133319872" style="zoom:150%;" />

#### Vuex核心概念

**state**

**getters**: 同计算属性computed类似

**mutations**

- mutation的定义方式：![image-20200922142246078](/Users/apple/Library/Application%20Support/typora-user-images/image-20200922142246078.png)

- 通过mutation更新![image-20200922142320477](/Users/apple/Library/Application%20Support/typora-user-images/image-20200922142320477.png)

- Vuex的store中的state是**响应式的**, 当state中的数据发生改变时, Vue组件会**自动更新.**
  这就要求我们必须遵守一些Vuex对应的规则:
  **提前在store中初始化好所需的属性**.
  当给state中的对象添加新属性时, 使用下面的方式:
  **方式一**: 使用**Vue.set(obj, 'newProp', 123)**
  删除：

  - **Vue.delete(obj, ' ')**

- ```js
  //响应式的添加和删除
  //添加属性
  Vue.set(state.info, 'address', '北京')
  //删除属性
  Vue.delete(state.info, 'age')
  ```

**actions**

**modules**
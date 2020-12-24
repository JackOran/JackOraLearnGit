#### vue的响应式原理

### 1.响应式原理

在生成**vue实例**时，为对传入的data进行遍历，使用`Object.defineProperty`把这些属性转为`getter/setter`.

`Object.defineProperty` 是 ES5 中一个无法 shim 的特性，这也就是 Vue 不支持 IE8 以及更低版本浏览器的原因。

每个**vue实例**都有一个**watcher实例**，它会在实例渲染时记录这些属性，并在**setter触发**时重新渲染。

![image-20201027115927312](/Users/apple/Library/Application%20Support/typora-user-images/image-20201027115927312.png)

Vue 无法检测到对象属性的添加或删除

Vue **不允许动态添加根级别的响应式属性**。但是，可以使用 `Vue.set(object, propertyName, value)`方法向嵌套对象添加响应式属性。

**initData -> new Observer -> this.walk(value) -> defineReactive -> Object.defineProperty**

**初始化数据 -> 数据观测 -> 进行对象的处理 ->循环对象属性定义响应式变化 -> 重新定义数据**



### **Vue如何检测数组变化**

**initData -> new Observer -> protoAugment -> notify**

**初始化数据 -> 数据观测 -> 改写数组原型方法 -> 通知视图更新**



### 3.异步更新队列

vue更新dom时是异步执行的

数据变化、更新是在主线程中同步执行的；在侦听到数据变化时，watcher将数据变更存储到异步队列中，当本次数据变化，即主线程任务执行完毕，异步队列中的任务才会被执行（已去重）。

**如果你在js中更新数据后立即去操作DOM，这时候DOM还未更新；vue提供了nextTick接口来处理这样的情况，它的参数是一个回调函数，会在本次DOM更新完成后被调用。**

使用方法：

- 1.在组件内使用 vm.$nextTick() 实例方法特别方便，因为它不需要全局 Vue，并且回调函数中的 this 将自动绑定到当前的 Vue 实例上：



```js
Vue.component('example', {
  template: '<span>{{ message }}</span>',
  data: function () {
    return {
      message: '未更新'
    }
  },
  methods: {
    updateMessage: function () {
      this.message = '已更新'
      console.log(this.$el.textContent) // => '未更新'
      this.$nextTick(function () {
        console.log(this.$el.textContent) // => '已更新'
      })
    }
  }
})
```

- 2.因为 `$nextTick()` 返回一个 `Promise` 对象，所以你可以使用新的 [ES2016 async/await](https://links.jianshu.com/go?to=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fasync_function) 语法完成相同的事情：



```js
methods: {
  updateMessage: async function () {
    this.message = '已更新'
    console.log(this.$el.textContent) // => '未更新'
    await this.$nextTick()
    console.log(this.$el.textContent) // => '已更新'
  }
}
```


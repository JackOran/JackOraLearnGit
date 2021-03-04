### 迭代

#### 迭代对象
可迭代的对象 - 实现了[Symbol.iterator]方法

#### 迭代语句
for...in

for...of

#### Generator迭代器
```js
function*fn() {
    yield 1;
    yield 2;
    yield 3;
}
let f = fn()
for (let val of f) {
    console.log(val);
}
```
// 同步 阻塞

**js就是单线程**

// 异步 非阻塞

// 自定义事件并且派发事件
```js
// 自定义事件定义
let eventObj = new EventTarget()
let num = 1
eventObj.dispatchEvent(new CustomEvent('myevent' + num))
num += 1
move(ele, 300, 'left')
eventObj.addEventListener('myevent1', () => {
console.log('运动完成')
move(ele, 300, 'top')
})
```
#### Promise
```js
// 1.new Promise(() => {}) 2. return new Promise(() => {}) 3.Promise.resolve()
let p = Promise.resolve('success')
console.log(p)

//all
let p1 = new Promise((resolve, reject) => {
setTimeout(() => {
  resolve(111)
}, 1000)
})

let p2 = new Promise((resolve, reject) => {
setTimeout(() => {
  // resolve(222)
  reject(222)
}, 1000)
})
// all 是全部都成功才返回成功
Promise.all([p1, p2]).then(res => {
console.log(res, '成功')
}).catch(err => {
console.log(err, 'error')
})

// 只要一个成功就返回数据
Promise.race([p1, p2]).then((res)=> {
console.dir(res, "成功")
}).catch((err) => {
console.error(err, "err")
})
```

#### 数据响应的实现

##### 初次渲染

```js
// 初次渲染：把data中的数据根据表达式渲染到视图
// 先在视图中找大胡子语法 ---> message ---> message 在data中查找 ---> 将找到的数据替换视图
```

##### 数据响应

```js
//ES5
  let obj = {}
  // 数据劫持
  // 创建对象并且对对象中的属性进行设置
  Object.defineProperty(obj, 'name', {
    // value: 'bob',
    // enumerable: true,
    // configurable: true,
    // writable: true
    get() {
      return 'bob'
    },
    set(newValue) {
      console.log(newValue)
    }
  })
  console.log(obj)

  // 修改对象中的属性
  let data = {
    name: 'man',
    age: 20
  }
  let value = data.name
  Object.defineProperty(data, 'name', {
    configurable: true,
    enumerable: true,
    get() {
      console.log('get')
      return value
    },
    set(newValue) {
      console.log('set')
      value = newValue
    }
  })
  console.log(data)
  data.name = 'women'

  // 封装成为一个可以数据观察 数据劫持的函数
  function Observer(data) {
    let keys = Object.keys(data)
    keys.forEach(key => {
      let value = data[key]
      Object.defineProperty(data, key, {
        configurable: true,
        enumerable: true,
        get() {
          return value
        },
        set(newValue) {
          value = newValue
        }
      })
    })
  }
  Observer(data)
  console.log(data)
```

#### 观察者模式

```js
class Vue extends EventTarget{
  constructor(opts) {
    super()
    this.opts = opts
    this._data = opts.data
    this.Observer(this._data)
    this.compile()
  }
  compile() {
    let el = document.querySelector(this.opts.el)
    // console.log(el)
    this.compileNode(el)
  }
  // 观察函数 数据劫持函数
  Observer(data) {
    let keys = Object.keys(data)
    let _this = this
    keys.forEach(key => {
      let value = data[key]
      Object.defineProperty(data, key, {
        configurable: true,
        enumerable: true,
        get() {
          console.log('get')
          return value
        },
        set(newValue) {
          console.log('set', newValue)
          _this.dispatchEvent(new CustomEvent(key, {
            detail: newValue
          }))
          value = newValue
        }
      })
    })
  }
  compileNode(el) {
    let childNodes = el.childNodes
    // console.log(childNodes)
    childNodes.forEach(node => {
      if (node.nodeType === 3) {
        // console.log('文本')
        let textContent = node.textContent
        // console.log(textContent)
        let reg = /\{\{\s*([^\{\}\s}]+)\s*\}\}/g
        if (reg.test(textContent)) {
          console.log('存在大胡子语法')
          let $1 = RegExp.$1
          node.textContent = textContent.replace(reg, this._data[$1])
          this.addEventListener($1, (e) => {
            console.log('设置了值')
            console.log(e.detail)
            node.textContent = textContent.replace(reg, e.detail)
          })
        }
      } else if (node.nodeType === 1) {
        console.log('节点')
        if (node.childNodes.length > 0) {
          this.compileNode(node)
        }
      }
    })
  }
}
```

**观察者模式是通过在数据劫持的`set`中派发事件，在替换数据的地方去渲染`新的数据`**

#### 发布订阅者模式

```js
class Vue{
  constructor(opts) {
    this.opts = opts
    this._data = opts.data
    this.Observer(this._data)
    this.compile()
  }
  compile() {
    let el = document.querySelector(this.opts.el)
    // console.log(el)
    this.compileNode(el)
  }
  Observer(data) {
    let keys = Object.keys(data)
    let _this = this
    keys.forEach(key => {
      let value = data[key]
      let dep = new Dep()
      Object.defineProperty(data, key, {
        configurable: true,
        enumerable: true,
        get() {
          console.log('get')
          // 发布订阅者模式在get时候收集watcher
          if (Dep.target) {
            dep.addSub(Dep.target)
          }
          return value
        },
        set(newValue) {
          console.log('set', newValue)
          // 观察者模式
          // _this.dispatchEvent(new CustomEvent(key, {
          //   detail: newValue
          // }))
          //发布订阅者模式在set时候触发watcher
          dep.notify(newValue)
          value = newValue
        }
      })
    })
  }
  compileNode(el) {
    let childNodes = el.childNodes
    // console.log(childNodes)
    childNodes.forEach(node => {
      if (node.nodeType === 3) {
        let textContent = node.textContent
        let reg = /\{\{\s*([^\{\}\s}]+)\s*\}\}/g
        if (reg.test(textContent)) {
          console.log('存在大胡子语法')
          let $1 = RegExp.$1
          node.textContent = textContent.replace(reg, this._data[$1])
          // 观察者模式
          // this.addEventListener($1, (e) => {
          //   console.log('设置了值')
          //   console.log(e.detail)
          //   node.textContent = textContent.replace(reg, e.detail)
          // })
          // 发布订阅者模式
          new Watcher(this._data, $1,(newValue) => {
            console.log(newValue)
            node.textContent = textContent.replace(reg, newValue)
          })
        }
      } else if (node.nodeType === 1) {
        console.log('节点')
        if (node.childNodes.length > 0) {
          this.compileNode(node)
        }
      }
    })
  }
}

// 发布订阅者模式
// 订阅者模式
class Watcher {
  constructor(data, key, cb) {
    this.cb = cb
    // 静态属性
    Dep.target = this
    data[key] // 触发get
    Dep.target = null //清空
  }
  update(newValue) {
    this.cb(newValue)
  }
}

// dep管理器
class Dep {
  constructor() {
    this.subs = []
  }
  addSub(sub) {
    this.subs.push(sub)
  }
  notify(newValue) {
    this.subs.forEach(sub => {
      sub.update(newValue)
    })
  }
}

```

**通过三者之间的关系 发布者 管理器 订阅者来关联 通过对象来进行事件传递**

#### v-model

```js
class Vue{
  constructor(opts) {
    this.opts = opts
    this._data = opts.data
    this.Observer(this._data)
    this.compile()
  }
  compile() {
    let el = document.querySelector(this.opts.el)
    // console.log(el)
    this.compileNode(el)
  }
  Observer(data) {
    let keys = Object.keys(data)
    let _this = this
    keys.forEach(key => {
      let value = data[key]
      let dep = new Dep()
      Object.defineProperty(data, key, {
        configurable: true,
        enumerable: true,
        get() {
          console.log('get')
          // 发布订阅者模式在get时候收集watcher
          if (Dep.target) {
            dep.addSub(Dep.target)
          }
          return value
        },
        set(newValue) {
          console.log('set', newValue)
          // 观察者模式
          // _this.dispatchEvent(new CustomEvent(key, {
          //   detail: newValue
          // }))
          //发布订阅者模式在set时候触发watcher
          dep.notify(newValue)
          value = newValue
        }
      })
    })
  }
  compileNode(el) {
    let childNodes = el.childNodes
    console.log(childNodes)
    childNodes.forEach(node => {
      if (node.nodeType === 3) {
        let textContent = node.textContent
        let reg = /\{\{\s*([^\{\}\s}]+)\s*\}\}/g
        if (reg.test(textContent)) {
          console.log('存在大胡子语法')
          let $1 = RegExp.$1
          node.textContent = textContent.replace(reg, this._data[$1])
          // 观察者模式
          // this.addEventListener($1, (e) => {
          //   console.log('设置了值')
          //   console.log(e.detail)
          //   node.textContent = textContent.replace(reg, e.detail)
          // })
          // 发布订阅者模式
          new Watcher(this._data, $1,(newValue) => {
            console.log(newValue)
            node.textContent = textContent.replace(reg, newValue)
          })
        }
      } else if (node.nodeType === 1) {
        console.log('节点')
        console.log(node)
        let attrs = node.attributes
        attrs = [...attrs]
        attrs.forEach(attr => {
          console.log(attr)
          let attrValue = attr.value
          let attrName = attr.name
          // console.log(attr.name)
          // console.log(attr.value)
          // 拿到v-model属性
          if (attrName === 'v-model') {
            console.log(this._data[attrValue])
            node.value = this._data[attrValue]
            console.log(node.value)
            node.addEventListener('input', (e) => {
              console.log(e.target.value)
              let newValue = e.target.value
              // 触发了set
              this._data[attrValue] = newValue
            })
          }
        })
        console.log(attrs)
        if (node.childNodes.length > 0) {
          this.compileNode(node)
        }
      }
    })
  }
}

// 发布订阅者模式
// 订阅者模式
class Watcher {
  constructor(data, key, cb) {
    this.cb = cb
    Dep.target = this
    data[key] // 触发get
    Dep.target = null //清空
  }
  update(newValue) {
    this.cb(newValue)
  }
}

// dep管理器
class Dep {
  constructor() {
    this.subs = []
  }
  addSub(sub) {
    this.subs.push(sub)
  }
  notify(newValue) {
    this.subs.forEach(sub => {
      sub.update(newValue)
    })
  }
}

```


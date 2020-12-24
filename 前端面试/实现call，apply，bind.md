# call

**⾸先 context 为可选参数，如果不传的话默认上下⽂为 window**

**接下来给 context 创建⼀个 fn 属性，并将值设置为需要调⽤的函数** 

**因为 call 可以传⼊多个参数作为调⽤函数的参数，所以需要将参数剥离出来** 

**然后调⽤函数并将对象上的函数删除**

```js
Function.prototype.myCall = function (context) {
    if (typeof this != "function") {
      throw new TypeError("Error");
    }
    context = context || window;
    context.fn = this;
    const args = [...arguments].slice(1);
    const result = context.fn(...args);
    delete context.fn;
    return result;
  }
```

# apply

```js
Function.prototype.myApply = function(context) {
if (typeof this !== 'function') {
throw new TypeError('Error') }
context = context || window
context.fn = this
let result
// 处理参数和 call 有区别
if (arguments[1]) {
 result = context.fn(...arguments[1]) 
} else {
 result = context.fn() 
}
 delete context.fn
 return result
}
```


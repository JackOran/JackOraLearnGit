## 1 准备

### 区别实例对象与函数对象

1. 实例对象： new 函数产生的对象，称为实例对象，简称为对象
2. 函数对象： 将函数作为对象使用时，简称为函数对象

```js
function Fn(){

}
const fn = new Fn();       // fn 是实例对象 Fn 是构造函数
console.log(Fn.prototype); // Fn 是函数对象
Fn.bind({});               // Fn是构造函数
$('#test');                // JQuery 函数 
$.get('/test');            // jQueey 函数对象
```

### 两种类型的回调函数

#### 同步回调

- 理解 ： 立即执行，完全执行完了才结束，不会放入回调队列中

- 例子： 数组遍历相关的回调函数 / Promise 的 excutor 函数

- ```js
  const arr = [1,3,5];
  arr.forEach(item=>console.log(item));
  console.log('foEach 之后')
  // 输出结果  135 forEach 之后
  ```

- 

#### 异步回调

- 理解： 不会立即执行，会放入回调队列中将来执行
- 例子 ： 定时器回调 / ajax 回调 / Promise 的成功或失败的回调

```js
setTimeout(()=>{    // 异步回调函数，会放入队列中将来执行
	console.log('a')
})
console.log('b');
```

### JS 的 error 处理

#### 错误的类型

1. Error ： 所有错误的父类型
2. ReferenceError： 引用的变量不存在  `console.log(a)` ReferenceError : a sis not defined 没有捕获 error 下面的代码不会执行；
3. TypeError： 数据类型不正确的错误  `TypeError`: Cannot read property 'xxx' of undefined
4. RangeError ： 数据值不在其所允许的范围内 fn (){ fn()  }; fn();
5. SyntaxError ： 语法错误

#### 错误处理

1. 捕获错误 ： try....catch

2. 抛出错误： throw error

   ```js
   function something(){
     if(Date.now() % 2 === 1){
       console.log('ok');
     }else{   				// 如果时间是偶数抛出异常，由调用来处理
       throw new Error('当前时间为偶数');  // 参数为错误信息
     }
   }
   
   try{
     someting();
   }catch(error){
     console.log(error.message)   // 当前时间为偶数
   }
   ```

   

#### 错误对象

1. message 属性 ： 错误相关信息
2. stack属性： 函数调用栈记录信息



## Promise 的理解和使用

### 指定回调函数的方式更加灵活

1. 旧的 ： 必须在启动异步任务前指定
2. Promise ： 启动异步任务 =》 返回Promise 对象 =》 给 Promise 对象绑定回调函数 甚至可以在异步任务结束后指定多个 

简单理解 ： Promise 是 Js 中进行异步编程的新的解决方案

### 支持链式调用，可以解决回调地狱问题

1. 什么是回调地狱  ： 回调函数的嵌套调用，外部回调函数异步执行的结果是嵌套的回调函数执行的条件
2. 回调地狱的缺点 ： 不便于阅读 不便于异常处理
3. 解决方案 ： Promise 链式调用
4. 最终解决方案 ： async / await

### 具体表达

1. 从语法上来说 ： Promise 是一个构造函数
2. 从功能上来说： promise 对象用来封装一个异步操作并可以获取其结果

### Promise 的状态改变

1. pendding 变为 resolved

2. pendding 变为 rejected

   说明 ： 只有这 两种，且一个promise 对象只能改变一次

   ​			 无论变为成功还是失败，都会有一个结果数据

   ​			 成功的结果数据一般称为 value， 失败的结果数据一般称为 reason （原因）

```js
															成功 --> promise对象 --> then()
																			resolved 状态			回调 onResolved()--->
new Promise() ---> 执行异步操作																							新的promise对象
pendding状态
															失败 --> promise对象 --> 	 回调 onRejected()--->
																			rejected 状态			then()/ catch()
```

```js
// 创建一个新的 Promise 对象
const p = new Promise((resolve,reject)=>{ // 执行器函数  同步回调
    // 2. 执行异步操作任务
    setTimeout(()=>{
        const time = Date.now();  // 如果当前时间是偶数就代表成功，否则代表失败
         // 如果成功了   调用 resolve(value)
        if(time % 2 === 0 ){
            resolve(' 成功的数据:' + time);
        }else{
         // 如果失败了   调用 reject (reason)
         reject('失败的数据 ：' + time);
        }
    })  
})

p.then(value=>{
    // 接收得到成功的value 数据    onResolved
    console.log('成功的回调:',value);              // 成功的回调:  成功的数据:1597894429058
},reason=>{
    // 接收得到失败的 reason 数据  onRejected
    console.log('失败的回调:' + value); 						// 失败的回调： 失败的数据 ：1597894430907
})
```



### 如何使用 Promise

#### API

1. Promise 构造函数 : Promise(excuto) {}

   1. Excutor 函数 ： 执行前期 (resolve,reject) => {}

   2. resolve 函数 ： 内部定义成功是我们调用的函数 value => {}

   3. reject 函数 ： 内部定义失败是我们调用的函数 reason => {}

      说明 ： excutor 会在 Promise 内部立即同步回调 ，异步操作在执行器中执行

2. Promise.prototype.then 方法 :(onResolved,onRejected) => {} 

   onResolved 函数 ：成功的回调函数 (value) => {}

   onRejected 函数 ：失败的回调函数 (reason) => {}

   说明 ：指定用于得到成功 value 的成功回调和用于得到失败 reason 的失败回调

   ​				返回一个新的 promise 对象

3. Promise.prototype.catch 方法： (onRejected) => {}

   onRejected 函数 ： 失败的回调函数 (reason) => {}

   说明 ： then() 的语法糖 相当于 : then (undefined,onRejected)

4.  Promise.resolve 方法 ： (value) => {}

     value : 成功的数据 或 promise 对象

   说明 ：返回一个成功/ 失败的  promise 对象

5. Promise.reject 方法 ： (reason) => {}

   reason : 失败的回调

   说明 ： 返回一个失败的 promise 对象

6. Promise.all 方法 ： (promises) => {}

   promises : 包含n 个 promise 的数组

   说明 ：返回一个新的 promise 只有所有的promise都成功才成功，只要有一个失败率就直接失败

7. Promise.race 方法 : (promises) => {}

   Promises : 包含 n个 promise 的数组

   说明 ： 返回一个新的 promise 第一个完成的 promise 的结果状态就是最终的结果状态

```js
new Promise((resolve, reject) => {
  setTimeout(() => {
    // resolve('成功的数据');
    reject('失败的数据')
  }, 1000)
}).then(value => {
  console.log(value);
}).catch(reason => {
  console.log(reason);
})

// 产生一个成功值 为 1 的 promise 对象
const p1 = new Promise((resolve, reject) => {
  setTimeout(()=>{
    resolve(1);
  },1)
})

const p2 = Promise.resolve(2);
const p3 = Promise.reject(3);
p1.then(value=>{ console.log(value);});
p2.then(value => { console.log(value);})
p3.then(value=>{},reason => {console.log(reason);})

const pAll = Promise.all([p1,p2]);

pAll.then(value=>{
  console.log('all onResolved',value);    // 成功为 成功的promise
},reason=>{
  console.log('all onRejected()',reason);  // 如果失败 为失败的那个 promise
})
console.log(0);

const pRace = Promise.race([p1,p2,p3])
pRace.then(value =>{
  console.log('race onResolved',value);
},reason =>{
  console.log('race onRejected',reason);
})
```



### promise 的几个关键问题

1. 如何改变 promise 的状态

   1. Resolve(value) : 如果当前是 penddig 就会变为 resolve
   2. reject(reason): 如果当前是 pendding 就会变为 rejected
   3. 抛出异常 ： 如果当前是 pendding 就会变为 rejected

   ```js
    const p = new Promise((resolve,reject)=>{
           // resolve(1); // promise 变为 resolved 成功状态 成功的值 1
           // reject(2);  // promise 变为 rejected 失败状态 失败的值 2
           throw new Error('出错了'); // 抛出异常 promise 变为 rejected 失败状态 reason 为抛出的 error
       })
       p.then(value=>{},reason=>{
           console.log(reason.message);
       })
       p.then(value=>{},reason => {
           console.log(reason.message);
       })
   ```

   

2. 一个promise 指定多个成功/失败回调函数 都会调用吗？

   1. 当promise 改变为对应状态时都会调用

3. 改变 promise 状态和指定回调函数谁先谁后

   1. 都有可能，正常情况下是先指定回调再改变状态，但也可以改状态再指定回调

   2. 如何先改状态再指定回调

      1. 在执行器中直接调用 resolve()/ reject()
      2. 延迟更长时间才调用 then()

      ````js
      // 常规 ： 先指定回调函数，后改变的状态
      new Promise((resolve,reject)=>{
        setTimeout(()=>{
          console.log(2); 
          // resolve(1); // 后改变的状态(同时指定数据) 异步执行回调函数
          reject(3);
        },1000)             
      })  
        .then(value=>{     // 先指定回调，保存当前指定的回调函数
        // console.log(value);
      },reason=>{
        console.log(reason);
      })
      
      // 如何先改状态 ，后指定回调函数
      new Promise((resolve,reject)=>{
        resolve('a'); // 先改变的状态        
        reject('b');  
      })  
        .then(value=>{     // 后指定回调，异步执行回调函数
        console.log(value);
      },reason=>{
        console.log(reason);
      })
      ````

4.  Promise.then() 返回的新 promise 的结果状态由什么决定

   1. 简单表达 ： 由 then() 指定的回调函数执行的结果决定
   2. 详细表达 ：
      1. 如果抛出异常，新 promise 变为 rejected，reason 为抛出异常结果
      2. 如果返回的时非 promise 的任意值，新promise 变为 resolved value为返回的值
      3. 如果返回的是另一个新 promise 此 promise的结果就会成为新promise的结果

   ```js
   const p = new Promise((resolve,reject)=>{
     // resolve(1)
     reject(1)
   }).then(
     value => {
       console.log('onResolve1()',value);
     },
     reason => {
       console.log('onReject()1',reason);
     }
   ).then(
     value => {
       console.log('onResolve2()',value);
     },
     reason => {
       console.log('onReject()2',reason);
     }
   )
   ```

5. Promise 如何串联多个操作任务

   1. promise 的 then()返回一个新的promise，可以开成then() 的链式调用
   2. 通过then的链式调用串联多个同步/异步操作

   ```js
   new Promise((resolve,reject)=>{
     setTimeout(()=>{
       console.log('执行异步任务1');
       resolve(1);
     },1000)
   }).then(
     value=>{
       console.log('执行同步任务2');
       return 2;
     }
   ).then(
     value => {
       console.log('任务2的结果',value);
   
       return new Promise((resolve,reject)=>{
         // 启动任务3 异步
         setTimeout(()=>{
           console.log('执行任务 3 异步');
           resolve(3);
         },1000)
       })
     }
   ).then(
     value => {
       console.log('任务3的结果',value);
     }
   )
   ```

6. Promise 异常传透

   1. 当使用promise 的then链式调用时，可以在最后指定失败的回调
   2. 前面任何操作处理异常，都会传到最后失败的回调中处理

7. 中断promise链

   1. 当使用 promise的then 链式调用时，在中间中断，不再调用后面的回调函数
   2. 办法 ： 在回调函数中返回一个 pendding 状态的promise对象

   ```
   返回一个 pendding状态的 promise
   ```

   

## 自定义（手写）Promise

### 定义整体结构

```js
// 自定义 Promise 函数模块
(function (window) {
  const PENDING = 'pending';
  const RESOLVED = 'resolved';
  const REJECTED = 'rejected'
  // Promise 构造函数
  // excutor 执行器
  function Promise(excutor) {
    const that = this;
    that.status = PENDING // 给 promise 对象指定status 属性 初始值为pending
    that.data = undefined;   // 给 promise 对象指定一个用于存储结果数据的属性
    that.callbacks = [];     // 每个元素的结构 { onResolved(){},onRejected(){}}
    function resolve(value) {

      // 如果当前状态不是 pending 直接结束
      if (that.status !== PENDING) {
        return
      }

      // 将状态改为 RESOLVED
      that.status = RESOLVED;
      // 保存 value数据
      that.data = value;
      // 如果有待执行的 callback 函数，立即异步执行回调
      if (that.callbacks.length > 0) {
        setTimeout(() => { // 放入队列中执行所有的成功回调
          that.callbacks.forEach(callbacksObj => {
            callbacksObj.onResolved(value)
          })
        })
      }
    }

    function reject(reason) {

      if (that.status !== PENDING) {
        return
      }

      that.status = REJECTED;
      that.data = reason;

      if (that.callbacks.length > 0) {
        setTimeout(() => {
          that.callbacks.forEach(callbacksObj => {
            callbacksObj.onRejected(reason);
          })
        })
      }
    }

    // 立即执行excutor
    try {
      excutor(resolve, reject);

    } catch (error) {  // 如果执行器抛出异常 promise对象变为 rejected失败状态
      reject(error)
    }
  }

  // Promise原型对的then()
  // 指定成功和失败的回调函数
  // 返回一个新的 Promise 对象
  Promise.prototype.then = function (onResolved, onRejected) {
    onResolved = typeof onResolved === 'function' ? onResolved : value => value;
    // 指定默认失败的回调 （实现错误/异常传透的关键点）
    onRejected = typeof onRejected === 'function' ? onRejected : reason => { throw reason };
    // 假设当前状态还是 pending状态 将回调函数保存起来
    const that = this;
    // 返回一个新的promise 对象
    return new Promise((resolve, reject) => {
      function handle(callback) {
        // 1. 如果抛出异常  return promise 就会是啊比 reason 就是err

        // 2. 如果回调函数执行返回 非 promise return 的promise 就会成功 value 就是成功的值
        // 3. 如果回调函数返回是 promise return的promise 结果就是这个promise的结果
        try {
          const result = callback(that.data);
          if (result instanceof Promise) {
            // result.then(
            //     value => resolve(value), // 当result 成功时
            //     reason => reject(reason) // 当 result 失败时
            // )
            result.then(resolve, reject)
          } else {
            resolve(result);
          }
        } catch (error) {
          reject(error);
        }
      }
      if (that.status === PENDING) {
        that.callbacks.push({
          onResolved() {
            handle(onResolved);
          },
          onRejected() {
            handle(onRejected)
          }
        })
      } else if (that.status === RESOLVED) {
        setTimeout(() => {
          handle(onResolved);
        })
      } else {
        setTimeout(() => {
          handle(onRejected)
        })
      }
    })
  }


  // Promise 原型对象 catch 方法
  // 指定失败的回调函数 
  // 返回一个新的 Promise 对象
  Promise.prototype.catch = function (onRejected) {
    return this.then(undefined, onRejected)
  }

  // Promise 函数对象resolve
  // 返回一个指定结果的成功 Promise
  Promise.resolve = function (value) {
    return new Promise((resolve, reject) => {
      if (value instanceof Promise) { // 使用 value的结果作为 promise的结果
        value.then(resolve, reject);
      } else {  // value 不是 promise =》 promise 变为成功，数据是value
        resolve(value)
      }
    })
  }

  // Promise 函数对象reject 方法
  // 返回一个指定 reason 的失败 promise
  Promise.reject = function (reason) {
    // 返回一个失败的 promise
    return new Promise((resolve, reject) => {
      reject(reason);
    })
  }

  //Promise 函数对象 all 方法
  // 返回一个 promise 只有当所有的promises都成功是才成功，否则只要有一个失败的就失败
  Promise.all = function (promises) {
    const values = new Array(promises.length); // 用来保存所有成功value 的值

    // 用来保存成功promise的数量
    let resolvedCount = 0;
    return new Promise((resolve, reject) => {
      // 遍历获取每个promise的结果
      promises.forEach((p, index) => {
        Promise.resolve(p).then(
          value => { // p成功 将成功的值保存values
            resolvedCount++;
            values[index] = value;
            // 如果全部成功，将return 的promise改为成功
            if (resolvedCount === promises.length) {
              resolve(values);
            }
          },
          reason => { // 只要有一个失败率 return的pomise就是啊比
            reject(reason);
          }
        )
      })
    })
  }

  // Promise 构造对象 的race 方法
  // 返回一个 promise 其结果由第一个完成的promise决定
  Promise.race = function (promises) {
    // 返回一个 promise
    return new Promise((resolve, reject) => {
      promises.forEach((p, index) => {
        Promise.resolve(p).then(
          value => { // 一旦成功了 将return变为成
            resolve(value);
          },
          reason => { // 一旦又失败 将return 变为失败
            reject(reason)
          }
        )
      })
    })
  }

  
  // 返回一个 promise对象 他在指定的时间才确定结果
  Promise.resolveDelay = function(value,time){
    return new Promise((resolve,reject)=>{
      setTimeout(() => {
        if(value instanceof Promise){
          value.then(resolve,reject);
        }else{
          resolve(value);
        }
      },time)
    })
  }

  // 返回一个 promise 对象，他在指定的时候后才失败
  Promise.rejectDelay = function(reason,time){
    return new Promise((resolve,reject) => {
      setTimeout(()=>{
        reject(reason)
      },time)
    })
  }
  window.Promise = Promise;
})(window)
```

### Promise 构造类

```js
// 自定义 Promise 函数模块
(function (window) {
  const PENDING = 'pending';
  const RESOLVED = 'resolved';
  const REJECTED = 'rejected'
  // Promise 构造函数
  // excutor 执行器
  class Promise {
    constructor(excutor) {
      const that = this;
      that.status = PENDING // 给 promise 对象指定status 属性 初始值为pending
      that.data = undefined;   // 给 promise 对象指定一个用于存储结果数据的属性
      that.callbacks = [];     // 每个元素的结构 { onResolved(){},onRejected(){}}
      function resolve(value) {

        // 如果当前状态不是 pending 直接结束
        if (that.status !== PENDING) {
          return
        }

        // 将状态改为 RESOLVED
        that.status = RESOLVED;
        // 保存 value数据
        that.data = value;
        // 如果有待执行的 callback 函数，立即异步执行回调
        if (that.callbacks.length > 0) {
          setTimeout(() => { // 放入队列中执行所有的成功回调
            that.callbacks.forEach(callbacksObj => {
              callbacksObj.onResolved(value)
            })
          })
        }
      }

      function reject(reason) {

        if (that.status !== PENDING) {
          return
        }

        that.status = REJECTED;
        that.data = reason;

        if (that.callbacks.length > 0) {
          setTimeout(() => {
            that.callbacks.forEach(callbacksObj => {
              callbacksObj.onRejected(reason);
            })
          })
        }
      }

      // 立即执行excutor
      try {
        excutor(resolve, reject);

      } catch (error) {  // 如果执行器抛出异常 promise对象变为 rejected失败状态
        reject(error)
      }
    }

    // Promise原型对的then()
    // 指定成功和失败的回调函数
    // 返回一个新的 Promise 对象
    then(onResolved, onRejected) {
      onResolved = typeof onResolved === 'function' ? onResolved : value => value;
      // 指定默认失败的回调 （实现错误/异常传透的关键点）
      onRejected = typeof onRejected === 'function' ? onRejected : reason => { throw reason };
      // 假设当前状态还是 pending状态 将回调函数保存起来
      const that = this;
      // 返回一个新的promise 对象
      return new Promise((resolve, reject) => {
        function handle(callback) {
          // 1. 如果抛出异常  return promise 就会是啊比 reason 就是err

          // 2. 如果回调函数执行返回 非 promise return 的promise 就会成功 value 就是成功的值
          // 3. 如果回调函数返回是 promise return的promise 结果就是这个promise的结果
          try {
            const result = callback(that.data);
            if (result instanceof Promise) {
              // result.then(
              //     value => resolve(value), // 当result 成功时
              //     reason => reject(reason) // 当 result 失败时
              // )
              result.then(resolve, reject)
            } else {
              resolve(result);
            }
          } catch (error) {
            reject(error);
          }
        }
        if (that.status === PENDING) {
          that.callbacks.push({
            onResolved() {
              handle(onResolved);
            },
            onRejected() {
              handle(onRejected)
            }
          })
        } else if (that.status === RESOLVED) {
          setTimeout(() => {
            handle(onResolved);
          })
        } else {
          setTimeout(() => {
            handle(onRejected)
          })
        }
      })
    }


    // Promise 原型对象 catch 方法
    // 指定失败的回调函数 
    // 返回一个新的 Promise 对象
    catch(onRejected) {
      return this.then(undefined, onRejected)
    }

    // Promise 函数对象resolve
    // 返回一个指定结果的成功 Promise
    static resolve = function (value) {
      return new Promise((resolve, reject) => {
        if (value instanceof Promise) { // 使用 value的结果作为 promise的结果
          value.then(resolve, reject);
        } else {  // value 不是 promise =》 promise 变为成功，数据是value
          resolve(value)
        }
      })
    }

  // Promise 函数对象reject 方法
  // 返回一个指定 reason 的失败 promise
  static reject = function (reason) {
    // 返回一个失败的 promise
    return new Promise((resolve, reject) => {
      reject(reason);
    })
  }

  //Promise 函数对象 all 方法
  // 返回一个 promise 只有当所有的promises都成功是才成功，否则只要有一个失败的就失败
  static all = function (promises) {
    const values = new Array(promises.length); // 用来保存所有成功value 的值

    // 用来保存成功promise的数量
    let resolvedCount = 0;
    return new Promise((resolve, reject) => {
      // 遍历获取每个promise的结果
      promises.forEach((p, index) => {
        Promise.resolve(p).then(
          value => { // p成功 将成功的值保存values
            resolvedCount++;
            values[index] = value;
            // 如果全部成功，将return 的promise改为成功
            if (resolvedCount === promises.length) {
              resolve(values);
            }
          },
          reason => { // 只要有一个失败率 return的pomise就是啊比
            reject(reason);
          }
        )
      })
    })
  }

  // Promise 构造对象 的race 方法
  // 返回一个 promise 其结果由第一个完成的promise决定
  static race = function (promises) {
    // 返回一个 promise
    return new Promise((resolve, reject) => {
      promises.forEach((p, index) => {
        Promise.resolve(p).then(
          value => { // 一旦成功了 将return变为成
            resolve(value);
          },
          reason => { // 一旦又失败 将return 变为失败
            reject(reason)
          }
        )
      })
    })
  }

  // 返回一个 promise对象 他在指定的时间才确定结果
  static resolveDelay = function (value, time) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (value instanceof Promise) {
          value.then(resolve, reject);
        } else {
          resolve(value);
        }
      }, time)
    })
  }

  // 返回一个 promise 对象，他在指定的时候后才失败
  static rejectDelay = function (reason, time) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        reject(reason)
      }, time)
    })
  }


}


 window.Promise = Promise;
 })(window)
```

## async 和 await

### Async function

1. 函数的返回值为 promise 对象
2. promise 对象的结果由async 函数执行的返回值决定

### await表达式

1. await 右侧的表达式一般为promise 对象，但也可以是其它的值
2. 如果表达式是 promise 对象，await 返回的是 promise 成功的值

### 注意： 

await必须写在 async 函数中，但async 函数中可以没有 await

如果await 的promise 失败了，就会抛出异常，需要通过 try...catch 来捕获处理

```js
async function fn1 (){
  throw 1
}
const result = fn1();
// console.log(result);
result.then(
  value => {
    console.log('onResolved',value);
  },
  reason => {
    console.log('onRejected',reason);
  }
)

function fn2 (){
  return new Promise((resolve,reject) => {
    setTimeout(()=>{
      reject(5);
    },1000)
  })

}

function fn4(){
  return 6;
}
async function fn3(){
  try{
    const value = await fn2();
    console.log(value);
  }catch(error){
    console.log(error);
  }
  // const value = await fn2(); // await 右侧表达为promise，得到的结果是promise成功
  // const value = await fn4();      // await 右侧表达不是promise，得到的结果就是表达式的返回值
  // console.log(value);
}
fn3();

// 执行结果
Promise onResolved1 1
Promise onResolved2 2
timeout callback1()
Promise onResolved3 3
timeout callback2()
```

## Js 异步之宏队列与微队列



![截屏2020-08-21 下午1.45.12](/Users/tanganchun/Desktop/截屏2020-08-21 下午1.45.12.png)

### 说明

1. Js 中用来存储待执行回调函数的队列包含2个不同特定的列队
2. 宏列队：用来保存待执行的宏任务(回调)，比如：定时器回调/DOM 事件回调/AJAX回调
3. 微队列：用来保存待执行的微任务(回调)，比如 ： Promise的回调 / MutationObserver 回调
4. JS执行时会区别这 2 个队列
   1. JS 引擎首先必须先执行所有的初始化同步任务代码
   2. 每次准备去除第一个宏任务执行前，都要将所有的微任务一个一个取出来执行



## Promise 相关面试题

```js
setTimeout(()=>{
  console.log(1);
})
Promise.resolve().then(()=>{
  console.log(2);
})
Promise.resolve().then(()=>{
  console.log(4);
})
console.log(3);

// 执行结果 
3
2
4
1
```

2.

``````js
setTimeout(() => {
  console.log(1);
})
new Promise((resolve) => {
  console.log(2)
  resolve();
}).then(() => {
  console.log(3);
}).then(() => {
  console.log(4);
})
console.log(5);

// 执行结果 
2
5
3
4
1
``````

3.

```js
const first = () => (new Promise((resolve, reject) => {
  console.log(3);
  let p = new Promise((resolve, reject) => {
    console.log(7);
    setTimeout(() => {
      console.log(5);
      resolve(6)
    })
    resolve(1)
  })
  resolve(2)
  p.then((arg) => {
    console.log(arg); // 1
  })
}))

first().then((arg) => {
  console.log(arg); // 2
})
console.log(4);

// 同步 3 7 4
// 宏队列 [5]
// 微队列 [1,2]
```

4

```js
setTimeout(() => {
  console.log('0');
})
new Promise((resolve,reject) => {
  console.log('1');
  resolve()
}).then(() => {
  console.log('2');
  new Promise((resolve,reject) => {
    console.log('3');
    resolve()
  }).then(() => {
    console.log('4');
  }).then(()=>{
    console.log('5');
  })
}).then(() => {
  console.log('6');
})

new Promise((resolve,reject) => {
  console.log('7');
  resolve();
}).then(() => {
  console.log('8');
})


// 同步 1 3  7
// 微 [2,8,4,6,5]
// 宏 [0]
```

## Promise与AJAX，NODEAPI

```js
 // 创建 promise 对象
    const p = new Promise((resolve,reject) =>{
        setTimeout(()=>{
            resolve('用户数据');
            // reject('失败');
        },1000)
    });

    // 调用then 方法，then方法的返回结果是Promise 对象，对象状态由回调函数的执行结果决定
    // 1.如果回调函数中返回的结果是 非Promise 类型的属性,状态为成功,返回值为对象的成功值
		// 通过改变返回值来决定Promise 对象的状态 或者直接抛出错误  Promise对象 的PromiseValue的值 				就是返回值
   const result = p.then(value =>{
        console.log(value);
        // 1.非promise 类型的属性
        // return 123;				
        // 2.是promise 对象
        // return new Promise((resolve,reject)=>{
        //     // resolve('ok');
        //     reject('error')
        // })
        // 3. 抛出错误
        throw new Error('出错了');
    },reason =>{
        console.log(reason);
    })
    console.log(result);

	then方法可以连续调用 链式调用
  then方法指定回调的时候也可以指定一个，也就是可以省略一个
  then方法的回调中也可以在跟着一个异步任务，形成链式调用，杜绝回调地狱
  p.then(value=>{},reason=>{}).then(value=>{},reason=>{})
```

### Promise then链式调用解决回调地狱

```js
// 引入fs模块
const fs = require('fs');
const { resolve } = require('path');
// const { resolve } = require('path');
// fs.readFile('/Users/tanganchun/Desktop/js/js阶段/7第七篇 ES6/床前明月光.md',(err,data1) => {
//     fs.readFile('/Users/tanganchun/Desktop/js/js阶段/7第七篇 ES6/面对疾风.md',(err,data2)=>{
//         fs.readFile('/Users/tanganchun/Desktop/js/js阶段/7第七篇 ES6/数据.md',(err,data3)=>{
//             let result = data1 +'\r\n'+ data2 +'\r\n'+ data3;
//             console.log(result);
//         });
//     });
// });


const p = new Promise((resolve, reject) => {
  fs.readFile('/Users/tanganchun/Desktop/js/js阶段/7第七篇 ES6/床前明月光.md', (err, data) => {
    resolve(data);
  })
})
p.then(value => {
  return new Promise((resolve, reject) => {
    fs.readFile('/Users/tanganchun/Desktop/js/js阶段/7第七篇 ES6/面对疾风.md', (err, data) => {
      resolve([value,data])
    })
  })
}).then(value =>{
  return new Promise((resolve, reject) => {
    fs.readFile('/Users/tanganchun/Desktop/js/js阶段/7第七篇 ES6/数据.md', (err, data) => {
      value.push(data);
      resolve(value)
    })
  })
}).then(value =>{
  console.log(value.join('\r\n'));
})
```

### Promise.allsettled() 方法

```js
Promise.allSettled() 方法接收一个promise对象组成的数组参数，返回结果也是promise 对象 而且状态为成功
 #    而且成功的值是每一个Promise 对象的结果的值 以及成功 或 失败的状态
   // 声明 两个 Promise 对象
    const p1 = new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve('嘿嘿嘿 + 1')
        },1000)
    })
    const p2 = new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve('嘿嘿嘿 + 2');
        })
    })
    // 调用 allSettled 方法
    const result = Promise.allSettled([p1,p2]);
    console.log(result);

# 如果每一个异步任务都需要知道结果就用 allSettled 如果必须每一个异步任务都需要成功执行则用 all
```

### promise封装AJAX

```js
// 发送AJAX请求，返回的结果是 Promise 对象
function sendAJAX(url) {
  return new Promise((resolve, reject) => {
    // 创建对象
    const x = new XMLHttpRequest();
    // 初始化
    x.open('GET', url);

    // 发送
    x.send();

    // 事件绑定
    x.onreadystatechange = function () {
      if (x.readyState === 4) {
        if (x.status >= 200 && x.status < 300) {
          // 成功
          resolve(x.response);
        }else{
          // 失败
          reject(x.status);
        }
      }
    }
  })
}

sendAJAX('https://api.apiopen.top/getJoke').then(value=>{
  console.log(value);
},reason=>{
  console.error(reason);
});

#// 使用 async await
// 发送AJAX请求，返回的结果是 Promise 对象
function sendAJAX(url) {
  return new Promise((resolve, reject) => {
    // 创建对象
    const x = new XMLHttpRequest();
    // 初始化
    x.open('GET', url);
    // 发送
    x.send();
    // 事件绑定
    x.onreadystatechange = function () {
      if (x.readyState === 4) {
        if (x.status >= 200 && x.status < 300) {
          // 成功
          resolve(x.response);
        } else {
          // 失败
          reject(x.status);
        }
      }
    }
  })
}

async function main() {
  let result = await sendAJAX('https://api.apiopen.top/getJoke');
  // let tianqi = await sendAJAX();
  console.log(result);
}
main();
```

### 封装Promise版本的 readFile

```js
const fs = require('fs');
function pReadFile(filePath){
  return new Promise((resolve,reject)=>{
    fs.readFile(filePath,'utf8',(err,data)=>{
      if(err) return  reject(err);
      resolve(data);
    })
  })
};

pReadFile('./a')
  .then(value=>{
  console.log(value);
  return pReadFile('./b')
})
  .then(value=>{
  console.log(value);
  return pReadFile('./c');
})
  .then(value=>{
  console.log(value);
})
```

## 闭包作用域链

1. 变量的查找基于作用域链，如果整条作用域链上都没有对应变量的声明，则会报错(右查询)

2. 变量的查找基于作用域链，如果整条作用域链上都没有对应变量的声明 则在全局自动声明一分(左查询)

   变量的查找 ： 左右查询

   左查询 ： 对等号左边的变量发起查询

   右查询： 对等号的非左边进行查询
   
   
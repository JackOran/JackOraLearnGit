### promise是什么？

1、主要用于**异步计算**。
2、可以将**异步操作队列化**，按照期望的顺序执行，返回符合预期的结果。
3、可以在对象之间传递和操作promise，帮助我们处理队列。



### promise

- promise是一个对象，对象和函数的区别就是对象可以保存状态，函数不可以（闭包除外）
- 并未剥夺函数return的能力，因此无需层层传递callback，进行回调获取数据
- 代码风格，容易理解，便于维护
- 多个异步等待合并便于解决

```js
new Promise(
  function (resolve, reject) {
    // 一段耗时的异步操作
    resolve('成功') // 数据处理完成
    // reject('失败') // 数据处理出错
  }
).then(
  (res) => {console.log(res)},  // 成功
  (err) => {console.log(err)} // 失败
)
```

resolve作用是，将Promise对象的状态从“未完成”变为“成功”（即从 pending 变为 resolved），在异步操作成功时调用，并将异步操作的结果，作为参数传递出去；
 reject作用是，将Promise对象的状态从“未完成”变为“失败”（即从 pending 变为 rejected），在异步操作失败时调用，并将异步操作报出的错误，作为参数传递出去。

promise有三个状态：
 **1、pending[待定]初始状态**
 **2、fulfilled[实现]操作成功**
 **3、rejected[被否决]操作失败**
 当promise状态发生改变，就会触发then()里的响应函数处理后续步骤；
 promise状态一经改变，不会再变。

Promise对象的状态改变，只有两种可能：
 **从pending变为fulfilled**
 **从pending变为rejected。**
 这两种情况只要发生，状态就凝固了，不会再变了。

```js
//分两次执行
new Promise(resolve => {
    setTimeout(() => {
      resolve('hello')
    }, 2000)
  }).then(val => {
    console.log(val) //  参数val = 'hello'
    return new Promise(resolve => {
      setTimeout(() => {
        resolve('world')
      }, 2000)
    })
  }).then(val => {
    console.log(val) // 参数val = 'world'
  })
```

##### Promise.all() 批量执行

Promise.all([p1, p2, p3])用于将**多个promise实例**，包装成一个新的Promise实例，返回的实例就是普通的**promise**
 它接收一个数组作为参数
 数组里可以是Promise对象，也可以是别的值，只有Promise会等待状态改变
 当所有的子Promise都完成，该Promise完成，返回值是**全部值的数组**
 有任何一个失败，该Promise失败，返回值是第一个失败的子Promise结果



```js
//切菜
    function cutUp(){
        console.log('开始切菜。');
        var p = new Promise(function(resolve, reject){        //做一些异步操作
            setTimeout(function(){
                console.log('切菜完毕！');
                resolve('切好的菜');
            }, 1000);
        });
        return p;
    }

    //烧水
    function boil(){
        console.log('开始烧水。');
        var p = new Promise(function(resolve, reject){        //做一些异步操作
            setTimeout(function(){
                console.log('烧水完毕！');
                resolve('烧好的水');
            }, 1000);
        });
        return p;
    }

    Promise.all([cutUp(), boil()])
        .then((result) => {
            console.log('准备工作完毕');
            console.log(result);
        })
```

##### Promise.race() 类似于Promise.all() ，区别在于它有任意一个完成就算完成

```js
let p1 = new Promise(resolve => {
        setTimeout(() => {
            resolve('I\`m p1 ')
        }, 1000)
    });
let p2 = new Promise(resolve => {
        setTimeout(() => {
            resolve('I\`m p2 ')
        }, 2000)
    });

    Promise.race([p1, p2])
        .then(value => {
            console.log(value)
        })
```



```js
// Promise 写法
  // 第一步：获取城市列表
  const cityList = new Promise((resolve, reject) => {
    $.ajax({
      url: 'https://www.easy-mock.com/mock/5a52256ad408383e0e3868d7/lagou/city',
      success (res) {
        resolve(res)
      }
    })
  })

  // 第二步：找到城市是北京的id
    cityList.then(res => {
      let findCityId = res.filter(item => {
        if (item.id == 'c1') {
          return item
        }
      })[0].id
      
      findCompanyId().then(res => {
        // 第三步（2）：根据北京的id -> 找到北京公司的id
        let findPostionId = res.filter(item => {
            if(item.cityId == findCityId) {
              return item
            }
        })[0].id

        // 第四步（2）：传入公司的id
        companyInfo(findPostionId)

      })

    })

  // 第三步（1）：根据北京的id -> 找到北京公司的id
  function findCompanyId () {
    let aaa = new Promise((resolve, reject) => {
      $.ajax({
        url: 'https://www.easy-mock.com/mock/5a52256ad408383e0e3868d7/lagou/position-list',
        success (res) {
          resolve(res)
        }
      })
    })
    return aaa
  }

// 第四步：根据上一个API的id(findPostionId)找到具体公司，然后返回公司详情
function companyInfo (id) {
  let companyList = new Promise((resolve, reject) => {
    $.ajax({
      url: 'https://www.easy-mock.com/mock/5a52256ad408383e0e3868d7/lagou/company',
      success (res) {
        let comInfo = res.filter(item => {
            if (id == item.id) {
               return item
            }
        })[0]
        console.log(comInfo)
      }
    })
  })
}
```


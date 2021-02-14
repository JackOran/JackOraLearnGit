### Vue记录

​	[将原生事件绑定到组件](https://cn.vuejs.org/v2/guide/components-custom-events.html#将原生事件绑定到组件)

​	 你可能有很多次想要在一个组件的根元素上直接监听一个原生事件。这时，你可以使用 `v-on` 的 `.native` 修饰符： 

```html
<base-input v-on:focus.native="onFocus"></base-input>
```

 有了这个 `$listeners` property，你就可以配合 `v-on="$listeners"` 将所有的事件监听器指向这个组件的某个特定的子元素。对于类似 `` 的你希望它也可以配合 `v-model` 工作的组件来说，为这些监听器创建一个类似下述 inputListeners` 的计算属性通常是非常有用的： 

```js
Vue.component('base-input', {
  inheritAttrs: false,
  props: ['label', 'value'],
  computed: {
    inputListeners: function () {
      var vm = this
      // `Object.assign` 将所有的对象合并为一个新对象
      return Object.assign({},
        // 我们从父级添加所有的监听器
        this.$listeners,
        // 然后我们添加自定义监听器，
        // 或覆写一些监听器的行为
        {
          // 这里确保组件配合 `v-model` 的工作
          input: function (event) {
            vm.$emit('input', event.target.value)
          }
        }
      )
    }
  },
  template: `
    <label>
      {{ label }}
      <input
        v-bind="$attrs"
        v-bind:value="value"
        v-on="inputListeners"
      >
    </label>
  `
})
```

#### vm.$attrs

包含了父作用域中不作为 `prop` 被识别 (且获取) 的特性绑定 (`class` 和 `style` 除外)。当一个组件没有声明任何`prop` 时，这里会包含所有父作用域的绑定 (`class` 和 `style` 除外)，并且可以通过 `v-bind="$attrs"` 传入内部组件——在创建高级别的组件时非常有用。
 简单点讲就是包含了所有**父组件在子组件上设置的属性**（除了`prop`传递的属性、`class` 和 `style` ）。

```jsx
    <div id="app">
      <base-input
        label="姓名"
        class="name-input"
        placeholder="请输入姓名"
        test-attrs="$attrs"
      ></base-input>
    </div>
      Vue.component("base-input", {
        inheritAttrs: true, //此处设置禁用继承特性
        props: ["label"],
        template: `
        <label>
          {{label}}-
          {{$attrs.placeholder}}-
          <input v-bind="$attrs"/>
        </label>
        `,
        mounted: function() {
          console.log(this.$attrs);
        }
      });
      const app = new Vue({
        el: "#app"
      });
```

![1608172364466](C:\Users\18567\AppData\Roaming\Typora\typora-user-images\1608172364466.png)

#### vm.$listeners

包含了父作用域中的 (不含 `.native` 修饰器的) `v-on` 事件监听器。它可以通过 `v-on="$listeners"` 传入内部组件——在创建更高层次的组件时非常有用。
 简单点讲它是一个对象，里面包含了作用在这个组件上所有的监听器（监听事件），可以通过 `v-on="$listeners"` 将事件监听**指向这个组件内的子元素（包括内部的子组件）。**
 为了查看方便，我们设置`inheritAttrs: true`

```html
    <div id="app">
      <child1
        :p-child1="child1"
        :p-child2="child2"
        :p-child-attrs="1231"
        v-on:test1="onTest1"
        v-on:test2="onTest2">
      </child1>
    </div>
   <script>
      Vue.component("Child1", {
        inheritAttrs: true,
        props: ["pChild1"],
        template: `
        <div class="child-1">
        <p>in child1:</p>
        <p>props: {{pChild1}}</p>
        <p>$attrs: {{this.$attrs}}</p>
        <hr>
        <child2 v-bind="$attrs" v-on="$listeners"></child2></div>`,
        mounted: function() {
          this.$emit("test1");
        }
      });
      Vue.component("Child2", {
        inheritAttrs: true,	
        props: ["pChild2"],
        template: `
        <div class="child-2">
        <p>in child->child2:</p>
        <p>props: {{pChild2}}</p>
        <p>$attrs: {{this.$attrs}}</p>
          <button @click="$emit('test2','按钮点击')">触发事件</button>
        <hr> </div>`,
        mounted: function() {
          this.$emit("test2");
        }
      });
      const app = new Vue({
        el: "#app",
        data: {
          child1: "pChild1的值",
          child2: "pChild2的值"
        },
        methods: {
          onTest1() {
            console.log("test1 running...");
          },
         onTest2(value) {
            console.log("test2 running..." + value);
          }
        }
      });
    </script>
```

上例中，父组件在`child1`组件中设置两个监听事件`test1`和`test2`,分别在`child1`组件和`child1`组件内部的`child2`组件中执行。还设置了三个属性`p-child1`、`p-child2`、`p-child-attrs`。其中`p-child1`、`p-child2`被对应的组件的`prop`识别。所以：
 `p-child1`组件中`$attrs`为`{ "p-child2": "pChild2的值", "p-child-attrs": 1231 }`;
 `p-child2`组件中`$attrs`为`{ "p-child-attrs": 1231 }`。

<img src="C:\Users\18567\AppData\Roaming\Typora\typora-user-images\1608181251030.png" alt="1608181251030" style="zoom:50%;" />



#### inheritAttrs

![1608181622725](C:\Users\18567\AppData\Roaming\Typora\typora-user-images\1608181622725.png)

 没有被 `props`绑定的属性就没有作为普通的 HTML 特性应用在子组件的根元素上。 

#### [JavaScript call和apply的三大用途](https://www.cnblogs.com/liamlee/p/12215800.html)

```js
//改变this的指向
var obj1 = { 
 name: 'sven' 
}; 
var obj2 = { 
 name: 'anne' 
}; 
window.name = 'window'; 
var getName = function(){ 
 alert ( this.name ); 
}; 
getName(); // 输出: window 
getName.call( obj1 ); // 输出: sven 
getName.call( obj2 ); // 输出: anne 
```

#### bind的用法

```js
//方用法1  
console.log(this);
  this.x = 9;
  var moudle = {
    x: 81,
    getX: function () {
      return this.x;
    }
  }
  console.log(moudle.getX()); // 81

  var retrieveX = moudle.getX;
  console.log(retrieveX()); // 9

  var bindRetrieveX = retrieveX.bind(moudle);
  console.log(bindRetrieveX()); // 81

//module.getX(); 的结果是 81，因为 getX 里的 this 是 module, 所以 this.x 是 module 里的 x = 81。
//retrieveX(); 的结果是 9，因为这时相当于 var retrieveX = function() { return this.x; };， retrieveX(); 相当于在全局跑了遍函数里的内容，this.x 是 全局的 this.x = 9。

//用法2
function LateBloomer() {
    this.petalCount = 1;
  }
  LateBloomer.prototype.bloom = function () {
    console.log(this);
    setTimeout(this.declare.bind(this), 1000);
  }
  LateBloomer.prototype.declare = function () {
    console.log("I am a flower " + this.petalCount);
  }

  var flower = new LateBloomer()
  flower.bloom()

//window.setTimeout(function, milliseconds) 这是这个函数的用法，function 是延迟的函数，milliseconds 是延迟的时间。如果console.log(this.declare()); 一下就会发现, 结果是 undefined， console.log(this.declare.bind(this)); 的结果则是 declare 这个函数，在使用 bind() 了之后，会创建一个新的函数。
```

 **在 bind(arg1, arg2) 被调用时，会创建一个新函数，这个新函数的 this，都是 arg1，也就是第一个参数。** 
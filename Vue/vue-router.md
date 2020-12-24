## Vue-router

1. 安装npm install vue-router --save

2. ```js
   //配置路由相关的信息
   import Vue from 'vue'
   import VueRouter from "vue-router"
   
   import Home from ''
   import About from ''
   //安装插件 Vue.user(插件)
   Vue.use(VueRouter)
   
   //定义路由
   const routes = [
   	{
   	path: '/home',
   	component: Home
   },
   	{
   	path: '/about',
   	component: About
   }
   ]
   //创建router实例
   const router = new VueRouter({
     routes
   })
   
   //导出router实例
   export default router
   ```

   

3. 在App.vue中加入

   1. ```vue
      <div id='app'>
        //会被渲染成a标签
      	<router-link to="/home">首页</router-link>
        <router-link to="/about">关于</router-link>
        //渲染出不同的组件
        <router-view></router-view>
      </div>	
      ```

      

$router

$route:谁活跃拿到的就是谁的对象

**$route.params.xxx**

#### 懒加载

```js
const Home = () => import('')
const About = () => import('')
const User = () => import('')

```

#### 传递参数问题

params的类型:
	配置路由格式: /router/:id
	传递的方式: 在path后面跟上对应的值
	传递后形成的路径: /router/123, /router/abc
query的类型:
	配置路由格式: /router, 也就是普通配置
	传递的方式: 对象中使用query的key作为传递方式
	传递后形成的路径: /router?id=123, /router?id=abc

```vue
<router-link :to="{path: '/profile', query: {name:'txc', age:18, height: 1.88}}" tag="button">档案</router-link>
```

#### 导航守卫

#### 加入meta: {

​	title: '首页'

#### }

```js
router.beforeEach((to, from, next) => {
  document.title = to.matched[0].meta.title
  console.log(to);
  next()
})
```



```js
//这两个函数只有在该组件保持了状态，用了keep-alive时候才能被调用
activated() {
    this.$router.push(this.path)
  },
deactivated() {
    console.log('deactivated');
  },
```


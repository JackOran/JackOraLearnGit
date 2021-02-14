![image-20210102191041491](/Users/apple/Library/Application%20Support/typora-user-images/image-20210102191041491.png)

![image-20210102224750070](/Users/apple/Library/Application%20Support/typora-user-images/image-20210102224750070.png)

```js
//导入字体图标
import '../src/assets/iconFont/iconfont.css'

//导入axios
import axios from "axios";
axios.defaults.baseURL = 'http://127.0.0.1:8888/api/private/v1'
Vue.prototype.$http = axios
```

```js
//登录表单的数据绑定对象
loginForm: {
  username: '',
    password: '',
},
  //登录表单的验证规则
  loginFormRules: {
    username: [
      { required: true, message: '请输入登录名称', trigger: 'blur' },
      { min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur' }
    ],
      password: [
        { required: true, message: '请输入密码', trigger: 'blur'},
        { min: 6, max: 16, message: '长度在 6 到 16 个字符', trigger: 'blur'}
      ],
  }
```

```js
//点击重置按钮，重置登录
    resetClick() {
      console.log(this);
      this.$refs.loginFormRef.resetFields();
    },
    //点击进行登录前的预校验
    login() {
      this.$refs.loginFormRef.validate(async valid => {
        // console.log(valid);
        if (!valid) return;
        const {data : res} = await this.$http.post("/login", this.loginForm);
        if (res.meta.status !== 200) {
          this.$message.error("登录失败")
        } else {
          this.$message({
            type: 'success',
            message: '登录成功'
          })
        }
      })
    }
```

```js
//导入消息提示
import {Message} from "element-ui";
//需要挂载
Vue.prototype.$message = Message
```



#### 将登录成功的token保存到客户端的sessionStorage中

1. 项目中的其他API接口必须在登录后才能访问
2. token只应在网站打开期间有效，所以将token保存到sessionStorage中

![image-20210103213939338](/Users/apple/Library/Application%20Support/typora-user-images/image-20210103213939338.png)

```js
//将token保存到sessionStorage中
sessionStorage.setItem("token", res.data.token);
```

```js
// 清除token
sessionStorage.clear()
//强制跳转login
setTimeout(() => {
  this.$router.push({ path: '/login' })
}, 1000)
```

#### 通过接口获取菜单数据

```js
//通过axios请求拦截器添加token，保证拥有获取数据的权限
//设置请求拦截器
axios.interceptors.request.use(config => {	
  console.log(config);
  //最后必须return config
  //为请求头对象,添加token验证的Authorization字段
  config.headers.Authorization = sessionStorage.getItem('token');
  return config;
})
```

#### 获取左侧菜单数据

```js
//获取所有的左侧菜单数据
    async getMenuList() {
      const {data: res} = await this.$http.get('/menus');
      console.log(res);
      if (res.meta.status !== 200) return this.$message.error(res.meta.msg)
      this.menuList = res.data;
    }
```

#### 默认打开一个菜单其他都关闭

```js
//一个elementui中的一个属性 unique-opened
```

#### 实现首页路由的重定向效果

```js
{
    path: '/home',
    name: 'home',
    redirect: '/welcome',
    component: () => import('../components/Home'),
    children:[
      {
        path: '/welcome',
        name: 'welcome',
        componet:() => import('../components/Welcome')
      }
    ]
  }

//在el-main放一个占位符，然后就可以直接重定向跳转链接
```

#### 通过router属性开启侧边栏路由链接的跳转

```vue
<!-- 二级菜单-->
//开启router 通过index来进行路由的跳转
<el-menu-item
:index="'/' + childItem.path"
v-for="childItem in item.children"
:key="childItem.id"
@click="saveActivePath('/' + childItem.path)"
>
</el-menu-item>
```



#### 在sessionStorage中保存左侧菜单的激活状态

```js
//开启一个属性:default-active
:default-active="activePath"
//在二级菜单添加点击事件
saveActivePath(activePath) {
  sessionStorage.setItem("activePath", activePath)
  this.activePath = activePath
}

//在创建的时候就给activePath赋值
created() {
    //在创建的时候就给activePath赋值
    this.activePath = sessionStorage.getItem("activePath")
  },
```

#### 通过v-slot="scope" {{scope.row}}来显示一行的数据

```vue
//显示一行的内容
<el-table-column prop="mg_state" label="状态" width="180">
  <template v-slot="scope">
    {{scope.row}}
   </template>
</el-table-column>
```

#### 通过作用域插槽渲染操作列

```vue
<el-table-column prop="" label="操作" width="180">
<template>
<el-button type="primary" icon="el-icon-edit" size="mini"></el-button>
<el-button type="danger" icon="el-icon-delete" size="mini"></el-button>
//周围缠绕的文字
<el-tooltip  effect="dark" content="编辑权限" placement="top" :enterable="false">
  <el-button type="warning" icon="el-icon-setting" size="mini"></el-button>
</el-tooltip>
</template>
</el-table-column>
```

#### 分页

```js
<el-pagination
  @size-change="handleSizeChange"
  @current-change="handleCurrentChange"
  :current-page="queryInfo.pagenum"
  :page-sizes="[1, 2, 5, 7]"
  :page-size="queryInfo.pagesize"
  layout="total, sizes, prev, pager, next, jumper"
  :total="total">
</el-pagination>
export default {
data() {
    return {
      queryInfo: {
        query: '',
        //当前的页数
        pagenum: 1,
        //每页显示的数据
        pagesize: 2
      },
      userList: [],
      total: 0
    }
  }
},
methods: {
  //每页显示的条数发生变化时候触发
handleSizeChange(newSize) {
  console.log(newSize)
  this.queryInfo.pagesize = newSize
  this.getUserList()
},
  //当前页面改变时候会触发
handleCurrentChange(newNum) {
  console.log(newNum)
  this.queryInfo.pagenum = newNum
  this.getUserList()
	}
}
```

#### 监听开关的改变

```js
<template v-slot="scope">
  																				//监听用户开关状态的改变change
  <el-switch v-model="scope.row.mg_state" @change="userStateChange(scope.row)"></el-switch>
</template>
//监听switch开关状态的改变
async userStateChange(userInfo) {
  console.log(userInfo);
  const {data:res} = await this.$http.put(`/users/${userInfo.id}/state/${userInfo.mg_state}`)
  if (res.meta.status !== 200) {
    userInfo.mg_state = !userInfo.mg_state;
    this.$message.error("更新用户状态失败");
  }
  this.$message.success("更新用户状态成功");
}
```

#### 自定义校验规则

```js
// 验证邮箱的校验规则
var checkEmail = (rule, value, cb) => {
  var reg = new RegExp('^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$')
  if (reg.test(value)) {
    return cb()
  } else {
    cb(new Error('邮箱输入错误'))
  }
}

// 验证手机号校验规则
var checkMobile = (rule, value, cb) => {
  if (!(/^1(3|4|5|7|8)\d{9}$/.test(value))) {
    cb(new Error('手机号格式输入错误'))
  } else {
    return cb()
  }
}


email: [
  { validator: checkEmail }
],
mobile: [
    { validator: checkMobile }
]
```

#### 根据id来获取对应得用户信息来展示到编辑信息页面

```js
// 编辑用户信息校验
editUserInfo () {
  this.$refs.editFormRef.validate(async valid => {
    if (!valid) return
    const { data: res } = await this.$http.put(`/users/${this.editForm.id}`, { email: this.editForm.email, mobile: this.editForm.mobile })
    if (res.meta.status !== 200) {
      this.$message.error('用户更新失败')
    }
    this.$message.success('用户更新成功')
    // 用户dialog对话框隐藏
    this.editDialogVisible = false
    // 重新获取用户信息
    await this.getUserList()
  })
}
```

#### MessageBox弹出框

```js
import MessageBox from 'element-ui';
Vue.prototype.$confirm = Message.confirm
this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
})

// 通过id来删除用户的信息
async removeById (row) {
  console.log(row)
  const result = await this.$confirm('是否永久删除用户', '提示', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning'
  }).catch(err => err)
  if (result === 'confirm') {
    this.$message.success('删除用户成功')
  } else {
    this.$message.info('已取消')
  }
}
```

#### 权限管理

```

```

#### 树形控件的使用

```vue
<el-tree :data="data" :props="defaultProps" @node-click="handleNodeClick"></el-tree>
data(){
	return {
		defaultProps: {
		// 列表中看到的是哪一个属性
			label:'authName'
		// 是使用的哪一个嵌套对象
			children:children
		}
	}
}
```

#### 过滤器得使用

```jsx
Vue.filter('filterDate', function (originValue) {
  const dt = new Date(originValue)
  const y = dt.getFullYear()
  const m = (dt.getMonth() + '').padStart(2, '0')
  const d = (dt.getDay() + '').padStart(2, '0')
  const hh = (dt.getHours() + '').padStart(2, '0')
  const mm = (dt.getMinutes() + '').padStart(2, '0')
  const ss = (dt.getSeconds() + '').padStart(2, '0')
  return `${y}-${m}-${d} ${hh}:${mm}:${ss}`
})


<el-table-column prop="add_time" label="创建时间" width="140px">
  <template v-slot="scope">
    {{scope.row.add_time | filterDate}}
      </template>
</el-table-column>
```


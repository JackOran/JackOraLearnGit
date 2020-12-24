### webpack配置

#### commonJS的导入和导出

```javascript
//导出
module.exports = {
  name,
  age
}
//导入
const {name, age} = require('./aaa.js')
```

使用node前先初始化 **npm init**

如果有依赖加 **npm install**

创建一个**webpack.config.js**

```javascript
const path = require('path')

module.exports = {
  //入口
  entry: './src/main.js',
  //出口
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  }
}
```

有时候需要本地安装webpack，因为和全局的版本可能不一样 **npm install webpack@3.6.0 --save-dev**



导入css文件的时候需要在main.js中导入

```javascript
require('./css/normal.css')
```

### webpack配置Vue

安装**npm install vue --save**

import Vue from 'vue'

Const app = new Vue({



})



在webpack.config.js中配置信息

resolve: {

​	alias: {

​	'vue$': 'vue/dist/vue.esm.js'

}

}

**使用.vue文件需要安装vue-loader和vue-template-compiler**

**配置webpack.config.js**


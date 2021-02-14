### 封装df-form

#### df-form

- 1.接收事件

  2.可校验

- #### df-form-item

  - 执行校验
  - 显示错误信息
  - df-input
    - 维护数据

```js
//在df-form中通过provide将form导出
provide() {
    return {
      form: this
    }
  }
//在df-form-item中通过inject导入form
inject: ['form']


//校验规则
import Schema from "async-validator";
validate() {
      // console.log(this.form.model[this.prop]);
      //校验规则
      const rules = this.form.rules[this.prop]
      // console.log(this.form.rules[this.prop]);
      //当前值
      const values = this.form.model[this.prop]
      //校验对象
      const desc = {[this.prop] : rules}
      //创建Schema实例
      const schema = new Schema(desc);
      //都是promise                  //校验源
      return schema.validate({[this.prop]:values},errors => {
        if (errors) {
          this.error = errors[0].message
        } else {
          //校验通过
          this.error = ''
        }
      })
    }
```



#### 具体流程

```js
//创建input组件并通过props传入value和type
//创建form-item组件通过props传入label和prop
//创建form组件通过props传入model和rules和ref
//在form组件上通过provide传入form
//在form-item组件上通过inject来接收form

//通过input组件this.$parent.$emit('validate')向父组件发送校验请求
//父组件form-item通过
this.$on('validate', () => {
	this.validate()
    //this.validate通过一系列校验规则进行校验并且返回一个promise对象
})

//在index.vue中登录时候login
login() {
      this.$refs.loginForm.validate((valid) => {
        if (valid) {
          alert('submit!');
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    }

//在form组件上
validate(cb) {
      //获取所有孩子的KformItem
      const tasks = this.$children.filter(item=>item.prop).map(item => item.validate());
      console.log(tasks);
      Promise.all(tasks)
          .then(() => {cb(true)})
          .catch(() => {cb(false)})
    }
  }
```



#### 实现弹窗组件

```

```


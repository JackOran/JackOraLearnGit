# Instanceof

#### ⾸先获取类型的原型 

#### 然后获得对象的原型 

#### 然后⼀直循环判断对象的原型是否等于类型的原型，直到对象原型为 null ，因为原型链 

#### 最终为 null

```js
function myInstanceof(left, right) {
    let prototype = right.prototype;
    left = left.__proto__;
    while (true) {
      if (left === null || left === undefined) {
        return false;
      } else if (left === prototype) {
        return true
      }
      left = left.__proto__;
    }
  }
```


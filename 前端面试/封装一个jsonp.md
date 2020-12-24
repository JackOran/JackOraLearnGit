## Jsonp 只能get请求

```js
function myJsonp(url,jsonpCallback,success) {
    let script = document.createElement("script");
    script.src = url;
    script.async = true; //异步
    script.type = "text/javascript";
    window[jsonpCallback] = function (data) {
      success && success(data);
    }
    document.body.appendChild(script);
  }
  myJsonp("", 'callback', (value) => {
    console.log(value);
  })
```


### slot

```vue
<body>
		<div id="app">
			<h2>slot</h2>
			<v-demo>
				<p slot='con'>11111111111</p>
				<ul slot='con1'>
					<li>helo</li>
					<li>hello</li>
					<li>lloo</li>
				</ul>
			</v-demo>
		</div>
		
		<template id="demo">
			<div>
				<h2>组件 slot分发</h2>
				<div>
					<slot name='con'>当组件没有内容的时候显示我</slot>
					<slot name='con1'>哈哈哈哈哈</slot>
				</div>
			</div>
		</template>
  
1111111111

helo
hello
lloo
```


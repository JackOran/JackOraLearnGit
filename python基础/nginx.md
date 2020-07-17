# [Mac下用brew安装nginx


1. [nginx](http://nginx.org/)

> nginx [engine x] is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server.

从[niginx基本介绍](http://nginx.org/en/)上看到*Other HTTP server features*中有一项:

> * FLV and MP4 streaming;

可知nginx也支持流媒体.

## 2. [brew](http://brew.sh/)

brew又叫Homebrew，是Mac中的一款软件包管理工具，通过brew可以很方便的在Mac中安装软件或者是卸载软件.
一般Mac电脑会默认安装有brew.
常用指令如下:

* brew 搜索软件
  `brew search nginx`
* brew 安装软件
  `brew install nginx`
* brew 卸载软件
  `brew uninstall nginx`
* brew 升级
  `sudo brew update`
* 查看安装信息(经常用到, 比如查看安装目录等)
  `sudo brew info nginx`
* 查看已经安装的软件
  `brew list`



## 3\. brew安装nginx

* 安装nginx
  可以用brew很方便地安装nginx.
  `sudo brew install nginx`
* 启动nginx服务
  `sudo brew services start nginx`
  利用`http://localhost:8080`进行访问, 如果出现如下界面，说明启动成功.


* 查看nginx版本
  `nginx -v`
* 关闭nginx服务
  `sudo brew services stop nginx`

另外几个比较方便的指令

* 重新加载nginx
  `nginx -s reload`
* 停止nginx
  `nginx -s stop`



# Nginx简介

Nginx是一个高性能的HTTP和反向代理服务器，也是一个IMAP/POP3/SMTP服务器。

Nginx是一款轻量级的Web服务器/反向代理服务器以及电子邮件代理服务器，其特点是占用内存少，并发能力强，在同类型的网页服务器中表现优秀

Nginx是由伊戈尔.塞索耶夫开发的，于2004年10月4日公开源码，以类BSD许可证形式发布

Nginx因它的稳定性，丰富的功能，示例配置文件和低系统资源的消耗而闻名

中国大陆使用Nginx的网站:
	淘宝，京东，腾讯，百度，新浪，网易...

官网
	http://nginx.org/

中文资料
	http://www.nginx.cn/doc/index.html
	http://tengine.taobao.org/book/

为什么选择Nginx
	作为We服务器：相比Apache，Nginx使用资源更少，支持更多的并发连接，体现更高的效率，使Nginx倍受欢迎，能够支持高达50000个并发连接数的响应
	作为负载均衡服务器：Nginx既可以在内部直接支持Redis和PHP，也可以支持作为HTTP代理服务器对外进行服务，Nginx使用C编写，不论是系统资源开销还是CPU使用效率都处理的非常优秀
	Nginx安装非常简单，配置文件非常简洁，Bug非常少：Nginx启动非常容易，并且几乎可以做到7 * 24小时不间断运行，即使运行数个月也不需要重新启动
	

#Nginx安装

Nginx安装主要有两种方式
	源码安装

  		1. 下载源码压缩包
       2. 安装源码编译依赖包 gcc,zlib,make...
          3. 配置编译模块
          4. make && make test 
          5. make	install
             包管理工具安装
          6. 去官网将所使用依赖添加到包管理工具中
          7. 更新包管理工具资源
          8. 使用包管理工具安装
             启动Nginx
             nginx 	[ -c  configpath]
             信息查看
             nginx 	-v
             nginx	-V
             控制Nginx
             nginx -s signal
             stop 		快速关闭
             quit		优雅的关闭
             reload		重新加载配置

通过系统管理
	systemctl  status  nginx	查看nginx状态
	systemctl  start    nginx	启动nginx服务
	systemctl  stop     nginx            关闭nginx服务
	systemctl  enable nginx	设置开机自启
	systemctl  disable nginx	禁止开机自启

​		

#Nginx配置文件

Nginx配置文件包含指定指令控制的模块。
	指令分为简单指令和块指令
		一个简单指令由名称和参数组成，以空格分隔，并以分号结尾
		一个块指令和简单指令具有相同的结构，但不是以分号结束，而是以一个大括号包围的一堆附			加指令结束
	如果一个大括号内可以有其他的指令，它就被称为一个上下文，比如（events，http，server，location）
	

指令
	nginx 	-t		不运行，仅测试配置文件
	nginx        -c     configpath	从指定路径加载配置文件
	nginx     -t    -c    configpath      测试指定配置文件

```
main		全局设置

events{		工作模式，连接配置
	...
}
http{		http的配置
	...
	upstream xxx{	负载均衡配置
		...
	}
	server{		主机设置
		...
		location xxx{	URL匹配
			...
		}
	}
}
```

```
#main
user 	nginx;	worker进程运行的用户和组

worker_processes	1;	指定Nginx开启的子进程数，多核CPU建议设置和CPU数量一样的进程数

error_log	  xxx  level;		用来定义全局错误日志文件，通常放在var中，level有 debug，info，notice，										warn，error，crit

pid          xxx;		指定进程id的存储文件位置

```

```
#events
指定工作模式和以及连接上限

events{
	use epoll;
	worker_connections 1024;
}

use 指定nginx工作模式
	epoll	高效工作模式，linux
	kqueue	高效工作模式， bsd
	poll	标准模式
	select	标准模式

worker_connections 定义nginx每个进程的最大连接数
	正向代理	连接数 * 进程数
	反向代理	连接数 * 进程数 / 4
	linux系统限制最多能同时打开65535个文件，默认上限就是65535，可解除 ulimit -n 65535

```

```
#http
最核心的模块，主要负责http服务器相关配置，包含server，upstream子模块

include mime.types;设置文件的mime类型

include xxxconfig;	包含其它配置文件，分开规划解耦

default_type  xxx;	设置默认类型为二进制流，文件类型未知时就会使用默认

log_format 	设置日志格式

sendfile		设置高效文件传输模式

keepalive_timeout	设置客户端连接活跃超时

gzip	 	gzip压缩

```

```
#server
用来指定虚拟主机

listen 	80;		指定虚拟主机监听的端口

server_name localhost;	指定ip地址或域名，多个域名使用空格隔开

charset  	utf-8;		指定网页的默认编码格式

error_page 500 502 /50x.html 指定错误页面

access_log   xxx main;	指定虚拟主机的访问日志存放路径

error_log   xxx main;	指定虚拟主机的错误日志存放路径

root	xxx;		指定这个虚拟主机的根目录

index	xxx;		指定默认首页

```

```
#localtion
核心中的核心，以后的主要配置都在这

主要功能:定位url，解析url，支持正则匹配，还能支持条件，实现动静分离

语法
	location [modifier]  uri{
		...
	}

modifier 修饰符
	=	使用精确匹配并且终止搜索
	~	区分大小写的正则表达式
	~*	不区分大小写的正则表达式
	^~	最佳匹配，不是正则匹配，通常用来匹配目录
	
常用指令
	alias	别名，定义location的其他名字，在文件系统中能够找到，如果location指定了正则表达式，alias将会引用正则表达式中的捕获，alias替代lication中匹配的部分，没有匹配的部分将会在文件系统中搜索

```

```
#反向代理
proxy_pass  URL;			反向代理转发地址，默认不转发header，需要转发header则设置
					proxy_set_header HOST $host;
proxy_method  POST;		转发的方法名

proxy_hide_header Cache-Control;	指定头部不被转发		

proxy_pass_header Cache-Control;	设置哪些头部转发

proxy_pass_request_header on;	设置转发http请求头

proxy_pass_request_body on;	设置转发请求体



```

```
#upstream
负载均衡模块，通过一个简单的调度算法来实现客户ip到后端服务器的负载平衡

写法 upstream  myproject{
	ip_hash;
          	server 127.0.0.1:8000;
	server 127.0.0.1:8001 down;
	server 127.0.0.1:8002 weight=3;
	server 127.0.0.1:8003 backup；
	fair；
          }
负载均衡算法
	weight 	负载权重
	down	当前server不参与负载均衡
	backup	其它机器全down掉或满载使用此服务
	ip_hash	按每个请求的hash结果分配
	fair	按后端响应时间来分（第三方的）

```

# nginx命令

```
sudo nginx #打开 nginx
nginx -s reload|reopen|stop|quit  #重新加载配置|重启|停止|退出 nginx
nginx -t   #测试配置是否有语法错误

nginx [-?hvVtq] [-s signal] [-c filename] [-p prefix] [-g directives]

-?,-h           : 打开帮助信息
-v              : 显示版本信息并退出
-V              : 显示版本和配置选项信息，然后退出
-t              : 检测配置文件是否有语法错误，然后退出
-q              : 在检测配置文件期间屏蔽非错误信息
-s signal       : 给一个 nginx 主进程发送信号：stop（停止）, quit（退出）, reopen（重启）, reload（重新加载配置文件）
-p prefix       : 设置前缀路径（默认是：/usr/local/Cellar/nginx/1.2.6/）
-c filename     : 设置配置文件（默认是：/usr/local/etc/nginx/nginx.conf）
-g directives   : 设置配置文件外的全局指令
```


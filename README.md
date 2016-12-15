# ScrapyTest

项目目录是```test/```
这里会做一些scrapy的测试，分别用不同的spider文件来实现

###aSpider.py

* 测试了所有通过scrapy.Request发出的请求是有用到中间件的，而自己通过urllib2或者request库发送的请求是不走中间件的。
* 可以直接override start_request()，但是请求要设置好回调函数
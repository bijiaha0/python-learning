## 注意事项

#### 1、课前准备
```
1、安装好linux操作系统
        1、virtual-box虚拟机 下载地址：https://www.virtualbox.org/
        2、ubuntu图形化操作系统优麒麟，下载地址： https://www.ubuntukylin.com/downloads/  选择桌面版
        3、deepin,底层ubuntu系统 下载地址: https://www.deepin.org/download/
2、安装好Python3.6运行环境  
        参考安装文档：http://47.94.6.102/PythonandAITrainingCamp2/1-Lesson/blob/master/Linux%E4%B8%8BPython%E7%8E%AF%E5%A2%83%E5%AE%89%E8%A3%85%E6%96%87%E6%A1%A3
        如果安装了deepin这个系统，python就不用重新装了，要不然会出问题,deepin自带了python3.6
3、安装好Python IDE：pycharm
4、运行Hello World 成功
5、注册好博客园、CSDN等博客账号
6、注册好github账号（未来的作业，需要同步到这个gitlab上，并且同步到github上）
```

#### 2、 作业提交方式
- 创建自己的私有仓库即可，每一次作业都提交到自己的仓库上
- 创建一个叫做homework的仓库，每一次作业对应的名称为 (课程次数)-homework。 作业会根据大家的情况进行难度提升


## 课程表：每周二四六 晚8:30-10:30（除法定节假日）

# 已讲内容
|课次序号| 阶段|   日期  |    主题  |   大纲  |  作业 | Deadline | 扩展材料  | 
|---------|---------|---------|---------|---------|---------|---------|---------|
|1|Python基础阶段| 4月16日 |课程介绍、基本数据类型及循环控制 | 1、课程介绍及使用环境说明<br> 2、数字类型、数字的数学运算、注释、字符串操作 <br>3、 初识linux<br>  | | |[1、git使用](http://www.greedyai.com/my/course/46)<br>[2、git操作文档](http://47.94.6.102/PythonandAITrainingCamp2/2-Lesson/blob/master/git%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C) | 
|2|Python基础阶段| 4月18日 |Python基础一 | 1、逻辑控制(if与循环)、条件控制运算 <br/>2、数组数据类型<br/>3、通过if/else及简单正则实现问答思路讲解 <br>4、pycharm的基本使用 <br>5、git的基本操作<br>6、排序算法冒泡排序的讲解| | | |
|3|Python基础阶段| 4月20日 |Python基础二 | 1、set、dist、tuple类型<br/>2、Python中自定义函数及函数的基本使用<br/>递归的概念及应用|  || |
|4|Python基础阶段| 4月23日 |基于规则的聊天机器人项目(1) | 1、高级条件控制-循环的中断(break/continue)<br/>2、函数的返回值<br> 3、初识正则 <br/>4、AIML框架介绍<br/>5、案例讲解：利用AIML写规则，并实现简单的问答系统 |1、本地安装AIML框架<br/>2、把v0.1 Bot的规则写入AIML框架<br/>3、实现简单的对话<br/>4、书写邮箱和手机号码匹配的正则  |2019-04-25 15:00 | |
|5|Python基础阶段| 4月25日 |基于规则的聊天机器人项目(2) | 1、正则表达式的高级应用<br/>2、聊天中的上下文理解<br/>3、AIML中的多层条件控制<br/>4、AIML中的template高级教程<br/>5、利用AIML实现多伦对话<br/> 6、中文分词技术 |1、实现快速排序  |2019-04-27 15:00 | |
|6|Python高级编程| 4月27日 |Python面向对象(1) | 1、面向对象的基本思想 <br>2、Python的工程结构及命名规范<br>3、面向对象的类设计  <br>4、快排的实现|  [2、对象的封装](http://47.94.6.102/PythonandAITrainingCamp2/6-Lesson/blob/master/homework) ||[常见排序方法阅读](https://www.cnblogs.com/hokky/p/8529042.html) | 
|7|Python高级编程| 5月07日 |Python面向对象(2) | 1、导包 <br>2、面向对象三大特性|   ||| 
|8|Python高级编程| 5月09日 |Python函数式编程(1) | 1、闭包<br>2、装饰器(语法糖/注解)开发 <br>3、时间复杂度 | 开发一个可以验证函数参数类型的装饰器 || [python排序与时间复杂度](https://www.cnblogs.com/wuxinyan/p/8615127.html) | 
|9|Python高级编程| 5月11日 |Python函数式编程(2) | 1、lambda表达式与高阶函数的应用<br>2、yield生成器<br>3、三大推导式<br>4、异常<br>5、文件的操作  |  || | 
|10|Python高级编程|5月14日 |Python的文件操作 |1、日志的作用与操作<br>2、(多)进程与(多)线程 |[0、多线程作业](http://47.94.6.102/PythonandAITrainingCamp2/10-Lesson/blob/master/%E5%A4%9A%E7%BA%BF%E7%A8%8B%E4%BD%9C%E4%B8%9A-%E7%94%9F%E4%BA%A7%E8%80%85%E4%B8%8E%E6%B6%88%E8%B4%B9%E8%80%85)<br>1、阅读 [更多日志配置格式](http://www.cnblogs.com/yyds/p/6885182.html) 配置yaml格式的日志配置   || [0、日志配置格式说明](http://47.94.6.102/PythonandAITrainingCamp2/10-Lesson/blob/master/%E6%97%A5%E5%BF%97%E6%A0%BC%E5%BC%8F%E8%AF%B4%E6%98%8E.md)<br>[1、更多日志基本用法](https://docs.python.org/2/library/logging.html#) <br> [2、更多日志高级用法](https://docs.python.org/3.5/howto/logging-cookbook.html) <br> [3、更多日志配置格式](http://www.cnblogs.com/yyds/p/6885182.html)| 
|11|关系型数据库MySQL | 5月16日 |数据库(1) |0、多线程作业讲解<br>1、MySQL 数据库的创建 | ||| 
|12|关系型数据库MySQL | 5月18日 |数据库(2) |1、MySQL的增删改查<br>2、数据库、表、字段的字符集<br> 3、数据库的5大约束 |[1、部门工资最高的员工](http://47.94.6.102/PythonAndAITrainingCamp2/12-Lesson/blob/master/%E9%83%A8%E9%97%A8%E5%B7%A5%E8%B5%84%E6%9C%80%E9%AB%98%E7%9A%84%E5%91%98%E5%B7%A5)<br>[2、部门工资前三高的员工](http://47.94.6.102/PythonandAITrainingCamp2/12-Lesson/blob/master/%E9%83%A8%E9%97%A8%E5%B7%A5%E8%B5%84%E5%89%8D%E4%B8%89%E9%AB%98%E7%9A%84%E5%91%98%E5%B7%A5%20) ||| 
|13|关系型数据库MySQL |5月21日 |git的高级使用与Linux常用命令 |1、MySQL关联查询/慢查询/索引/存储引擎|1、写一篇git操作的博客,并把博客地址给到班主任<br>2、预习vim命令|| [git中文官方教程](https://git-scm.com/book/zh/v2) <br> [vim编辑器常用命令](https://www.cnblogs.com/yangjig/p/6014198.html)<br>[Linux常用命令](https://www.cnblogs.com/myon/p/6242921.html)<br>[MySQL事物隔离级别](http://www.php.cn/mysql-tutorials-378953.html) <br>[慢查询结果说明](https://www.jianshu.com/p/ea3fc71fdc45)|
|14|Git使用进阶 |5月23日 |git的高级使用与Linux常用命令 |1、文件过滤/分支创建/合并 <br>3、版本回退 <br> 4、提交历史 <br> 5、文件暂存  <br> 6、差异比对  <br> 7、标签  <br>8、vim命令  <br> 9、虚拟环境的创建与实用 ||| |
|15|爬虫 |5月25日 |selenium框架 | 0、虚拟环境的创建与实用<br>1、Selenium的基本定位方法  <br>2、Selenium的鼠标事件 <br>3、Selenium的键盘事件 ||| [1、chrome driver谷歌下载地址](https://sites.google.com/a/chromium.org/chromedriver/downloads) 或者选择 [chrome driver淘宝镜像下载地址](http://npm.taobao.org/mirrors/chromedriver/)选择对应版本。备注：如果下载不到找我要<br>2、环境安装:pip install selenium<br>[3、Selenium driver官方API文档](https://seleniumhq.github.io/selenium/docs/api/py/api.html#)<br>[4、Selenium官方教程](https://selenium-python.readthedocs.io/)|
|16|爬虫 |5月28日 |selenium框架 | 1、xpath定位 <br>2、CSS选择器定位<br>3、js定位<br>4、requirements的作用与使用 <br>cookies操作与截图方法封装|作业:定位京东商城-电脑-笔记本-销量最高的这一台笔记本的配置信息，并打印出来|| |
|17|爬虫 |5月30日 |selenium框架 | 1、京东商品信息抓取并写入文件<br>2、元素的等待<br>3、mysql数据库的连接<br>4、selenium的远程分布式启动|作业:以分布式的方式将京东商品信息写入数据库|| |
|18|爬虫 |6月01日 |selenium框架 | 1、python中的元类<br>2、面向对象思想的应用-PageObject模式<br>3、对象关系映射(ORM)||| |
|19|爬虫 |6月04日 |scrapy框架 | 1、Scrapy框架的工作流<br>2、使用Scrapy进行爬虫开发||| |
|20 | Web开发| 6月06日 | Flask框架 | 1、Flask的基本使用 <br> 2、微服务的开发理念|||[requests库文档](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)<br>[Flask官方文档](http://docs.jinkan.org/docs/flask/)<br>|
|21 | Web开发| 6月11日 | Flask框架 | 1、restful风格的理解 <br> 2、Flask与Flask-RESTful的结合使用<br>3、uwsgi部署|||[Flask-RESTful官方文档](http://www.pythondoc.com/Flask-RESTful/quickstart.html)|
|22 | 数据处理 | 6月13日 | 数据计算 | 1、anaconda环境安装 <br> 2、jupyter环境安装<br>3、NumPy的嵌套序列<br>4、定长数组<br> 5、矢量化<br>6、花式索引<br>7、数组转置和轴对换<br> 8、使用Numpy进行简单数据处理||||
|23 | 数据处理 | 6月15日 | 数据计算 | 1、Pandas的使用||||


 
# 机器学习部分内容
|课次序号| 阶段|   日期  |    主题  |   大纲  |  材料  | 
|---------|---------|---------|---------|---------|------------------|
|1 |第一周<br>直播 | 6月23日 | 机器学习简介 |1、机器学习应用场景<br>2、机器学习工程化流程<br> 3、监督学习与非监督学习一览<br> 4、机器学习中的数据（训练数据与测试数据）<br> 5、回归问题与分类问题<br> 6、数据处理技巧<br>7、归一化处理<br>8、降维处理| [PPT, 代码, 数据](http://47.94.6.102/PythonandAITrainingCamp2/1introduction)|
|2 |第一周<br>录播 | 6月25日 | sklearn的学习与应用 |1、sklearn工具的安装<br>2、sklearn的使用| |||
|3 |第二周<br>录播 | 6月27日 | 机器学习必备数学知识(上) |1、随机变量<br> 2、条件概率与联合概率<br>3、贝叶斯定理<br>4、期望和方差<br>5、向量与矩阵<br>|[PPT](http://47.94.6.102/PythonandAITrainingCamp2/2math)|
|4 |第二周<br>直播 | 6月30日 | 机器学习必备数学知识(下)| 6、导数的计算<br>7、最优化简介<br>8、凸优化简介 | [PPT](http://47.94.6.102/PythonandAITrainingCamp2/2math)|
|5 |第三周<br>录播 |7月2日  | 线性回归模型 |1、线性回归模型介绍<br>2、线性回归模型推导<br>3、利用normal equation求解线性回归<br>4、特征之间的线性相关| [PPT](http://47.94.6.102/PythonandAITrainingCamp2/3LinearRegression)|
|6 |第三周<br>录播 |7月4日  | 逻辑回归模型 |1、逻辑回归模型详解<br>2、梯度下降法<br>3、逻辑回归模型的似然函数 <br> 4、对逻辑回归模型的似然函数求梯度 <br>5、多元分类逻辑回归模型的似然函数, 及其梯度|[PPT](http://47.94.6.102/PythonandAITrainingCamp2/3LogisticRegression)|
|7 |第三周<br>直播 |7月7日  | 线性回归与逻辑回归项目实战| 1、股票预测案例讲解<br>2、银行电话营销效果预测案例讲解| [线性回归代码](http://47.94.6.102/PythonandAITrainingCamp2/3LinearRegression), [逻辑回归代码, 作业代码](http://47.94.6.102/PythonandAITrainingCamp2/3LogisticRegression)|
|8 |第四周<br>录播 |7月9日  | 朴素贝叶斯模型 |1、朴素贝叶斯模型介绍<br>2、贝叶斯定理<br>3、垃圾邮件的过滤<br>4、朴素贝叶斯的MLE<br>5、log trick| |||
|9 |第四周<br>录播 |7月11日 | 文本技术处理|1、文本的表示<br>2、文本之间 的相似度计算<br>3、文本预处理技术<br>4、tf-idf向量化技术<br>5、语言模型<br>6、词向量技术<br>| |||
|10 |第四周<br>直播 |7月14日 | 朴素贝叶斯项目实战| 垃圾短信检测案例讲解| [朴素贝叶斯垃圾短信检测案例代码](http://47.94.6.102/PythonandAITrainingCamp2/4NaiveBayes)|
|11 |第五周<br>录播 |7月16日 | 情感分析项目实战|掌握如何利用文本处理技术和分类算法来搭建情感分析系统| |||
|12 |第五周<br>录播 |7月19日 | 支持向量机 | 1、SVM介绍<br>2、SVM原理<br>3、拉格朗日惩罚项| [PPT](https://pan.baidu.com/s/1YZ9sMaf4e8a9ir9qCS_joA) 下载需要提取码:fhwu|
|13 |第五周<br>直播 |7月21日 | 核函数 | 1、Primal-Dual问题 <br> 2、核函数介绍<br> 3、交叉验证<br> 4、调参技术|[PPT](https://pan.baidu.com/s/1YZ9sMaf4e8a9ir9qCS_joA) 下载需要提取码:fhwu|
|14 |第六周<br>录播 |7月23日 | KNN模型 | 1、KNN模型介绍<br>2、KNN模型的实现<br>3、KNN模型的缺点|[PPT](http://47.94.6.102/PythonandAITrainingCamp2/knn)|
|15 |第六周<br>录播 |7月25日 | KNN模型项目实战| 二手车价格预测案例讲解| |||
|16 |第六周<br>直播 |7月28日 | SVM模型项目实战 | 使用SVM检测🍄蘑菇是否有毒| [代码和数据](http://47.94.6.102/PythonandAITrainingCamp2/svm.svr.project)|
|17 |第七周<br>录播 |7月30日 | 决策树 | 1、决策树介绍<br>2、信息熵的介绍<br>3、决策树的构建<br> 4、过拟合现象<br> 5、基尼不存度(Gini Impurity)| [PPT](https://pan.baidu.com/s/1GB1bAKSk_FJIXYw3-vaiuA) 下载需要提取码:wj4v|
|18 |第七周<br>录播 |8月1日  | 随机森林|1、随机森林介绍<br>2、Bootstrap介绍<br>3、使用决策树和随机森林计算特征重要性<br> 4、使用分箱(Binning)将连续值分为不同的区间用于决策树的分支 | 见上面决策树的PPT |
|19 |第七周<br>直播 |8月4日  | 随机森林模型项目实战 | 预测员工离职率| [代码和数据](http://47.94.6.102/PythonandAITrainingCamp2/7.DecisionTree.RandomForest.Project)|
|20 |第八周<br>录播 |TBD | Gradient Boosting与XGBoost|1、Gradient Boosting方法论<br>2、GBDT与随机森林区别<br>3、XGBoost介绍| |||
|21 |第八周<br>录播/直播 |TBD | 综合项目实战 |人脸识别| [代码和数据](http://47.94.6.102/PythonandAITrainingCamp2/FinalProject)|













<!-- markdownlint-disable first-line-heading -->
<p align="center">
  <img src="https://github.com/d3ckx1/Fvuln/blob/main/image/logo.png" alt="Fvuln" height="150" />
  <h1 align="center" > F-vuln </h1>
<p align="center">
  
<h4 align="center" > F-vuln（全称：Find-Vulnerability）是为了自己工作方便专门编写的一款自动化工具，主要适用于日常安全服务、渗透测试人员和RedTeam红队人员，它集合的功能包括：存活IP探测、开放端口探测、web服务探测、web漏洞扫描、smb爆破、ssh爆破、ftp爆破、mssql爆破等其他数据库爆破工作以及大量web漏洞检测模块。它可以根据目标开放的服务进行特定操作，不做无用功。适用于内网环境、互联网，对发现的安全问题，自动生成保存有用的内容在txt表里，以方便安全人员对授权项目完成测试工作。</h4>

 
  
<p align="center">
    <a href="https://www.github.com/d3ckx1" target="_blank"><img src="https://img.shields.io/badge/作者-d3ckx1-2277cc.svg?style=flat-square&logo=GitHub"></a>
    <a href="https://github.com/d3ckx1/Fvuln"><img alt="Fvuln" src="https://visitor-badge.glitch.me/badge?page_id=Paper-Pen.Fvuln"></a>
  <a href="https://github.com/d3ckx1/Fvuln"><img alt="Fvuln" src="https://img.shields.io/github/forks/d3ckx1/Fvuln.svg"></a>
    <a href="https://github.com/d3ckx1/Fvuln"><img alt="Fvuln" src="https://img.shields.io/github/issues/d3ckx1/Fvuln.svg"></a>
    <a href="https://github.com/d3ckx1/Fvuln"><img alt="Fvuln" src="https://img.shields.io/github/stars/d3ckx1/Fvuln.svg"></a>
    <a href="https://github.com/d3ckx1/Fvuln"><img alt="Fvuln" src="https://img.shields.io/badge/Fvuln-green"></a>
</p>


# v1.4.4 更新
1、新增 spring cloud function SpEL RCE漏洞；
2、新增4个poc；
3、修复部分漏洞检测bug。

# v1.4.3 更新
1、新增32个poc，现共271个web漏洞；
2、修复fofa.so。



# 已经支持检测的漏洞表
https://github.com/d3ckx1/Fvuln/blob/main/vuln-list.txt

# 注：未经允许不可用于非法扫描攻击，请遵守国家法律法规



# 建议运行环境
Windows环境安装Terminal命令行，（这样运行显示更漂亮美观）
如下图这些都可以
![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20210926222313.png)

Linux环境使用默认命令行终端即可。

# 使用命令_v1.4 版:

fofa批量搜索检测：Fvuln.exe -fofa "泛微云桥"

 
![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/fofa.png)

 注：再同目录下创建“key.txt”文件，文件内第一行写入邮箱地址；第二行写入你的key
 ![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/key.png)



批量URL检测：Fvuln.exe -us urls.txt

![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/urls.png)

注：url.txt 里面放的是URL网站，如下图，
![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/url_txt.png)
或者直接不要http，我写了识别没有http，会自己添加  "http://" 与 “/”

单URL检测：Fvuln.exe -u http://192.168.1.1

![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/url-check.png)

查看帮助: Fvuln.exe -h 

![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/1.png)

查看现在能检测的漏洞模块：Fvuln.exe -l  or Fvuln.exe --list

![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/2.png)
![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/3.png)
![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/4.png)
![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/5.png)

执行： Fvuln.exe -t 192.168.0.100  or Fvuln.exe 192.168.0.1/24

![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/6.png)
![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/7.png)
![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/8.png)

执行完成，查看报表：

![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/9.png)

批量执行：Fvuln.exe -f ip.txt

如果觉得我存活探测慢或者工作中又其他需求需要对特定IP进行扫描工作，可以把IP地址，写进txt里，使用这个功能正常进行全部工作。

如图；
![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/ip_txt.png)


# 缺点

1、爆破ssh工作时命令行上会出现大量报错，但不影响爆破工作、报表里不会保存这些报错。

# 支持的系统
windowexe版本\Linux版本请在 Releases 中下载
https://github.com/d3ckx1/Fvuln/releases

:)


# 欢迎大家使用，并向我提出宝贵意见，以及欢迎大家给我提供poc/exp.

![Image text](https://github.com/d3ckx1/Fvuln/blob/main/image/%E5%BE%AE%E4%BF%A1.jpg)

## 🏁 Star曲线
![star](https://starchart.cc/d3ckx1/Fvuln.svg)


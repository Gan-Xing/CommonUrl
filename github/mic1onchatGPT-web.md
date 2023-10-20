ChatGPT-WEB 更新日志： 快速开始 1\. docker 部署 2\. 本地部署 如果你不想动手 答疑

##  README.md

## ChatGPT-WEB

[![](https://camo.githubusercontent.com/50a25ec6abef2bc573f4127d2b0f3f373d648366a4ef1077742ae53c8d483375/68747470733a2f2f6d69636c6f6e2d6a6f622e6f73732d636e2d68616e677a686f752e616c6979756e63732e636f6d2f696d672f32303233303330363231333935382e706e67)](https://camo.githubusercontent.com/50a25ec6abef2bc573f4127d2b0f3f373d648366a4ef1077742ae53c8d483375/68747470733a2f2f6d69636c6f6e2d6a6f622e6f73732d636e2d68616e677a686f752e616c6979756e63732e636f6d2f696d672f32303233303330363231333935382e706e67)

注意：图中的余额指的是`chatgpt`中`API_KEY`的余额。

本项目为`chatgpt`私有化部署，基于`fastapi` `vue3` `chatgpt api`实现。

  * [笔者案例 - 我用AI帮我完成了单子](https://52caiji.com/posts/other/developer-use-openai.html)



## 更新日志：

03-04：支持代理，环境变量`HTTPS_PROXY`，如`HTTPS_PROXY=http://127.0.0.1:7890`，如果不需要代理，可以不设置。

03-02：支持 `gpt-3.5-turbo` 模型

02-20：支持了API的 **连续对话**

02-15：前端可以自定义 `API_KEY` ，优先级大于后端自定义的 `API_KEY` 。

## 快速开始

### 1\. docker 部署

作者已经将 `chatgpt` 打包成镜像，可以直接使用 `docker` 部署。
    
    
    docker run --name chatgpt -d -p 8000:8000 -e API_KEY=sk-xxxx miclon/chatgpt:latest

docker-compose 部署
    
    
    version: '3'
    
    services:
      chatgpt:
        image: miclon/chatgpt:latest
        container_name: chatgpt
        ports:
          - "8000:8000"
        environment:
          # 填写你的 API_KEY
          - API_KEY=sk-xxxxxx
          # 填写API请求代理地址
          - HTTPS_PROXY=http://192.168.1.17:7890

代理相关问题移步： [PROXY.md](/mic1on/chatGPT-web/blob/main/PROXY.md)

### 2\. 本地部署

  * 拉取项目，安装依赖


    
    
    cd web
    pnpm install
    pnpm run build
    
    
    cp -r web/dist api/dist
    cd api
    pip install -r requirements.txt

  * 启动项目


    
    
    # 启动前端
    cd web
    pnpm run dev
    
    
    # 启动后端
    cd api
    python app.py

## 如果你不想动手

笔者自建了微信公众号： **代码领悟** ，您关注后即可直接与AI对话。

公众号搭建chatGPT搭建流程图：

[![](https://camo.githubusercontent.com/bcd6eb4cf8746c303b21d54172d07c15f443a2d0b8c762cc586f9df8e4b54969/68747470733a2f2f6d69636c6f6e2d6a6f622e6f73732d636e2d68616e677a686f752e616c6979756e63732e636f6d2f696d672f32303233303231303232303130392e706e67)](https://camo.githubusercontent.com/bcd6eb4cf8746c303b21d54172d07c15f443a2d0b8c762cc586f9df8e4b54969/68747470733a2f2f6d69636c6f6e2d6a6f622e6f73732d636e2d68616e677a686f752e616c6979756e63732e636f6d2f696d672f32303233303231303232303130392e706e67)

## 答疑

  * 为什么需要`API_KEY`？



`API_KEY`是`chatgpt`的API密钥，通过API_KEY方可调用官方接口，您可以在[chatgpt](https://platform.openai.com/account/api-keys)官网申请。`API_KEY`通常是`sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`这种形式。

  * 我想修改项目中版权信息，如何修改？



如果你不懂前端，你可以直接fork项目，替换前端字符串然后提交自己仓库，然后会自动docker构建。但是有个前提，你需要在github actions中配置`DOCKER_USERNAME`和`DOCKER_PASSWORD`，这两个变量是你的docker账号和密码。

  * 为什么要内置后端？



前端其实可以直接通过`axios`请求`chatgpt`官方接口，但是为了数据安全，如果前端调用那就会暴露自己的`API_KEY`，所以笔者将前端和后端分离，前端只负责展示，后端负责调用`chatgpt`官方接口。

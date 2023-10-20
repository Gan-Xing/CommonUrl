ChatGPT for Bot 🐎 命令 🔧 搭建 🕸 HTTP API 🦊 加载预设 📷 文字转图片 🎙 文字转语音 🎈 相似项目 🛠 贡献者名单 💪 支持我们

##  README.md

[![cover](https://user-images.githubusercontent.com/117586514/230783378-34ddb86a-c8d3-47a6-baa5-86e39200b258.png)](https://user-images.githubusercontent.com/117586514/230783378-34ddb86a-c8d3-47a6-baa5-86e39200b258.png)

* * *

## ChatGPT for Bot

一款支持各种主流语言模型的聊天的机器人！   
  
[**» 查看使用教程 »**](https://chatgpt-qq.lss233.com/)   


[![Github stars](https://camo.githubusercontent.com/b8caff4611fd61d4e15e7ac3b65d33b5b084cd26a44d053ef6ed18b79faecb15/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6c73733233332f636861746770742d6d697261692d71712d626f743f636f6c6f723d453243444243266c6f676f3d676974687562267374796c653d666f722d7468652d6261646765)](https://github.com/lss233/chatgpt-mirai-qq-bot/stargazers) [![Docker build latest](https://camo.githubusercontent.com/0764b30bbab2687a2564cdaa7689836e30f1ae1ff11172c354ec8f2fcf076172/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f6c73733233332f636861746770742d6d697261692d71712d626f742f646f636b65722d6c61746573742e796d6c3f636f6c6f723d453243444243266c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465267374796c653d666f722d7468652d6261646765)](https://github.com/lss233/chatgpt-mirai-qq-bot/actions/workflows/docker-latest.yml) [![Docker Pulls](https://camo.githubusercontent.com/b7995e13d747147fd7fec466bb3071f00393758838352a72fcde21e9cae1250b/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f6c73733233332f636861746770742d6d697261692d71712d626f743f636f6c6f723d453243444243266c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465267374796c653d666f722d7468652d6261646765)](https://hub.docker.com/r/lss233/chatgpt-mirai-qq-bot/) [![License](https://camo.githubusercontent.com/06aa16982d13f6bf6899107be5bce9f079c32b06dd00e3ead805d304b009c862/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6c73733233332f636861746770742d6d697261692d71712d626f743f26636f6c6f723d453243444243267374796c653d666f722d7468652d6261646765)](/lss233/chatgpt-mirai-qq-bot/blob/browser-version/LICENSE)

* * *

  * [交流群（Discord）](https://discord.gg/cc3S2R6RQV)会发布最新的项目动态、问题答疑和交流 [QQ 群](https://jq.qq.com/?_wv=1027&k=XbGuxdTu) 。  
加群之前先看[这里](https://github.com/lss233/chatgpt-mirai-qq-bot/issues)的内容能不能解决你的问题。  
如果不能解决，把遇到的问题、 **日志** 和配置文件准备好后再提问。
  * [调试群](https://jq.qq.com/?_wv=1027&k=TBX8Saq7) 这个群里有很多 ChatGPT QQ 机器人，不解答技术问题。

[![猫娘问答](https://camo.githubusercontent.com/2bb37641baf2e9800dfc96ff031a2064afb85137dffef1159d0b81d3f1eae7dc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d2545372538432541422545352541382539382545392539372541452545372541442539342d4532434442433f7374796c653d666f722d7468652d6261646765)](https://camo.githubusercontent.com/2bb37641baf2e9800dfc96ff031a2064afb85137dffef1159d0b81d3f1eae7dc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d2545372538432541422545352541382539382545392539372541452545372541442539342d4532434442433f7374796c653d666f722d7468652d6261646765) | [![生活助手](https://camo.githubusercontent.com/762d5a55e011bc45ffa238cbc73e139a1b0914200c5c1c4c34ec3178e03981f3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d2545372539342539462545362542342542422545352538412541392545362538392538422d4532434442433f7374796c653d666f722d7468652d6261646765)](https://camo.githubusercontent.com/762d5a55e011bc45ffa238cbc73e139a1b0914200c5c1c4c34ec3178e03981f3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d2545372539342539462545362542342542422545352538412541392545362538392538422d4532434442433f7374796c653d666f722d7468652d6261646765) | [![文字 RPG](https://camo.githubusercontent.com/786d3bc299b4a8163d749fdfbabd6f4c43b2e0faf583dcd135bfa88720f12724/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d2545362539362538372545352541442539375250472d4532434442433f7374796c653d666f722d7468652d6261646765)](https://camo.githubusercontent.com/786d3bc299b4a8163d749fdfbabd6f4c43b2e0faf583dcd135bfa88720f12724/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d2545362539362538372545352541442539375250472d4532434442433f7374796c653d666f722d7468652d6261646765)  
---|---|---  
[![image](https://user-images.githubusercontent.com/8984680/230702158-73967aa9-01be-44d6-bbd9-24437e333140.png)](https://user-images.githubusercontent.com/8984680/230702158-73967aa9-01be-44d6-bbd9-24437e333140.png) | [![image](https://user-images.githubusercontent.com/8984680/230702177-de96f89b-053e-4313-a131-715af969db04.png)](https://user-images.githubusercontent.com/8984680/230702177-de96f89b-053e-4313-a131-715af969db04.png) | [![image](https://user-images.githubusercontent.com/8984680/230702635-fb1de3bf-acbd-46ca-8d6f-caa47368b4d4.png)](https://user-images.githubusercontent.com/8984680/230702635-fb1de3bf-acbd-46ca-8d6f-caa47368b4d4.png)  
  
**⚡ 支持**

  * 图片发送
  * 关键词触发回复
  * 多账号支持
  * 百度云内容审核
  * 额度限制
  * 人格设定
  * 支持 Mirai、 go-cqhttp、 Telegram、Discord
  * 可作为 HTTP 服务端提供 Web API
  * 支持 ChatGPT 网页版
  * 支持 ChatGPT Plus
  * 支持 ChatGPT API
  * 支持 Bing 聊天
  * 支持 Google bard
  * 支持 poe.com 网页版
  * 支持 文心一言 网页版
  * 支持 ChatGLM-6B 本地版



**🤖 多平台兼容**

我们支持多种聊天平台。

平台 | 群聊回复 | 私聊回复 | 条件触发 | 管理员指令 | 绘图 | 语音回复  
---|---|---|---|---|---|---  
Mirai | 支持 | 支持 | 支持 | 支持 | 支持 | 支持  
OneBot | 支持 | 支持 | 支持 | 支持 | 支持 | 支持  
Telegram | 支持 | 支持 | 部分支持 | 部分支持 | 支持 | 支持  
Discord | 支持 | 支持 | 部分支持 | 不支持 | 支持 | 支持  
  
## 🐎 命令

**你可以在[Wiki](https://github.com/lss233/chatgpt-mirai-qq-bot/wiki/) 了解机器人的内部命令。**

## 🔧 搭建

如果你是手机党，可以看这个纯用手机的部署教程（使用 Linux 服务器）：<https://www.bilibili.com/video/av949514538>

Linux: 通过快速部署脚本部署 （新人推荐) 执行下面这行命令启动自动部署脚本。 它会为你安装 Docker、 Docker Compose 和编写配置文件。 
    
    
    bash -c "$(curl -fsSL https://gist.githubusercontent.com/lss233/54f0f794f2157665768b1bdcbed837fd/raw/chatgpt-mirai-installer-154-16RC3.sh)"

Linux: 通过 Docker Compose 部署 （自带 Mirai) 我们使用 `docker-compose.yaml` 整合了 [lss233/mirai-http](<https://github.com/lss233/mirai-http-docker>) 和本项目来实现快速部署。 但是在部署过程中仍然需要一些步骤来进行配置。 

你可以在 [Wiki](https://github.com/lss233/chatgpt-mirai-qq-bot/wiki/%E4%BD%BF%E7%94%A8-Docker-Compose-%E9%83%A8%E7%BD%B2%EF%BC%88Mirai---%E6%9C%AC%E9%A1%B9%E7%9B%AE%EF%BC%89) 查看搭建教程。

Linux: 通过 Docker 部署 （适合已经有 Mirai 的用户)

  1. 找个合适的位置，写你的 `config.cfg`。

  2. 执行以下命令，启动 bot：



    
    
    # 修改 /path/to/config.cfg 为你 config.cfg 的位置
    # XPRA_PASSWORD=123456 中的 123456 是你的 Xpra 密码，建议修改
    docker run --name mirai-chatgpt-bot \
        -e XPRA_PASSWORD=123456 \
        -v /path/to/config.cfg:/app/config.cfg \
        --network host \
        lss233/chatgpt-mirai-qq-bot:browser-version

  3. 启动后，在浏览器访问 `http://你的服务器IP:14500` 可以访问到登录 ChatGPT 的浏览器页面

Windows: 快速部署包 (自带 Mirai，新人推荐）

我们为 Windows 用户制作了一个快速启动包，可以在 [Release](https://github.com/lss233/chatgpt-mirai-qq-bot/releases) 中找到。

文件名为：`quickstart-windows-amd64.zip` 或者 `Windows快速部署包.zip`

Mac: 快速部署包 (自带 Mirai，新人推荐）

Windows快速部署包Mac用户也可以使用，@magisk317 已测试通过，功能基本都正常 不过，需要注意的是，如果需要使用图片模式，由于`wkhtmltoimage.exe`在Mac上无法运行，可以使用`wkhtmltopdf`代替，安装命令：
    
    
    brew install --cask wkhtmltopdf
    

brew的安装及使用方法详见：[链接](https://brew.sh/index_zh-cn)

手动部署

提示：你需要 Python >= 3.11 才能运行本项目

  1. 部署 Mirai ，安装 mirai-http-api 插件。

  2. 下载本项目:



    
    
    git clone https://github.com/lss233/chatgpt-mirai-qq-bot
    cd chatgpt-mirai-qq-bot
    pip3 install -r requirements.txt

  3. 参照项目文档调整配置文件。

  4. 启动 bot.



    
    
    python3 bot.py

**[广告] 免费 OpenAI API Key**  
[![](https://user-images.githubusercontent.com/8984680/232325002-c3e4550e-f642-45fc-b51c-f570386721c3.png)](https://user-images.githubusercontent.com/8984680/232325002-c3e4550e-f642-45fc-b51c-f570386721c3.png)  
你可以在[这里获取免费的 OpenAI API Key](https://freeopenai.xyz/) 测试使用。

## 🕸 HTTP API

在 `config.cfg` 中加入以下配置后，将额外提供 HTTP API 支持。
    
    
    [http]
    # 填写提供服务的端口
    host = "0.0.0.0"
    port = 8080
    debug = false

启动后将提供以下接口：

**POST** `/v1/chat`

**请求参数**

参数名 | 必选 | 类型 | 说明  
---|---|---|---  
session_id | 是 | String | 会话ID，默认：`friend-default_session`  
username | 是 | String | 用户名，默认：`某人`  
message | 是 | String | 消息，不能为空  
  
**请求示例**
    
    
    {
        "session_id": "friend-123456",
        "username": "testuser",
        "message": "ping"
    }

**响应格式**

参数名 | 类型 | 说明  
---|---|---  
result | String | SUCESS,DONE,FAILED  
message | String[] | 文本返回，支持多段返回  
voice | String[] | 音频返回，支持多个音频的base64编码；参考：data:audio/mpeg;base64,...  
image | String[] | 图片返回，支持多个图片的base64编码；参考：data:image/png;base64,...  
  
**响应示例**
    
    
    {
        "result": "DONE",
        "message": ["pong!"],
        "voice": [],
        "image": []
    }

**POST** `/v2/chat`

**请求参数**

参数名 | 必选 | 类型 | 说明  
---|---|---|---  
session_id | 是 | String | 会话ID，默认：`friend-default_session`  
username | 是 | String | 用户名，默认：`某人`  
message | 是 | String | 消息，不能为空  
  
**请求示例**
    
    
    {
        "session_id": "friend-123456",
        "username": "testuser",
        "message": "ping"
    }

**响应格式** 字符串：request_id

**响应示例**
    
    
    1681525479905
    

**GET** `/v2/chat/response`

**请求参数**

参数名 | 必选 | 类型 | 说明  
---|---|---|---  
request_id | 是 | String | 请求id，/v2/chat返回的值  
  
**请求示例**
    
    
    /v2/chat/response?request_id=1681525479905
    

**响应格式**

参数名 | 类型 | 说明  
---|---|---  
result | String | SUCESS,DONE,FAILED  
message | String[] | 文本返回，支持多段返回  
voice | String[] | 音频返回，支持多个音频的base64编码；参考：data:audio/mpeg;base64,...  
image | String[] | 图片返回，支持多个图片的base64编码；参考：data:image/png;base64,...  
  
  * 每次请求返回增量并清空。DONE、FAILED之后没有更多返回。



**响应示例**
    
    
    {
        "result": "DONE",
        "message": ["pong!"],
        "voice": ["data:audio/mpeg;base64,..."],
        "image": ["data:image/png;base64,...", "data:image/png;base64,..."]
    }

## 🦊 加载预设

如果你想让机器人自动带上某种聊天风格，可以使用预设功能。

我们自带了 `猫娘` 和 `正常` 两种预设，你可以在 `presets` 文件夹下了解预设的写法。

使用 `加载预设 猫娘` 来加载猫娘预设。

下面是一些预设的小视频，你可以看看效果：

  * MOSS： <https://www.bilibili.com/video/av309604568>
  * 丁真：<https://www.bilibili.com/video/av267013053>
  * 小黑子：<https://www.bilibili.com/video/av309604568>
  * 高启强：<https://www.bilibili.com/video/av779555493>



关于预设系统的详细教程：[Wiki](https://github.com/lss233/chatgpt-mirai-qq-bot/wiki/%F0%9F%90%B1-%E9%A2%84%E8%AE%BE%E7%B3%BB%E7%BB%9F)

你可以在 [Awesome ChatGPT QQ Presets](https://github.com/lss233/awesome-chatgpt-qq-presets/tree/master) 获取由大家分享的预设。

你也可以参考 [Awesome-ChatGPT-prompts-ZH_CN](https://github.com/L1Xu4n/Awesome-ChatGPT-prompts-ZH_CN) 来调教你的 ChatGPT，还可以参考 [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts) 来解锁更多技能。

## 📷 文字转图片

在发送代码或者向 QQ 群发送消息失败时，自动将消息转为图片发送。

字体文件存放于 `fonts/` 目录中。

默认使用的字体是 [更纱黑体](https://github.com/be5invis/Sarasa-Gothic)。

## 🎙 文字转语音

自 v2.2.5 开始，我们支持接入微软的 Azure 引擎 和 VITS 引擎，让你的机器人发送语音。

**提示** ：在 Windows 平台上使用语音功能需要安装最新的 VC 运行库，你可以在[这里](https://learn.microsoft.com/zh-CN/cpp/windows/latest-supported-vc-redist?view=msvc-170)下载。`

## 🎈 相似项目

如果你自己也有做机器人的想法，可以看看下面这些项目：

  * [Ariadne](https://github.com/GraiaProject/Ariadne) \- 一个优雅且完备的 Python QQ 机器人框架 （主要是这个 ！！！）
  * [mirai-api-http](https://github.com/project-mirai/mirai-api-http) \- 提供HTTP API供所有语言使用 mirai QQ 机器人
  * [Reverse Engineered ChatGPT by OpenAI](https://github.com/acheong08/ChatGPT) \- 非官方 ChatGPT Python 支持库



本项目基于以上项目开发，所以你可以给他们也点个 star ！

除了我们以外，还有这些很出色的项目：

  * [LlmKira / Openaibot](https://github.com/LlmKira/Openaibot) \- 全平台，多模态理解的 OpenAI 机器人
  * [RockChinQ / QChatGPT](https://github.com/RockChinQ/QChatGPT) \- 基于 OpenAI 官方 API， 使用 GPT-3 的 QQ 机器人
  * [fuergaosi233 / wechat-chatgpt](https://github.com/fuergaosi233/wechat-chatgpt) \- 在微信上迅速接入 ChatGPT



## 🛠 贡献者名单

欢迎提出新的点子、 Pull Request。

[ ![](https://camo.githubusercontent.com/0e009257ee96504a47c2e494a4d9d46a4666f5920c04779997d1b9d8495647fc/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d6c73733233332f636861746770742d6d697261692d71712d626f74) ](https://github.com/lss233/chatgpt-mirai-qq-bot/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks).

## 💪 支持我们

如果我们这个项目对你有所帮助，请给我们一颗 ⭐️

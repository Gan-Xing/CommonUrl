Ex-ChatGPT - ChatGPT with ToolFormer 交互界面 ExChatGPT WebChatGPTEnhance Highlights 计划更新 安装 Ex-chatGPT Installation Docker 快速部署 方法一 使用构建好的镜像 方法二 自己构建镜像 使用 WebChatGPTEnhance Installation 模式介绍 Web Mode Chat Mode WebDirect Mode Detail Mode Keyword Mode 更新日志

##  README.md

# Ex-ChatGPT - ChatGPT with ToolFormer

[![language](https://camo.githubusercontent.com/3e0487d09e255c280c6aaca8cd55a5d1762e4f77a762e90a9321a45b8a722961/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c616e67756167652d707974686f6e2d626c7565)](https://camo.githubusercontent.com/3e0487d09e255c280c6aaca8cd55a5d1762e4f77a762e90a9321a45b8a722961/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c616e67756167652d707974686f6e2d626c7565) [![GitHub](https://camo.githubusercontent.com/5157cc0f676821ee53b728468df54b93dad8260e175bc5a94b906245eaab8e96/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f636972636c65737461727a65726f2f45582d63686174475054)](https://camo.githubusercontent.com/5157cc0f676821ee53b728468df54b93dad8260e175bc5a94b906245eaab8e96/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f636972636c65737461727a65726f2f45582d63686174475054) [![GitHub last commit](https://camo.githubusercontent.com/acd3804f1bd7b6ab6d25dea368e6f6dbcf6b2a6b6177fafa3bdccd912d0a9377/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f636972636c65737461727a65726f2f45582d63686174475054)](https://camo.githubusercontent.com/acd3804f1bd7b6ab6d25dea368e6f6dbcf6b2a6b6177fafa3bdccd912d0a9377/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f636972636c65737461727a65726f2f45582d63686174475054) [![GitHub Repo stars](https://camo.githubusercontent.com/8b71f18c6c7d8a05995e633faf842221e74f4d150ea7b728798e520deae2370b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f636972636c65737461727a65726f2f45582d636861744750543f7374796c653d736f6369616c)](https://camo.githubusercontent.com/8b71f18c6c7d8a05995e633faf842221e74f4d150ea7b728798e520deae2370b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f636972636c65737461727a65726f2f45582d636861744750543f7374796c653d736f6369616c)

简体中文 [English](/circlestarzero/EX-chatGPT/blob/main/README.en.md) / [Background](/circlestarzero/EX-chatGPT/blob/main/BACKGROUND.md)

ChatGPT 是一个强大的工具平台，可以无需任何调整就生成 API 请求来协助回答问题。`Ex-ChatGPT` 使得 ChatGPT 能够调用外部 API，例如 **WolframAlpha、Google 和 WikiMedia** ，以提供更准确和及时的答案。

这个项目分为 `Ex-ChatGPT` 和 `WebChatGPTEnhance` 两部分。前者是一个使用了 `GPT3.5 Turbo API`、 **WolframAlpha、Google 和 WikiMedia** 等 API 的服务，能够提供更强大的功能和更准确的答案。后者是一个 **浏览器扩展程序** ，它更新了原有的 WebChatGPT 插件以支持添加外部 API，支持 ChatGPT 网页调用不同的 API 和提示。

## 交互界面

### ExChatGPT

[![chatHistory](/circlestarzero/EX-chatGPT/raw/main/img/newPage.jpg)](/circlestarzero/EX-chatGPT/blob/main/img/newPage.jpg)

### WebChatGPTEnhance

[![WebChatGPT](/circlestarzero/EX-chatGPT/raw/main/img/chatGPTChromeEnhance.png)](/circlestarzero/EX-chatGPT/blob/main/img/chatGPTChromeEnhance.png)

## Highlights

  * **OAuth2.0多用户鉴权管理** (见webTest分支)
  * **语音对话功能** ，使用微软 Azure API，优化响应速度 ( 1-2 秒左右 ) ，包含语音识别和文字转语音，支持多种音色和语言，自定义声音。
  * **docker 和 proxy 支持**
  * **聊天记录冗余备份**
  * 支持 OpenAI GPT-3.5 Turbo API
  * 允许 ChatGPT 调用外部 API 接口 ( **Google,WolframAlpha,WikiMedia** )
  * 对 Google 搜索结果进行数据清洗, 减少token占用
  * 自动保存载入对话历史， **自动压缩对话**
  * **可显示使用的 Token 数量**
  * **API池** , **API** 冷却
  * **Markdown and MathJax** 渲染
  * 调用 **API 过程显示动画** , 类似必应
  * **历史对话管理** 载入，类 chatgpt 页面布局
  * **快捷键** 快速选择模式 `Tab` 和换行 `Shift+Enter`,`Enter` 发送， `up`,`down` 选择历史发送消息，类似终端
  * `stream` 特性，它类似于打字机的效果，可以更快地响应结果。与一次性加载所有内容不同，stream会逐步输出结果。如示例中所示： [![stream](/circlestarzero/EX-chatGPT/raw/main/img/stream.gif)](/circlestarzero/EX-chatGPT/blob/main/img/stream.gif) [ ![stream](https://github.com/circlestarzero/EX-chatGPT/raw/main/img/stream.gif) ](https://github.com/circlestarzero/EX-chatGPT/blob/main/img/stream.gif) [ ](https://github.com/circlestarzero/EX-chatGPT/blob/main/img/stream.gif)
  * `chat` 模式下 **prompt 自动补全** 选择，支持模糊搜索， 拼音搜索， 支持自定义 prompt, 项目中自带 [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) 中的 `prompt` [![promptCompletion](/circlestarzero/EX-chatGPT/raw/main/img/promptCompletion.gif)](/circlestarzero/EX-chatGPT/blob/main/img/promptCompletion.gif) [ ![promptCompletion](https://github.com/circlestarzero/EX-chatGPT/raw/main/img/promptCompletion.gif) ](https://github.com/circlestarzero/EX-chatGPT/blob/main/img/promptCompletion.gif) [ ](https://github.com/circlestarzero/EX-chatGPT/blob/main/img/promptCompletion.gif)



## 计划更新

  * 移动端界面适配
  * 发送图片OCR识别公式文字
  * OAuth2.0多用户鉴权 (见webTest分支)
  * 调用diffusing model生成图片(达到类似多模态效果)
  * 网页搜索结果进一步爬虫总结清洗数据
  * 增加代码运行API,以及更多API
  * 聊天记录/本地知识数据库embedding对齐检索



## 安装

### Ex-chatGPT Installation

  * `pip install` `pip install -r requirements.txt`
  * 将 `apikey.ini.example` 复制改名为 `apikey.ini`,然后在 `apikey.ini` 中填入你的 API 密钥， 以及代理 ( 如果只有一个 `openAI` 的 `API key`,将 `key1 = sk-xxxx; key2 = sk-xxxx` 删除即可 )
  * `Google api key and search engine id` [申请](https://developers.google.com/custom-search/v1/overview?hl=en)
  * `wolframAlpha app id key` [申请](https://products.wolframalpha.com/api/)
  * `openAI api key`( 新功能 ) 或 `chatGPT access_token` ( 旧版本 ) [申请](https://platform.openai.com)
  * (可选) 在 `apikey.ini` 中填写`Azure API key` 和 `region` [申请](https://learn.microsoft.com/zh-cn/azure/cognitive-services/speech-service)
  * 运行 `main.py` 并打开 `http://127.0.0.1:1234/`
  * 选择模式 ( 可以使用 `Tab` ) ，例如 `chat,detail,web,webDirect,WebKeyWord`
  * `chat` 模式下 使用 `\{promptname} {query}` 格式来模糊搜索选择 prompt
  * **快捷键** 快速选择模式 `Tab` 和换行 `Shift+Enter`,`Enter` 发送， `up`,`down` 选择历史发送消息，类似终端
  * **语音对话聊天** (可选功能), 在 `chatGPTEx/static/styles/tts.js` 中选择语言和音色, 在聊天界面中点击麦克风`启动/关闭`对话模式



#### Docker 快速部署

##### 方法一 使用构建好的镜像

  1. 创建配置文件目录并拉取配置文件

`mkdir config && wget https://raw.githubusercontent.com/circlestarzero/EX-chatGPT/main/chatGPTEx/apikey.ini.example -O ./config/apikey.ini`

  2. 编辑配置文件或者把编辑好的配置文件传到config文件夹下。

`vim ./config/apikey.ini`

  3. 拉取docker镜像

`docker pull 0nlylty/exchatgpt:latest`

  4. 创建容器
    
        docker run -dit \
      -v ~/config:/config \
      -p 5000:5000 \
      --name exchatgpt \
      --restart unless-stopped \
     0nlylty/exchatgpt:latest




##### 方法二 自己构建镜像

  1. 创建配置文件目录并拉取配置文件

`mkdir config && wget https://raw.githubusercontent.com/circlestarzero/EX-chatGPT/main/chatGPTEx/apikey.ini.example -O ./config/apikey.ini`

  2. 编辑配置文件或者把编辑好的配置文件传到config文件夹下。

`vim ./config/apikey.ini`

  3. 构建并运行
    
        # 克隆代码
    git clone https://github.com/circlestarzero/EX-chatGPT.git --depth=1
    # 进入项目目录
    cd EX-chatGPT/chatGPTEx
    # 编辑docker-compose.yaml的挂载路径
    ~/config:/config   # 冒号左边请修改为保存配置的路径
    # 配置补充完整后启动
    docker compose up -d
    




##### 使用
    
    
    # 访问
    http://your_ip:5000
    
    # 查看日志
    docker logs -f --tail 100 exchatgpt

### WebChatGPTEnhance Installation

  * 在 `chatGPTChromeEhance/src/util/apiManager.ts/getDefaultAPI` 中填入 Google API 信息
  * 运行 `npm install`
  * 运行 `npm run build-prod`
  * 在 `chatGPTChromeEhance/build` 中获取构建好的扩展
  * add your `prompts` and `APIs` in option page.
  * `APIs` and `prompts` examples are in `/WebChatGPTAPI`
  * `wolframAlpha` needs to run local sever - `WebChatGPTAPI/WolframLocalServer.py`



## 模式介绍

### Web Mode

Web Mode 开始时会直接询问 ChatGPT 一个问题。ChatGPT 会生成一系列与查询相关的 API 调用，并使用第一个返回的结果和问题进行验证和补充。最后，ChatGPT 会对信息进行总结。Web Mode 具有比仅总结响应更好的聊天能力。

### Chat Mode

Chat Mode 仅调用 OpenAI API 接口，类似于 ChatGPT 的 Web 版本。您可以通过输入 `/promtname` 来搜索和选择不同的提示，它还支持模糊搜索。

### WebDirect Mode

WebDirect Mode 首先让 ChatGPT 生成一系列与查询相关的 API 调用。然后，它直接调用第三方 API 搜索每个查询的答案，最后 ChatGPT 对信息进行总结。WebDirect Mode 对于单个查询信息更快且相对更准确。

### Detail Mode

Detail Mode 是 WebDirect Mode 的扩展，它会进行额外的 API 调用来补充当前结果中未找到的信息 ( 例如之前未搜索到的信息 ) 。最后，ChatGPT 对信息进行总结。

### Keyword Mode

Keyword Mode 直接从 ChatGPT 中生成关键词进行查询，使用 DDG 进行查询，不需要其他 API 密钥。但是其准确性相对较差。

## 更新日志

  * **OAuth2.0多用户鉴权管理** (见webTest分支)
  * 对 Google 搜索结果进行数据清洗, 减少token占用
  * 更新所有API代理池, 增加API限制冷却机制(Google 403 冷却1天)
  * **语音对话功能** , 使用微软azureAPI, 优化响应速度, 包含识别语音和文字转语音, 支持多种音色和语言,自定义声音
  * `stream` 特性，它类似于打字机的效果，可以更快地响应结果。与一次性加载所有内容不同，stream会逐步输出结果。如示例中所示： [![stream](/circlestarzero/EX-chatGPT/raw/main/img/stream.gif)](/circlestarzero/EX-chatGPT/blob/main/img/stream.gif) [ ![stream](https://github.com/circlestarzero/EX-chatGPT/raw/main/img/stream.gif) ](https://github.com/circlestarzero/EX-chatGPT/blob/main/img/stream.gif) [ ](https://github.com/circlestarzero/EX-chatGPT/blob/main/img/stream.gif)
  * 聊天记录冗余备份
  * chat 模式下 prompt 自动补全选择，支持模糊搜索和拼音搜索



[![promptCompletion](/circlestarzero/EX-chatGPT/raw/main/img/promptCompletion.gif)](/circlestarzero/EX-chatGPT/blob/main/img/promptCompletion.gif) [ ![promptCompletion](https://github.com/circlestarzero/EX-chatGPT/raw/main/img/promptCompletion.gif) ](https://github.com/circlestarzero/EX-chatGPT/blob/main/img/promptCompletion.gif) [ ](https://github.com/circlestarzero/EX-chatGPT/blob/main/img/promptCompletion.gif)

  * 更新 Docker 和 proxy 支持
  * 支持 OpenAI GPT-3.5 Turbo API，快速且价格低廉
  * 提供额外的 API 调用和搜索摘要，以提供更全面和详细的答案
  * 使用快捷键快速选择模式 `Tab` 和换行 `Shift+Enter`，同时使用 `Enter` 发送消息。使用 `up` 和 `down` 选择历史发送消息，类似终端操作
  * 更新历史对话管理，支持载入、删除和保存历史对话



[![chatHistory](/circlestarzero/EX-chatGPT/raw/main/img/newPage.jpg)](/circlestarzero/EX-chatGPT/blob/main/img/newPage.jpg)

  * 更新 API 调用处理动画



[![APIAnimation](/circlestarzero/EX-chatGPT/raw/main/img/APIAnimation.png)](/circlestarzero/EX-chatGPT/blob/main/img/APIAnimation.png)

  * 页面美化



[![WebBeautification](/circlestarzero/EX-chatGPT/raw/main/img/WebPageBeautification.jpg)](/circlestarzero/EX-chatGPT/blob/main/img/WebPageBeautification.jpg)

  * Markdown 和 MathJax 渲染器



[![MathJax](/circlestarzero/EX-chatGPT/raw/main/img/mathjax.jpg)](/circlestarzero/EX-chatGPT/blob/main/img/mathjax.jpg)

  * 更新聊天记录 token 优化器，Web 模式可以根据聊天记录进行响应；添加 token 成本计数器



[![history](/circlestarzero/EX-chatGPT/raw/main/img/webHistory.jpg)](/circlestarzero/EX-chatGPT/blob/main/img/webHistory.jpg)

  * 更新 Web 聊天模式选择，优化 prompt 和 token 成本，限制 token 上限



[![mode](/circlestarzero/EX-chatGPT/raw/main/img/mode.jpg)](/circlestarzero/EX-chatGPT/blob/main/img/mode.jpg)

  * 改进对中文查询的支持，并添加当前日期信息



[![date](/circlestarzero/EX-chatGPT/raw/main/img/date.jpg)](/circlestarzero/EX-chatGPT/blob/main/img/date.jpg)

  * 更新 Web 聊天模式并修复一些错误
  * 更新 API 配置
  * 更新 API 池
  * 自动保存载入对话历史，ChatGPT 可联系之前对话



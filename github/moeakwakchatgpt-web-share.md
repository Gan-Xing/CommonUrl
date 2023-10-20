ChatGPT Web Share 关于项目 特点 部署指南 声明 调试信息收集和隐私声明 风险声明 捐助和支持

##  README.md

# ChatGPT Web Share

[![GitHub tag \(latest by date\)](https://camo.githubusercontent.com/5d5dba3303655e583a5af09d8326849a126602d7486dc08e48b782a8ef41400f/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f7461672f6d6f65616b77616b2f636861746770742d7765622d73686172653f6c6162656c3d636f6e7461696e6572266c6f676f3d646f636b6572)](https://github.com/moeakwak/chatgpt-web-share/pkgs/container/chatgpt-web-share) [![Github Workflow Status](https://camo.githubusercontent.com/5dceb8ecb23b3c31eede7c9da454ba0107e923a91f26b63c29e1ee79f3fcf85e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f6d6f65616b77616b2f636861746770742d7765622d73686172652f646f636b65722d696d6167652e796d6c3f6c6162656c3d6275696c64)](https://github.com/moeakwak/chatgpt-web-share/actions) [![License](https://camo.githubusercontent.com/38d35281d8e7fc5518bf98d7151c3176e874f7577b078fe4df67c813f5ba430e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6d6f65616b77616b2f636861746770742d7765622d7368617265)](https://github.com/moeakwak/chatgpt-web-share/blob/main/LICENSE)

**> >> [English Readme](/moeakwak/chatgpt-web-share/blob/main/README.en.md) <<<**

共享一个 ChatGPT 账号给多用户同时使用的 web 应用，使用 FastAPI + Vue3 开发。可用于朋友之间共享或合租 ChatGPT 账号。支持 ChatGPT Plus / 设置对话模型 / 用户请求限制等功能。支持使用 GPT-4！

[![screenshot](/moeakwak/chatgpt-web-share/raw/main/docs/screenshot.jpeg)](/moeakwak/chatgpt-web-share/blob/main/docs/screenshot.jpeg)

[![screenshot_admin](/moeakwak/chatgpt-web-share/raw/main/docs/screenshot_admin.jpeg)](/moeakwak/chatgpt-web-share/blob/main/docs/screenshot_admin.jpeg)

通知/讨论 Channel：<https://t.me/chatgptwebshare>

## 关于项目

ChatGPT Web Share (简称 CWS) 的目的是「共享」一个 ChatGPT Plus 账号给多个用户。CWS 是：

  * 前后端分离的应用，因此你需要自行部署后端到一个稳定且 IP 可靠的服务器上
  * 用于共享 ChatGPT 账号，而不是官方 API
  * 支持用户管理，并支持设置各用户的权限和对话次数
  * 优先支持 ChatGPT Plus 账号



## 特点

  * 美观简洁的 web 界面，使用 [naive-ui](https://www.naiveui.com/)
    * 多语言（简体中文、英语）支持
    * 适配夜间模式
    * 支持一键复制回复内容或代码内容
    * 支持显示回复中的图像/表格/数学公式/代码语法高亮
    * 一键导出对话为美观的 Markdown 或 PDF 文件
    * 动态显示回复内容
    * 支持停止生成对话
  * 多用户共享管理 
    * 创建多用户用于共享一个 ChatGPT 账号
    * 不同用户创建的 ChatGPT 对话互相分隔，不会相互影响
    * 多用户同时请求时，会进行排队处理
    * 管理员可设置用户的最大对话数量、对话次数限制等
    * 提供实时更新的服务使用状态，从而能够避开使用高峰
  * 完善的管理功能 
    * 修改用户对话限制
    * 管理对话/查看成员对话记录/分配对话给特定用户
    * 实时查看日志
    * 记录请求及对话统计信息



## 部署指南

参见 WIKI：[中文指南](https://github.com/moeakwak/chatgpt-web-share/wiki/%E4%B8%AD%E6%96%87%E6%8C%87%E5%8D%97)

## 声明

### 调试信息收集和隐私声明

~~从版本 v0.2.16 开始，本项目使用 Sentry 来收集错误信息。使用本项目即表示您同意 Sentry 的隐私政策。通过 Sentry 收集的任何匿名信息仅用于开发和调试目的。~~ 我们永远不会收集或存储您的私人数据，如用户名、密码、access token 等。

目前，自 v0.3.5 版本后已不再通过 Sentry 收集错误信息。

### 风险声明

本项目仅供学习和研究使用，不鼓励用于商业用途。我们不对任何因使用本项目而导致的任何损失负责。

## 捐助和支持

如果觉得本项目对您有帮助，欢迎通过扫描下方赞赏码捐助项目 :)

[![donate](/moeakwak/chatgpt-web-share/raw/main/docs/donate.png)](/moeakwak/chatgpt-web-share/blob/main/docs/donate.png)

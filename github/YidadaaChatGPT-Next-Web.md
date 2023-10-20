ChatGPT Next Web Features Roadmap Not in Plan 主要功能 开发计划 不会开发的功能 Get Started FAQ Keep Updated Enable Automatic Updates Manually Updating Code Access Password Environment Variables OPENAI_API_KEY (required) CODE (optional) BASE_URL (optional) OPENAI_ORG_ID (optional) Development Local Development Deployment Docker (Recommended) Shell Screenshots Donation Special Thanks Sponsor Contributor LICENSE

##  README.md

[![icon](/Yidadaa/ChatGPT-Next-Web/raw/main/docs/images/icon.svg)](/Yidadaa/ChatGPT-Next-Web/blob/main/docs/images/icon.svg)

# ChatGPT Next Web

English / [简体中文](/Yidadaa/ChatGPT-Next-Web/blob/main/README_CN.md)

One-Click to deploy well-designed ChatGPT web UI on Vercel.

一键免费部署你的私人 ChatGPT 网页应用。

[Demo](https://chat-gpt-next-web.vercel.app/) / [Issues](https://github.com/Yidadaa/ChatGPT-Next-Web/issues) / [Join Discord](https://discord.gg/zrhvHCr79N) / [Buy Me a Coffee](https://www.buymeacoffee.com/yidadaa)

[演示](https://chat-gpt-next-web.vercel.app/) / [反馈](https://github.com/Yidadaa/ChatGPT-Next-Web/issues) / [QQ 群](https://user-images.githubusercontent.com/16968934/233002565-139daa1a-eb3a-4a12-ac37-6418e7a15d36.png) / [打赏开发者](https://user-images.githubusercontent.com/16968934/227772541-5bcd52d8-61b7-488c-a203-0330d8006e2b.jpg)

[![Deploy with Vercel](https://camo.githubusercontent.com/5e471e99e8e022cf454693e38ec843036ec6301e27ee1e1fa10325b1cb720584/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FYidadaa%2FChatGPT-Next-Web&env=OPENAI_API_KEY&env=CODE&project-name=chatgpt-next-web&repository-name=ChatGPT-Next-Web)

[![Open in Gitpod](https://camo.githubusercontent.com/76e60919474807718793857d8eb615e7a50b18b04050577e5a35c19421f260a3/68747470733a2f2f676974706f642e696f2f627574746f6e2f6f70656e2d696e2d676974706f642e737667)](https://gitpod.io/#https://github.com/Yidadaa/ChatGPT-Next-Web)

[![cover](/Yidadaa/ChatGPT-Next-Web/raw/main/docs/images/cover.png)](/Yidadaa/ChatGPT-Next-Web/blob/main/docs/images/cover.png)

## Features

  * **Deploy for free with one-click** on Vercel in under 1 minute
  * Privacy first, all data stored locally in the browser
  * Responsive design, dark mode and PWA
  * Fast first screen loading speed (~100kb), support streaming response
  * Awesome prompts powered by [awesome-chatgpt-prompts-zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) and [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts)
  * Automatically compresses chat history to support long conversations while also saving your tokens
  * One-click export all chat history with full Markdown support
  * I18n supported



## Roadmap

  * System Prompt: pin a user defined prompt as system prompt [#138](https://github.com/Yidadaa/ChatGPT-Next-Web/issues/138)
  * User Prompt: user can edit and save custom prompts to prompt list
  * Prompt Template: create a new chat with pre-defined in-context prompts
  * Share as image, share to ShareGPT
  * Desktop App with tauri
  * Self-host Model: support llama, alpaca, ChatGLM, BELLE etc.
  * Plugins: support network search, calculator, any other apis etc. [#165](https://github.com/Yidadaa/ChatGPT-Next-Web/issues/165)



### Not in Plan

  * User login, accounts, cloud sync
  * UI text customize



## 主要功能

  * 在 1 分钟内使用 Vercel **免费一键部署**
  * 精心设计的 UI，响应式设计，支持深色模式，支持 PWA
  * 极快的首屏加载速度（~100kb），支持流式响应
  * 隐私安全，所有数据保存在用户浏览器本地
  * 海量的内置 prompt 列表，来自[中文](https://github.com/PlexPt/awesome-chatgpt-prompts-zh)和[英文](https://github.com/f/awesome-chatgpt-prompts)
  * 自动压缩上下文聊天记录，在节省 Token 的同时支持超长对话
  * 一键导出聊天记录，完整的 Markdown 支持
  * 拥有自己的域名？好上加好，绑定后即可在任何地方 **无障碍** 快速访问



## 开发计划

  * 为每个对话设置系统 Prompt [#138](https://github.com/Yidadaa/ChatGPT-Next-Web/issues/138)
  * 允许用户自行编辑内置 Prompt 列表
  * 提示词模板：使用预制上下文快速定制新对话
  * 分享为图片，分享到 ShareGPT
  * 使用 tauri 打包桌面应用
  * 支持自部署的大语言模型
  * 插件机制，支持联网搜索、计算器、调用其他平台 api [#165](https://github.com/Yidadaa/ChatGPT-Next-Web/issues/165)



### 不会开发的功能

  * 界面文字自定义
  * 用户登录、账号管理、消息云同步



## Get Started

> [简体中文 > 如何开始使用](/Yidadaa/ChatGPT-Next-Web/blob/main/README_CN.md#%E5%BC%80%E5%A7%8B%E4%BD%BF%E7%94%A8)

  1. Get [OpenAI API Key](https://platform.openai.com/account/api-keys);
  2. Click [![Deploy with Vercel](https://camo.githubusercontent.com/5e471e99e8e022cf454693e38ec843036ec6301e27ee1e1fa10325b1cb720584/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FYidadaa%2FChatGPT-Next-Web&env=OPENAI_API_KEY&env=CODE&project-name=chatgpt-next-web&repository-name=ChatGPT-Next-Web), remember that `CODE` is your page password;
  3. Enjoy :)



## FAQ

[简体中文 > 常见问题](/Yidadaa/ChatGPT-Next-Web/blob/main/docs/faq-cn.md)

[English > FAQ](/Yidadaa/ChatGPT-Next-Web/blob/main/docs/faq-en.md)

## Keep Updated

> [简体中文 > 如何保持代码更新](/Yidadaa/ChatGPT-Next-Web/blob/main/README_CN.md#%E4%BF%9D%E6%8C%81%E6%9B%B4%E6%96%B0)

If you have deployed your own project with just one click following the steps above, you may encounter the issue of "Updates Available" constantly showing up. This is because Vercel will create a new project for you by default instead of forking this project, resulting in the inability to detect updates correctly.

We recommend that you follow the steps below to re-deploy:

  * Delete the original repository;
  * Use the fork button in the upper right corner of the page to fork this project;
  * Choose and deploy in Vercel again, [please see the detailed tutorial](/Yidadaa/ChatGPT-Next-Web/blob/main/docs/vercel-cn.md).



### Enable Automatic Updates

After forking the project, due to the limitations imposed by GitHub, you need to manually enable Workflows and Upstream Sync Action on the Actions page of the forked project. Once enabled, automatic updates will be scheduled every hour:

[![Automatic Updates](/Yidadaa/ChatGPT-Next-Web/raw/main/docs/images/enable-actions.jpg)](/Yidadaa/ChatGPT-Next-Web/blob/main/docs/images/enable-actions.jpg)

[![Enable Automatic Updates](/Yidadaa/ChatGPT-Next-Web/raw/main/docs/images/enable-actions-sync.jpg)](/Yidadaa/ChatGPT-Next-Web/blob/main/docs/images/enable-actions-sync.jpg)

### Manually Updating Code

If you want to update instantly, you can check out the [GitHub documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) to learn how to synchronize a forked project with upstream code.

You can star or watch this project or follow author to get release notifictions in time.

## Access Password

> [简体中文 > 如何增加访问密码](/Yidadaa/ChatGPT-Next-Web/blob/main/README_CN.md#%E9%85%8D%E7%BD%AE%E9%A1%B5%E9%9D%A2%E8%AE%BF%E9%97%AE%E5%AF%86%E7%A0%81)

This project provides limited access control. Please add an environment variable named `CODE` on the vercel environment variables page. The value should be passwords separated by comma like this:
    
    
    code1,code2,code3
    

After adding or modifying this environment variable, please redeploy the project for the changes to take effect.

## Environment Variables

> [简体中文 > 如何配置 api key、访问密码、接口代理](/Yidadaa/ChatGPT-Next-Web/blob/main/README_CN.md#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)

### `OPENAI_API_KEY` (required)

Your openai api key.

### `CODE` (optional)

Access passsword, separated by comma.

### `BASE_URL` (optional)

> Default: `https://api.openai.com`

> Examples: `http://your-openai-proxy.com`

Override openai api request base url.

### `OPENAI_ORG_ID` (optional)

Specify OpenAI organization ID.

## Development

> [简体中文 > 如何进行二次开发](/Yidadaa/ChatGPT-Next-Web/blob/main/README_CN.md#%E5%BC%80%E5%8F%91)

[![Open in Gitpod](https://camo.githubusercontent.com/76e60919474807718793857d8eb615e7a50b18b04050577e5a35c19421f260a3/68747470733a2f2f676974706f642e696f2f627574746f6e2f6f70656e2d696e2d676974706f642e737667)](https://gitpod.io/#https://github.com/Yidadaa/ChatGPT-Next-Web)

Before starting development, you must create a new `.env.local` file at project root, and place your api key into it:
    
    
    OPENAI_API_KEY=<your api key here>
    

### Local Development
    
    
    # 1. install nodejs and yarn first
    # 2. config local env vars in `.env.local`
    # 3. run
    yarn install
    yarn dev

## Deployment

> [简体中文 > 如何部署到私人服务器](/Yidadaa/ChatGPT-Next-Web/blob/main/README_CN.md#%E9%83%A8%E7%BD%B2)

### Docker (Recommended)
    
    
    docker pull yidadaa/chatgpt-next-web
    
    docker run -d -p 3000:3000 \
       -e OPENAI_API_KEY="sk-xxxx" \
       -e CODE="your-password" \
       yidadaa/chatgpt-next-web

You can start service behind a proxy:
    
    
    docker run -d -p 3000:3000 \
       -e OPENAI_API_KEY="sk-xxxx" \
       -e CODE="your-password" \
       -e PROXY_URL="http://localhost:7890" \
       yidadaa/chatgpt-next-web

### Shell
    
    
    bash <(curl -s https://raw.githubusercontent.com/Yidadaa/ChatGPT-Next-Web/main/scripts/setup.sh)

## Screenshots

[![Settings](/Yidadaa/ChatGPT-Next-Web/raw/main/docs/images/settings.png)](/Yidadaa/ChatGPT-Next-Web/blob/main/docs/images/settings.png)

[![More](/Yidadaa/ChatGPT-Next-Web/raw/main/docs/images/more.png)](/Yidadaa/ChatGPT-Next-Web/blob/main/docs/images/more.png)

## Donation

[Buy Me a Coffee](https://www.buymeacoffee.com/yidadaa)

## Special Thanks

### Sponsor

> 仅列出捐赠金额 >= 100RMB 的用户。

[@mushan0x0](https://github.com/mushan0x0) [@ClarenceDan](https://github.com/ClarenceDan) [@zhangjia](https://github.com/zhangjia) [@hoochanlon](https://github.com/hoochanlon) [@relativequantum](https://github.com/relativequantum) [@desenmeng](https://github.com/desenmeng) [@webees](https://github.com/webees) [@chazzhou](https://github.com/chazzhou) [@hauy](https://github.com/hauy) [@Corwin006](https://github.com/Corwin006) [@yankunsong](https://github.com/yankunsong) [@ypwhs](https://github.com/ypwhs) [@fxxxchao](https://github.com/fxxxchao)

### Contributor

[Contributors](https://github.com/Yidadaa/ChatGPT-Next-Web/graphs/contributors)

## LICENSE

[Anti 996 License](https://github.com/kattgu7/Anti-996-License/blob/master/LICENSE_CN_EN)

ChatGPT-web URL: https://niek.github.io/chatgpt-web/ Features Development Use with Docker compose Mocked api Desktop app Contributors

##  README.md

# ChatGPT-web

[![GitHub Workflow Status](https://camo.githubusercontent.com/3b6697afe86b4d8ccb696b203ae02468b8a2b3fe742b168ebad3fa91f6f68930/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f4e69656b2f636861746770742d7765622f70616765732e796d6c3f7374796c653d666c61742d737175617265)](https://github.com/Niek/chatgpt-web/actions/workflows/pages.yml) [![JavaScript Style Guide](https://camo.githubusercontent.com/da7a41846fbdd766554cdf34ee55f10410a12e7a1390ac47e283aa4ed7e8f83f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64655f7374796c652d7374616e646172642d627269676874677265656e2e7376673f7374796c653d666c61742d737175617265)](https://standardjs.com) [![GitHub](https://camo.githubusercontent.com/e153196ff587c64d5304440408f1e8031cc2cb5f65c916e3d5fd2d1ecd7c78ee/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f4e69656b2f636861746770742d776562)](/Niek/chatgpt-web/blob/main/LICENSE) ![All Contributors](https://camo.githubusercontent.com/4886b9bae206efebd3e8989c8437f0041b667ea4d4c718752c51e9687e5a7e3b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616c6c2d636f6e7472696275746f72732f4e69656b2f636861746770742d7765623f636f6c6f723d656538343439267374796c653d666c61742d737175617265)

## **URL** : <https://niek.github.io/chatgpt-web/>

[![Screenshot of ChatGPT-web](/Niek/chatgpt-web/raw/main/.github/screenshot.png)](/Niek/chatgpt-web/blob/main/.github/screenshot.png)

ChatGPT-web is a simple one-page web interface to the OpenAI ChatGPT API. To use it, you need to register for [an OpenAI API key](https://platform.openai.com/account/api-keys) first. All messages are stored in your browser's local storage, so everything is **private**. You can also close the browser tab and come back later to continue the conversation.

## Features

  * **Open source** : ChatGPT-web is open source ([GPL-3.0](/Niek/chatgpt-web/blob/main/LICENSE)), so you can host it yourself and make changes as you want.
  * **Private** : All chats and messages are stored in your browser's local storage, so everything is private.
  * **Customizable** : You can customize the prompt, the temperature, and other model settings. Multiple models (including GTP-4) are supported.
  * **Cheaper** : ChatGPT-web uses the commercial OpenAI API, so it's much cheaper than a ChatGPT Plus subscription.
  * **Fast** : ChatGPT-web is a single-page web app, so it's [fast and responsive](https://pagespeed.web.dev/analysis/https-niek-github-io-chatgpt-web/8xv5uwrnes).
  * **Mobile-friendly** : ChatGPT-web is mobile-friendly, so you can use it on your phone.
  * **Voice input** : ChatGPT-web supports voice input, so you can talk to ChatGPT. It will also talk back to you.
  * **Pre-selected prompts** : ChatGPT-web comes with a list of [pre-selected prompts](https://github.com/f/awesome-chatgpt-prompts), so you can get started quickly.
  * **Export** : ChatGPT-web can export chats as a Markdown file, so you can share them with others.
  * **Code** : ChatGPT-web recognizes and highlights code blocks and allows you to copy them with one click.
  * **Desktop app** : ChatGPT-web can be bundled as a desktop app, so you can use it outside of the browser.



## Development

To run the development server, run
    
    
    npm ci
    npm run dev # or: npm run build

To update the [`awesome-chatgpt-prompts`](/Niek/chatgpt-web/blob/main/src/awesome-chatgpt-prompts) subtree, run :
    
    
    git subtree pull --prefix src/awesome-chatgpt-prompts https://github.com/f/awesome-chatgpt-prompts.git main --squash

## Use with Docker compose
    
    
    docker compose up -d

## Mocked api

If you don't want to wait for the API to respond, you can use the mocked API instead. To use the mocked API, edit the `.env` file at root of the project ans set the key `VITE_API_BASE=http://localhost:5174` in it. Then, run the `docker compose up -d` command above.

You can customize the mocked API response by sending a message that consists of `d` followed by a number, it will delay the response the the specified number of seconds. You can customize the length of the response by including `l` followed by a number, it will return a response with the specified number of sentences. For example, sending the message `d2 l10` will result in a 2 seconds delay and 10 sentences response.

## Desktop app

You can also use ChatGPT-web as a desktop app. To do so, [install Rust first](https://www.rust-lang.org/tools/install). Then, simply run `npm run tauri dev` for the development version or `npm run tauri build` for the production version of the desktop app. The desktop app will be built in the `src-tauri/target` folder.

## Contributors

[![Michael Tanzer](https://avatars.githubusercontent.com/u/23483071?v=4?s=100)  
**Michael Tanzer**](https://github.com/Michael-Tanzer)  
🤔 [💻](https://github.com/Niek/chatgpt-web/commits?author=Michael-Tanzer "Code") | [![Peter](https://avatars.githubusercontent.com/u/870655?v=4?s=100)  
**Peter**](https://github.com/petergeneric)  
🤔 | [![Dan Brown](https://avatars.githubusercontent.com/u/8343178?v=4?s=100)  
**Dan Brown**](https://danb.me)  
🤔 [💻](https://github.com/Niek/chatgpt-web/commits?author=ssddanbrown "Code") | [![littlemoonstones](https://avatars.githubusercontent.com/u/32943414?v=4?s=100)  
**littlemoonstones**](https://github.com/littlemoonstones)  
[ 💻](https://github.com/Niek/chatgpt-web/commits?author=littlemoonstones "Code") 🤔 | [![maxrye1996](https://avatars.githubusercontent.com/u/28844671?v=4?s=100)  
**maxrye1996**](https://github.com/maxrye1996)  
[ 🐛](https://github.com/Niek/chatgpt-web/issues?q=author%3Amaxrye1996 "Bug reports") | [![Mikemansour](https://avatars.githubusercontent.com/u/50986937?v=4?s=100)  
**Mikemansour**](https://github.com/Mikemansour)  
🤔 | [![abc91199](https://avatars.githubusercontent.com/u/16594734?v=4?s=100)  
**abc91199**](https://github.com/abc91199)  
🤔  
---|---|---|---|---|---|---  
[![fuegovic](https://avatars.githubusercontent.com/u/32828263?v=4?s=100)  
**fuegovic**](https://github.com/fuegovic)  
🤔 | [![Sixzeroo](https://avatars.githubusercontent.com/u/20949383?v=4?s=100)  
**Sixzeroo**](https://www.liuin.cn)  
[ 💻](https://github.com/Niek/chatgpt-web/commits?author=Sixzeroo "Code") | [![terryoy](https://avatars.githubusercontent.com/u/1171589?v=4?s=100)  
**terryoy**](http://terryoy.github.io/)  
🤔 [💻](https://github.com/Niek/chatgpt-web/commits?author=terryoy "Code") | [![Yang Lyu](https://avatars.githubusercontent.com/u/15838074?v=4?s=100)  
**Yang Lyu**](https://www.linkedin.com/in/yang-lyu-902/)  
[ 🐛](https://github.com/Niek/chatgpt-web/issues?q=author%3Ayanglyu902 "Bug reports") | [![ryanhex53](https://avatars.githubusercontent.com/u/360426?v=4?s=100)  
**ryanhex53**](https://github.com/ryanhex53)  
[ 💻](https://github.com/Niek/chatgpt-web/commits?author=ryanhex53 "Code") 🎨 | [![Emil Elgaard](https://avatars.githubusercontent.com/u/40603805?v=4?s=100)  
**Emil Elgaard**](https://github.com/shivan2418)  
🤔 🎨 [💻](https://github.com/Niek/chatgpt-web/commits?author=shivan2418 "Code")

Welcome to wechat-chatgpt 👋 🌟 Features 🚀 Usage Use with Railway Use with Fly.io Use with docker Use with docker compose Use with nodejs 📝 Environment Variables 📝 Using Custom ChatGPT API ⌨️ Commands ✨ Contributor 🤝 Contributing Show your support

##  README.md

# Welcome to wechat-chatgpt 👋

[![Version](https://camo.githubusercontent.com/f3f001c434f6a65366705df2cb20d68850f54fe46b9d4b2043d9b3cf7e1fdeab/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d312e302e302d626c75652e7376673f63616368655365636f6e64733d32353932303030)](https://camo.githubusercontent.com/f3f001c434f6a65366705df2cb20d68850f54fe46b9d4b2043d9b3cf7e1fdeab/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d312e302e302d626c75652e7376673f63616368655365636f6e64733d32353932303030) ![License: ISC](https://camo.githubusercontent.com/eab1a35d6b347493d4c0784a527b56e643684c1854d457e5509c26a215a658a4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4953432d79656c6c6f772e737667) [ ![Twitter: fuergaosi](https://camo.githubusercontent.com/e027495004b115a845c74d72b626973206101ad01f008e66c75b23d0534abdb8/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6675657267616f73692e7376673f7374796c653d736f6369616c) ](https://twitter.com/fuergaosi) [ ![join discord community of github profile readme generator](https://camo.githubusercontent.com/7efaa20023d461835dd3b4c322429a2841f551dba40df156b1f384abcb1379a5/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f313035383939343831363434363336393833323f6c6162656c3d4a6f696e253230436f6d6d756e697479266c6f676f3d646973636f7264267374796c653d666c61742d737175617265) ](https://discord.gg/8fXNrxwUJH)

> Use ChatGPT On Wechat via wechaty  
>  English | [中文文档](/fuergaosi233/wechat-chatgpt/blob/main/README_ZH.md)

[![Deploy on Railway](https://camo.githubusercontent.com/081df3dd8cff37aab35044727b02b94a8e948052487a8c6253e190f5940d776d/68747470733a2f2f7261696c7761792e6170702f627574746f6e2e737667)](https://railway.app/template/dMLG70?referralCode=bIYugQ)

## 🌟 Features

  * Interact with WeChat and ChatGPT:

    * Use ChatGPT on WeChat with [wechaty](https://github.com/wechaty/wechaty) and [Official API](https://openai.com/blog/introducing-chatgpt-and-whisper-apis)
    * Add conversation support
    * Support command setting
  * Deployment and configuration options:

    * Add Dockerfile, deployable with docker
    * Support deployment using docker compose
    * Support Railway and Fly.io deployment
  * Other features:

    * Support [Dall·E](https://labs.openai.com/)
    * Support [whisper](https://openai.com/blog/introducing-chatgpt-and-whisper-apis)
    * Support setting prompt
    * Support proxy (in development)



## 🚀 Usage

  * Use with Railway(PaaS, Free, Stable, ✅Recommended)
  * Use with Fly.io(Paas, Free, ✅Recommended)
  * Use with docker(Self-hosted, Stable, ✅Recommended)
  * Use with docker compose(Self-hosted, Stable, ✅Recommended)
  * Use with nodejs(Self-hosted)



## Use with Railway

> Railway offers $5 or 500 hours of runtime per month

  1. Click the [Railway](https://railway.app/template/dMLG70?referralCode=bIYugQ) button to go to the Railway deployment page
  2. Click the `Deploy Now` button to enter the Railway deployment page
  3. Fill in the repository name and `OPENAI_API_KEY` (need to link GitHub account)
  4. Click the `Deploy` button
  5. Click the `View Logs` button and wait for the deployment to complete



## Use with Fly.io

> Please allocate 512MB memory for the application to meet the application requirements

> fly.io offers free bills up to $5(Free Allowances 3 256MB are not included in the bill)

  1. Install [flyctl](https://fly.io/docs/getting-started/installing-flyctl/)
    
         # macOS
     brew install flyctl
     # Windows
     scoop install flyctl
     # Linux
     curl https://fly.io/install.sh | sh

  2. Clone the project and enter the project directory 
    
        git clone https://github.com/fuergaosi233/wechat-chatgpt.git && cd wechat-chatgpt

  3. Create a new app 
    
        ➜ flyctl launch 
     ? Would you like to copy its configuration to the new app? No
     ? App Name (leave blank to use an auto-generated name): <YOUR APP NAME>
     ? Select region: <YOUR CHOOSE REGION>
     ? Would you like to setup a Postgresql database now? No
     ? Would you like to deploy now? No

  4. Configure the environment variables 
    
        flyctl secrets set OPENAI_API_KEY="<YOUR OPENAI API KEY>" MODEL="<CHATGPT-MODEL>"

  5. Deploy the app 
    
        flyctl deploy




## Use with docker
    
    
    # pull image
    docker pull holegots/wechat-chatgpt
    # run container
    docker run -d --name wechat-chatgpt \
        -e OPENAI_API_KEY=<YOUR OPENAI API KEY> \
        -e MODEL="gpt-3.5-turbo" \
        -e CHAT_PRIVATE_TRIGGER_KEYWORD="" \
        -v $(pwd)/data:/app/data/wechat-assistant.memory-card.json \
        holegots/wechat-chatgpt:latest
    # View the QR code to log in to wechat
    docker logs -f wechat-chatgpt

> How to get OPENAI API KEY? [Click here](https://platform.openai.com/account/api-keys)

## Use with docker compose
    
    
    # Copy the configuration file according to the template
    cp .env.example .env
    # Edit the configuration file
    vim .env
    # Start the container
    docker-compose up -d
    # View the QR code to log in to wechat
    docker logs -f wechat-chatgpt

## Use with nodejs

> You need NodeJS 18.0.0 version and above
    
    
    # Clone the project
    git clone https://github.com/fuergaosi233/wechat-chatgpt.git && cd wechat-chatgpt
    # Install dependencies
    npm install
    # Copy the configuration file according to the template
    cp .env.example .env
    # Edit the configuration file
    vim .env
    # Start project
    npm run dev

> Please make sure your WeChat account can log in [WeChat on web](https://wx.qq.com/)

## 📝 Environment Variables

name | description  
---|---  
API | API endpoint of ChatGPT  
OPENAI_API_KEY | [create new secret key](https://platform.openai.com/account/api-keys)  
MODEL | ID of the model to use. Currently, only gpt-3.5-turbo and gpt-3.5-turbo-0301 are supported.  
TEMPERATURE | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.  
CHAT_TRIGGER_RULE | Private chat triggering rules.  
DISABLE_GROUP_MESSAGE | Prohibited to use ChatGPT in group chat.  
CHAT_PRIVATE_TRIGGER_KEYWORD | Keyword to trigger ChatGPT reply in WeChat private chat  
BLOCK_WORDS | Chat blocker words, (works for both private and group chats, Use, Split)  
CHATGPT_BLOCK_WORDS | The blocked words returned by ChatGPT(works for both private and group chats, Use, Split)  
  
## 📝 Using Custom ChatGPT API

> <https://github.com/fuergaosi233/openai-proxy>
    
    
    # Clone the project
    git clone https://github.com/fuergaosi233/openai-proxy
    # Install dependencies
    npm install && npm install -g wrangler && npm run build
    # Deploy to CloudFlare Workers
    npm run deploy
    # Custom domain (optional)
    Add `Route` to `wrangler.toml`
    routes = [
        { pattern = "Your Custom Domain", custom_domain = true },
    ]

## ⌨️ Commands

> Enter in the WeChat chat box
    
    
    /cmd help # Show help
    /cmd prompt <PROMPT> # Set prompt
    /cmd clear # Clear all sessions since last boot

## ✨ Contributor

[ ![](https://camo.githubusercontent.com/b19b8707f274c58336e25dad9d484df8df14824d7c022e50bab8d641c5557187/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d6675657267616f73693233332f7765636861742d63686174677074) ](https://github.com/fuergaosi233/wechat-chatgpt/graphs/contributors)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!  
Feel free to check [issues page](https://github.com/fuergaosi233/wechat-chatgpt/issues).

## Show your support

Give a ⭐️ if this project helped you!

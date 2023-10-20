ChatGPT-API Demo Running Locally Pre environment Getting Started Deploy Deploy With Vercel 🔒 Need website password? Deploy With Netlify Deploy with Docker Deploy on more servers Environment Variables Frequently Asked Questions Contributing License

##  README.md

[![](https://camo.githubusercontent.com/37c87b74ea23d85c3d75b984e3f65b2a99ace27f5450bb1d3bdc4c2d245868a6/68747470733a2f2f636c6f75642d757079756e2e646469752e736974652f706963747572652f323032332f30342f31352f7841653064592e706e67)](https://v2.chatgpt.ddiu.me)

> We are working on V2 Version! Preview & more info on [#247](https://github.com/ddiu8081/chatgpt-demo/discussions/247).

# ChatGPT-API Demo

English | [简体中文](/ddiu8081/chatgpt-demo/blob/main/README.zh-CN.md)

A demo repo based on [OpenAI GPT-3.5 Turbo API.](https://platform.openai.com/docs/guides/chat)

**🍿 Live preview**: <https://chatgpt.ddiu.me>

**🏖️ V2 Version(Beta)**: <https://v2.chatgpt.ddiu.me>

> ⚠️ Notice: Our API Key limit has been exhausted. So the demo site is not available now.

[![chat-logo](https://camo.githubusercontent.com/87fde0adf3cbf79cb77a0cfbf586618e6772aabb02775f1d1feef4177227ab91/68747470733a2f2f63646e2e737461746963616c792e636f6d2f67682f797a683939303931382f737461746963406d61737465722f636861742d6c6f676f2e77656270)](https://camo.githubusercontent.com/87fde0adf3cbf79cb77a0cfbf586618e6772aabb02775f1d1feef4177227ab91/68747470733a2f2f63646e2e737461746963616c792e636f6d2f67682f797a683939303931382f737461746963406d61737465722f636861742d6c6f676f2e77656270)

## Running Locally

### Pre environment

  1. **Node** : Check that both your development environment and deployment environment are using `Node v18` or later. You can use [nvm](https://github.com/nvm-sh/nvm) to manage multiple `node` versions locally。 
    
         node -v

  2. **PNPM** : We recommend using [pnpm](https://pnpm.io/) to manage dependencies. If you have never installed pnpm, you can install it with the following command: 
    
         npm i -g pnpm

  3. **OPENAI_API_KEY** : Before running this application, you need to obtain the API key from OpenAI. You can register the API key at <https://beta.openai.com/signup>.



### Getting Started

  1. Install dependencies 
    
         pnpm install

  2. Copy the `.env.example` file, then rename it to `.env`, and add your [OpenAI API key](https://platform.openai.com/account/api-keys) to the `.env` file. 
    
         OPENAI_API_KEY=sk-xxx...

  3. Run the application, the local project runs on `http://localhost:3000/`
    
         pnpm run dev




## Deploy

### Deploy With Vercel

[![Deploy with Vercel](https://camo.githubusercontent.com/5e471e99e8e022cf454693e38ec843036ec6301e27ee1e1fa10325b1cb720584/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fddiu8081%2Fchatgpt-demo&env=OPENAI_API_KEY&envDescription=OpenAI%20API%20Key&envLink=https%3A%2F%2Fplatform.openai.com%2Faccount%2Fapi-keys)

> #### 🔒 Need website password?
> 
> Deploy with the `SITE_PASSWORD`
> 
> [![Deploy with Vercel](https://camo.githubusercontent.com/5e471e99e8e022cf454693e38ec843036ec6301e27ee1e1fa10325b1cb720584/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fddiu8081%2Fchatgpt-demo&env=OPENAI_API_KEY&env=SITE_PASSWORD&envDescription=OpenAI%20API%20Key&envLink=https%3A%2F%2Fplatform.openai.com%2Faccount%2Fapi-keys)

[![image](https://camo.githubusercontent.com/f77b36f89c3009e372393a0f11d533adc03db5fe10a17d67317527b9da045413/68747470733a2f2f63646e2e737461746963616c792e636f6d2f67682f797a683939303931382f737461746963406d61737465722f32303233303331302f696d6167652e34777a666237397174376b302e77656270)](https://camo.githubusercontent.com/f77b36f89c3009e372393a0f11d533adc03db5fe10a17d67317527b9da045413/68747470733a2f2f63646e2e737461746963616c792e636f6d2f67682f797a683939303931382f737461746963406d61737465722f32303233303331302f696d6167652e34777a666237397174376b302e77656270)

### Deploy With Netlify

[![Deploy with Netlify](https://camo.githubusercontent.com/417d890ba67c98ad5856b715343a61cdbf07d72b9bd5b79dd45d43de634c29ea/68747470733a2f2f7777772e6e65746c6966792e636f6d2f696d672f6465706c6f792f627574746f6e2e737667)](https://app.netlify.com/start/deploy?repository=https://github.com/ddiu8081/chatgpt-demo#OPENAI_API_KEY=&HTTPS_PROXY=&OPENAI_API_BASE_URL=&HEAD_SCRIPTS=&PUBLIC_SECRET_KEY=&OPENAI_API_MODEL=&SITE_PASSWORD=)

**Step-by-step deployment tutorial:**

  1. [Fork](https://github.com/ddiu8081/chatgpt-demo/fork) this project，Go to <https://app.netlify.com/start> new Site, select the project you `forked` done, and connect it with your `GitHub` account.



[![image](https://camo.githubusercontent.com/0e17b2f5c7e017f05411feaa915c327a37726c6931f80c9c7dadcc4027c7d40f/68747470733a2f2f63646e2e737461746963616c792e636f6d2f67682f797a683939303931382f737461746963406d61737465722f32303233303331302f696d6167652e336e6c743468677a6231366f2e77656270)](https://camo.githubusercontent.com/0e17b2f5c7e017f05411feaa915c327a37726c6931f80c9c7dadcc4027c7d40f/68747470733a2f2f63646e2e737461746963616c792e636f6d2f67682f797a683939303931382f737461746963406d61737465722f32303233303331302f696d6167652e336e6c743468677a6231366f2e77656270)

[![image](https://camo.githubusercontent.com/fe6a0edec4f10c64d3fd47f5bfc5ffac83895162ba73af6b6c115ab2ae111d15/68747470733a2f2f63646e2e737461746963616c792e636f6d2f67682f797a683939303931382f737461746963406d61737465722f32303233303331302f696d6167652e356668666f756170323730672e77656270)](https://camo.githubusercontent.com/fe6a0edec4f10c64d3fd47f5bfc5ffac83895162ba73af6b6c115ab2ae111d15/68747470733a2f2f63646e2e737461746963616c792e636f6d2f67682f797a683939303931382f737461746963406d61737465722f32303233303331302f696d6167652e356668666f756170323730672e77656270)

  2. Select the branch you want to deploy, then configure environment variables in the project settings.



[![image](https://camo.githubusercontent.com/76b0f1b5a099b680288d86f9a5e30c628511ed81f74c5bf84e1d2af6e2778641/68747470733a2f2f63646e2e737461746963616c792e636f6d2f67682f797a683939303931382f737461746963406d61737465722f32303233303331312f696d6167652e676673396c7838633835342e77656270)](https://camo.githubusercontent.com/76b0f1b5a099b680288d86f9a5e30c628511ed81f74c5bf84e1d2af6e2778641/68747470733a2f2f63646e2e737461746963616c792e636f6d2f67682f797a683939303931382f737461746963406d61737465722f32303233303331312f696d6167652e676673396c7838633835342e77656270)

  3. Select the default build command and output directory, Click the `Deploy Site` button to start deploying the site。



[![image](https://camo.githubusercontent.com/deed7afcba0392b6ffcbdffa715f9bd42948b953c1c7a852ad89642ab9d7e94e/68747470733a2f2f63646e2e737461746963616c792e636f6d2f67682f797a683939303931382f737461746963406d61737465722f32303233303331312f696d6167652e346a6b7939653177626f6a6b2e77656270)](https://camo.githubusercontent.com/deed7afcba0392b6ffcbdffa715f9bd42948b953c1c7a852ad89642ab9d7e94e/68747470733a2f2f63646e2e737461746963616c792e636f6d2f67682f797a683939303931382f737461746963406d61737465722f32303233303331312f696d6167652e346a6b7939653177626f6a6b2e77656270)

### Deploy with Docker

Environment variables refer to the documentation below. [Docker Hub address](https://hub.docker.com/r/ddiu8081/chatgpt-demo).

**Direct run**
    
    
    docker run --name=chatgpt-demo -e OPENAI_API_KEY=YOUR_OPEN_API_KEY -p 3000:3000 -d ddiu8081/chatgpt-demo:latest

`-e` define environment variables in the container.

**Docker compose**
    
    
    version: '3'
    
    services:
      chatgpt-demo:
        image: ddiu8081/chatgpt-demo:latest
        container_name: chatgpt-demo
        restart: always
        ports:
          - '3000:3000'
        environment:
          - OPENAI_API_KEY=YOUR_OPEN_API_KEY
          # - HTTPS_PROXY=YOUR_HTTPS_PROXY
          # - OPENAI_API_BASE_URL=YOUR_OPENAI_API_BASE_URL
          # - HEAD_SCRIPTS=YOUR_HEAD_SCRIPTS
          # - PUBLIC_SECRET_KEY=YOUR_SECRET_KEY
          # - SITE_PASSWORD=YOUR_SITE_PASSWORD
          # - OPENAI_API_MODEL=YOUR_OPENAI_API_MODEL
    
    
    # start
    docker compose up -d
    # down
    docker-compose down

### Deploy on more servers

Please refer to the official deployment documentation：<https://docs.astro.build/en/guides/deploy>

## Environment Variables

You can control the website through environment variables.

Name | Description | Default  
---|---|---  
`OPENAI_API_KEY` | Your API Key for OpenAI. | `null`  
`HTTPS_PROXY` | Provide proxy for OpenAI API. e.g. `http://127.0.0.1:7890` | `null`  
`OPENAI_API_BASE_URL` | Custom base url for OpenAI API. | `https://api.openai.com`  
`HEAD_SCRIPTS` | Inject analytics or other scripts before `</head>` of the page | `null`  
`PUBLIC_SECRET_KEY` | Secret string for the project. Use for generating signatures for API calls | `null`  
`SITE_PASSWORD` | Set password for site, support multiple password separated by comma. If not set, site will be public | `null`  
`OPENAI_API_MODEL` | ID of the model to use. [List models](https://platform.openai.com/docs/api-reference/models/list) | `gpt-3.5-turbo`  
  
## Frequently Asked Questions

Q: TypeError: fetch failed (can't connect to OpenAI Api)

A: Configure environment variables `HTTPS_PROXY`，reference: [#34](https://github.com/ddiu8081/chatgpt-demo/issues/34)

Q: throw new TypeError(${context} is not a ReadableStream.)

A: The Node version needs to be `v18` or later，reference: [#65](https://github.com/ddiu8081/chatgpt-demo/issues/65)

Q: Accelerate domestic access without the need for proxy deployment tutorial?

A: You can refer to this tutorial: [#270](https://github.com/ddiu8081/chatgpt-demo/discussions/270)

Q: `PWA` is not working?

A: Current `PWA` does not support deployment on Netlify, you can choose vercel or node deployment.

## Contributing

This project exists thanks to all those who contributed.

Thank you to all our supporters!🙏

[![img](https://camo.githubusercontent.com/e210d41844fd5f15345cefc0443fa2bd6c72a31b6344f6effca99447ce00941c/68747470733a2f2f636f6e7472696275746f72732e6e6e2e63692f6170693f7265706f3d64646975383038312f636861746770742d64656d6f)](https://github.com/ddiu8081/chatgpt-demo/graphs/contributors)

## License

MIT © [ddiu8081](https://github.com/ddiu8081/chatgpt-demo/blob/main/LICENSE)

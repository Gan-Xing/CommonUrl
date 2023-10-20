Introduction Quick jump Deploy on your server 1\. Pull this repo to the local 2\. Installations 3\. Build 4\. Running Services Deploy on Zeabur Deploy on Vercel How to use

##  README.md

[![Banner](/imyuanx/chatgpt-proxy/raw/main/public/chatgpt-proxy-banner.png)](/imyuanx/chatgpt-proxy/blob/main/public/chatgpt-proxy-banner.png)

One-click deployment of the ChatGPT private proxy, power by Next.js, support SSE!

English | [简体中文](/imyuanx/chatgpt-proxy/blob/main/README-CN.md)

## Introduction

This project is based on Next.js, use Rewriter to complete proxy function, only [2 lines](https://github.com/imyuanx/chatgpt-proxy/blob/main/next.config.js#L7-L8) of core code, combining Zeabur or Vercel can easily host your private proxy service

Before you start, you'd better check the How to use section to determine whether this project is applicable to you

ps: The SSE part of the code from [chatgptProxyAPI](https://github.com/x-dr/chatgptProxyAPI)

## Quick jump

  * Deploy on your server
  * ~~Deploy on Zeabur~~
  * ~~Deploy on Vercel~~
  * How to use



## Deploy on your server

> You must have a server and make sure your server can access ChatGPT
> 
> You need some knowledge about [Docker](https://www.docker.com/)

  1. Fork this repository for your own repository



[![fork](/imyuanx/chatgpt-proxy/raw/main/public/frok.png)](/imyuanx/chatgpt-proxy/blob/main/public/frok.png)

  2. Switch to the your forked project directory and run `docker build -t chatgpt-proxy .`

  3. then run `docker run --name chatgpt-proxy -d -p 8000:3000 chatgpt-proxy`

  4. open `http://127.0.0.1:8000` on your browser




If you don't use Docker, you can also manually deploy it

Steps for manually deploy

> Your nodejs version needs to be greater than or equal to 14

#### 1\. Pull this repo to the local
    
    
    $ git pull https://github.com/imyuanx/chatgpt-proxy
    $ cd chatgpt-proxy

#### 2\. Installations
    
    
    $ pnpm install

#### 3\. Build
    
    
    $ pnpm build

#### 4\. Running Services
    
    
    $ pnpm start

## Deploy on Zeabur

> ❗️⚠️❗️ **Warning: This project may violate the`Never Fair Use - Proxies and VPNs` entries under the Zeabur Terms of Use. Zeabur hosting this project is strongly not recommended!**
> 
> ❗️⚠️❗️ **Warning: If your account is punished due to the deployment of this project to Zeabur, please bear the consequences**

Steps for deployment

> ❗️⚠️❗️ **Assuming that you have completely read the warning information and understand the possible risks and consequences, you can still continue to complete the deployment**

Specific operations are as follows

  1. Fork this repository for your own repository

[![fork](/imyuanx/chatgpt-proxy/raw/main/public/frok.png)](/imyuanx/chatgpt-proxy/blob/main/public/frok.png)

  2. Add a new service on [Zeabur](https://zeabur.com) console

[![step 1](/imyuanx/chatgpt-proxy/raw/main/public/zeabur.png)](/imyuanx/chatgpt-proxy/blob/main/public/zeabur.png)

  3. Add service and deploy from source code

[![step 2](/imyuanx/chatgpt-proxy/raw/main/public/zeabur-1.png)](/imyuanx/chatgpt-proxy/blob/main/public/zeabur-1.png) [![step 2-1](/imyuanx/chatgpt-proxy/raw/main/public/zeabur-1-1.png)](/imyuanx/chatgpt-proxy/blob/main/public/zeabur-1-1.png)

  4. Select your forked repo

[![step 3](/imyuanx/chatgpt-proxy/raw/main/public/zeabur-2.png)](/imyuanx/chatgpt-proxy/blob/main/public/zeabur-2.png)

  5. Select main and deploy

[![step 4](/imyuanx/chatgpt-proxy/raw/main/public/zeabur-3.png)](/imyuanx/chatgpt-proxy/blob/main/public/zeabur-3.png)

  6. After the deployment is successful, Generate the domain name.

[![step 5](/imyuanx/chatgpt-proxy/raw/main/public/zeabur-4.png)](/imyuanx/chatgpt-proxy/blob/main/public/zeabur-4.png)

  7. Finally get your service

[![step 6](/imyuanx/chatgpt-proxy/raw/main/public/zeabur-5.png)](/imyuanx/chatgpt-proxy/blob/main/public/zeabur-5.png)

## Deploy on Vercel

> ❗️⚠️❗️ **Warning: This project may violate the[Never Fair Use - Proxies and VPNs](https://vercel.com/docs/concepts/limits/fair-use-policy#never-fair-use) entries under the Vercel Terms of Use. Vercel hosting this project is strongly not recommended!**
> 
> ❗️⚠️❗️ **Warning: If your account is punished due to the deployment of this project to Vercel, please bear the consequences**

Steps for deployment

> ❗️⚠️❗️ **Assuming that you have completely read the warning information and understand the possible risks and consequences, you can still continue to complete the deployment**

If you use Vercel deploy services, you must [custom domain name](https://vercel.com/docs/concepts/get-started/assign-domain), beacuse the [custom domain name](https://vercel.com/docs/concepts/get-started/assign-domain) is not affected by the GFW, Specific operations are as follows

[![Deploy to Vercel](https://camo.githubusercontent.com/5e471e99e8e022cf454693e38ec843036ec6301e27ee1e1fa10325b1cb720584/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/import/project?template=https://github.com/imyuanx/chatgpt-proxy)

  1. Click the deploy button at the top

[![One-click deploy](/imyuanx/chatgpt-proxy/raw/main/public/vercel.png)](/imyuanx/chatgpt-proxy/blob/main/public/vercel.png)

  2. After deployment, the repository will be forked automatically for you, entering a custom repository name in the input field

[![Deploy](/imyuanx/chatgpt-proxy/raw/main/public/vercel-deploy.png)](/imyuanx/chatgpt-proxy/blob/main/public/vercel-deploy.png)

  3. After successful deployment, get your service

[![Alt text](/imyuanx/chatgpt-proxy/raw/main/public/vercel-success.png)](/imyuanx/chatgpt-proxy/blob/main/public/vercel-success.png)

  4. You must add a custom domain name for your service, otherwise you will not be able to access your service in the country

[![Domain](/imyuanx/chatgpt-proxy/raw/main/public/vercel-domain.png)](/imyuanx/chatgpt-proxy/blob/main/public/vercel-domain.png)

## How to use

Whether you use Zeabur or Vercel, you will get the following proxy service after deployment

[![Proxy service](/imyuanx/chatgpt-proxy/raw/main/public/proxy.png)](/imyuanx/chatgpt-proxy/blob/main/public/proxy.png)

The resulting two addresses will be fully forwarded to `https://api.openai.com` and both will be domestically accessible, where `.../proxy-sse` supports SSE

You can use the proxy service in applications that support custom apis to invoke the "openai" interface domestically

Fro example, [openai-translator](https://github.com/yetone/openai-translator):

[![Alt text](/imyuanx/chatgpt-proxy/raw/main/public/openai-translator.png)](/imyuanx/chatgpt-proxy/blob/main/public/openai-translator.png)

Back to top

Demo 演示站为公共服务，如有大规模使用需求请自行部署，演示站有点不堪重负 1、利用Cloudflare Worker中转api.openai.com 2、使用CloudFlare Pages进行中转 3、利用nextjs edge中转api.openai.com 利用Cloudflare pages部署 docker 部署（要境外vps） 使用 用法 Star History

##  README.md

### Demo

<https://chatai.1rmb.tk>

> api
    
    
    https://openai.1rmb.tk

或
    
    
    https://openai-proxy-api.pages.dev/api

### 演示站为公共服务，如有大规模使用需求请自行部署，演示站有点不堪重负

[![worker](/x-dr/chatgptProxyAPI/raw/main/docs/img/worker.png)](/x-dr/chatgptProxyAPI/blob/main/docs/img/worker.png)

## 1、利用Cloudflare Worker中转api.openai.com

  1. 新建一个 Cloudflare Worker
  2. 复制 [cf_worker.js](https://cdn.jsdelivr.net/gh/x-dr/chatgptProxyAPI@main/cf_worker.js) 里的代码粘贴到 Worker 中并部署
  3. 给 Worker 绑定一个没有被墙的域名
  4. 使用自己的域名代替 api.openai.com



**[详细教程](/x-dr/chatgptProxyAPI/blob/main/docs/cloudflare_workers.md)**

## 2、使用CloudFlare Pages进行中转

**[详细教程](/x-dr/chatgptProxyAPI/blob/main/docs/cloudflare_proxy_pages.md)**

## 3、利用nextjs edge中转api.openai.com

### 利用Cloudflare pages部署

> [官方文档](https://developers.cloudflare.com/pages/framework-guides/deploy-a-nextjs-site/)

  1. ~~Fork本项目~~ 点击[Use this template](https://github.com/x-dr/chatgptProxyAPI/generate)按钮创建一个新的代码库。
  2. 登录到[Cloudflare](https://dash.cloudflare.com/)控制台.
  3. 在帐户主页中，选择`pages`> ` Create a project` > `Connect to Git`
  4. 选择你 Fork 的项目存储库，在`Set up builds and deployments`部分中，选择`Next.js`作为您的框架预设。您的选择将提供以下信息。



> 一般默认即可

Configuration option | Value  
---|---  
Production branch | main  
Framework preset | next.js  
Build command | npx @cloudflare/next-on-pages --experimental-minify  
Build directory | .vercel/output/static  
  
> 在 `Environment variables (advanced)`添加一个参数

Variable name | Value  
---|---  
NODE_VERSION | 16  
  
  5. 点击`Save and Deploy`部署，然后点`Continue to project`即可看到访问域名



> 把官方接口的`https://api.openai.com`替换为`https://xxx.pages.dev/api` 即可 (<https://xxx.pages.dev/api> 为你的域名)

_注意路径多了一个`api`_

**[详细教程](/x-dr/chatgptProxyAPI/blob/main/docs/cloudflare_pages.md)**

### docker 部署（要境外vps）

> 好像不支持sse 所以不建议

e.g.
    
    
    docker run -itd --name openaiproxy \
                -p 3000:3000 \
                --restart=always \
               gindex/openaiproxy:latest

#### 使用

_api :<http://vpsip:3000/proxy/v1/chat/completions>_
    
    
    curl --location 'http://vpsip:3000/proxy/v1/chat/completions' \
    --header 'Authorization: Bearer sk-xxxxxxxxxxxxxxx' \
    --header 'Content-Type: application/json' \
    --data '{
       "model": "gpt-3.5-turbo",
      "messages": [{"role": "user", "content": "Hello!"}]
     }'
    

## 用法

JavaScript用fetch
    
    
    const requestOptions = {
        method: 'POST',
        headers: {
            "Authorization": "Bearer sk-xxxxxxxxxxxx",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": "hello word"
                }
            ]
        })
    };
    
    fetch("https://openai.1rmb.tk/v1/chat/completions", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
      

用python
    
    
    import requests
    
    url = "https://openai.1rmb.tk/v1/chat/completions"
    api_key = 'sk-xxxxxxxxxxxxxxxxxxxx'
    
    headers = {
      'Authorization': f'Bearer {api_key}',
      'Content-Type': 'application/json'
    }
    
    payload = {
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "user",
          "content": "hello word"
        }
      ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status() # 抛出异常，如果响应码不是200
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
    except json.JSONDecodeError as e:
        print(f"无效的 JSON 响应: {e}")

用nodejs chatgpt库

[transitive-bullshit/chatgpt-api](https://github.com/transitive-bullshit/chatgpt-api)
    
    
    import { ChatGPTAPI } from 'chatgpt'
    
    async function example() {
      const api = new ChatGPTAPI({
        apiKey: "sk-xxxxxxxxxxxxxx",
      // proxy+/v1
        apiBaseUrl:"https://openai.1rmb.tk/v1"
    
    
      })
    
      const res = await api.sendMessage('Hello World!')
      console.log(res.text)
    }
    
    example()

查询余额
    
    
        const headers = {
          'content-type': 'application/json',
          'Authorization': `Bearer sk-xxxxxxxxxxxxxxxxx`
        }
        // 查是否订阅
        const subscription = await fetch("https://openai.1rmb.tk/v1/dashboard/billing/subscription", {
          method: 'get',
          headers: headers
        })
        if (!subscription.ok) {
          const data = await subscription.json()
          // console.log(data);
          return data
          // throw new Error('API request failed')
        } else {
          const subscriptionData = await subscription.json()
          const endDate = subscriptionData.access_until
          const startDate = new Date(endDate - 90 * 24 * 60 * 60);
          console.log(formatDate(endDate, "YYYY-MM-DD"));
          console.log(formatDate(startDate, "YYYY-MM-DD"));
          const response = await fetch(`https://openai.1rmb.tk/v1/dashboard/billing/usage?start_date=${formatDate(startDate, "YYYY-MM-DD")}&end_date=${formatDate(endDate, "YYYY-MM-DD")}`, {
            method: 'get',
            headers: headers
          })
          
          const usageData = await response.json();
          // 账号类型
          const plan = subscriptionData.plan.id
          console.log(usageData);
          }

## Star History

[![Star History Chart](https://camo.githubusercontent.com/95d6ea2a40ee69d3e9fccd74e6e24e5b3ccbe5c3996760c5f5e936691cfba256/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d782d64722f6368617467707450726f787941504926747970653d44617465)](https://star-history.com/#x-dr/chatgptProxyAPI&Date)

ChatGPT Java API 项目合作洽谈请联系微信 plexpt（在微信里自行搜索并添加好友，请注明来意，如有关于仓库问题需讨论请参考下文入群讨论，不要加此微信）。 QQ群：645132635 免费5刀的帐号已被限速，回答龟速，需要不限速的可购买ChatGPT120美金额度成品独享帐号：购买 问题表 功能特性 PRO版 使用指南 最简使用 进阶使用 流式使用 流式配合Spring SseEmitter使用 多KEY自动轮询 上下文 常见问题 注册教程 另外请看看我的另一个项目 ChatGPT中文使用指南 云服务器 Star History

##  README.md

# ChatGPT Java API

[![stable](https://camo.githubusercontent.com/b82d4dd001fd2a41d0624bbe0bb5b77d0e58d66f5ad57a71efe37813edee52b0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73746162696c6974792d737461626c652d627269676874677265656e2e737667)](https://camo.githubusercontent.com/b82d4dd001fd2a41d0624bbe0bb5b77d0e58d66f5ad57a71efe37813edee52b0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73746162696c6974792d737461626c652d627269676874677265656e2e737667) [![Maven Central](https://camo.githubusercontent.com/caa0c40ac16a1177a533a5fa75b4c89a33b404f7550490bcdc55075cc8629c01/68747470733a2f2f696d672e736869656c64732e696f2f6d6176656e2d63656e7472616c2f762f636f6d2e6769746875622e706c657870742f63686174677074)](https://maven-badges.herokuapp.com/maven-central/com.github.plexpt/chatgpt)

[English Doc](https://github.com/PlexPt/chatgpt-java/blob/main/README_en.md).

OpenAI ChatGPT 的SDK。觉得不错请右上角Star

感谢 [revChatGPT](https://github.com/acheong08/ChatGPT).

#### 项目合作洽谈请联系微信 plexpt（在微信里自行搜索并添加好友，请注明来意，如有关于仓库问题需讨论请参考下文入群讨论，不要加此微信）。

### QQ群：645132635

### 免费5刀的帐号已被限速，回答龟速，需要不限速的可购买 **ChatGPT** 120美金额度成品独享帐号：[购买](https://fk.fq.mk/?code=YT0xJmI9MjU%3D)

# 问题表

[共约67万个问题，欢迎拿去炼丹](https://github.com/PlexPt/awesome-chatgpt-prompts-zh/blob/main/question/README.md)

点击👇🏻传送链接，购买云服务器炼丹：

  * [**阿里云服务器**](https://51015.cn/ss/3vpds)
  * [**【腾讯云】云服务器，低至4.2元/月**](https://url.cn/B7m0OYnG)



# 功能特性

功能 | 特性  
---|---  
GPT 3.5 | 支持  
GPT 4.0 | 支持  
GPT 4.0-32k | 支持  
流式对话 | 支持  
阻塞式对话 | 支持  
前端 | 无  
上下文 | 支持  
计算Token | [用jtokkit](https://github.com/knuddelsgmbh/jtokkit)  
多KEY轮询 | 支持  
代理 | 支持  
反向代理 | 支持  
  
# PRO版

如需使用，请购买。

| 开源免费版 | PRO版 | PRO MAX版  
---|---|---|---  
价格 | 开源免费 | 299 | 399  
简介 |  | 开源版+前端+1对1指导 | 网页逆向版+1对1指导  
地址 | 本仓库 | [购买](https://fk.fq.mk/?code=YT0yJmI9Nw%3D%3D) [演示站](https://javachat.plexpt.com) | [购买](https://fk.fq.mk/?code=YT0yJmI9OA%3D%3D)  
GPT 4.0 | 支持 | 支持 | 支持  
优势 | 免费 | 有前端，稳定，+专业指导 | 满血网页逆向版+专业指导  
1对1指导 | 无 | 有 | 有  
登录方式 | APIKEY | APIKEY | sessionToken、邮箱密码  
使用方式 | Java API | Java API + 在线 | Java API  
前端 | 无 | 有（HTML5 + SSE） | 无  
  
[![image](https://user-images.githubusercontent.com/15922823/206353660-47d99158-a664-4ade-b2f1-e2cc8ac68b74.png)](https://user-images.githubusercontent.com/15922823/206353660-47d99158-a664-4ade-b2f1-e2cc8ac68b74.png)

[![image](https://user-images.githubusercontent.com/15922823/206615422-23c5e587-d29a-4f04-8d0d-f8dd7c19da37.png)](https://user-images.githubusercontent.com/15922823/206615422-23c5e587-d29a-4f04-8d0d-f8dd7c19da37.png)

## 使用指南

最新版本 [![Maven Central](https://camo.githubusercontent.com/caa0c40ac16a1177a533a5fa75b4c89a33b404f7550490bcdc55075cc8629c01/68747470733a2f2f696d672e736869656c64732e696f2f6d6176656e2d63656e7472616c2f762f636f6d2e6769746875622e706c657870742f63686174677074)](https://maven-badges.herokuapp.com/maven-central/com.github.plexpt/chatgpt)

maven
    
    
    <dependency>
        <groupId>com.github.plexpt</groupId>
        <artifactId>chatgpt</artifactId>
        <version>4.0.5</version>
    </dependency>
    

gradle
    
    
    implementation group: 'com.github.plexpt', name: 'chatgpt', version: '4.0.5'
    

### 最简使用

也可以使用这个类进行测试 [ConsoleChatGPT](/PlexPt/chatgpt-java/blob/main/src/main/java/com/plexpt/chatgpt/ConsoleChatGPT.java)
    
    
          //国内需要代理
          Proxy proxy = Proxys.http("127.0.0.1", 1081);
         //socks5 代理
        // Proxy proxy = Proxys.socks5("127.0.0.1", 1080);
    
          ChatGPT chatGPT = ChatGPT.builder()
                    .apiKey("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")
                    .proxy(proxy)
                    .apiHost("https://api.openai.com/") //反向代理地址
                    .build()
                    .init();
                    
            String res = chatGPT.chat("写一段七言绝句诗，题目是：火锅！");
            System.out.println(res);

### 进阶使用
    
    
          //国内需要代理 国外不需要
          Proxy proxy = Proxys.http("127.0.0.1", 1080);
    
          ChatGPT chatGPT = ChatGPT.builder()
                    .apiKey("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")
                    .proxy(proxy)
                    .timeout(900)
                    .apiHost("https://api.openai.com/") //反向代理地址
                    .build()
                    .init();
         
            Message system = Message.ofSystem("你现在是一个诗人，专门写七言绝句");
            Message message = Message.of("写一段七言绝句诗，题目是：火锅！");
    
            ChatCompletion chatCompletion = ChatCompletion.builder()
                    .model(ChatCompletion.Model.GPT_3_5_TURBO.getName())
                    .messages(Arrays.asList(system, message))
                    .maxTokens(3000)
                    .temperature(0.9)
                    .build();
            ChatCompletionResponse response = chatGPT.chatCompletion(chatCompletion);
            Message res = response.getChoices().get(0).getMessage();
            System.out.println(res);

### 流式使用
    
    
          //国内需要代理 国外不需要
          Proxy proxy = Proxys.http("127.0.0.1", 1080);
    
          ChatGPTStream chatGPTStream = ChatGPTStream.builder()
                    .timeout(600)
                    .apiKey("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")
                    .proxy(proxy)
                    .apiHost("https://api.openai.com/")
                    .build()
                    .init();
    
                    
            ConsoleStreamListener listener = new ConsoleStreamListener();
            Message message = Message.of("写一段七言绝句诗，题目是：火锅！");
            ChatCompletion chatCompletion = ChatCompletion.builder()
                    .messages(Arrays.asList(message))
                    .build();
            chatGPTStream.streamChatCompletion(chatCompletion, listener);

### 流式配合Spring SseEmitter使用

参考 [SseStreamListener](/PlexPt/chatgpt-java/blob/main/src/main/java/com/plexpt/chatgpt/listener/SseStreamListener.java)
    
    
      
    
        @GetMapping("/chat/sse")
        @CrossOrigin
        public SseEmitter sseEmitter(String prompt) {
           //国内需要代理 国外不需要
           Proxy proxy = Proxys.http("127.0.0.1", 1080);
    
           ChatGPTStream chatGPTStream = ChatGPTStream.builder()
                    .timeout(600)
                    .apiKey("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")
                    .proxy(proxy)
                    .apiHost("https://api.openai.com/")
                    .build()
                    .init();
            
            SseEmitter sseEmitter = new SseEmitter(-1L);
    
            SseStreamListener listener = new SseStreamListener(sseEmitter);
            Message message = Message.of(prompt);
    
            listener.setOnComplate(msg -> {
                //回答完成，可以做一些事情
            });
            chatGPTStream.streamChatCompletion(Arrays.asList(message), listener);
    
    
            return sseEmitter;
        }

## 多KEY自动轮询

只需替换chatGPT构造部分
    
    
    chatGPT = ChatGPT.builder()
            .apiKeyList(
                   // 从数据库或其他地方取出多个KEY
                    Arrays.asList("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",
                            "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",
                            "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",
                            "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",
                            ))
            .timeout(900)
            .proxy(proxy)
            .apiHost("https://api.openai.com/") //代理地址
            .build()
            .init();
    

## 上下文

参考 [ChatContextHolder.java](/PlexPt/chatgpt-java/blob/main/src/main/java/com/plexpt/chatgpt/util/ChatContextHolder.java)

# 常见问题

问 | 答  
---|---  
KEY从哪来？ | 手动注册生成：ai.com(需要海外手机号)、或者成品独享帐号：[购买](https://fk.fq.mk/?code=YT0xJmI9Mg%3D%3D)  
哪些地区不能用 | **以下国家IP不支持使用：中国(包含港澳台) 俄罗斯 乌克兰 阿富汗 白俄罗斯 委内瑞拉 伊朗 埃及!!**  
有封号风险吗 | 充值的没有。你免费白嫖不封你封谁。  
我是尊贵的Plus会员，能用吗 | 能用，照封不误。PLUS调用API没啥区别  
GPT4.0 怎么用 | 申请 <https://openai.com/waitlist/gpt-4-api>  
api.openai.com ping不通？ | 禁ping，用curl测试连通性  
显示超时？ | IP不好，换个IP  
显示`Your access was terminated due to violation of our policies`... | 你号没了，下一个  
显示`That model is currently overloaded with other requests. You can retry your request` | 模型过载，官方炸了，重试  
生成的图片不能用？ | 图片是它瞎编的，洗洗睡吧  
如何充值？ | 用国外信用卡，国内的不行  
没有国外信用卡怎么办？ | 用这个, 扫码免费开卡并充值[![](/PlexPt/chatgpt-java/raw/main/pic/depay.jpg)](/PlexPt/chatgpt-java/blob/main/pic/depay.jpg)  
返回http 401 | API 密钥写错了/没写  
返回http 429 | 请求超速了，或者官方超载了。充钱可解决  
返回http 500 | 服务器炸了  
|   
  
* * *

### 注册教程

<https://juejin.cn/post/7173447848292253704>

<https://mirror.xyz/boxchen.eth/9O9CSqyKDj4BKUIil7NC1Sa1LJM-3hsPqaeW_QjfFBc>

#### 另外请看看我的另一个项目 [ChatGPT中文使用指南](https://github.com/PlexPt/awesome-chatgpt-prompts-zh)

# 云服务器

点击👇🏻传送链接，购买云服务器：

  * [**阿里云服务器**](https://reurl.cc/NqQXyx)
  * [**【腾讯云】云服务器等爆品抢先购，低至4.2元/月**](https://url.cn/B7m0OYnG)



# Star History

[![Star History Chart](https://camo.githubusercontent.com/9ac970252a09107eeda82df1cf0c4c4606211b1f5ac9600a1b0a95f69563504b/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d506c657850742f636861746770742d6a61766126747970653d44617465)](https://star-history.com/#PlexPt/chatgpt-java&Date)

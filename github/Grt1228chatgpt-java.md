此项目不仅仅支持chat对话模型，支持openai官方所有api，包括 整合Spring Boot 实现CahtGPT对话模式，思路可以参考：https://github.com/Grt1228/chatgpt-steam-output 有bug欢迎朋友们指出，互相学习，所有咨询全部免费。 更新日志 工程简介 快速开始 1、导入pom依赖 2、流式客户端使用示例： 默认OkHttpClient 自定义OkHttpClient客户端使用示例： 3、默认客户端使用示例（支持全部API）： 默认OkHttpClient 自定义OkHttpClient客户端使用示例： 方式二（下载源码直接运行） OpenAI全部接口支持调用 Star History 站在巨人的肩膀 如果项目对你有帮助，可以选择请我喝杯奶茶

##  README.md

it’s an “unofficial" or "community-maintained” library. 这是一个非官方的社区维护的库。

> **原创发布转载注明出处！** 开源协议：[LICENSE](https://github.com/Grt1228/chatgpt-java/blob/main/LICENSE)

**基于本SDK开发案例收集** ：[chatgpt-java SDK案例征集](https://github.com/Grt1228/chatgpt-java/issues/87)

## 此项目不仅仅支持chat对话模型，支持openai官方所有api，包括

  * tokens 计算——[Tokens_README.md](https://github.com/Grt1228/chatgpt-java/blob/main/Tokens_README.md)
  * Billing 余额查询——[OpenAiClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiClientTest.java) 、[OpenAiStreamClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiStreamClientTest.java)
  * Models 模型检索
  * Completions chatgpt对话
  * Images 图片模型
  * Embeddings 模型自定义训练
  * Files 文件上传自定义模型
  * Fine-tune 微调
  * Moderations 文本审核，敏感词鉴别
  * Engines 官方已移除
  * Chat gpt-3.5对话模型
  * Speech To Text 语音转文字，语音翻译



**国内访问可以看下这个解决方案** ：[noobnooc/noobnooc#9](https://github.com/noobnooc/noobnooc/discussions/9)

### 整合Spring Boot 实现CahtGPT对话模式，思路可以参考：<https://github.com/Grt1228/chatgpt-steam-output>

此项目支持两种流式输出有完整示例代码可参考 。

流式输出实现方式 | 小程序 | 安卓 | ios | H5  
---|---|---|---|---  
SSE参考：[OpenAISSEEventSourceListener](https://github.com/Grt1228/chatgpt-steam-output/blob/main/src/main/java/com/unfbx/chatgptsteamoutput/listener/OpenAISSEEventSourceListener.java) | 不支持 | 支持 | 支持 | 支持  
WebSocket参考：[OpenAIWebSocketEventSourceListener](https://github.com/Grt1228/chatgpt-steam-output/blob/main/src/main/java/com/unfbx/chatgptsteamoutput/listener/OpenAIWebSocketEventSourceListener.java) | 支持 | 支持 | 支持 | 支持  
  
### 有bug欢迎朋友们指出，互相学习，所有咨询全部免费。

一起探讨chatgpt-java，SDK问题咨询  
项目产品开发交流 | 群失效关注公众号恢复：chatgpt-java | 个人微信  
---|---|---  
[![二维码](https://user-images.githubusercontent.com/27008803/225246389-7b452214-f3fe-4a70-bd3e-832a0ed34288.jpg)](https://user-images.githubusercontent.com/27008803/225246389-7b452214-f3fe-4a70-bd3e-832a0ed34288.jpg) | [![二维码](https://camo.githubusercontent.com/3d656c81971655d05f212fa3bb86df427305a727f0f5ee76b5d6339cb3e28e44/68747470733a2f2f672d70686f746f2e6f73732d636e2d7368616e676861692e616c6979756e63732e636f6d2f686431352e6a7067)](https://camo.githubusercontent.com/3d656c81971655d05f212fa3bb86df427305a727f0f5ee76b5d6339cb3e28e44/68747470733a2f2f672d70686f746f2e6f73732d636e2d7368616e676861692e616c6979756e63732e636f6d2f686431352e6a7067) | [![二维码](https://user-images.githubusercontent.com/27008803/225246581-15e90f78-5438-4637-8e7d-14c68ca13b59.jpg)](https://user-images.githubusercontent.com/27008803/225246581-15e90f78-5438-4637-8e7d-14c68ca13b59.jpg)  
  
* * *

## 更新日志

  * 1.0.12 tokens计算优化、删除模型接口修改、语音接口更新支持官方最新参数
  * 1.0.11 增加新的余额查询接口参考：[OpenAiClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiClientTest.java) 和[OpenAiStreamClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiStreamClientTest.java) ,修复tokens计算慢的问题，
  * 1.0.10 支持tokens计算：[TikTokensTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/TikTokensTest.java) ，更多详细的资料参考文档：[Tokens_README.md](https://github.com/Grt1228/chatgpt-java/blob/main/Tokens_README.md)
  * 1.0.9 支持自定义key使用策略参考：[OpenAiClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiClientTest.java) 和[OpenAiStreamClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiStreamClientTest.java) ，弃用ChatGPTClient，优化Moderation接口
  * 1.0.8 修改OpenAiClient和OpenAiStreamClient的自定义相关实现，超时设置，代理设置，自定义拦截器设置改为通过自定义OkHttpClient实现，将OkHttpClient交由用户自定义控制更加合理，可以实现更多的参数自定义。支持多Api Keys配置。
  * 1.0.7 修复反序列化报错Bug：[#79](https://github.com/Grt1228/chatgpt-java/issues/79) ，Image SDK枚举值bug：[#76](https://github.com/Grt1228/chatgpt-java/issues/76) ，感谢两位朋友指出：[@CCc3120](https://github.com/CCc3120) 、[@seven-cm](https://github.com/seven-cm)
  * 1.0.6 支持余额查询参考：[OpenAiClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiClientTest.java) 和[OpenAiStreamClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiStreamClientTest.java) creditGrants方法,支持最新GPT-4模型，参考：[ChatCompletion.Model](https://github.com/Grt1228/chatgpt-java/blob/main/src/main/java/com/unfbx/chatgpt/entity/chat/ChatCompletion.java/)构建消息体传入模型即可。感谢群友提供的余额接口地址以及[@PlexPt](https://github.com/PlexPt) 提供的模型参数
  * 1.0.5 支持自定义Api Host，使用Builder构建。参考下面的快速开始部分代码。
  * 1.0.4 官方最新的ChatGPT Stream模式下的Api返回值改动。
  * 1.0.3 支持最新的GPT-3.5-Turbo模型和Whisper-1模型，支持语音功能转文字，语音翻译。OpenAiClient和OpenAiStreamClient支持Builder构造，支持代理。
  * 1.0.2 支持Stream流式输出，参考：OpenAiStreamClient
  * 1.0.1 支持自定义超时时间，自定义OkHttpClient拦截器，参考：OpenAiClient构造函数
  * 1.0.0 支持所有的OpenAI官方接口



* * *

Q | A  
---|---  
如何实现连续对话？ | issues：[#8](https://github.com/Grt1228/chatgpt-java/issues/8)  
如何实现流式输出？ | 升级1.0.2版本，参考源码：[OpenAiStreamClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiStreamClientTest.java/)  
如何整合SpringBoot实现流式输出的Api接口？ | 参考另外一个项目：[chatgpt-steam-output](https://github.com/Grt1228/chatgpt-steam-output)  
最新版GPT-3.5-TURBO是否支持？ | 升级1.0.3 已经支持ChatCompletion, 参考测试案例：[OpenAiStreamClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiStreamClientTest.java/) 和[OpenAiStreamClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiClientTest.java/)  
最新版语言转文字和语言翻译是否支持？ | 升级1.0.3 已经支持whisper参考测试案例：[OpenAiStreamClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiStreamClientTest.java/) 和[OpenAiStreamClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiClientTest.java/)  
  
* * *

# 工程简介

**ChatGPT的Java客户端**

OpenAI官方Api的Java SDK

目前支持api-keys的方式调用，获取api-keys可以百度或者csdn查一下。

**api-keys的方式调用目前需要用梯子才可访问。**

OpenAi官方文档地址：<https://platform.openai.com/docs/api-reference>

# 快速开始

本项目支持 **默认输出** 和 **流式输出**

## 1、导入pom依赖
    
    
    <dependency>
        <groupId>com.unfbx</groupId>
        <artifactId>chatgpt-java</artifactId>
        <version>1.0.12</version>
    </dependency>
    

## 2、流式客户端使用示例：

更多SDK示例参考：[OpenAiStreamClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiStreamClientTest.java)

### 默认OkHttpClient
    
    
    public class Test {
        public static void main(String[] args) {
            OpenAiStreamClient client = OpenAiStreamClient.builder()
                    .apiKey(Arrays.asList("sk-********","sk-********"))
                    //自定义key的获取策略：默认KeyRandomStrategy
                    //.keyStrategy(new KeyRandomStrategy())
                    .keyStrategy(new FirstKeyStrategy())
                    //自己做了代理就传代理地址，没有可不不传
    //                .apiHost("https://自己代理的服务器地址/")
                    .build();
            //聊天模型：gpt-3.5
            ConsoleEventSourceListener eventSourceListener = new ConsoleEventSourceListener();
            Message message = Message.builder().role(Message.Role.USER).content("你好啊我的伙伴！").build();
            ChatCompletion chatCompletion = ChatCompletion.builder().messages(Arrays.asList(message)).build();
            client.streamChatCompletion(chatCompletion, eventSourceListener);
            CountDownLatch countDownLatch = new CountDownLatch(1);
            try {
                countDownLatch.await();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    

### 自定义OkHttpClient客户端使用示例：
    
    
    public class Test {
        public static void main(String[] args) {
            //国内访问需要做代理，国外服务器不需要
            Proxy proxy = new Proxy(Proxy.Type.HTTP, new InetSocketAddress("127.0.0.1", 7890));
            HttpLoggingInterceptor httpLoggingInterceptor = new HttpLoggingInterceptor(new OpenAILogger());
            //！！！！千万别再生产或者测试环境打开BODY级别日志！！！！
            //！！！生产或者测试环境建议设置为这三种级别：NONE,BASIC,HEADERS,！！！
            httpLoggingInterceptor.setLevel(HttpLoggingInterceptor.Level.HEADERS);
            OkHttpClient okHttpClient = new OkHttpClient
                    .Builder()
                    .proxy(proxy)//自定义代理
                    .addInterceptor(httpLoggingInterceptor)//自定义日志
                    .connectTimeout(30, TimeUnit.SECONDS)//自定义超时时间
                    .writeTimeout(30, TimeUnit.SECONDS)//自定义超时时间
                    .readTimeout(30, TimeUnit.SECONDS)//自定义超时时间
                    .build();
            OpenAiStreamClient client = OpenAiStreamClient.builder()
                    .apiKey(Arrays.asList("sk-********","sk-********"))
                    //自定义key的获取策略：默认KeyRandomStrategy
                    //.keyStrategy(new KeyRandomStrategy())
                    .keyStrategy(new FirstKeyStrategy())
                    .okHttpClient(okHttpClient)
                    //自己做了代理就传代理地址，没有可不不传
    //                .apiHost("https://自己代理的服务器地址/")
                    .build();
        }
    }
    

输出日志（text是持续输出的）：
    
    
    23:03:59.158 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI建立sse连接...
    23:03:59.160 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：{"id": "cmpl-6pIHnOOJiiUEVMesXwxzzcSQFoZHj", "object": "text_completion", "created": 1677683039, "choices": [{"text": "\n", "index": 0, "logprobs": null, "finish_reason": null}], "model": "text-davinci-003"}
    23:03:59.172 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：{"id": "cmpl-6pIHnOOJiiUEVMesXwxzzcSQFoZHj", "object": "text_completion", "created": 1677683039, "choices": [{"text": "\n", "index": 0, "logprobs": null, "finish_reason": null}], "model": "text-davinci-003"}
    23:03:59.251 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：{"id": "cmpl-6pIHnOOJiiUEVMesXwxzzcSQFoZHj", "object": "text_completion", "created": 1677683039, "choices": [{"text": "\u5fc3", "index": 0, "logprobs": null, "finish_reason": null}], "model": "text-davinci-003"}
    23:03:59.313 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：{"id": "cmpl-6pIHnOOJiiUEVMesXwxzzcSQFoZHj", "object": "text_completion", "created": 1677683039, "choices": [{"text": "\u60c5", "index": 0, "logprobs": null, "finish_reason": null}], "model": "text-davinci-003"}
    23:03:59.380 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：{"id": "cmpl-6pIHnOOJiiUEVMesXwxzzcSQFoZHj", "object": "text_completion", "created": 1677683039, "choices": [{"text": "\u8212", "index": 0, "logprobs": null, "finish_reason": null}], "model": "text-davinci-003"}
    23:03:59.439 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：{"id": "cmpl-6pIHnOOJiiUEVMesXwxzzcSQFoZHj", "object": "text_completion", "created": 1677683039, "choices": [{"text": "\u7545", "index": 0, "logprobs": null, "finish_reason": null}], "model": "text-davinci-003"}
    23:03:59.532 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：{"id": "cmpl-6pIHnOOJiiUEVMesXwxzzcSQFoZHj", "object": "text_completion", "created": 1677683039, "choices": [{"text": "\uff0c", "index": 0, "logprobs": null, "finish_reason": null}], "model": "text-davinci-003"}
    23:03:59.579 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：{"id": "cmpl-6pIHnOOJiiUEVMesXwxzzcSQFoZHj", "object": "text_completion", "created": 1677683039, "choices": [{"text": "\u5fc3", "index": 0, "logprobs": null, "finish_reason": null}], "model": "text-davinci-003"}
    23:03:59.641 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：{"id": "cmpl-6pIHnOOJiiUEVMesXwxzzcSQFoZHj", "object": "text_completion", "created": 1677683039, "choices": [{"text": "\u65f7", "index": 0, "logprobs": null, "finish_reason": null}], "model": "text-davinci-003"}
    23:03:59.673 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：{"id": "cmpl-6pIHnOOJiiUEVMesXwxzzcSQFoZHj", "object": "text_completion", "created": 1677683039, "choices": [{"text": "\u795e", "index": 0, "logprobs": null, "finish_reason": null}], "model": "text-davinci-003"}
    23:03:59.751 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：{"id": "cmpl-6pIHnOOJiiUEVMesXwxzzcSQFoZHj", "object": "text_completion", "created": 1677683039, "choices": [{"text": "\u6021", "index": 0, "logprobs": null, "finish_reason": null}], "model": "text-davinci-003"}
    23:03:59.782 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：{"id": "cmpl-6pIHnOOJiiUEVMesXwxzzcSQFoZHj", "object": "text_completion", "created": 1677683039, "choices": [{"text": "\u3002", "index": 0, "logprobs": null, "finish_reason": null}], "model": "text-davinci-003"}
    23:03:59.815 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据：[DONE]
    23:03:59.815 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI返回数据结束了
    23:03:59.815 [省略无效信息] INFO com.unfbx.chatgpt.sse.ConsoleEventSourceListener - OpenAI关闭sse连接...
    

## 3、默认客户端使用示例（支持全部API）：

更多SDK示例参考：[OpenAiClientTest](https://github.com/Grt1228/chatgpt-java/blob/main/src/test/java/com/unfbx/chatgpt/OpenAiClientTest.java)

### 默认OkHttpClient
    
    
    public class Test {
        public static void main(String[] args) {
            OpenAiClient openAiClient = OpenAiClient.builder()
                    .apiKey(Arrays.asList("sk-********","sk-********"))
                    //自定义key的获取策略：默认KeyRandomStrategy
                    //.keyStrategy(new KeyRandomStrategy())
                    .keyStrategy(new FirstKeyStrategy())
                    //自己做了代理就传代理地址，没有可不不传
    //                .apiHost("https://自己代理的服务器地址/")
                    .build();
                    //聊天模型：gpt-3.5
            Message message = Message.builder().role(Message.Role.USER).content("你好啊我的伙伴！").build();
            ChatCompletion chatCompletion = ChatCompletion.builder().messages(Arrays.asList(message)).build();
            ChatCompletionResponse chatCompletionResponse = openAiClient.chatCompletion(chatCompletion);
            chatCompletionResponse.getChoices().forEach(e -> {
                System.out.println(e.getMessage());
            });
        }
    }
    

### 自定义OkHttpClient客户端使用示例：
    
    
    public class Test {
        public static void main(String[] args) {
            //国内访问需要做代理，国外服务器不需要
            Proxy proxy = new Proxy(Proxy.Type.HTTP, new InetSocketAddress("127.0.0.1", 7890));
            HttpLoggingInterceptor httpLoggingInterceptor = new HttpLoggingInterceptor(new OpenAILogger());
            //！！！！千万别再生产或者测试环境打开BODY级别日志！！！！
            //！！！生产或者测试环境建议设置为这三种级别：NONE,BASIC,HEADERS,！！！
            httpLoggingInterceptor.setLevel(HttpLoggingInterceptor.Level.HEADERS);
            OkHttpClient okHttpClient = new OkHttpClient
                    .Builder()
                    .proxy(proxy)//自定义代理
                    .addInterceptor(httpLoggingInterceptor)//自定义日志输出
                    .addInterceptor(new OpenAiResponseInterceptor())//自定义返回值拦截
                    .connectTimeout(10, TimeUnit.SECONDS)//自定义超时时间
                    .writeTimeout(30, TimeUnit.SECONDS)//自定义超时时间
                    .readTimeout(30, TimeUnit.SECONDS)//自定义超时时间
                    .build();
            //构建客户端
            OpenAiClient openAiClient = OpenAiClient.builder()
                    .apiKey(Arrays.asList("sk-********","sk-********"))
                    //自定义key的获取策略：默认KeyRandomStrategy
                    //.keyStrategy(new KeyRandomStrategy())
                    .keyStrategy(new FirstKeyStrategy())
                    .okHttpClient(okHttpClient)
                    //自己做了代理就传代理地址，没有可不不传
    //                .apiHost("https://自己代理的服务器地址/")
                    .build();
                    //聊天模型：gpt-3.5
            Message message = Message.builder().role(Message.Role.USER).content("你好啊我的伙伴！").build();
            ChatCompletion chatCompletion = ChatCompletion.builder().messages(Arrays.asList(message)).build();
            ChatCompletionResponse chatCompletionResponse = openAiClient.chatCompletion(chatCompletion);
            chatCompletionResponse.getChoices().forEach(e -> {
                System.out.println(e.getMessage());
            });
        }
    }
    

## 方式二（下载源码直接运行）

### **OpenAI全部接口支持调用**

完整测试案例参考：com.unfbx.chatgpt.OpenAiClientTest 和 com.unfbx.chatgpt.OpenAiStreamClientTest

* * *

注意：由于这个接口：

<https://platform.openai.com/docs/api-reference/files/retrieve-content>

**免费用户无法使用，所以并未经过测试！！！** （哪位朋友有收费版keys也可以提供下）

**完整测试案例参考源码中的：com.unfbx.chatgpt.OpenAiClientTest** 和 **com.unfbx.chatgpt.OpenAiStreamClientTest**

# Star History

[![Star History Chart](https://camo.githubusercontent.com/fbd1614280075c99593f2efb59b22b414ce6e7331b01ac23e222b428053518e4/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d477274313232382f636861746770742d6a61766126747970653d44617465)](https://star-history.com/#Grt1228/chatgpt-java&Date)

# 站在巨人的肩膀

鸣谢： OpenAi：<https://openai.com/>

[knuddelsgmbh](https://github.com/knuddelsgmbh) 的[jtokkit](https://github.com/knuddelsgmbh/jtokkit) 的开源计算算法。

# 如果项目对你有帮助，可以选择请我喝杯奶茶

[![微信截图_20230405222411](https://user-images.githubusercontent.com/27008803/230111508-3179cf30-e128-4b2e-9645-157266c491ce.png)](https://user-images.githubusercontent.com/27008803/230111508-3179cf30-e128-4b2e-9645-157266c491ce.png)[![微信截图_20230405222357](https://user-images.githubusercontent.com/27008803/230111525-322f5036-d06d-46bb-94d1-db8ce9ed2adf.png)](https://user-images.githubusercontent.com/27008803/230111525-322f5036-d06d-46bb-94d1-db8ce9ed2adf.png)

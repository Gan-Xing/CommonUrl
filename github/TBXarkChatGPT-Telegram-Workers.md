ChatGPT-Telegram-Workers 使用说明 分支 配置 部署流程 自动更新 支持的平台 1\. Cloudflare Workers 2\. Vercel 3\. Render 4\. Local 更新日志 最佳实践 支持我 贡献者 许可证

##  README.md

# ChatGPT-Telegram-Workers

[English Version](/TBXark/ChatGPT-Telegram-Workers/blob/master/doc/en/README.md)

最简单快捷部署属于自己的ChatGPT Telegram机器人的方法。使用Cloudflare Workers，单文件，直接复制粘贴一把梭，无需任何依赖，无需配置本地开发环境，不用域名，免服务器。 可以自定义系统初始化信息，让你调试好的性格永远不消失。

查看Demo [![image](/TBXark/ChatGPT-Telegram-Workers/raw/master/doc/demo.jpg)](/TBXark/ChatGPT-Telegram-Workers/blob/master/doc/demo.jpg)

## 使用说明

#### 分支

  * [`master`](https://github.com/TBXark/ChatGPT-Telegram-Workers/tree/master) 经过测试基本没有BUG的版本
  * [`dev`](https://github.com/TBXark/ChatGPT-Telegram-Workers/tree/dev) 有一些新功能，但是没有经过完整的测试，dist文件为基本可用的版本



#### 配置

> 推荐在Workers配置界面填写环境变量， 而不是直接修改js代码中的变量

配置信息和命令使用说明，见 [配置文档](/TBXark/ChatGPT-Telegram-Workers/blob/master/doc/CONFIG.md)

#### 部署流程

详情见 [部署流程](/TBXark/ChatGPT-Telegram-Workers/blob/master/doc/DEPLOY.md)

#### 自动更新

> 使用`Github Action`自动更新 `Cloudflare Workers`

详情见 [自动更新](/TBXark/ChatGPT-Telegram-Workers/blob/master/doc/ACTION.md)

#### 支持的平台

##### 1\. [Cloudflare Workers](https://workers.cloudflare.com/)

最简单的方法，本项目默认支持的部署方式，详情看[部署流程](/TBXark/ChatGPT-Telegram-Workers/blob/master/doc/DEPLOY.md)。免费，无需域名，无需服务器，无需配置本地开发环境。KV存储，无需数据库，但是有一定的存储限制，

> KV每天写入限制为1000次，不过对于聊天机器人来说，应该够用了。(调试模式`DEBUG_MODE`会保存最新一条消息到KV，token统计每次对话成功都会更新统计数据，所以会有一定的写入次数。如果你经常使用次数超过1000次，可以考虑关闭调试模式和者使用统计)

##### 2\. [Vercel](https://vercel.com/)

详情看[Vercel](/TBXark/ChatGPT-Telegram-Workers/blob/master/adapter/vercel/README.md)。免费，无需域名，无需服务器。需要配置本地开发环境部署，不能通过复制粘贴部署。无存储服务，需要自己配置数据库。可以使用[Redis Cloud](https://redis.com)的免费redis。可以连接github自动部署，但是需要了解vercel的配置。

##### 3\. [Render](https://render.com/)

详情看[Render](/TBXark/ChatGPT-Telegram-Workers/blob/master/adapter/render)。免费，无需域名，无需服务器。需要有一定的开发能力。

##### 4\. Local

详情看[Local](/TBXark/ChatGPT-Telegram-Workers/blob/master/adapter/local/README.md)。本地的部署方式，需要配置本地开发环境，需要有一定的开发能力。

## 更新日志

  * v1.5.0 
    * perf: 调整命令顺序
    * perf: openai发送请求前前发送loading消息
    * feat: 添加流式输出支持(默认开启)。使用`STREAM_MODE=false`关闭
    * feat: 添加安全模式(默认开启)解决TG无限重试的问题
    * feat: 增加对多个KEY的适配，随机选择KEY使用
    * feat: 增加快捷按钮 `/new`, `/redo`



其他更新日志见[CHANGELOG.md](/TBXark/ChatGPT-Telegram-Workers/blob/master/doc/CHANGELOG.md)

## 最佳实践

~~新建多个机器人绑定到同一个workers，设置`TELEGRAM_AVAILABLE_TOKENS`,每个机器人赋予不同的`SYSTEM_INIT_MESSAGE`~~。开启群聊模式，新建多个群聊，每个群内只有自己个机器人，每个群的机器人由不同的`SYSTEM_INIT_MESSAGE`，比如翻译专家，文案专家，代码专家。然后每次根据自己的需求和不同的群里的机器人聊天，这样就不用经常切换配置属性。

## 支持我

如果使用openai期间需要绑卡可以使用我的onekey的邀请码: <https://card.onekey.so/?i=QO19EC> 如果有其他问题可以加群交流。

## 贡献者

这个项目存在是因为所有贡献者的帮助。[贡献](https://github.com/tbxark/ChatGPT-Telegram-Workers/graphs/contributors).

## 许可证

**ChatGPT-Telegram-Workers** 以 MIT 许可证的形式发布。[查看许可证](/TBXark/ChatGPT-Telegram-Workers/blob/master/LICENSE) 获取更多细节。

ChatGPT-Feishu 效果 如何使用本项目代码？ 1\. 创建一个飞书开放平台应用，并获取到 APPID 和 Secret 2\. 开启机器人能力 3\. 访问 AirCode ，创建一个新的项目 4\. 复制本项目下的 event.js 的源码内容，并粘贴到 Aircode 当中 5\. 安装所需依赖 6\. 配置环境变量 7\. 获取 OpenAI 的 KEY ，并配置环境变量 8\. 开启权限并配置事件 9\. 发布版本，等待审核 如何贡献？ 有问题沟通可加群 FAQ 1\. 提交事件订阅地址时提示 Challenge Code 没有返回？ 2\. 可以私聊回复，但没办法群聊回复？ 3\. aircode 提示报错 failed to obtain token? 4\. cannot set propoertis of undefined (setting 'event_type')? LICENSE

##  README.md

# ChatGPT-Feishu

给飞书用户准备的 ChatGPT 机器人。视频演示如下，生成略慢，请耐心等待~

## 效果

202302100113456.mp4

## 如何使用本项目代码？

> 视频教程见 -> <https://youtu.be/axvH1D0Dhnk> | <https://www.bilibili.com/video/BV1uT411R7TL/>

### 1\. 创建一个飞书开放平台应用，并获取到 APPID 和 Secret

访问 [开发者后台](https://open.feishu.cn/app?lang=zh-CN)，创建一个名为 **ChatGPT** 的应用，并上传应用头像。创建完成后，访问【凭证与基础信息】页面，复制 APPID 和 Secret 备用。

[![image-20230210012031179](https://camo.githubusercontent.com/9d5594a656f0918a25f3600d76adbdc35ea1036ebaa90d0cc8f52f25950c6bd7/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303132303333392e706e67)](https://camo.githubusercontent.com/9d5594a656f0918a25f3600d76adbdc35ea1036ebaa90d0cc8f52f25950c6bd7/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303132303333392e706e67)

### 2\. 开启机器人能力

打开应用的机器人应用功能

[![image-20230210012110735](https://camo.githubusercontent.com/4ba2f491069e91cf6cd55c686f5a9ec368c2731158caaa98dc4c6aa412a96dd6/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303132313030382e706e67)](https://camo.githubusercontent.com/4ba2f491069e91cf6cd55c686f5a9ec368c2731158caaa98dc4c6aa412a96dd6/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303132313030382e706e67)

### 3\. 访问 [AirCode](https://aircode.io/dashboard) ，创建一个新的项目

登录 [AirCode](https://aircode.io/dashboard) ，创建一个新的 Node.js v16 的项目，项目名可以根据你的需要填写，可以填写 ChatGPT

[![image-20230210012334145](https://camo.githubusercontent.com/fd336bd5d91b4d194f16224bf397a0b57aa6b3cf8912e7afd0fcdca2840ff13d/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303132333235342e706e67)](https://camo.githubusercontent.com/fd336bd5d91b4d194f16224bf397a0b57aa6b3cf8912e7afd0fcdca2840ff13d/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303132333235342e706e67)

### 4\. 复制本项目下的 event.js 的源码内容，并粘贴到 Aircode 当中

访问[ChatGPT-Feishu/event.js at master · bestony/ChatGPT-Feishu (github.com)](https://github.com/bestony/ChatGPT-Feishu/blob/master/event.js)，复制代码

[![image-20230210012555571](https://camo.githubusercontent.com/aab974c1cd76bdbc01dda752f7b7f1053b9043d4da5a9c527dc21e0feac5806e/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303132353735302e706e67)](https://camo.githubusercontent.com/aab974c1cd76bdbc01dda752f7b7f1053b9043d4da5a9c527dc21e0feac5806e/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303132353735302e706e67)

并把代码粘贴到 AIrcode 默认创建的 hello.js 。然后点击顶部的 deploy ，完成第一次部署。

[![image-20230210012653296](https://camo.githubusercontent.com/fae026277fc8f7242076fd05b47d14b9a5397ed059275ec77d5abc8583ee98aa/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303132363533362e706e67)](https://camo.githubusercontent.com/fae026277fc8f7242076fd05b47d14b9a5397ed059275ec77d5abc8583ee98aa/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303132363533362e706e67)

部署成功后，可以在下方看到。

[![image-20230210012808063](https://camo.githubusercontent.com/6f84895c8cb5d619bc5e8d692d05e6529b7a22e8a26d2c4c9b52dc52494eaff7/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303132383238382e706e67)](https://camo.githubusercontent.com/6f84895c8cb5d619bc5e8d692d05e6529b7a22e8a26d2c4c9b52dc52494eaff7/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303132383238382e706e67)

### 5\. 安装所需依赖

这个开发过程中，我们使用了飞书开放平台官方提供的 SDK，以及 axios 来完成调用。点击页面左下角的包管理器，安装 `axios` 和 `@larksuiteoapi/node-sdk`。安装完成后，点击上方的部署，使其生效。

[![image-20230210025955556](https://camo.githubusercontent.com/024c45e0bb91f8c03b907b355f26b00848422ee432ecbb89dc19268a2fe90e1d/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303235393736312e706e67)](https://camo.githubusercontent.com/024c45e0bb91f8c03b907b355f26b00848422ee432ecbb89dc19268a2fe90e1d/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303235393736312e706e67)

### 6\. 配置环境变量

接下来我们来配置环境变量，你需要配置三个环境变量 `APPID` 、`SECRET` 和 `BOTNAME`，APPID 填写你刚刚在飞书开放平台获取的 APPID，SECRET 填写你在飞书开放平台获取到的 SECRET，BOTNAME 填写你的机器人的名字。

> 配置环境变量可能会失败，可以多 deploy 几次，确保配置成功。

[![image-20230210013355689](https://camo.githubusercontent.com/15ab2e64ef5a24240494c01bb98c67f2aa98e72fb0b60c4c7a93fcdaf294be2f/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303133333739382e706e67)](https://camo.githubusercontent.com/15ab2e64ef5a24240494c01bb98c67f2aa98e72fb0b60c4c7a93fcdaf294be2f/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303133333739382e706e67)

配置完成后，点击上方的 **Deploy** 按钮部署，使这些环境变量生效。

[![image-20230210013518142](https://camo.githubusercontent.com/7ee95707d1f1423caa5c9a7b2e82ac2d58b7da3d268ea933d85865aaec569ed0/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303133353230392e706e67)](https://camo.githubusercontent.com/7ee95707d1f1423caa5c9a7b2e82ac2d58b7da3d268ea933d85865aaec569ed0/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303133353230392e706e67)

会变成这样的

[![image-20230210013603084](https://camo.githubusercontent.com/41e2b1e5a70c33a502c33b30cea77c6342a4d09699e5cd25c3e218632f4ba2e4/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303133363132342e706e67)](https://camo.githubusercontent.com/41e2b1e5a70c33a502c33b30cea77c6342a4d09699e5cd25c3e218632f4ba2e4/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303133363132342e706e67)

### 7\. 获取 OpenAI 的 KEY ，并配置环境变量

访问 [Account API Keys - OpenAI API](https://platform.openai.com/account/api-keys) ，点击这里的 Create new secret key ，创建一个新的 key ，并保存备用。

[![image-20230210013702015](https://camo.githubusercontent.com/762eb47ea39d6b581ef5421656aaed24bd52db2c5358c0ecef7b57f0f37537fb/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303133373037382e706e67)](https://camo.githubusercontent.com/762eb47ea39d6b581ef5421656aaed24bd52db2c5358c0ecef7b57f0f37537fb/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303133373037382e706e67)

重新回到 Aircode， 配置一个名为 `KEY` 的环境变量，并填写你刚刚生成的 Key 。配置完成后，点击部署使其生效。

[![image-20230210022322720](https://camo.githubusercontent.com/cbae19a9fe8f7ffb3a82a04a53efe38f1093d2c4e01b138058cee42abd3cea00/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303232333833392e706e67)](https://camo.githubusercontent.com/cbae19a9fe8f7ffb3a82a04a53efe38f1093d2c4e01b138058cee42abd3cea00/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303232333833392e706e67)

### 8\. 开启权限并配置事件

访问开放平台页面，开通如下 6 个权限：

  * im:message
  * im:message.group_at_msg
  * im:message.group_at_msg:readonly
  * im:message.p2p_msg
  * im:message.p2p_msg:readonly
  * im:message:send_as_bot



[![image-20230210022432066](https://camo.githubusercontent.com/f8f0e4953601ba3b54497098aaa09a10827f84312fb3d58e0d7cea3270271ec4/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303232343332352e706e67)](https://camo.githubusercontent.com/f8f0e4953601ba3b54497098aaa09a10827f84312fb3d58e0d7cea3270271ec4/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303232343332352e706e67)

然后回到 AirCode ，复制函数的调用地址。

[![image-20230210022628784](https://camo.githubusercontent.com/a6769dc948f207b1fed12ee69bbb483cb8af4beaf0fdb0eb08a3c0c691e81e06/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303232363834362e706e67)](https://camo.githubusercontent.com/a6769dc948f207b1fed12ee69bbb483cb8af4beaf0fdb0eb08a3c0c691e81e06/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303232363834362e706e67)

然后回到事件订阅界面，添加事件。

[![image-20230210022720552](https://camo.githubusercontent.com/b253b88e795ce0785d3ac82e6828b850af62b960715694b66dcf8fdc71ee9b3e/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303232373738362e706e67)](https://camo.githubusercontent.com/b253b88e795ce0785d3ac82e6828b850af62b960715694b66dcf8fdc71ee9b3e/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303232373738362e706e67)

### 9\. 发布版本，等待审核

上述这些都配置完成后，你的机器人就配置好了，接下来只需要在飞书开放平台后台找到应用发布，创建一个全新的版本并发布版本即可。

## 如何贡献？

欢迎通过 issue 提交你的想法，帮助我迭代这个项目 or 直接通过 Pull Request 来提交你的代码。发布成功后，你就可以在飞书当中体验 ChatGPT 了。

[![image-20230210022834052](https://camo.githubusercontent.com/2e28e93fdb7b0a19751db3a2f80b55884a7f94d725caa2f6f7b5b377148cc634/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303232383135392e706e67)](https://camo.githubusercontent.com/2e28e93fdb7b0a19751db3a2f80b55884a7f94d725caa2f6f7b5b377148cc634/68747470733a2f2f706f7374696d672e616c696176762e636f6d2f706963676f2f3230323330323130303232383135392e706e67)

## 有问题沟通可加群

[![飞书20230418-015544](https://user-images.githubusercontent.com/13283837/232570671-1058555f-c9e5-4f64-889b-1d8efd0101ba.png)](https://user-images.githubusercontent.com/13283837/232570671-1058555f-c9e5-4f64-889b-1d8efd0101ba.png)

## FAQ

### 1\. 提交事件订阅地址时提示 Challenge Code 没有返回？

可以看看是不是配置了 Encrypt Key ，暂时不支持对加密数据解密。路径是应用后台 - 事件订阅

[![image](https://user-images.githubusercontent.com/13283837/218002249-362a40ab-3f5d-493b-80ec-a2b0efa2b5c9.png)](https://user-images.githubusercontent.com/13283837/218002249-362a40ab-3f5d-493b-80ec-a2b0efa2b5c9.png)

### 2\. 可以私聊回复，但没办法群聊回复？

确保 6 项开放平台权限都已经开通且已经发布版本，权限进入可用状态。

另一情况是飞书机器人名称与 BOTNAME 变量不一致。由于 aircode 的环境变量 **不支持中文** ，如果机器人名称为中文也会造成部署失败。

解决办法：修改飞书机器人的名称为英文，或直接修改代码中的 BOTNAME 值。

### 3\. aircode 提示报错 failed to obtain token?

说明你的 aircode 的环境变量配置没成功，可以重新配置一下，然后再部署一下。

### 4\. cannot set propoertis of undefined (setting 'event_type')?

说明你用 HTTP 发起请求 / 或者用了 aircode 的debug 功能，是正常现象。

## LICENSE

[GPLv3](/bestony/ChatGPT-Feishu/blob/master/LICENSE)

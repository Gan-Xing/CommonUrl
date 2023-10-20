川虎 Chat 🐯 Chuanhu Chat 为ChatGPT/ChatGLM/LLaMA/StableLM/MOSS等多种LLM提供了一个轻快好用的Web图形界面 目录 使用技巧 安装方式、使用方式 疑难杂症解决 了解更多 Starchart Contributors 捐款

##  README.md

简体中文 | [English](/GaiZhenbiao/ChuanhuChatGPT/blob/main/readme/README_en.md "English") | [日本語](/GaiZhenbiao/ChuanhuChatGPT/blob/main/readme/README_ja.md "Japanese")

# 川虎 Chat 🐯 Chuanhu Chat

[ ![Logo](https://user-images.githubusercontent.com/70903329/227087087-93b37d64-7dc3-4738-a518-c1cf05591c8a.png) ](https://github.com/GaiZhenBiao/ChuanhuChatGPT)

### 为ChatGPT/ChatGLM/LLaMA/StableLM/MOSS等多种LLM提供了一个轻快好用的Web图形界面

[ ![Tests Passing](https://camo.githubusercontent.com/a56ed5992e7d0d54c8b43d2e0499fad685106c4051fa472fdf215a48d945f9f7/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f4761695a68656e6269616f2f436875616e687543686174475054) ](https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/main/LICENSE) [ ![GitHub Contributors](https://camo.githubusercontent.com/57337512132862c980be237679bca029a9cfc251f2ec85b2ebea4bf1ff13da9f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f426173652d47726164696f2d6662376431613f7374796c653d666c6174) ](https://gradio.app/) [ ![GitHub pull requests](https://camo.githubusercontent.com/910272963058e000c9b0a2a722dc98a830e23a260975f2de4ddbf14a0db8eca5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54656c656772616d2d47726f75702d626c75652e7376673f6c6f676f3d74656c656772616d) ](https://t.me/tkdifferent)

流式传输 / 无限对话 / 保存对话 / 预设Prompt集 / 联网搜索 / 根据文件回答   
渲染LaTeX / 渲染表格 / 代码高亮 / 自动亮暗色切换 / 自适应界面 / “小而美”的体验   
自定义api-Host / 多参数可调 / 多API Key均衡负载 / 多用户显示 / 适配GPT-4 / 支持本地部署LLM 

[**视频教程**](https://www.bilibili.com/video/BV1mo4y1r7eE) · [**2.0介绍视频**](https://www.bilibili.com/video/BV1184y1w7aP) || [**在线体验**](https://huggingface.co/spaces/JohnSmith9982/ChuanhuChatGPT) · [**一键部署**](https://huggingface.co/login?next=%2Fspaces%2FJohnSmith9982%2FChuanhuChatGPT%3Fduplicate%3Dtrue)

[![Animation Demo](https://user-images.githubusercontent.com/51039745/226255695-6b17ff1f-ea8d-464f-b69b-a7b6b68fffe8.gif)](https://user-images.githubusercontent.com/51039745/226255695-6b17ff1f-ea8d-464f-b69b-a7b6b68fffe8.gif) [ ![Animation Demo](https://user-images.githubusercontent.com/51039745/226255695-6b17ff1f-ea8d-464f-b69b-a7b6b68fffe8.gif) ](https://user-images.githubusercontent.com/51039745/226255695-6b17ff1f-ea8d-464f-b69b-a7b6b68fffe8.gif) [ ](https://user-images.githubusercontent.com/51039745/226255695-6b17ff1f-ea8d-464f-b69b-a7b6b68fffe8.gif)

## 目录

使用技巧 | [安装方式](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B) | [常见问题](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98) | 给作者买可乐🥤  
---|---|---|---  
  
## 使用技巧

  * 使用System Prompt可以很有效地设定前提条件。
  * 使用Prompt模板功能时，选择Prompt模板集合文件，然后从下拉菜单中选择想要的prompt。
  * 如果回答不满意，可以使用 `重新生成`按钮再试一次
  * 对于长对话，可以使用 `优化Tokens`按钮减少Tokens占用。
  * 输入框支持换行，按 `shift enter`即可。
  * 可以在输入框按上下箭头在输入历史之间切换
  * 部署到服务器：将程序最后一句改成 `demo.launch(server_name="0.0.0.0", server_port=<你的端口号>)`。
  * 获取公共链接：将程序最后一句改成 `demo.launch(share=True)`。注意程序必须在运行，才能通过公共链接访问。
  * 在Hugging Face上使用：建议在右上角 **复制Space** 再使用，这样App反应可能会快一点。



## 安装方式、使用方式

请查看[本项目的wiki页面](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)。

## 疑难杂症解决

在遇到各种问题查阅相关信息前，您可以先尝试手动拉取本项目的最新更改并更新 gradio，然后重试。步骤为：

  1. 点击网页上的 `Download ZIP` 下载最新代码，或 
    
        git pull https://github.com/GaiZhenbiao/ChuanhuChatGPT.git main -f

  2. 尝试再次安装依赖（可能本项目引入了新的依赖） 
    
        pip install -r requirements.txt
    

  3. 更新gradio 
    
        pip install gradio --upgrade --force-reinstall
    




很多时候，这样就可以解决问题。

如果问题仍然存在，请查阅该页面：[常见问题](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)

该页面列出了 **几乎所有** 您可能遇到的各种问题，包括如何配置代理，以及遇到问题后您该采取的措施， **请务必认真阅读** 。

## 了解更多

若需了解更多信息，请查看我们的 [wiki](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki)：

  * [想要做出贡献？](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/%E8%B4%A1%E7%8C%AE%E6%8C%87%E5%8D%97)
  * [项目更新情况？](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/%E6%9B%B4%E6%96%B0%E6%97%A5%E5%BF%97)
  * [二次开发许可？](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/%E4%BD%BF%E7%94%A8%E8%AE%B8%E5%8F%AF)
  * [如何引用项目？](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/%E4%BD%BF%E7%94%A8%E8%AE%B8%E5%8F%AF#%E5%A6%82%E4%BD%95%E5%BC%95%E7%94%A8%E8%AF%A5%E9%A1%B9%E7%9B%AE)



## Starchart

[![Star History Chart](https://camo.githubusercontent.com/53d9c9236397667ba350a3bc7d3e9a0f3734fc1ab3ae22cc15256d471c170317/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d4761695a68656e6269616f2f436875616e68754368617447505426747970653d44617465)](https://star-history.com/#GaiZhenbiao/ChuanhuChatGPT&Date)

## Contributors

[ ![](https://camo.githubusercontent.com/99fbecd4579cca6a44723267bb8e0c82e315f1b2e537e14091077b944922f4bf/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d4761695a68656e6269616f2f436875616e687543686174475054) ](https://github.com/GaiZhenbiao/ChuanhuChatGPT/graphs/contributors)

## 捐款

🐯如果觉得这个软件对你有所帮助，欢迎请作者喝可乐、喝咖啡～

[![Buy Me A Coffee](https://camo.githubusercontent.com/d4916bc754508835b8885c24c06ac2ba0e275b1e90bbd162cf9375f4f0214c7d/68747470733a2f2f696d672e6275796d6561636f666665652e636f6d2f627574746f6e2d6170692f3f746578743d427579206d65206120636f6666656526656d6f6a693d26736c75673d436875616e68754368617426627574746f6e5f636f6c6f75723d32313964353326666f6e745f636f6c6f75723d66666666666626666f6e745f66616d696c793d506f7070696e73266f75746c696e655f636f6c6f75723d66666666666626636f666665655f636f6c6f75723d464644443030)](https://www.buymeacoffee.com/ChuanhuChat)

[![image](https://user-images.githubusercontent.com/51039745/226920291-e8ec0b0a-400f-4c20-ac13-dafac0c3aeeb.JPG)](https://user-images.githubusercontent.com/51039745/226920291-e8ec0b0a-400f-4c20-ac13-dafac0c3aeeb.JPG)

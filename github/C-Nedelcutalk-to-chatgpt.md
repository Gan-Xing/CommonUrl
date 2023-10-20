How to install Option 1: CHROME or EDGE STORE Option 2: MANUAL INSTALL FAQ Press coverage Change log Donations

##  README.md

**Talk-to-ChatGPT** is a Google Chrome and Microsoft Edge extension that allows users to talk with the ChatGPT AI using their voice (speech recognition), and listen to the bot's answer with a voice (text-to-speech), rather than just by typing. With this tool, users can speak to the AI and receive spoken responses, making the interaction feel more natural and conversational. This could be useful in a variety of settings where it would be helpful to have a more human-like interaction with an AI.

The extension can be downloaded from here:

  * From the **Chrome Web store** here: <https://chrome.google.com/webstore/detail/talk-to-chatgpt/hodadfhfagpiemkeoliaelelfbboamlk>
  * From the **Edge Web store** here: (link coming soon, extension is under review, you can download/install manually for now)
  * Manual installation option, detailed further below



After installing the extension, open or reload the ChatGPT page ( <https://chat.openai.com/> ) and you should be seeing a 'Start' button on the top right corner of the page. After you click Start, you will be asked for permission to use your Microphone. This is required to enable voice recognition.

[![Talk-to-GPT Menu](/C-Nedelcu/talk-to-chatgpt/raw/main/images/menu.png?raw=true&v2.2?)](/C-Nedelcu/talk-to-chatgpt/blob/main/images/menu.png?raw=true&v2.2?)

Once started, Talk-to-ChatGPT displays a menu on the top right corner of the page where users can access settings (such as voice, language, and more), skip the current message, toggle voice recognition on or off, and toggle text-to-speech on or off.

The settings menu can be seen below. Settings are saved in a cookie and reloaded automatically each time you activate the script.

[![Settings dialog](/C-Nedelcu/talk-to-chatgpt/raw/main/images/settings.png?raw=true&v2.2?)](/C-Nedelcu/talk-to-chatgpt/blob/main/images/settings.png?raw=true&v2.2?)

Demo V2.0: <https://www.youtube.com/watch?v=sKjkOwkoMNM>

# How to install

### Option 1: CHROME or EDGE STORE

  * Google Chrome: download from the Chrome extension store at <https://chrome.google.com/webstore/detail/talk-to-chatgpt/hodadfhfagpiemkeoliaelelfbboamlk>
  * Microsoft Edge: the extension is still under review, link will be given soon, use manual install for now



### Option 2: MANUAL INSTALL

If the extension is temporarily unavailable (this can happen when OpenAI make breaking changes), or if you want to install the latest updates before they are available on the Chrome/Edge web store, you can install the extension manually. Here is how you do it.

  1. Download the .zip file here: <https://github.com/C-Nedelcu/talk-to-chatgpt/raw/main/chrome-extension/chrome-extension.zip> (this link will always point to the latest version)
  2. Extract the .zip file in a folder somewhere
  3. Follow this tutorial to install the extension in Chrome/Edge in dev mode: <https://webkul.com/blog/how-to-install-the-unpacked-extension-in-chrome/>



# FAQ

**Q: Which web browsers are supported?** A: This extension is designed for Google Chrome and Microsoft Edge, desktop version only. The extension will not work in any other web browser, especially not mobile browsers, because these browsers do not support the necessary APIs for speech recognition and speech synthesis.

**Q: Can you make it speak faster or in a different voice or language?** A: Yes, use the settings menu. You can select a variety of settings among which the speech rate, voice type, and language.

**Q: What is the purpose of this project?** A: Originally, it was mostly a fun proof of concept. This AI is mind-bogglingly intelligent and I had a deep desire to converse with it orally, to make it more interesting. Surely OpenAI themselves will make a proper voice-controlled version of ChatGPT in the future, at which point my project will be rendered useless. For now, it seems to be helping people with disabilities / visually impaired people, so I'm going to be actively working on the project for as long as I can, as a form of contribution to society.

**Q: Is it safe to use?** A: Yes, it's simple javascript code that will execute only in the context of the ChatGPT webpage. It doesn't request any particular permissions, and it is fully open source. As soon as you navigate away from ChatGPT, everything is cleared, except for the addon settings.

**Q: Will it always work?** A: it might not work indefinitely, and here's why. The code is based on the current HTML structure of the ChatGPT page. If OpenAI change the HTML code, this project will likely stop working. I will probably keep updating it to maintain compatibility, but I'm not sure I'll be doing that forever. If you want to contribute to the project you are more than welcome to submit your own changes through Github.

**Q: I have an error or a problem...** A: Feel free to update the javascript yourself and propose changes on Github, or simply report the issue if you aren't a programmer.

**Q: Can I make changes to your code?** A: Yes, feel free to make changes, and do whatever you want, commit, fork, just have fun.

**Q: How do I know what languages are supported?** A: this is entirely based on the web browser APIs (Google Chrome, Microsoft Edge), so you need to ask Google or Microsoft, as I cannot provide an up-to-date answer. I've only tested it with English, French, and Chinese. The languages in the settings menu are the same ones found on the Google and Edge demos.

# Press coverage

Talk-to-ChatGPT has been receiving press coverage since its release. It is currently featured on the following sites:

  * BGR.com - <https://bgr.com/tech/free-talk-to-chatgpt-chrome-extension-gives-ai-a-voice/>
  * GeekFlare - <https://geekflare.com/best-chatgpt-chrome-extensions/>
  * NerdsChalk - <https://nerdschalk.com/talk-to-chatgpt/>
  * MakeUseOf - <https://www.makeuseof.com/chatgpt-chrome-extensions-better-ai-prompts-answers-in-browsers/>
  * TechBriefly - <https://techbriefly.com/2023/03/30/how-to-talk-to-chatgpt/>
  * Skool.com - <https://www.skool.com/chatgpt/fancy-a-real-time-voice-conversation-with-chatgpt>
  * GBAtemp - <https://gbatemp.net/threads/talk-to-chatgpt-actual-vocal-discussion-with-an-ai-using-voice-recognition-and-text-to-speech-in-chrome.622942/>
  * JustGeek - <https://www.justgeek.fr/talk-to-chatgpt-discuter-a-voix-haute-avec-chatgpt-103657/>
  * Comment Ca Marche - <https://www.commentcamarche.net/informatique/technologies/27295-application-et-extension-vocale-chatgpt-de-nouveaux-outils-pour-l-ia/#talk-to-chatgpt--discuter-a-haute-voix-avec-lia>
  * This list will be updated over time.



# Change log

Version 2.3.0 - April 18th, 2023

  * New: option to skip code blocks while reading bot's response (#17)
  * Fixed: when speech recognition returns an empty sentence, this could cause the addon to disfunction (#72)



Version 2.2.0 - April 16th, 2023:

  * New: 'pause' vocal command was revamped. When you say the pause word, the addon will continue listening but won't send anything to ChatGPT. To resume normal functionality, say the pause word again, or click the Resume button
  * Updated: minor UI and text updates here and there
  * Bugfix: when the addon is started in the middle of a conversation with ChatGPT, the last message received was always spoken out loud. It won't be the case anymore.



Version 2.1.0 - April 15th, 2023:

  * New: UI was revamped. Credits to pixelsoda and Shaun James



Version 2.0.2 - April 15th, 2023:

  * Fixed: the addon will properly activate on every ChatGPT conversational pages



Version 2.0.1 - April 14th, 2023:

  * Fixed: the ChatGPT URL was changed by OpenAI, therefore disabling the addon



Version 2.0.0 - April 10th, 2023:

  * New: keyboard shortcuts to control the addon. The shortcuts are listed in the settings menu or appear when you move the mouse over the UI buttons
  * New: an option to avoid breaking down sentences with commas or other punctuation marks such as colons and semicolons
  * Fixed: vocal commands such as the stop and pause words wouldn't always work because the speech recognition would add a dot at the end



For older change logs, please check the commit messages: <https://github.com/C-Nedelcu/talk-to-chatgpt/commits/main>

# Donations

Thanks for reading all the way down. Are you enjoying Talk-To-ChatGPT and want me to continue improving it? You can help by making a donation to the project. Please click the Donate button to proceed.

[![paypal](https://camo.githubusercontent.com/c64602e146d0075de0709503f8d0e38b9e2803431b11c7ba9b727b9f4d2b136b/68747470733a2f2f6564756e6578742e636f6d2e73672f70617970616c2e706e67)](https://www.paypal.com/donate/?business=BZ43BM7XSSKKW&no_recurring=0&item_name=Are+you+enjoying+Talk-To-ChatGPT?+If+so%2C+consider+making+a+donation+to+keep+the+project+going%2C+and+I%27ll+continue+improving+it%21&currency_code=EUR)

ChatGPT Chrome Extension 🤖 ✨ Install Troubleshooting Plugins Related License

##  README.md

# ChatGPT Chrome Extension 🤖 ✨

A Chrome extension that adds [ChatGPT](https://chat.openai.com) to every text box on the internet! Use it to write tweets, revise emails, fix coding bugs, or whatever else you need, all without leaving the site you're on. Includes a plugin system for greater control over ChatGPT behavior and ability to interact with 3rd party APIs.

[![](https://camo.githubusercontent.com/4ee1cc99964b086eefe95b2dcc5d723dcaa25e619cc1a9c1aaf156232c45bf18/68747470733a2f2f692e696d6775722e636f6d2f43504d4f7947372e676966)](https://camo.githubusercontent.com/4ee1cc99964b086eefe95b2dcc5d723dcaa25e619cc1a9c1aaf156232c45bf18/68747470733a2f2f692e696d6775722e636f6d2f43504d4f7947372e676966) [ ![68747470733a2f2f692e696d6775722e636f6d2f43504d4f7947372e676966](https://camo.githubusercontent.com/4ee1cc99964b086eefe95b2dcc5d723dcaa25e619cc1a9c1aaf156232c45bf18/68747470733a2f2f692e696d6775722e636f6d2f43504d4f7947372e676966) ](https://camo.githubusercontent.com/4ee1cc99964b086eefe95b2dcc5d723dcaa25e619cc1a9c1aaf156232c45bf18/68747470733a2f2f692e696d6775722e636f6d2f43504d4f7947372e676966) [ ](https://camo.githubusercontent.com/4ee1cc99964b086eefe95b2dcc5d723dcaa25e619cc1a9c1aaf156232c45bf18/68747470733a2f2f692e696d6775722e636f6d2f43504d4f7947372e676966)

## Install

First clone this repo on your local machine

Then install dependencies
    
    
    npm install

Copy `.env-example` into a new file named `.env` and add your ChatGPT API Key.

Run the server so the extension can communicate with ChatGPT.
    
    
    node server.js

This will automate interaction with ChatGPT through OpenAI's API, thanks to the [chatgpt-api](https://github.com/transitive-bullshit/chatgpt-api) library.

Add the extension

  1. Go to chrome://extensions in your Google Chrome browser
  2. Check the Developer mode checkbox in the top right-hand corner
  3. Click "Load Unpacked" to see a file-selection dialog
  4. Select your local `chatgpt-chrome-extension/extension` directory



You'll now see "Ask ChatGPT" if you right click in any text input or content editable area.

## Troubleshooting

If ChatGPT is taking a very long time to respond or not responding at all then it could mean that their servers are currently overloaded. You can confirm this by going to [chat.openai.com/chat](https://chat.openai.com/chat) and seeing whether their website works directly.

## Plugins

Plugins have the ability to inform ChatGPT of specific conversation rules and parse replies from ChatGPT before they are sent to the browser.

[Default](/gragland/chatgpt-chrome-extension/blob/main/plugins/Default.js) \- Sets some default conversation rules 🧑‍🏫

[Image](/gragland/chatgpt-chrome-extension/blob/main/plugins/Image.js) \- Tells ChatGPT to describe things visually when asked for an image and then replaces the description with a matching AI generated image from [Lexica](http://lexica.art) 📸

Your really cool plugin - Go make a plugin, do a pull-request and I'll add it the list 🤝

## Related

Huge thanks to [Travis Fischer](https://twitter.com/transitive_bs) for creating [chatgpt-api](https://github.com/transitive-bullshit/chatgpt-api)

## License

MIT © Gabe Ragland (follow me on [Twitter](https://twitter.com/gabe_ragland))

ChatGPT for Google Notice (2023-02-20) Supported Search Engines Screenshot Features Troubleshooting How to make it work in Brave How to make it work in Opera Build from source

##  README.md

# ChatGPT for Google

[![GitHub Workflow Status](https://camo.githubusercontent.com/5dd2086f4149275c9440777aceccc34ab8711d1c6a33f3aef66acca02960b00b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f776f6e67322f636861746770742d676f6f676c652d657874656e73696f6e2f7072652d72656c656173652d6275696c642e796d6c)](https://camo.githubusercontent.com/5dd2086f4149275c9440777aceccc34ab8711d1c6a33f3aef66acca02960b00b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f776f6e67322f636861746770742d676f6f676c652d657874656e73696f6e2f7072652d72656c656173652d6275696c642e796d6c) [![Visitors](https://camo.githubusercontent.com/e08372bb4c20b99d55d50b398904ebae79cee6c8ab28f456a8688c2b872fd37d/68747470733a2f2f76697369746f722d62616467652e676c697463682e6d652f62616467653f706167655f69643d776f6e67322e636861742d6770742d676f6f676c652d657874656e73696f6e266c6566745f636f6c6f723d677265656e2672696768745f636f6c6f723d726564)](https://camo.githubusercontent.com/e08372bb4c20b99d55d50b398904ebae79cee6c8ab28f456a8688c2b872fd37d/68747470733a2f2f76697369746f722d62616467652e676c697463682e6d652f62616467653f706167655f69643d776f6e67322e636861742d6770742d676f6f676c652d657874656e73696f6e266c6566745f636f6c6f723d677265656e2672696768745f636f6c6f723d726564) [![Twitter Follow](https://camo.githubusercontent.com/3ec4172115332468748a38554898d66aa94687962acb02a12679af1a93e08252/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6368617467707434676f6f676c653f7374796c653d736f6369616c)](https://twitter.com/chatgpt4google) [![License](https://camo.githubusercontent.com/47365f7ce9b896944c17b74677a41ca0a57016fdb1bf121ba11b60696aa103eb/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f776f6e67322f636861746770742d676f6f676c652d657874656e73696f6e)](https://camo.githubusercontent.com/47365f7ce9b896944c17b74677a41ca0a57016fdb1bf121ba11b60696aa103eb/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f776f6e67322f636861746770742d676f6f676c652d657874656e73696f6e)

### Notice (2023-02-20)

As this extension has been acquired, this code repository will no longer be updated from now on.

**My new project:** [ChatHub: All-in-one chatbot client](https://github.com/chathub-dev/chathub)

* * *

A browser extension to display ChatGPT response alongside Google (and other search engines) results

[Install from Chrome Web Store](https://chatgpt4google.com/chrome?utm_source=github)

[Install from Mozilla Add-on Store](https://chatgpt4google.com/firefox?utm_source=github)

[Changelog](https://chatgpt-for-google.canny.io/changelog)

## Supported Search Engines

Google, Baidu, Bing, DuckDuckGo, Brave, Yahoo, Naver, Yandex, Kagi, Searx

## Screenshot

[![Screenshot](/wong2/chatgpt-google-extension/raw/main/screenshots/extension.png?raw=true)](/wong2/chatgpt-google-extension/blob/main/screenshots/extension.png?raw=true)

## Features

  * Supports all popular search engines
  * Supports the official OpenAI API
  * Supports ChatGPT Plus
  * Markdown rendering
  * Code highlights
  * Dark mode
  * Provide feedback to improve ChatGPT
  * Copy to clipboard
  * Custom trigger mode
  * Switch languages



## Troubleshooting

### How to make it work in Brave

[![Screenshot](/wong2/chatgpt-google-extension/raw/main/screenshots/brave.png?raw=true)](/wong2/chatgpt-google-extension/blob/main/screenshots/brave.png?raw=true)

Disable "Prevent sites from fingerprinting me based on my language preferences" in `brave://settings/shields`

### How to make it work in Opera

[![Screenshot](/wong2/chatgpt-google-extension/raw/main/screenshots/opera.png?raw=true)](/wong2/chatgpt-google-extension/blob/main/screenshots/opera.png?raw=true)

Enable "Allow access to search page results" in the extension management page

## Build from source

  1. Clone the repo
  2. Install dependencies with `npm`
  3. `npm run build`
  4. Load `build/chromium/` or `build/firefox/` directory to your browser



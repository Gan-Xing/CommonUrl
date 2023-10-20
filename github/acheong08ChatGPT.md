ChatGPT  Support my work Discord Server: https://discord.gg/9K2BvbXEHT Installation Suport Python Version V1 Standard ChatGPT Rate limits Configuration Authentication method: (Choose 1) \- Email/Password \- Access token \- Optional configuration: Usage Command line Developer API Basic example (streamed): Basic example (single result): All API methods V3 Official Chat API Command line Developer API Basic example Streaming example Awesome ChatGPT Disclaimers Contributors Additional credits

##  README.md

# ChatGPT [![](https://github.com/acheong08/ChatGPT/raw/main/logo.png?raw=true)](https://github.com/acheong08/ChatGPT/blob/main/logo.png?raw=true)

English - [中文](/acheong08/ChatGPT/blob/main/docs/README_zh.md) \- [Spanish](/acheong08/ChatGPT/blob/main/docs/README_sp.md) \- [日本語](/acheong08/ChatGPT/blob/main/docs/README_ja.md)

[![PyPi](https://camo.githubusercontent.com/73610d8a582bdbbc9b982b9f622dab45c8deeabce0325bcf38532cc2a93d93d3/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f726576436861744750542e737667)](https://pypi.python.org/pypi/revChatGPT) [![Support_Platform](https://camo.githubusercontent.com/f6c4e72b154a3332f25730e10956dc2e5e84b4f19de77a8d2e06ee3d90fa4eba/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f72657643686174475054)](https://pypi.python.org/pypi/revChatGPT) [![Downloads](https://camo.githubusercontent.com/b9d161dea503f44fb966e6136a6961cddde307947e16651e1b58093040f3a2d4/68747470733a2f2f7374617469632e706570792e746563682f62616467652f72657663686174677074)](https://pypi.python.org/pypi/revChatGPT)

Reverse Engineered ChatGPT API by OpenAI. Extensible for chatbots etc.

[![](https://github.com/acheong08/ChatGPT/raw/main/docs/view.gif?raw=true)](https://pypi.python.org/pypi/revChatGPT) [ ![view.gif?raw=true](https://github.com/acheong08/ChatGPT/raw/main/docs/view.gif?raw=true) ](https://pypi.python.org/pypi/revChatGPT) [ ](https://pypi.python.org/pypi/revChatGPT)

> ## Support my work
> 
> Make a pull request and fix my bad code.
> 
> [![support](https://camo.githubusercontent.com/cd07f1a5d90e454e7bbf69d22ebe4cdbd3a0b3dcf56ba0b6c2495a8e99c776be/68747470733a2f2f6b6f2d66692e636f6d2f696d672f676974687562627574746f6e5f736d2e737667)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

> #### Discord Server: <https://discord.gg/9K2BvbXEHT>

# Installation
    
    
    python -m pip install --upgrade revChatGPT
    

### Suport Python Version

  * Minimum - Python3.9
  * Recommend - Python3.11+



# V1 Standard ChatGPT

Due to recent tightening of OpenAI's security, the default endpoint has been swapped over to one provided by @pengzhile. It is not open source and privacy is not guarenteed. Use it at your own risk. I am working on an open source implementation with the latest changes but that could take a while.

## Rate limits

  * Proxy server: 5 requests / 10 seconds
  * OpenAI: 50 requests / hour for each account



## Configuration

  1. Create account on [OpenAI's ChatGPT](https://chat.openai.com/)
  2. Save your email and password



### Authentication method: (Choose 1)

#### \- Email/Password

> _Currently broken for free users. Do`export PUID="..."` if you have a plus account. The PUID is a cookie named `_puid`_ Not supported for Google/Microsoft accounts.
    
    
    {
      "email": "email",
      "password": "your password"
    }

#### \- Access token

> Please this! <https://chat.openai.com/api/auth/session>
    
    
    {
      "access_token": "<access_token>"
    }

#### \- Optional configuration:
    
    
    {
      "conversation_id": "UUID...",
      "parent_id": "UUID...",
      "proxy": "...",
      "paid": false,
      "collect_analytics": true,
      "model": "gpt-4"
    }

Analytics is disabled by default. Set `collect_analytics` to `true` to enable it.

  3. Save this as `$HOME/.config/revChatGPT/config.json`
  4. If you are using Windows, you will need to create an environment variable named `HOME` and set it to your home profile for the script to be able to locate the config.json file.



## Usage

### Command line

`python3 -m revChatGPT.V1`
    
    
            ChatGPT - A command-line interface to OpenAI's ChatGPT (https://chat.openai.com/chat)
            Repo: github.com/acheong08/ChatGPT
    Type '!help' to show a full list of commands
    Logging in...
    You:
    (Press Esc followed by Enter to finish)
    

The command line interface supports multi-line inputs and allows navigation using arrow keys. Besides, you can also edit history inputs by arrow keys when the prompt is empty. It also completes your input if it finds matched previous prompts. To finish input, press `Esc` and then `Enter` as solely `Enter` itself is used for creating new line in multi-line mode.

Set the environment variable `NO_COLOR` to `true` to disable color output.

### Developer API

#### Basic example (streamed):
    
    
    from revChatGPT.V1 import Chatbot
    chatbot = Chatbot(config={
      "access_token": "<your access_token>"
    })
    print("Chatbot: ")
    prev_text = ""
    for data in chatbot.ask(
        "Hello world",
    ):
        message = data["message"][len(prev_text) :]
        print(message, end="", flush=True)
        prev_text = data["message"]
    print()

#### Basic example (single result):
    
    
    from revChatGPT.V1 import Chatbot
    chatbot = Chatbot(config={
      "access_token": "<your access_token>"
    })
    prompt = "how many beaches does portugal have?"
    response = ""
    for data in chatbot.ask(
      prompt
    ):
        response = data["message"]
    print(response)

#### All API methods

Refer to the [wiki](https://github.com/acheong08/ChatGPT/wiki/) for advanced developer usage.

# V3 Official Chat API

> Recently released by OpenAI
> 
>   * Paid
> 


Get API key from <https://platform.openai.com/account/api-keys>

## Command line

`python3 -m revChatGPT.V3 --api_key <api_key>`
    
    
      $ python3 -m revChatGPT.V3 --help
    
        ChatGPT - Official ChatGPT API
        Repo: github.com/acheong08/ChatGPT
    
    Type '!help' to show a full list of commands
    Press Esc followed by Enter or Alt+Enter to send a message.
    
    usage: V3.py [-h] --api_key API_KEY [--temperature TEMPERATURE] [--no_stream] [--base_prompt BASE_PROMPT]
                 [--proxy PROXY] [--top_p TOP_P] [--reply_count REPLY_COUNT] [--enable_internet]
                 [--config CONFIG] [--submit_key SUBMIT_KEY] [--model {gpt-3.5-turbo,gpt-4,gpt-4-32k}]
                 [--truncate_limit TRUNCATE_LIMIT]
    
    options:
      -h, --help            show this help message and exit
      --api_key API_KEY     OpenAI API key
      --temperature TEMPERATURE
                            Temperature for response
      --no_stream           Disable streaming
      --base_prompt BASE_PROMPT
                            Base prompt for chatbot
      --proxy PROXY         Proxy address
      --top_p TOP_P         Top p for response
      --reply_count REPLY_COUNT
                            Number of replies for each prompt
      --enable_internet     Allow ChatGPT to search the internet
      --config CONFIG       Path to V3 config json file
      --submit_key SUBMIT_KEY
                            Custom submit key for chatbot. For more information on keys, see README
      --model {gpt-3.5-turbo,gpt-4,gpt-4-32k}
      --truncate_limit TRUNCATE_LIMIT
    

## Developer API

### Basic example
    
    
    from revChatGPT.V3 import Chatbot
    chatbot = Chatbot(api_key="<api_key>")
    chatbot.ask("Hello world")

### Streaming example
    
    
    from revChatGPT.V3 import Chatbot
    chatbot = Chatbot(api_key="<api_key>")
    for data in chatbot.ask_stream("Hello world"):
        print(data, end="", flush=True)

# Awesome ChatGPT

[My list](https://github.com/stars/acheong08/lists/awesome-chatgpt)

If you have a cool project you want added to the list, open an issue.

# Disclaimers

This is not an official OpenAI product. This is a personal project and is not affiliated with OpenAI in any way. Don't sue me.

## Contributors

This project exists thanks to all the people who contribute.

[ ![](https://camo.githubusercontent.com/2b1ef43a2c272fdf5f7e8adec11707083dcf089e6ff57347f60e831ad8c8f549/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d616368656f6e6730382f43686174475054) ](https://github.com/acheong08/ChatGPT/graphs/contributors)

## Additional credits

  * Coding while listening to [this amazing song](https://www.youtube.com/watch?v=VaMR_xDhsGg) by [virtualharby](https://www.youtube.com/@virtualharby)



Check the new Google Bard Chatbot! 11-APRIL-2023 Update If you have any questions or need assistance, please join [Discord] Welcome to ChatGPT API FREE Reverse Proxy Table of Contents Features How to use ChatGPT API Reverse Proxy Self-Host Your Own API Use Our Hosted API Reverse Proxy Text Completion: Example: OpenAI Docs Chat Completion (ChatGPT): Example: OpenAI Docs Image Generation (DALL-E): Example: OpenAI Docs Examples using OpenAI libraries Python Node.js License

##  README.md

## [Check the new Google Bard Chatbot!](https://github.com/PawanOsman/GoogleBard)

# _11-APRIL-2023 Update_

We found a new way to use OpenAI API for free and now all API endpoints are working (text and chat completion, image generation). You can use the API by following the steps below:

### If you have any questions or need assistance, please join [[Discord](https://discord.pawan.krd)]

# Welcome to ChatGPT API _**FREE Reverse Proxy**_

**ChatGPT API Free Reverse Proxy** is a free reverse proxy to OpenAI API that allows users to access OpenAI API for free.

# Table of Contents

  * Features

  * How to use ChatGPT API Reverse Proxy

    * Self-Host Your Own API
    * Use Our Hosted API
      * Text Completion
      * Chat Completion (ChatGPT)
      * Image Generation (DALL-E)
    * Examples using OpenAI libraries
      * Python
      * Node.js
  * License




## Features

  * **Multiple OpenAI Keys** \- You can use multiple OpenAI keys. The API will randomly choose one of the keys to use.
  * **Moderation** \- The API has a built-in moderation system that will automatically check the prompt before sending it to OpenAI API (To prevent OpenAI terminate the account for violating OpenAI's policy).
  * **Streaming Response** \- The API supports streaming response, so you can get the response as soon as it's available.
  * **Same as Official** \- The API has the same endpoints as the official API, so you can use the same code to access the API (even the official OpenAI libraries)
  * **Free** \- The API is free to use through our hosted API (You can also self-host the API if you want).



**Note:** Self-hosting it isn't free, you need to use your OpenAI Account credit.

## How to use ChatGPT API Reverse Proxy

You can use ChatGPT API Reverse Proxy by choosing one of the following methods:

  * Self-Host Your Own API
  * Use Our Hosted API



‌

# Self-Host Your Own API

To self-host your own ChatGPT API, you can use the following steps:

  1. [Create an OpenAI API Key](https://platform.openai.com/account/api-keys)
  2. Clone this repository and install the dependencies:


    
    
    git clone https://github.com/PawanOsman/ChatGPT.git
    cd ChatGPT
    npm install

  3. Set your OpenAI key and other configurations in the `config.js` file.
  4. Start the server:


    
    
    npm start

  4. Use the API by sending an HTTP request to the API endpoints for example:


    
    
    http://localhost:3000/v1/completions
    http://localhost:3000/v1/chat/completions

# Use Our Hosted API Reverse Proxy

To use our hosted ChatGPT API, you can use the following steps:

  1. Join our [Discord](https://discord.pawan.krd) server.
  2. Get your API key from the `#Bot` channel by sending `/key` command.
  3. Use the API Key in your requests to the following endpoints.



## Text Completion:
    
    
    https://api.pawan.krd/v1/completions

### Example: [OpenAI Docs](https://platform.openai.com/docs/api-reference/completions)
    
    
    curl --location 'https://api.pawan.krd/v1/completions' \
    --header 'Authorization: Bearer pk-***[OUR_API_KEY]***' \
    --header 'Content-Type: application/json' \
    --data '{
        "model": "text-davinci-003",
        "prompt": "Human: Hello\\nAI:",
        "temperature": 0.7,
        "max_tokens": 256,
        "stop": [
            "Human:",
            "AI:"
        ]
    }'

## Chat Completion (ChatGPT):
    
    
    https://api.pawan.krd/v1/chat/completions

### Example: [OpenAI Docs](https://platform.openai.com/docs/api-reference/chat)
    
    
    curl --location 'https://api.pawan.krd/v1/chat/completions' \
    --header 'Authorization: Bearer pk-***[OUR_API_KEY]***' \
    --header 'Content-Type: application/json' \
    --data '{
        "model": "gpt-3.5-turbo",
        "max_tokens": 100,
        "messages": [
            {
                "role": "system",
                "content": "You are an helpful assistant."
            },
            {
                "role": "user",
                "content": "Who are you?"
            }
        ]
    }'

## Image Generation (DALL-E):
    
    
    https://api.pawan.krd/v1/images/generations

### Example: [OpenAI Docs](https://platform.openai.com/docs/api-reference/images)
    
    
    curl --location 'https://api.pawan.krd/v1/images/generations' \
    --header 'Authorization: Bearer pk-***[OUR_API_KEY]***' \
    --header 'Content-Type: application/json' \
    --data '{
        "prompt": "a photo of a happy corgi puppy sitting and facing forward, studio light, longshot.",
        "n": 1,
        "size": "1024x1024"
    }'

## Examples using OpenAI libraries

You can use the same code to access the API using the official OpenAI libraries, the only difference is that you need to change the API key and the API base URL.

Examples are for text completion, but you can use the same code for chat completion and image generation.

### Python

You need to add the following lines before your code to use the API:
    
    
    import openai
    
    openai.api_key = 'pk-**********************************************'
    openai.api_base = 'https://api.pawan.krd/v1'

Example code:
    
    
    import openai
    
    openai.api_key = 'pk-**********************************************'
    openai.api_base = 'https://api.pawan.krd/v1'
    
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Human: Hello\nAI:",
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["Human: ", "AI: "]
    )
    
    print(response.choices[0].text)

### Node.js

You need to add the following lines before your code to use the API:
    
    
    import { Configuration, OpenAIApi } from "openai";
    
    const configuration = new Configuration({
    	apiKey: "pk-**********************************************",
    	basePath: "https://api.pawan.krd/v1",
    });

Example code:
    
    
    import { Configuration, OpenAIApi } from "openai";
    
    const configuration = new Configuration({
    	apiKey: "pk-**********************************************",
    	basePath: "https://api.pawan.krd/v1",
    });
    
    const openai = new OpenAIApi(configuration);
    
    const response = await openai.createCompletion({
    	model: "text-davinci-003",
    	prompt: "Human: Hello\nAI:",
    	temperature: 0.7,
    	max_tokens: 256,
    	top_p: 1,
    	frequency_penalty: 0,
    	presence_penalty: 0,
    	stop: ["Human: ", "AI: "],
    });
    
    console.log(response.data.choices[0].text);

# License

This project is licensed under the MIT License - see the [LICENSE](/PawanOsman/ChatGPT/blob/main/LICENSE) file for details.

ChatGPT Clone Live Demo Video Important Notice Donation Join our discord server GPT-4 Using Docker Method I Clone this repository to your local machine Navigate to the project directory Build the image Run the app Open your web browser and go Method II Or you can use docker hub without cloning or building; Pull the image from Docker Hub Run the app Open your web browser and go Prerequisites Get Started Enable sqlite3 Clone this repository to your local machine Navigate to the project directory Install OrhanErday/OpenAI Set your OpenAI API key as the $open_ai_key variable in event-stream.php Start the PHP built-in web server Open your web browser and go to http://localhost:8000 You should now see the ChatGPT clone interface, where you can chat with the OpenAI language model. Chat History Credits

##  README.md

# ChatGPT Clone

[![ezgif-1-92e240a6d3](https://user-images.githubusercontent.com/22305274/220125119-ccbdb855-bdb9-476f-8f5f-f5d5530f0a24.gif)](https://user-images.githubusercontent.com/22305274/220125119-ccbdb855-bdb9-476f-8f5f-f5d5530f0a24.gif) [ ![ezgif-1-92e240a6d3](https://user-images.githubusercontent.com/22305274/220125119-ccbdb855-bdb9-476f-8f5f-f5d5530f0a24.gif) ](https://user-images.githubusercontent.com/22305274/220125119-ccbdb855-bdb9-476f-8f5f-f5d5530f0a24.gif) [ ](https://user-images.githubusercontent.com/22305274/220125119-ccbdb855-bdb9-476f-8f5f-f5d5530f0a24.gif)

This project is a ChatGPT clone that allows users to chat with an AI language model trained by OpenAI. It's powered by the github.com/orhanerday/OpenAI php library, which provides an easy-to-use interface for communicating with the OpenAI API.

[![Image](https://user-images.githubusercontent.com/22305274/219878523-6d8be435-35df-4cce-b2cd-52334f9e7f12.png)](https://user-images.githubusercontent.com/22305274/219878523-6d8be435-35df-4cce-b2cd-52334f9e7f12.png)

### Live Demo Video

  
ChatGPT_Clone-vimeo-800126555-hls-akfire_interconnect_quic_sep-436.mp4

# Important Notice

This project was created to highlight the [Stream Example](https://github.com/orhanerday/open-ai#stream-example) feature of [OpenAI GPT-3 Api Client in PHP by Orhan Erday](https://github.com/orhanerday/open-ai), please don't have too high expectations about the project.

## Donation

[![Buy Me A Coffee](https://camo.githubusercontent.com/c3f856bacd5b09669157ed4774f80fb9d8622dd45ce8fdf2990d3552db99bd27/68747470733a2f2f7777772e6275796d6561636f666665652e636f6d2f6173736574732f696d672f637573746f6d5f696d616765732f6f72616e67655f696d672e706e67)](https://www.buymeacoffee.com/orhane)

## Join our discord server

[![Discord Banner 2](https://camo.githubusercontent.com/97864a27a78be577b83056397113f4b4c98ece0d427ce71eceb46f98ecb5f5e9/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f313034373037343537323438383431373333302f7769646765742e706e673f7374796c653d62616e6e657232)](https://camo.githubusercontent.com/97864a27a78be577b83056397113f4b4c98ece0d427ce71eceb46f98ecb5f5e9/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f313034373037343537323438383431373333302f7769646765742e706e673f7374796c653d62616e6e657232)

[Click here to join the Discord server](https://discord.gg/xpGUD528XJ)

## GPT-4

Change model at `event-stream.php`
    
    
    ....
    $chat = $open_ai->chat([
        'model' => 'gpt-4',
    
    ....

## Using Docker

* * *

> #### Method I

#### Clone this repository to your local machine
    
    
    git clone https://github.com/orhanerday/ChatGPT.git

#### Navigate to the project directory
    
    
    cd ChatGPT

#### Build the image
    
    
    docker build -t chatgpt .

#### Run the app
    
    
    docker run -p 8000:8000 -e OPENAI_API_KEY=sk-o7hL4nCDcjw chatgpt

#### Open your web browser and go

<http://localhost:8000>

* * *

> #### Method II

### _Or_ you can use docker hub without cloning or building;

#### Pull the image from Docker Hub
    
    
    docker pull orhan55555/chatgpt

#### Run the app
    
    
    docker run -p 8000:8000 -e OPENAI_API_KEY=sk-o7hL4nCDcjw orhan55555/chatgpt

#### Open your web browser and go

<http://localhost:8000>

* * *

## Prerequisites

Before running this project, you should have the following:

  * PHP 7.4 or later with SQLite3 enabled
  * Composer
  * An OpenAI API key (which should be set to the $open_ai_key variable in event-stream.php) Getting Started



## Get Started

### Enable sqlite3

  * Open the php.ini file. This file is usually located in the PHP installation directory.

  * Find the following line: ;extension=php_sqlite3.dll

  * Remove the semicolon at the beginning of the line to uncomment it.

  * Save the file.

  * Restart the web server.

  * ### Clone this repository to your local machine



    
    
    git clone https://github.com/orhanerday/ChatGPT.git

  * ### Navigate to the project directory



    
    
    cd ChatGPT

  * ### Install OrhanErday/OpenAI



    
    
    composer require orhanerday/open-ai

  * ### Set your OpenAI API key as the `$open_ai_key` variable in `event-stream.php`



    
    
    $open_ai_key = ""; 

  * ### Start the PHP built-in web server



    
    
    php -S localhost:8000 -t .

  * ### Open your web browser and go to <http://localhost:8000>

  * ### You should now see the ChatGPT clone interface, where you can chat with the OpenAI language model.




## Chat History

This project saves chat history using cookies by default. If you want to change this to use authentication instead, you can modify the code in index.php to save chat history in a database or other storage mechanism.

## Credits

This project is powered by the github.com/orhanerday/OpenAI php library, which provides an easy-to-use interface for communicating with the OpenAI API.

🍬ChatGPT (and GPT4) Wrapper🍬 Welcome! Highlights How it works Requirements Installation Code From packages From source (recommended for development) Backend API (REST-based): DEFAULT Database configuration Initial user creation and login Setting the default model Playwright (browser-based): DEPRECATED Notes for Windows users Configuration Editing the configuration for the current profile Templates (alpha, subject to change) Builtin variables Front matter Plugins (alpha, subject to change) Using plugins Core plugins: Writing plugins Tutorials: Usage Shell Command line arguments One-shot mode Interactive mode Python Flask API (experimental) Docker (experimental) Test suite Troubleshooting OpenAI system issues Playwright (browser-based) backend issues Upgrading: Via pip Via git GPT4 API backend Method 1: Set the default user model Method 2: Dynamically switch Playwright (browser-based) backend: DEPRECATED Method 1: Command line argument Method 2: Modify the config.yaml file Method 3: Dynamically switch Python module Projects built with chatgpt-wrapper Contributing License Acknowledgments Star History

##  README.md

# 

🍬ChatGPT (and GPT4) Wrapper🍬

## Welcome!

What would you like to do?

  * Learn about the project
  * Install the wrapper
  * Learn more about configuration/features
  * Learn how to use it
  * Troubleshoot common issues
  * Upgrade the wrapper
  * Using GPT4
  * [Report a bug](/mmabrouk/chatgpt-wrapper/blob/main/ISSUES.md)
  * [Get support](/mmabrouk/chatgpt-wrapper/blob/main/SUPPORT.md)



ChatGPT Wrapper is an open-source unofficial **Power CLI** , **Python API** and **Flask API** that lets you interact programmatically with ChatGPT/GPT4.

## Highlights

🤖 The ChatGPT Wrapper lets you use the powerful ChatGPT/GPT4 bot from the _command line.

💬 **Runs in Shell**. You can call and interact with ChatGPT/GPT4 in the terminal.

💻 **Supports official ChatGPT API**. Make API calls directly to the OpenAI ChatGPT endpoint (all supported models accessible by your OpenAI account)

🐍 **Python API**. The ChatGPT Wrapper also has a Python library that lets you use ChatGPT/GPT4 in your Python scripts.

🔌 **Simple plugin architecture**. Extend the wrapper with custom functionality (alpha)

🐳 **Docker image**. The ChatGPT Wrapper is also available as a docker image. (experimental)

🧪 **Flask API**. You can use the ChatGPT Wrapper as an API. (experimental)

## How it works

Run an interactive CLI in the terminal:

[![kod](https://user-images.githubusercontent.com/4510758/212907070-602d61fe-708d-4a39-aaa2-0e84fcf88dcf.png)](https://user-images.githubusercontent.com/4510758/212907070-602d61fe-708d-4a39-aaa2-0e84fcf88dcf.png)

Or just get a quick response for one question:

[![kod\(1\)](https://user-images.githubusercontent.com/4510758/212906773-666be6fe-90e1-4f5e-b962-7748143bd744.png)](https://user-images.githubusercontent.com/4510758/212906773-666be6fe-90e1-4f5e-b962-7748143bd744.png)

See below for details on using ChatGPT as an API from Python.

## Requirements

To use this repository, you need `setuptools` installed. You can install it using `pip install setuptools`. Make sure that you have the last version of pip: `pip install --upgrade pip`

To use the 'chatgpt-api' backend (the default), you need a database backend (SQLite by default, any configurable in SQLAlchemy allowed).

## Installation

### Code

#### From packages

Install the latest version of this software directly from github with pip:
    
    
    pip install git+https://github.com/mmabrouk/chatgpt-wrapper

#### From source (recommended for development)

  * Install the latest version of this software directly from git: 
    
        git clone https://github.com/mmabrouk/chatgpt-wrapper.git

  * Install the the development package: 
    
        cd chatgpt-wrapper
    pip install -e .




### Backend

The wrapper works with several differnt backends to connect to the ChatGPT models, and installation is different for each backend.

#### API (REST-based): **DEFAULT**

  * Pros: 
    * Fast (many operations run locally for speed)
    * Simple API authentication
    * Full model customizations
    * You control your data
  * Cons: 
    * Only paid version available (as of this writing)
    * More complex setup suitable for technical users



Grab an API key from <https://platform.openai.com/account/api-keys>

Export the key into your local environment:
    
    
    export OPENAI_API_KEY=<API_KEY>

Windows users, see [here](https://www.computerhope.com/issues/ch000549.htm) for how to edit environment variables.

To tweak the configuration for the current profile, see Configuration

##### Database configuration

The API backend requires a database server to store conversation data. The wrapper leverages [SQLAlchemy](https://www.sqlalchemy.org/) for this.

The simplest supported database is SQLite (which is already installed on most modern operating systems), but you can use any database that is supported by SQLAlchemy.

Check the `database` setting from the `config` command above, which will show you the currently configured connection string for a default SQLite database.

If you're happy with that setting, nothing else needs to be done -- the database will be created automatically in that location when you run the program.

##### Initial user creation and login

Once the database is configured, run the program with no arguments:
    
    
    chatgpt

It will recognize no users have been created, and prompt you to create the first user:

  * Username: Required, no spaces or special characters
  * Email: Optional
  * Password: Optional, if not provided the user can log in without a password



Once the user is created, execute the `/login` command with the username:
    
    
    /login [username]

Once you're logged in, you have full access to all commands.

**IMPORTANT NOTE:** The user authorization system from the command line is 'admin party' -- meaning every logged in user has admin privileges, including editing and deleting other users.

##### Setting the default model

The default model used when communicating with the LLM service is configured per user.

To change the default model for a user:

  * Log in as the user
  * Run `/user-edit`
  * Step through the settings, including the one to set the default model



#### Playwright (browser-based): **DEPRECATED**

This backend is deprecated, and may be removed in a future release.

Support will not be provided for using the `ChatGPT` class of this backend directly.

  * Pros: 
    * Free or paid version available (as of this writing)
    * Fairly easy to set up for non-technical users
  * Cons: 
    * Slow (runs a full browser session)
    * Clunky authentication method
    * No model customizations
    * Third party controls your data



In your profile configuration file, you'll want to make sure the backend is set to the following in order to use the browser backend:
    
    
    backend: 'chatgpt-browser'

To tweak the configuration for the current profile, see Configuration

Install a browser in playwright (if you haven't already). The program will use firefox by default.
    
    
    playwright install firefox
    

Start up the program in `install` mode:
    
    
    chatgpt install

This opens up a browser window. Log in to ChatGPT in the browser window, walk through all the intro screens, then exit program.
    
    
    1> /exit

Restart the program without the `install` parameter to begin using it.
    
    
    chatgpt

### Notes for Windows users

Most other operating systems come with SQLite (the default database choice) installed, Windows may not.

If not, you can grab the 32-bit or 64-bit DLL file from <https://www.sqlite.org/download.html>, then place the DLL in `C:\Windows\System32` directory.

You also may need to install Python, if so grab the latest stable package from <https://www.python.org/downloads/windows/> \-- make sure to select the install option to `Add Python to PATH`.

For the `/editor` command to work, you'll need a command line editor installed and in your path. You can control which editor is used by setting the `EDITOR` environment variable to the name of the editor executable, e.g. `nano` or `vim`.

## Configuration

Run the program with the 'config' command:
    
    
    chatgpt config

This will show all the current configuration settings, the most important ones for installation are:

  * **Config dir:** Where configuration files are stored
  * **Current profile:** (shown in the 'Profile configuration' section)
  * **Config file:** The configuration file current being used
  * **Data dir:** The data storage directory



From a running `chatgpt` instance, execute `/config` to view the current configuration.

Configuration is optional, default values will be used if no configuration profile is provided. The default configuation settings can be seen in [config.sample.yaml](/mmabrouk/chatgpt-wrapper/blob/main/config.sample.yaml) \-- the file is commented with descriptions of the settings -- DON'T just copy this file as your configuration! Instead, use it as a reference to tweak the configuration to your liking.

_NOTE:_ Not all settings are available on all backends. See the example config for more information.

Command line arguments overrride custom configuration settings, which override default configuration settings.

### Editing the configuration for the current profile

  1. Start the program: `chatgpt`
  2. Open the profile's configuration file in an editor: `/config edit`
  3. Edit file to taste and save
  4. Restart the program



## Templates (alpha, subject to change)

The wrapper comes with a full template management system.

Templates allow storing text in template files, and quickly leveraging the contents as your user input.

Features:

  * Per-profile templates
  * Create/edit templates
  * `{{ variable }}` syntax substitution
  * Five different workflows for collecting variable values, editing, and running



See the various `/help template` commands for more information.

### Builtin variables

The wrapper exposes some builtin variables that can be used in templates:

  * `{{ clipboard }}` \- Insert the contents of the clipboard



### Front matter

Templates may include front matter (see [examples](/mmabrouk/chatgpt-wrapper/blob/main/examples/templates)).

These front matter attributes have special functionality:

  * title: Sets the title of new conversations to this value
  * description: Displayed in the output of `/templates`
  * model_customizations: A hash of model customizations to apply when the template is run (see `/config` for available model customizations)



All other attributes will be passed to the template as variable substitutions.

## Plugins (alpha, subject to change)

### Using plugins

  1. Place the plugin file in either:


  * The main `plugins` directory of this module
  * A `plugins` directory in your profile


  2. Enable the plugin in your configuration:
    
        plugins:
      enabled:
        # This is a list of plugins to enable, each list item should be the name of a plugin file, without the extension.
        - test

Note that setting `plugins.enabled` will overwrite the default enabled plugins. see `/config` for a list of default enabled plugins.




### Core plugins:

  * **test:** Test plugin, echos back the command you give it
  * **awesome:** Use a prompt from Awesome ChatGPT Prompts: <https://github.com/f/awesome-chatgpt-prompts>
  * **database:** Send natural language commands to a database **WARNING: POTENTIALLY DANGEROUS -- DATA INTEGRITY CANNOT BE GUARANTEED.**
  * **data_query:** Send natural language commands to a loaded file of structured data
  * **shell:** Transform natural language into a shell command, and optionally execute it **WARNING: POTENTIALLY DANGEROUS -- YOU ARE RESPONSIBLE FOR VALIDATING THE COMMAND RETURNED BY THE LLM, AND THE OUTCOME OF ITS EXECUTION.**
  * **zap:** Send natural language commands to Zapier actions: <https://nla.zapier.com/get-started/>



### Writing plugins

There is currently no developer documentation for writing plugins.

The `plugins` directory has some default plugins, examining those will give a good idea for how to design a new one.

Currently, plugins for the shell can only add new commands. An instantiated plugin has access to these resources:

  * `self.config`: The current instantiated Config object
  * `self.log`: The instantiated Logger object
  * `self.backend`: The instantiated backend
  * `self.shell`: The instantiated shell



## Tutorials:

  * **Newest Youtube video:** [ChatCPT intro, walkthrough of features](https://www.youtube.com/watch?v=Ho3-pzAf5e8)
  * Youtube Tutorial: [How To Use ChatGPT With Unity: Python And API Setup #2](https://www.youtube.com/watch?v=CthF8c8qk4c) includes a step by step guide to installing this repository on a windows machine
  * This [Blog post](https://medium.com/geekculture/using-chatgpt-in-python-eeaed9847e72) provides a visual step-by-step guide for installing this library.



## Usage

### Shell

#### Command line arguments

Run `chatgpt --help`

#### One-shot mode

To run the CLI in one-shot mode, simply follow the command with the prompt you want to send to ChatGPT:
    
    
    chatgpt Hello World!
    

#### Interactive mode

To run the CLI in interactive mode, execute it with no additional arguments:
    
    
    chatgpt
    

Once the interactive shell is running, you can see a list of all commands with:
    
    
    /help
    

...or get help for a specific command with:
    
    
    /help <command>
    

### Python

**IMPORTANT:** Use of browser backend's `ChatGPT` class has been deprectated, no support will be provided for this usage.

You can use the API backend's `OpenAIAPI` class to interact directly with the chat LLM.

Create an instance of the class and use the `ask` method to send a message to OpenAI and receive the response. For example:
    
    
    from chatgpt_wrapper import OpenAIAPI
    
    bot = OpenAIAPI()
    success, response, message = bot.ask("Hello, world!")
    if success:
        print(response)
    else:
        raise RuntimeError(message)

The ask method takes a string argument representing the message to send to the API, and returns a string representing the response received.

You may also stream the response as it comes in from the API in chunks using the `ask_stream` generator.

To pass custom configuration to ChatGPT, use the Config class:
    
    
    from chatgpt_wrapper import OpenAIAPI
    from chatgpt_wrapper.core.config import Config
    
    config = Config()
    config.set('browser.debug', True)
    bot = OpenAIAPI(config)
    success, response, message = bot.ask("Hello, world!")
    if success:
        print(response)
    else:
        raise RuntimeError(message)

### Flask API (experimental)

  * Run `python chatgpt_wrapper/gpt_api.py --port 5000` (default port is 5000) to start the server
  * Install pytest: `pip install pytest`
  * Test whether it is working using `pytest tests/integration/api_test.py`
  * See an example of interaction with api in `tests/integration/example_api_call.py`



## Docker (experimental)

Build a docker image for testing `chatgpt-wrapper`:

Make sure your OpenAI key has been exported into your host environment as `OPENAI_API_KEY`

Run the following commands:
    
    
    docker-compose build && docker-compose up -d
    docker exec -it chatgpt-wrapper-container /bin/bash -c "chatgpt"

Follow the instructions to create the first user.

Enjoy the chat!

## Test suite

The project uses [Pytest](https://docs.pytest.org).
    
    
    pip install pytest
    

To run all tests:
    
    
    pytest
    

## Troubleshooting

### OpenAI system issues

**Oftentimes issues are related to upstream service problems with OpenAI, so please check<https://status.openai.com> before concluding there's an issue with this codebase!**

### Playwright (browser-based) backend issues

It's possible that:

  1. Your session has gone stale: Try issuing a `/session` command to refresh it
  2. Your browser session information is corrupted: Try `chatgpt reinstall` and go through the login process again
  3. You're running an outdated version of this project, or one of its dependencies: Completely reinstall the project and its dependencies
  4. You're running into geolocation restrictions in OpenAI's security systems: Try proxying your requests through a VPN server in the US.



## Upgrading:

### Via pip

Until an official release exists, you'll need to uninstall and reinstall:
    
    
    pip uninstall -y chatGPT
    pip install chatGPT

### Via git

If the package was installed via `pip install -e`, simply pull in the latest changes from the repository:
    
    
    git pull

## GPT4

### API backend

To use GPT-4 with this backend, you must have been granted access to the model in your OpenAI account.

NOTE: If you have not been granted access, you'll probably see an error like this:
    
    
    InvalidRequestError(message='The model: `gpt-4` does not exist', param=None, code='model_not_found', http_status=404, request_id=None)
    

There is nothing this project can do to fix the error for you -- contact OpenAI and request GPT-4 access.

Follow one of the methods below to utilize GPT-4 in this backend:

##### Method 1: Set the default user model

See Setting the default model above.

##### Method 2: Dynamically switch

From within the shell, execute this command:
    
    
    /model gpt4
    

### Playwright (browser-based) backend: **DEPRECATED**

To use GPT-4 with this backend, you must have a ChatGPT-Plus subscription.

Follow one of the methods below to utilize GPT-4 in this backend:

##### Method 1: Command line argument

Enter the following command in your shell:
    
    
    chatgpt --model=gpt4
    

##### Method 2: Modify the `config.yaml` file

Update your `config.yaml` file to include the following line:
    
    
    chat:
      model: gpt4
    

Then start the program normally:
    
    
    chatgpt
    

##### Method 3: Dynamically switch

From within the shell, execute this command:
    
    
    /model gpt4
    

### Python module

To use GPT-4 within your Python code, follow the template below:
    
    
    from chatgpt_wrapper import OpenAIAPI
    from chatgpt_wrapper.core.config import Config
    
    config = Config()
    config.set('chat.model', 'gpt4')
    bot = OpenAIAPI(config)
    success, response, message = bot.ask("Hello, world!")

## Projects built with chatgpt-wrapper

  * [bookast: ChatGPT Podcast Generator For Books](https://github.com/SamMethnani/bookast)
  * [ChatGPT.el: ChatGPT in Emacs](https://github.com/joshcho/ChatGPT.el)
  * [ChatGPT Reddit Bot](https://github.com/PopDaddyGames/ChatGPT-RedditBot)
  * [Smarty GPT](https://github.com/citiususc/Smarty-GPT/tree/v1.1.0)
  * [ChatGPTify](https://github.com/idilsulo/ChatGPTify)
  * [selection-to-chatgpt](https://github.com/collin-murphy/selection-to-chatgpt)



## Contributing

We welcome contributions to ChatGPT Wrapper! If you have an idea for a new feature or have found a bug, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

  * This project is a modification from [Taranjeet](https://github.com/taranjeet/chatgpt-api) code which is a modification of [Daniel Gross](https://github.com/danielgross/whatsapp-gpt) code.



## Star History

[![Star History Chart](https://camo.githubusercontent.com/5560e15edd91b58824692edd11d4d5cfbd99f44c3d5f28f86c2833d9cbca0ef2/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6d6d6162726f756b2f636861746770742d7772617070657226747970653d44617465)](https://star-history.com/#mmabrouk/chatgpt-wrapper&Date)

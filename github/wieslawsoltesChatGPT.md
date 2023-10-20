ChatGPT Shortcuts Main Window Message Prompt Overriding OpenAI api url OpenAI ChatGPT web version import Build Dependencies .NET tool Usage Examples Settings file format COM Microsoft Work 2010 NuGet Docs License

##  README.md

# ChatGPT

[![Build Status](https://camo.githubusercontent.com/5b6a0564df88c011091411c291537a85b4de0c83fbfb5b4382500bcb020c1889/68747470733a2f2f6465762e617a7572652e636f6d2f776965736c6177736f6c7465732f4769744875622f5f617069732f6275696c642f7374617475732f776965736c6177736f6c7465732e436861744750543f7265706f4e616d653d776965736c6177736f6c74657325324643686174475054266272616e63684e616d653d6d61696e)](https://dev.azure.com/wieslawsoltes/GitHub/_build/latest?definitionId=109&repoName=wieslawsoltes%2FChatGPT&branchName=main) [![CI](https://github.com/wieslawsoltes/ChatGPT/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/wieslawsoltes/ChatGPT/actions/workflows/build.yml)

[![GitHub release](https://camo.githubusercontent.com/ee40f6a009b4559f8f8483a3e1e0d968a41b6cb6a75d04d8facdfd66384e45aa/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f776965736c6177736f6c7465732f436861744750542e737667)](https://github.com/wieslawsoltes/ChatGPT/releases) [![Github All Releases](https://camo.githubusercontent.com/bbe20203126cdabf371b702fb9663b6e721ffedb62f4ffd0a1c5642d6eae8281/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f776965736c6177736f6c7465732f436861744750542f746f74616c2e737667)](https://github.com/wieslawsoltes/ChatGPT/releases) [![Github Releases](https://camo.githubusercontent.com/7e5b11acdb710c4c54b7a2162fa3daa786f2fee35d92c99f4d00fe9592c8faa9/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f776965736c6177736f6c7465732f436861744750542f6c61746573742f746f74616c2e737667)](https://github.com/wieslawsoltes/ChatGPT/releases)

[![NuGet](https://camo.githubusercontent.com/c23569daa0464ebae746b6f286314269fb66aa50ddba69aa4d138f45e662c999/68747470733a2f2f696d672e736869656c64732e696f2f6e756765742f762f436861744750542e737667)](https://www.nuget.org/packages/ChatGPT) [![NuGet](https://camo.githubusercontent.com/e63a7393f9c419679e4f93331d7df1419e42c9ef0043e6e877804a8b5a3daf14/68747470733a2f2f696d672e736869656c64732e696f2f6e756765742f64742f436861744750542e737667)](https://www.nuget.org/packages/ChatGPT)

A ChatGPT C# client for graphical user interface runs on MacOS, Windows, Linux, Android, iOS and Browser. Powered by [Avalonia UI](https://avaloniaui.net/) framework.

To make the app work, you need to set the [OpenAI API key](https://beta.openai.com/account/api-keys) as the `OPENAI_API_KEY` environment variable or set API key directly in app settings.

You can try client using browser version [here](https://wieslawsoltes.github.io/ChatGPT/).

[![image](https://user-images.githubusercontent.com/2297442/224843834-a58190df-3bdb-4722-b737-94e7adc87805.png)](https://user-images.githubusercontent.com/2297442/224843834-a58190df-3bdb-4722-b737-94e7adc87805.png)

# Shortcuts

### Main Window

  * Ctrl+Shift+A - Toggle between transparent and acrylic blur window style.
  * Ctrl+Shift+S - Toggle between visible and hidden window state.



### Message Prompt

  * Enter - Send prompt.
  * Escape - Cancel edit.
  * F2 - Edit prompt.
  * Shift+Enter, Alt+Enter - Insert new line.



# Overriding OpenAI api url
    
    
    var chat = Defaults.Locator.GetService<IChatService>();
    chat.SetApiUrl("you api url");

# OpenAI ChatGPT web version import

You can import [OpenAI ChatGPT web version](https://chat.openai.com/chat) chats backup created using [this script](https://github.com/abacaj/chatgpt-backup).

# Build

  1. Install [.NET 7.0](https://dotnet.microsoft.com/en-us/download/dotnet/7.0)
  2. Run `dotnet workload install ios android wasm-tools` command
  3. `dotnet publish -c Release` command inside project directory (mobile/desktop) or `dotnet run` for desktop to just run



### Dependencies

  * [Avalonia](https://github.com/AvaloniaUI/Avalonia)
  * [Markdown.Avalonia](https://github.com/whistyun/Markdown.Avalonia)
  * [Avalonia.HtmlRenderer](https://github.com/AvaloniaUI/Avalonia.HtmlRenderer)
  * [CommunityToolkit.Mvvm](https://github.com/CommunityToolkit/dotnet)
  * [Microsoft.Extensions.DependencyInjection](https://www.nuget.org/packages/Microsoft.Extensions.DependencyInjection/)



# .NET tool

Install:
    
    
    dotnet tool install --global ChatGPT.CLI --version 1.0.0-preview.9

Uninstall:
    
    
    dotnet tool uninstall --global ChatGPT.CLI

  * [ChatGPT.CLI](https://www.nuget.org/packages/ChatGPT.CLI) \- An .NET ChatGPT tool.



### Usage
    
    
    ChatGPT.CLI:
    An .NET ChatGPT tool.
    
    Usage:
    ChatGPT.CLI [options]
    
    Options:
    -f, --inputFiles <inputfiles>              The relative or absolute path to the input files
    -d, --inputDirectory <inputdirectory>      The relative or absolute path to the input directory
    -o, --outputDirectory <outputdirectory>    The relative or absolute path to the output directory
    --outputFiles <outputfiles>                The relative or absolute path to the output files
    -p, --pattern <pattern>                    The search string to match against the names of files in the input directory
    -r, --recursive                            Recurse into subdirectories of input directory search
    -e, --extension <extension>                The output file extension
    -s, --settingsFile <settingsfile>          The relative or absolute path to the settings file
    --temperature <temperature>                What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
    --topP <topp>                              An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
    --presencePenalty <presencepenalty>        Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
    --frequencyPenalty <frequencypenalty>      Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
    --maxTokens <maxtokens>                    The maximum number of tokens to generate in the chat completion.
    --apiKey <apikey>                          Override OpenAI api key. By default OPENAI_API_KEY environment variable is used.
    --model <model>                            ID of the model to use. See the model endpoint compatibility table for details on which models work with the Chat API.
    --directions <directions>                  The system message (directions) helps set the behavior of the assistant. Typically, a conversation is formatted with a system message first, followed by alternating user and assistant messages.
    -t, --threads <threads>                    The number of parallel job threads
    --quiet                                    Set verbosity level to quiet
    --version                                  Show version information
    -?, -h, --help                             Show help and usage information
    

### Examples

  * Using .NET tool `chatgpt` command:



C# to VB
    
    
    chatgpt -d ./ -e vb -p *.cs --directions "You are C# to VB conversion expert. Convert input code from C# to VB. Write only converted code."

C# to F#
    
    
    chatgpt -d ./ -e fs -p *.cs --directions "You are C# to F# conversion expert. Convert input code from C# to F#. Write only code."

Refactor C# code
    
    
    chatgpt -d ./ -e cs -p *.cs --directions "You are C# expert. Refactor C# code to use fluent api. Write only code."

Write API documentation
    
    
    chatgpt -d ./ -e md -p *.cs --directions "You are a technical documentation writer. Write API documentation for C# code. If XML docs are missing write them."

  * Run from source



C# to VB
    
    
    dotnet run -- -d ./ -e vb -p *.cs --directions "You are C# to VB conversion expert. Convert input code from C# to VB. Write only converted code."

C# to F#
    
    
    dotnet run -- -d ./ -e fs -p *.cs --directions "You are C# to F# conversion expert. Convert input code from C# to F#. Write only code."

Write API documentation
    
    
    dotnet run -- -d ./ -e md -p *.cs --directions "You are a technical documentation writer. Write API documentation for C# code. If XML docs are missing write them."

### Settings file format
    
    
    {
        "temperature": 0.7,
        "top_p": 1,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "maxTokens": 2000,
        "apiKey": "",
        "model": "gpt-3.5-turbo",
        "directions": "You are a helpful assistant."
    }

# COM

In the build release directory `ChatGPT\ChatGptCom\bin\Release\net462\` run following command to register `ChatGptCom.dll`.

32-bit
    
    
    c:\Windows\Microsoft.NET\Framework\v4.0.30319\regasmm.exe /codebase /tlb ChatGptCom.dll
    

64-bit
    
    
    c:\Windows\Microsoft.NET\Framework64\v4.0.30319\regasm.exe /codebase /tlb ChatGptCom.dll
    

### Microsoft Work 2010

Add `ChatGPT\ChatGptCom\bin\Release\net462\ChatGptCom.tlb` to `References` using `Tools > References...` menu in `Microsoft Visual Basic for Applications`.
    
    
    Option Explicit
    
    Private WithEvents m_translateSource As Chat
    Private WithEvents m_demoSource As Chat
    Dim OriginalSelection As Range
    
    Sub TranslateSelection()
        Set OriginalSelection = Selection.Range
        Dim ProcessedText As String
        ProcessedText = OriginalSelection.Text
        m_translateSource.AskAsync "You are a professional translator to English. I will provide text and you will translate it to English.", ProcessedText
    End Sub
    
    Sub Translate_Initialize()
        Set m_translateSource = New ChatGptCom.Chat
    End Sub
    
    Sub m_translateSource_OnSendCompleted()
        OriginalSelection.Text = m_translateSource.Result
    End Sub
    
    Sub Chat_Initialize()
        Set m_demoSource = New ChatGptCom.Chat
    End Sub
    
    Sub Chat_Send()
        m_demoSource.AskAsync "You are a professional translator to English.", "To jest rewolucja szutcznej inteligencji! VBA na zawsze!"
    End Sub
    
    Sub m_demoSource_OnSendCompleted()
        MsgBox m_demoSource.Result
    End Sub
    
    Sub ChatGpt()
        Dim myObj As ChatGptCom.Chat
        Set myObj = New ChatGptCom.Chat
        myObj.AskAsync "You are a professional translato to English.", "Cześć, witamy z Office VBA"
    End Sub
    
    Sub GetEnvironmentVariable()
        Dim envVarName As String
        Dim envVarValue As String
        envVarName = "OPENAI_API_KEY"
        envVarValue = Environ(envVarName)
        MsgBox "The value of the " & envVarName & " environment variable is:" & vbCrLf & envVarValue
    End Sub

Chat form:
    
    
    Option Explicit
    
    Private WithEvents m_chatSource As Chat
    
    Private Sub UserForm_Initialize()
        Set m_chatSource = New ChatGptCom.Chat
        m_chatSource.Create "You are a helpful assistant", 2000, "gpt-3.5-turbo"
    End Sub
    
    Private Sub SendButton_Click()
        Dim MessageText As String
        MessageText = MessageTextBox.Text
        MessagesListBox.AddItem MessageText
        MessageTextBox.Text = ""
        m_chatSource.MessageAsync MessageText, "user", True
    End Sub
    
    Sub m_chatSource_OnSendCompleted()
        Dim MessageText As String
        MessageText = m_chatSource.Result
        MessagesListBox.AddItem MessageText
    End Sub

Chat form:
    
    
    Option Explicit
    
    Private WithEvents m_chatSource As Chat
    
    Private Sub UserForm_Initialize()
        Set m_chatSource = New ChatGptCom.Chat
        m_chatSource.Create "You are a helpful assistant", 2000, "gpt-3.5-turbo"
    End Sub
    
    Private Sub SendButton_Click()
        Dim MessageText As String
        MessageText = MessageTextBox.Text
        ChatTextBox.Text = ChatTextBox.Text & vbCrLf & MessageText
        MessageTextBox.Text = ""
        m_chatSource.MessageAsync MessageText, "user", True
    End Sub
    
    Sub m_chatSource_OnSendCompleted()
        Dim MessageText As String
        MessageText = m_chatSource.Result
        ChatTextBox.Text = ChatTextBox.Text & vbCrLf & MessageText
    End Sub

# NuGet

  * [ChatGPT](https://www.nuget.org/packages/ChatGPT) \- An OpenAI api library for .NET.
  * [ChatGPT.Core](https://www.nuget.org/packages/ChatGPT.Core) \- An OpenAI client core library for .NET.
  * [ChatGPT.UI](https://www.nuget.org/packages/ChatGPT.UI) \- An OpenAI client user interface library for .NET.
  * [ChatGPT.CLI](https://www.nuget.org/packages/ChatGPT.CLI) \- An .NET ChatGPT tool.
  * [ChatGptCom](https://www.nuget.org/packages/ChatGptCom) \- An OpenAI api library for .NET COM interop.



# Docs

  * [Guide Chat completions](https://platform.openai.com/docs/guides/chat)
  * [API Reference](https://platform.openai.com/docs/api-reference/chat)



# License

ChatGPT is licensed under the [MIT license](/wieslawsoltes/ChatGPT/blob/main/LICENSE).

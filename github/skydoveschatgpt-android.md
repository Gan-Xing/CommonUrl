📷 Previews 🛥 Stream Chat SDK 📲 Download APK 💻 How to build the project? ⚙️ How to run the application? 🛠 Tech Stack & Open Source Libraries 🏛️ Architecture Architecture Overview UI Layer Data Layer Modularization 💯 MAD Score 🤝 Contribution Find this repository useful? 💙 License

##  README.md

[![cover](https://user-images.githubusercontent.com/24237865/207994894-0cd5307b-f62e-4c38-be89-610a3ed459c0.jpg)](https://user-images.githubusercontent.com/24237865/207994894-0cd5307b-f62e-4c38-be89-610a3ed459c0.jpg)

[![License](https://camo.githubusercontent.com/2a2157c971b7ae1deb8eb095799440551c33dcf61ea3d965d86b496a5a65df55/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d417061636865253230322e302d626c75652e737667)](https://opensource.org/licenses/Apache-2.0) [![API](https://camo.githubusercontent.com/e4be58c2eb500c8634ceff111c34f70b52db29ed45acc60eaf229098fddc801c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4150492d32312532422d627269676874677265656e2e7376673f7374796c653d666c6174)](https://android-arsenal.com/api?level=21) [![Build Status](https://github.com/skydoves/chatgpt-android/actions/workflows/android.yml/badge.svg)](https://github.com/skydoves/chatgpt-android/actions/workflows/android.yml) [![Profile](https://camo.githubusercontent.com/00f0582ddd6c97886d8d85d82bb6ca1728554b3341bebd2059252426029744f3/68747470733a2f2f736b79646f7665732e6769746875622e696f2f6261646765732f736b79646f7665732e737667)](https://github.com/skydoves)

**ChatGPT Android** demonstrates [OpenAI's ChatGPT](https://chat.openai.com/chat) on Android with [Stream Chat SDK for Compose](https://getstream.io/chat/sdk/compose?utm_source=Github&utm_medium=Github_Repo_Content_Ad&utm_content=Developer&utm_campaign=Github_Dec2022_Jaewoong_ChatGPT&utm_term=DevRelOss).

The purpose of this repository is to demonstrate below:

  * Demonstrates [ChatGPT](https://chat.openai.com/chat)'s unofficial APIs.
  * Implementing entire UI elements with Jetpack Compose.
  * Implementation of Android architecture components with Jetpack libraries such as Hilt and AppStartup.
  * Performing background tasks with Kotlin Coroutines.
  * Integrating chat systems with Stream Chat SDK for real-time event handling.



[![Screenshot 2023-03-14 at 8 11 41 PM](https://user-images.githubusercontent.com/24237865/224983937-287075d3-474a-4aeb-9c6c-9d0605a6eecb.png)](https://user-images.githubusercontent.com/24237865/224983937-287075d3-474a-4aeb-9c6c-9d0605a6eecb.png)

## 📷 Previews

[![drawing](/skydoves/chatgpt-android/raw/main/previews/preview0.png)](/skydoves/chatgpt-android/blob/main/previews/preview0.png) [![drawing](/skydoves/chatgpt-android/raw/main/previews/preview1.png)](/skydoves/chatgpt-android/blob/main/previews/preview1.png) [![drawing](/skydoves/chatgpt-android/raw/main/previews/preview2.gif)](/skydoves/chatgpt-android/blob/main/previews/preview2.gif) [ ![drawing](https://github.com/skydoves/chatgpt-android/raw/main/previews/preview2.gif) ](https://github.com/skydoves/chatgpt-android/blob/main/previews/preview2.gif) [ ](https://github.com/skydoves/chatgpt-android/blob/main/previews/preview2.gif)   


[ ![](https://user-images.githubusercontent.com/24237865/138428440-b92e5fb7-89f8-41aa-96b1-71a5486c5849.png) ](https://getstream.io/chat/sdk/compose?utm_source=Github&utm_medium=Github_Repo_Content_Ad&utm_content=Developer&utm_campaign=Github_Dec2022_Jaewoong_ChatGPT&utm_term=DevRelOss)

## 🛥 Stream Chat SDK

**ChatGPT Android** is built with **[Stream Chat SDK for Compose](https://getstream.io/chat/sdk/compose?utm_source=Github&utm_medium=Github_Repo_Content_Ad&utm_content=Developer&utm_campaign=Github_Dec2022_Jaewoong_ChatGPT&utm_term=DevRelOss)** to implement messaging systems. If you’re interested in adding powerful In-App Messaging to your app, check out the **[Android Chat Messaging Tutorial](https://getstream.io/tutorials/android-chat?utm_source=Github&utm_medium=Github_Repo_Content_Ad&utm_content=Developer&utm_campaign=Github_Dec2022_Jaewoong_ChatGPT&utm_term=DevRelOss)**!

  * [Stream Chat SDK for Android on GitHub](https://github.com/getStream/stream-chat-android)
  * [Android Samples for Stream Chat SDK on GitHub](https://github.com/getStream/android-samples)
  * [Stream Chat Compose UI Componenets Guidelines](https://getstream.io/chat/docs/sdk/android/compose/overview/)



## 📲 Download APK

Go to the [Releases](https://github.com/skydoves/chatgpt-android/releases) to download the latest APK.

> Note: This app is using unofficial APIs, so normally it takes 10~15 seconds to get the entire response and the app might not work as your expected anytime.

## 💻 How to build the project?

To build this project properly, you should follow the instructions below:

  1. Go to the **[Stream login page](https://getstream.io/try-for-free?utm_source=Github&utm_medium=Github_Repo_Content_Ad&utm_content=Developer&utm_campaign=Github_Dec2022_Jaewoong_ChatGPT&utm_term=DevRelOss)**.
  2. If you have your GitHub account, click the **SIGN UP WITH GITHUB** button and you can sign up within a couple of seconds.



[![stream](/skydoves/chatgpt-android/raw/main/figures/stream0.png)](/skydoves/chatgpt-android/blob/main/figures/stream0.png)

  3. If you don't have a GitHub account, fill in the inputs and click the **START FREE TRIAL** button.
  4. Go to the **[Dashboard](https://dashboard.getstream.io?utm_source=Github&utm_medium=Github_Repo_Content_Ad&utm_content=Developer&utm_campaign=Github_Dec2022_Jaewoong_ChatGPT&utm_term=DevRelOss)** and click the **Create App** button like the below.



[![stream](/skydoves/chatgpt-android/raw/main/figures/stream1.png)](/skydoves/chatgpt-android/blob/main/figures/stream1.png)

  5. Fill in the blanks like the below and click the **Create App** button.



[![stream](/skydoves/chatgpt-android/raw/main/figures/stream2.png)](/skydoves/chatgpt-android/blob/main/figures/stream2.png)

  6. You will see the **Key** like the figure below and then copy it.



[![stream](/skydoves/chatgpt-android/raw/main/figures/stream3.png)](/skydoves/chatgpt-android/blob/main/figures/stream3.png)

  7. Add the key on your `local.properties` file on the project (Android Studio) like the below.



[![stream](/skydoves/chatgpt-android/raw/main/figures/stream5.png)](/skydoves/chatgpt-android/blob/main/figures/stream5.png)
    
    
    STREAM_CHAT_SDK=..

  8. Go to your **[Dashboard](https://dashboard.getstream.io?utm_source=Github&utm_medium=Github_Repo_Content_Ad&utm_content=Developer&utm_campaign=Github_Dec2022_Jaewoong_ChatGPT&utm_term=DevRelOss)** again and click your App.

  9. In the **Overview** menu, you can find the **Authentication** category by scrolling to the middle of the page.

  10. Switch on the **Disable Auth Checks** option and click the **Submit** button like the figure below.




[![stream](/skydoves/chatgpt-android/raw/main/figures/stream4.png)](/skydoves/chatgpt-android/blob/main/figures/stream4.png)

  11. Click the **Explorer** tab on the left side menu.

  12. Click **users** -> **Create New User** button sequentially and add fill in the user like the below:




[![stream](/skydoves/chatgpt-android/raw/main/figures/stream6.png)](/skydoves/chatgpt-android/blob/main/figures/stream6.png)

  * User Name: `Chat GPT`
  * User ID: `70ef052a-da88-4451-af92-99f7ed335a71`


  13. Build and run the project.



## ⚙️ How to run the application?

  1. Go to the [ChatGPT](https://chat.openai.com/chat) website and click the **Sign up** button.
  2. Create your account with your Google/Microsoft account or a manual email address like the one below:



[![login](/skydoves/chatgpt-android/raw/main/figures/login2.png)](/skydoves/chatgpt-android/blob/main/figures/login2.png)

  3. After finishing the additional steps, go back to the application screen like the below:



[![login](/skydoves/chatgpt-android/raw/main/figures/login0.png)](/skydoves/chatgpt-android/blob/main/figures/login0.png)

  4. Then click the **Log in** button and type your account information like the below. You must log in with your **Email address, not your Google or Microsoft account**.



[![login](/skydoves/chatgpt-android/raw/main/figures/login1.png)](/skydoves/chatgpt-android/blob/main/figures/login1.png)

  5. If you login correctly, you will get the success toast message and move to the channel list screen.



> Note: Before running the application, you must make sure you're in the [supported countries](https://platform.openai.com/docs/supported-countries).

## 🛠 Tech Stack & Open Source Libraries

  * Minimum SDK level 21.
  * 100% [Jetpack Compose](https://developer.android.com/jetpack/compose) based + [Coroutines](https://github.com/Kotlin/kotlinx.coroutines) \+ [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/) for asynchronous.
  * [Compose Chat SDK for Messaging](https://getstream.io/chat/sdk/compose?utm_source=Github&utm_medium=Github_Repo_Content_Ad&utm_content=Developer&utm_campaign=Github_Dec2022_Jaewoong_ChatGPT&utm_term=DevRelOss): The Jetpack Compose Chat Messaging SDK is built on a low-level chat client and provides modular, customizable Compose UI components that you can easily drop into your app.
  * Jetpack 
    * Compose: Android’s modern toolkit for building native UI.
    * ViewModel: UI related data holder and lifecycle aware.
    * App Startup: Provides a straightforward, performant way to initialize components at application startup.
    * Navigation: For navigating screens and [Hilt Navigation Compose](https://developer.android.com/jetpack/compose/libraries#hilt) for injecting dependencies.
    * Room: Constructs Database by providing an abstraction layer over SQLite to allow fluent database access.
    * [Hilt](https://dagger.dev/hilt/): Dependency Injection.
  * [Landscapist Glide](https://github.com/skydoves/landscapist#glide), [animation](https://github.com/skydoves/landscapist#animation), [placeholder](https://github.com/skydoves/landscapist#placeholder): Jetpack Compose image loading library that fetches and displays network images with Glide, Coil, and Fresco.
  * [Retrofit2 & OkHttp3](https://github.com/square/retrofit): Construct the REST APIs and paging network data.
  * [Sandwich](https://github.com/skydoves/Sandwich): Construct a lightweight and modern response interface to handle network payload for Android.
  * [Moshi](https://github.com/square/moshi/): A modern JSON library for Kotlin and Java.
  * [ksp](https://github.com/google/ksp): Kotlin Symbol Processing API.
  * [Balloon](https://github.com/skydoves/balloon): Modernized and sophisticated tooltips, fully customizable with an arrow and animations for Android.
  * [viewmodel-lifecycle](https://github.com/skydoves/viewmodel-lifecycle): ViewModel Lifecycle allows you to track and observe Jetpack's ViewModel lifecycle changes.
  * [StreamLog](https://github.com/GetStream/stream-log): A lightweight and extensible logger library for Kotlin and Android.
  * Baseline Profiles: To improve app performance by including a list of classes and methods specifications in your APK that can be used by Android Runtime.



## 🏛️ Architecture

**ChatGPT Android** follows the [Google's official architecture guidance](https://developer.android.com/topic/architecture).

[![architecture](/skydoves/chatgpt-android/raw/main/figures/figure0.png)](/skydoves/chatgpt-android/blob/main/figures/figure0.png)

**ChatGPT Android** was built with [Guide to app architecture](https://developer.android.com/topic/architecture), so it would be a great sample to show how the architecture works in real-world projects.  


The overall architecture is composed of two layers; UI Layer and the data layer. Each layer has dedicated components and they each have different responsibilities. The arrow means the component has a dependency on the target component following its direction.

### Architecture Overview

[![layer](/skydoves/chatgpt-android/raw/main/figures/figure1.png)](/skydoves/chatgpt-android/blob/main/figures/figure1.png)

Each layer has different responsibilities below. Basically, they follow [unidirectional event/data flow](https://developer.android.com/topic/architecture/ui-layer#udf).

### UI Layer

[![layer](/skydoves/chatgpt-android/raw/main/figures/figure2.png)](/skydoves/chatgpt-android/blob/main/figures/figure2.png)

The UI Layer consists of UI elements like buttons, menus, tabs that could interact with users and [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel) that holds app states and restores data when configuration changes.

### Data Layer

[![layer](/skydoves/chatgpt-android/raw/main/figures/figure3.png)](/skydoves/chatgpt-android/blob/main/figures/figure3.png)

The data Layer consists of repositories, which include business logic, such as querying data from the local database and requesting remote data from the network. It is implemented as an offline-first source of business logic and follows the [single source of truth](https://en.wikipedia.org/wiki/Single_source_of_truth) principle.  


For more information about the overall architecture, check out **[Build a Real-Time WhatsApp Clone With Jetpack Compose](https://getstream.io/blog/build-whatsapp-clone/)**.

## Modularization

[![modules](/skydoves/chatgpt-android/raw/main/figures/figure4.png)](/skydoves/chatgpt-android/blob/main/figures/figure4.png)

**ChatGPT Android** adopted modularization strategies below:

  * **Reusability** : Modulizing reusable codes properly enable opportunities for code sharing and limits code accessibility in other modules at the same time.

  * **Parallel Building** : Each module can be run in parallel and it reduces the build time.

  * **Decentralized focusing** : Each developer team can assign their dedicated module and they can focus on their own modules.




## 💯 MAD Score

[![summary](https://user-images.githubusercontent.com/24237865/158918011-bc766482-ec83-47dd-9237-d8a226cab263.png)](https://user-images.githubusercontent.com/24237865/158918011-bc766482-ec83-47dd-9237-d8a226cab263.png)

## 🤝 Contribution

Most of the features are not completed except the chat feature, so anyone can contribute and improve this project following the [Contributing Guideline](https://github.com/skydoves/chatgpt-android/blob/main/CONTRIBUTING.md).

## Find this repository useful? 💙

Support it by joining **[stargazers](https://github.com/skydoves/chatgpt-android/stargazers)** for this repository. ⭐   
Also, **[follow me](https://github.com/skydoves)** on GitHub for my next creations! 🤩

# License
    
    
    Designed and developed by 2022 skydoves (Jaewoong Eum)
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
       http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

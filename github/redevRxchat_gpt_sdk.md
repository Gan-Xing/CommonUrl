ChatGPT Application with flutter OpenAI Powerful Library Support GPT-4 Features Install Package Create OpenAI Instance Change Access Token Complete Text Chat Complete (GPT-4 and GPT-3.5) Q&A Generate Image With Prompt Edit Cancel Generate File Audio Embedding Fine Tune Moderations Model&Engine Flutter Example Video Tutorials

##  README.md

# ChatGPT Application with flutter

ChatGPT is a chat-bot launched by OpenAI in November 2022. It is built on top of OpenAI's GPT-3.5 family of large language models, and is fine-tuned with both supervised and reinforcement learning techniques.

# OpenAI Powerful Library Support GPT-4

  


[![GitHub commit activity](https://camo.githubusercontent.com/bb4ac309a5556466726cf66686fc60a24a57226850d24378586c67f79f053ad2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6d6d69742d61637469766974792f6d2f726564657652782f466c75747465722d43686174475054)](https://camo.githubusercontent.com/bb4ac309a5556466726cf66686fc60a24a57226850d24378586c67f79f053ad2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6d6d69742d61637469766974792f6d2f726564657652782f466c75747465722d43686174475054) [![GitHub contributors](https://camo.githubusercontent.com/d839709e2ad39b4f2238f6c3bd0032d542093a8bb700dc45d01711cec3cd1be1/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732f726564657652782f466c75747465722d43686174475054)](https://camo.githubusercontent.com/d839709e2ad39b4f2238f6c3bd0032d542093a8bb700dc45d01711cec3cd1be1/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732f726564657652782f466c75747465722d43686174475054) [![GitHub Repo stars](https://camo.githubusercontent.com/d42af1acb0f2e6a5cf0aa02ee99939614d5c7a002c0985738618adc205f7faa6/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f726564657652782f466c75747465722d436861744750543f7374796c653d736f6369616c)](https://camo.githubusercontent.com/d42af1acb0f2e6a5cf0aa02ee99939614d5c7a002c0985738618adc205f7faa6/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f726564657652782f466c75747465722d436861744750543f7374796c653d736f6369616c) [![GitHub Workflow Status](https://camo.githubusercontent.com/d030fb0c7eb51eb849dbe1cdb0408bd9e2a5c04e835152a03f1f0381d75ae05f/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f726564657652782f466c75747465722d436861744750542f646172742e796d6c3f6c6162656c3d7465737473)](https://camo.githubusercontent.com/d030fb0c7eb51eb849dbe1cdb0408bd9e2a5c04e835152a03f1f0381d75ae05f/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f726564657652782f466c75747465722d436861744750542f646172742e796d6c3f6c6162656c3d7465737473) [![GitHub](https://camo.githubusercontent.com/c6d503eade2a8db03c812e8c86327e9b91894e02177370805366437b3f45d1d6/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f726564657652782f466c75747465722d43686174475054)](https://camo.githubusercontent.com/c6d503eade2a8db03c812e8c86327e9b91894e02177370805366437b3f45d1d6/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f726564657652782f466c75747465722d43686174475054)

  


## Features

  * Install Package
  * Create OpenAI Instance
  * Change Access Token
  * Complete Text
    * Support Server Sent Event
  * Chat Complete GPT-4
    * Support GPT3.5 and GPT-4
    * Support Server Sent Event
  * Example Q&A
  * Generate Image With Prompt
  * Editing
  * Cancel Generate
  * File
  * Audio
  * Embedding
  * Fine-Tune
    * Support Server Sent Event
  * Moderations
  * Model And Engine
  * Flutter Code Example
  * Video Tutorial



## Install Package
    
    
    chat_gpt: 2.1.2

## Create OpenAI Instance

  * Parameter 
    * Token 
      * Your secret API keys are listed below. Please note that we do not display your secret API keys again after you generate them.
      * Do not share your API key with others, or expose it in the browser or other client-side code. In order to protect the security of your account, OpenAI may also automatically rotate any API key that we've found has leaked publicly.
      * <https://beta.openai.com/account/api-keys>
  * OrgId 
    * Identifier for this organization sometimes used in API requests
    * <https://beta.openai.com/account/org-settings>


    
    
    final openAI = OpenAI.instance.build(token: token,baseOption: HttpSetup(receiveTimeout: const Duration(seconds: 5)),isLogger: true);

## Change Access Token
    
    
    openAI.setToken('new-token');
    
    ///get toekn
    openAI.token;

## Complete Text

  * Text Complete API

    * Translate Method 
      * translateEngToThai
      * translateThaiToEng
      * translateToJapanese
    * Model 
      * kTranslateModelV3
      * kTranslateModelV2
      * kCodeTranslateModelV2 
        * Translate natural language to SQL queries.
        * Create code to call the Stripe API using natural language.
        * Find the time complexity of a function.
    * <https://beta.openai.com/examples>
  * Complete with Feature



    
    
      void _translateEngToThai() async{
      final request = CompleteText(
              prompt: translateEngToThai(word: _txtWord.text.toString()),
              max_tokens: 200,
              model: Model.textDavinci3);
    
      final response = await openAI.onCompletion(request: request);
      
      ///cancel request
      openAI.cancelAIGenerate();
      print(response);
    }

  * Complete with FutureBuilder


    
    
    Future<CTResponse?>? _translateFuture;
    
    _translateFuture = openAI.onCompletion(request: request);
    
    ///ui code
    FutureBuilder<CTResponse?>(
     future: _translateFuture,
     builder: (context, snapshot) {
       final data = snapshot.data;
       if(snapshot.connectionState == ConnectionState.done) return something 
       if(snapshot.connectionState == ConnectionState.waiting) return something
       return something
    })

  * GPT-3 with SSE


    
    
     void completeWithSSE() {
      final request = CompleteText(
              prompt: "Hello world", maxTokens: 200, model: Model.textDavinci3);
      openAI.onCompletionSSE(request: request).listen((it) {
        debugPrint(it.choices.last.text);
      });
    }

## Chat Complete (GPT-4 and GPT-3.5)

  * GPT-4


    
    
      void chatComplete() async {
        final request = ChatCompleteText(messages: [
          Map.of({"role": "user", "content": 'Hello!'})
        ], maxToken: 200, model: ChatModel.gpt_4);
    
        final response = await openAI.onChatCompletion(request: request);
        for (var element in response!.choices) {
          print("data -> ${element.message?.content}");
        }
      }

  * GPT-4 with SSE(Server Send Event)


    
    
     void chatCompleteWithSSE() {
      final request = ChatCompleteText(messages: [
        Map.of({"role": "user", "content": 'Hello!'})
      ], maxToken: 200, model: ChatModel.gpt_4);
    
      openAI.onChatCompletionSSE(request: request).listen((it) {
        debugPrint(it.choices.last.message?.content);
      });
    }

  * Support SSE(Server Send Event) 
    * GPT-3.5 Turbo


    
    
     void chatCompleteWithSSE() {
      final request = ChatCompleteText(messages: [
        Map.of({"role": "user", "content": 'Hello!'})
      ], maxToken: 200, model: ChatModel.chatGptTurbo);
    
      openAI.onChatCompletionSSE(request: request).listen((it) {
        debugPrint(it.choices.last.message?.content);
      });
    }

  * Chat Complete


    
    
      void chatComplete() async {
        final request = ChatCompleteText(messages: [
          Map.of({"role": "user", "content": 'Hello!'})
        ], maxToken: 200, model: ChatModel.chatGptTurbo0301);
    
        final response = await openAI.onChatCompletion(request: request);
        for (var element in response!.choices) {
          print("data -> ${element.message?.content}");
        }
      }

## Q&A

  * Example Q&A 
    * Answer questions based on existing knowledge.


    
    
    final request = CompleteText(prompt:'What is human life expectancy in the United States?'),
                    model: Model.textDavinci3, maxTokens: 200);
    
     final response = await openAI.onCompletion(request:request);

  * Request


    
    
    Q: What is human life expectancy in the United States?

  * Response


    
    
    A: Human life expectancy in the United States is 78 years.

## Generate Image With Prompt

  * Generate Image

    * prompt 
      * A text description of the desired image(s). The maximum length is 1000 characters.
    * n 
      * The number of images to generate. Must be between 1 and 10.
    * size 
      * The size of the generated images. Must be one of 256x256, 512x512, or 1024x1024.
    * response_format 
      * The format in which the generated images are returned. Must be one of url or b64_json.
    * user 
      * A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.
  *   * Generate with feature



    
    
      void _generateImage() {
      const prompt = "cat eating snake blue red.";
    
      final request = GenerateImage(prompt, 1,size: ImageSize.size256,
              response_format: Format.url);;
      final response = openAI.generateImage(request);
      print("img url :${response.data?.last?.url}");
    }

## Edit

  * Edit Prompt


    
    
    void editPrompt() async {
        final response = await openAI.editor.prompt(EditRequest(
            model: EditModel.textEditModel,
            input: 'What day of the wek is it?',
            instruction: 'Fix the spelling mistakes'));
    
        print(response.choices.last.text);
      }

  * Edit Image


    
    
     void editImage() async {
      final response = await openAI.editor.editImage(EditImageRequest(
              image: EditFile("${image?.path}", '${image?.name}'),
              mask: EditFile('file path', 'file name'),
              size: ImageSize.size1024,
              prompt: 'King Snake'));
    
      print(response.data?.last?.url);
    }

  * Variations


    
    
      void variation() async {
      final request =
      Variation(image: EditFile('${image?.path}', '${image?.name}'));
      final response = await openAI.editor.variation(request);
    
      print(response.data?.last?.url);
    }

## Cancel Generate

  * Stop Generate Prompt


    
    
    openAI.cancelAIGenerate();

  * Stop Edit 
    * image
    * prompt


    
    
    openAI.edit.cancelEdit();

  * Stop Embedding


    
    
    openAI.embed.cancelEmbedding();

  * Stop Audio 
    * translate
    * transcript


    
    
    openAI.audio.cancelAudio();

  * Stop File 
    * upload file
    * get file
    * delete file


    
    
    openAI.file.cancelFile();

## File

  * Get File


    
    
    void getFile() async {
      final response = await openAI.file.get();
      print(response.data);
    }

  * Upload File


    
    
    void uploadFile() async {
      final request = UploadFile(file: EditFile('file-path', 'file-name'),purpose: 'fine-tune');
      final response = await openAI.file.uploadFile(request);
      print(response);
    }

  * Delete File


    
    
      void delete() async {
      final response = await openAI.file.delete("file-Id");
      print(response);
    }

  * Retrieve File


    
    
      void retrieve() async {
      final response = await openAI.file.retrieve("file-Id");
      print(response);
    }

  * Retrieve Content File


    
    
      void retrieveContent() async {
      final response = await openAI.file.retrieveContent("file-Id");
      print(response);
    }

## Audio

  * Audio Translate


    
    
    void audioTranslate() async {
      final mAudio = File('mp3-path');
      final request =
      AudioRequest(file: EditFile(mAudio.path, 'name'), prompt: '...');
    
      final response = await openAI.audio.translate(request);
    }

  * Audio Transcribe


    
    
    void audioTranscribe() async {
      final mAudio = File('mp3-path');
      final request =
      AudioRequest(file: EditFile(mAudio.path, 'name'), prompt: '...');
    
      final response = await openAI.audio.transcribes(request);
    }

## Embedding

  * Embedding


    
    
    void embedding() async {
      final request = EmbedRequest(
              model: EmbedModel.embedTextModel,
              input: 'The food was delicious and the waiter');
    
      final response = await openAI.embed.embedding(request);
    
      print(response.data.last.embedding);
    }

## Fine Tune

  * Create Fine Tune


    
    
    void createTineTune() async {
      final request = CreateFineTune(trainingFile: 'The ID of an uploaded file');
      final response = await openAI.fineTune.create(request);
    }

  * Fine Tune List


    
    
     void tineTuneList() async {
        final response = await openAI.fineTune.list();
      }

  * Fine Tune List Stream (SSE)


    
    
     void tineTuneListStream() {
        openAI.fineTune.listStream('fineTuneId').listen((it) {
          ///handled data
        });
      }

  * Fine Tune Get by Id


    
    
    void tineTuneById() async {
        final response = await openAI.fineTune.retrieve('fineTuneId');
      }

  * Cancel Fine Tune


    
    
      void tineTuneCancel() async {
        final response = await openAI.fineTune.cancel('fineTuneId');
      }

  * Delete Fine Tune


    
    
     void deleteTineTune() async {
        final response = await openAI.fineTune.delete('model');
      }

## Moderations

  * Create Moderation


    
    
      void createModeration() async {
      final response = await openAI.moderation
              .create(input: 'input', model: ModerationModel.textLast);
    }

## Model&Engine

  * Model List 
    * List and describe the various models available in the API. You can refer to the Models documentation to understand what models are available and the differences between them.
    * <https://beta.openai.com/docs/api-reference/models>


    
    
    final models = await openAI.listModel();

  * Engine List 
    * Lists the currently available (non-finetuned) models, and provides basic information about each one such as the owner and availability.
    * <https://beta.openai.com/docs/api-reference/engines>


    
    
    final engines = await openAI.listEngine();

## Flutter Example
    
    
    class TranslateScreen extends StatefulWidget {
      const TranslateScreen({Key? key}) : super(key: key);
      @override
      State<TranslateScreen> createState() => _TranslateScreenState();
    }
    
    class _TranslateScreenState extends State<TranslateScreen> {
      /// text controller
      final _txtWord = TextEditingController();
    
      late OpenAI openAI;
    
      Future<CTResponse?>? _translateFuture;
      void _translateEngToThai() async {
        setState(() {
          final request = CompleteText(
                  prompt: translateEngToThai(word: _txtWord.text.toString()),
                  maxTokens: 200,
                  model: Model.textDavinci3);
          _translateFuture = openAI.onCompletion(request: request);
        });
      }
      
      @override
      void initState() {
        openAI = OpenAI.instance.build(
                token: token,
                baseOption: HttpSetup(
                        receiveTimeout: const Duration(seconds: 20),
                        connectTimeout: const Duration(seconds: 20)),
                isLog: true);
        super.initState();
      }
    
      @override
      Widget build(BuildContext context) {
        var size = MediaQuery.of(context).size;
        return Scaffold(
          backgroundColor: Colors.white,
          body: SingleChildScrollView(
            child: Center(
              child: Padding(
                padding: const EdgeInsets.symmetric(vertical: 16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    /**
                     * title translate
                     */
                    _titleCard(size),
                    /**
                     * input card
                     * insert your text for translate to th.com
                     */
                    _inputCard(size),
    
                    /**
                     * card input translate
                     */
                    _resultCard(size),
                    /**
                     * button translate
                     */
                    _btnTranslate()
                  ],
                ),
              ),
            ),
          ),
          bottomNavigationBar: _navigation(size),
        );
      }
    
      Widget _btnTranslate() {
        return Row(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            Padding(
                    padding: const EdgeInsets.only(right: 16.0),
                    child: MaterialButtonX(
                            message: "Translate",
                            height: 40.0,
                            width: 130.0,
                            color: Colors.blueAccent,
                            icon: Icons.translate,
                            iconSize: 18.0,
                            radius: 46.0,
                            onClick: () => _translateEngToThai())),
          ],
        );
      }
    
      Widget _resultCard(Size size) {
        return FutureBuilder<CTResponse?>(
                future: _translateFuture,
                builder: (context, snapshot) {
                  final text = snapshot.data?.choices.last.text;
                  return Container(
                    margin: const EdgeInsets.symmetric(vertical: 32.0),
                    padding: const EdgeInsets.symmetric(horizontal: 16.0),
                    alignment: Alignment.bottomCenter,
                    width: size.width * .86,
                    height: size.height * .3,
                    decoration: heroCard,
                    child: SingleChildScrollView(
                      child: Column(
                        children: [
                          Text(
                            text ?? 'Loading...',
                            style: const TextStyle(color: Colors.black, fontSize: 18.0),
                          ),
                          SizedBox(
                            width: size.width,
                            child: const Divider(
                              color: Colors.grey,
                              thickness: 1,
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(12.0),
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.end,
                              children: const [
                                Icon(
                                  Icons.copy_outlined,
                                  color: Colors.grey,
                                  size: 22.0,
                                ),
                                Padding(
                                  padding: EdgeInsets.symmetric(horizontal: 8.0),
                                  child: Icon(
                                    Icons.delete_forever,
                                    color: Colors.grey,
                                    size: 22.0,
                                  ),
                                )
                              ],
                            ),
                          )
                        ],
                      ),
                    ),
                  );
                });
      }
    
      Padding _navigation(Size size) {
        return Padding(
          padding: const EdgeInsets.symmetric(vertical: 16.0, horizontal: 18.0),
          child: Container(
            width: size.width * .8,
            height: size.height * .06,
            decoration: heroNav,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                Container(
                  padding: const EdgeInsets.all(4.0),
                  decoration: BoxDecoration(
                          color: Colors.indigoAccent,
                          borderRadius: BorderRadius.circular(50.0)),
                  child: const Icon(
                    Icons.translate,
                    color: Colors.white,
                    size: 22.0,
                  ),
                ),
                const Icon(
                  Icons.record_voice_over_outlined,
                  color: Colors.indigoAccent,
                  size: 22.0,
                ),
                const Icon(
                  Icons.favorite,
                  color: Colors.indigoAccent,
                  size: 22.0,
                ),
                const Icon(
                  Icons.person,
                  color: Colors.indigoAccent,
                  size: 22.0,
                )
              ],
            ),
          ),
        );
      }
    
      Widget _titleCard(Size size) {
        return Container(
          margin: const EdgeInsets.symmetric(vertical: 32.0),
          width: size.width * .86,
          height: size.height * .08,
          decoration: heroCard,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              Row(
                children: [
                  ClipRRect(
                    borderRadius: BorderRadius.circular(30),
                    child: Image.network(
                      "https://www.clipartmax.com/png/middle/200-2009207_francais-english-italiano-english-flag-icon-flat.png",
                      fit: BoxFit.cover,
                      width: 30.0,
                      height: 30.0,
                    ),
                  ),
                  const Padding(
                    padding: EdgeInsets.symmetric(horizontal: 4.0),
                    child: Text(
                      "Eng",
                      style: TextStyle(color: Colors.grey, fontSize: 12.0),
                    ),
                  ),
                  Transform.rotate(
                    angle: -pi / 2,
                    child: const Icon(
                      Icons.arrow_back_ios_new,
                      size: 16.0,
                      color: Colors.grey,
                    ),
                  )
                ],
              ),
              const Padding(
                padding: EdgeInsets.symmetric(horizontal: 12.0),
                child: Icon(
                  Icons.swap_horiz_outlined,
                  color: Colors.grey,
                  size: 22.0,
                ),
              ),
              Row(
                children: [
                  ClipRRect(
                    borderRadius: BorderRadius.circular(30),
                    child: Image.network(
                      "https://cdn-icons-png.flaticon.com/512/197/197452.png",
                      fit: BoxFit.cover,
                      width: 30.0,
                      height: 30.0,
                    ),
                  ),
                  const Padding(
                    padding: EdgeInsets.symmetric(horizontal: 4.0),
                    child: Text(
                      "Thai",
                      style: TextStyle(color: Colors.grey, fontSize: 12.0),
                    ),
                  ),
                  Transform.rotate(
                    angle: -pi / 2,
                    child: const Icon(
                      Icons.arrow_back_ios_new,
                      size: 16.0,
                      color: Colors.grey,
                    ),
                  )
                ],
              )
            ],
          ),
        );
      }
    
      Widget _inputCard(Size size) {
        return Container(
          padding: const EdgeInsets.symmetric(horizontal: 16.0),
          alignment: Alignment.bottomCenter,
          width: size.width * .86,
          height: size.height * .25,
          decoration: heroCard,
          child: SingleChildScrollView(
            child: Column(
              children: [
                TextField(
                  decoration: const InputDecoration(
                          border: InputBorder.none,
                          enabledBorder: InputBorder.none,
                          disabledBorder: InputBorder.none),
                  controller: _txtWord,
                  maxLines: 6,
                  textInputAction: TextInputAction.newline,
                  keyboardType: TextInputType.multiline,
                ),
                SizedBox(
                  width: size.width,
                  child: const Divider(
                    color: Colors.grey,
                    thickness: 1,
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(12.0),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: const [
                      Icon(
                        Icons.copy_outlined,
                        color: Colors.grey,
                        size: 22.0,
                      ),
                      Padding(
                        padding: EdgeInsets.symmetric(horizontal: 8.0),
                        child: Icon(
                          Icons.record_voice_over_outlined,
                          color: Colors.grey,
                          size: 22.0,
                        ),
                      )
                    ],
                  ),
                )
              ],
            ),
          ),
        );
      }
    }

[![](https://camo.githubusercontent.com/642d0eb9b2c9c8387d65286b12924b9fd6d29b8267abdf77065880e82304bb05/68747470733a2f2f73636f6e74656e742e666b6b63332d312e666e612e666263646e2e6e65742f762f7433392e33303830382d362f3332313935363330365f3532383437333836393231373633385f343935393633353233313537313039323635305f6e2e6a70673f5f6e635f6361743d313034266363623d312d37265f6e635f7369643d373330653134265f6e635f6f68633d59756d726d63664f376a414158394e3959676426746e3d615743696a46733049456551587a6645265f6e635f68743d73636f6e74656e742e666b6b63332d312e666e61266f683d30305f416643516b3965627a32716e506c3270736875676368446e6145584d506536726f675870647a6333554366636d67266f653d3633454637374534)](https://camo.githubusercontent.com/642d0eb9b2c9c8387d65286b12924b9fd6d29b8267abdf77065880e82304bb05/68747470733a2f2f73636f6e74656e742e666b6b63332d312e666e612e666263646e2e6e65742f762f7433392e33303830382d362f3332313935363330365f3532383437333836393231373633385f343935393633353233313537313039323635305f6e2e6a70673f5f6e635f6361743d313034266363623d312d37265f6e635f7369643d373330653134265f6e635f6f68633d59756d726d63664f376a414158394e3959676426746e3d615743696a46733049456551587a6645265f6e635f68743d73636f6e74656e742e666b6b63332d312e666e61266f683d30305f416643516b3965627a32716e506c3270736875676368446e6145584d506536726f675870647a6333554366636d67266f653d3633454637374534)

## Video Tutorials

  * [Flutter Chat bot](https://www.youtube.com/watch?v=qUEUMxGW_0Q&ab_channel=idealBy)

  * [Flutter Generate Image](https://www.youtube.com/watch?v=z25HfnEi2zQ&t=1s&ab_channel=idealBy)




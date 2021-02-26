# Pre-processor for NLP

[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/fpem123/pre-processor)

This project pre-processor web server for NLP.

### Module requirement

    num2words
    waitress
    Unidecode
    contractions
    flask
    spacy (and "en_core_web_sm" spacy model)


### How to use

    * First, Upload text file


### Pre-processing option

    space_normalizer: Whitespace normalization. (Including newline removal). No additional value required.

    to_capitalize: Capitalize only the first letter of the line, and change the rest to lowercase. No additional value required.  
    
    to_lower: Change all words to lowercase. No additional value required.

    accent: Replace accented characters like ï with regular characters. No additional value required.

    expander: Increases the abbreviation. (can't → can not). No additional value required.

    emoji_remover: Remove emojis. No additional value required.

    lemmatizer: Turns all words into basic form. (is -> be, bats -> bat). No additional value required.

    number_changer: Turn numbers into words. No additional value required.

    number_normalizer: Replace the number with another one you entered. Need additional value.

    short_line_remover: It also takes a number and removes the lines shorter than the number. Need additional value.

    short_word_remover: It also takes a number and removes words shorter than the number. Need additional value.
    
    full_stop_normalizer: It receives special characters and turns them all into dot. Need additional value.
    
    comma_normalizer: Receive special characters and turn them all into commas. Need additional value.

    special_remover: Receive the special characters to be deleted and delete them all. Need additional value.
    
    special_replacer: Input and replace special characters and words to be replaced. Need additional value, value2.

    word_replacer: Replace the word with another one you entered. Need additional value, value2.


### Post parameter

    text_file: Text file you want to pre-process.
    option: The pre-processing option.
    value: The value required by the specific option.
    value2: Second value required by specific option.

### Output foramt

    text/plain


## * With CLI *

### Input example

* space_normalizer


    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=space_normalizer" -F "text_file=@sample.txt;type=text/plain"


* to_capitalize 


    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=to_capitalize" -F "text_file=@sample.txt;type=text/plain"


* to_lower
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=to_lower" -F "text_file=@sample.txt;type=text/plain"


* accent
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=accent" -F "text_file=@sample.txt;type=text/plain"


* expander
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=expander" -F "text_file=@sample.txt;type=text/plain"


* emoji_remover
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=emoji_remover" -F "text_file=@sample.txt;type=text/plain"


* lemmatizer
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=lemmatizer" -F "text_file=@sample.txt;type=text/plain"


* number_changer
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=number_changer" -F "text_file=@sample.txt;type=text/plain"


* number_normalizer
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=number_normalizer" -F "value=number" -F "text_file=@sample.txt;type=text/plain"


* short_line_remover
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=short_line_remover" -F "value=3" -F "text_file=@sample.txt;type=text/plain"


* short_word_remover
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=short_word_remover" -F "value=3" -F "text_file=@sample.txt;type=text/plain"


* full_stop_normalizer
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=full_stop_normalizer" -F "value=;!?" -F "text_file=@sample.txt;type=text/plain"


* comma_normalizer
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=comma_normalizer" -F "value=&;-@" -F "text_file=@sample.txt;type=text/plain"


* special_remover
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=special_remover" -F "value=:;,-" -F "text_file=@sample.txt;type=text/plain"


* special_replacer
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=special_replacer" -F "value=&@" -F "value2=and" -F "text_file=@sample.txt;type=text/plain"


* word_replacer
  

    curl -X POST "https://master-pre-processor-fpem123.endpoint.ainize.ai/dpp" -H "accept: text/plain" -H "Content-Type: multipart/form-data" -F "option=word_replacer" -F "value=Orange" -F "value2=Apple" -F "text_file=@sample.txt;type=text/plain"



### Output example

Text_file
    
    Hello, guys my name is Kïm. And I have 10-blocks.
    I like         Orange🍊🍊🍊 & Banana🍌 @ peach🍑🍑 that yummy...!
    
    Okay; I love it. I can eat 23 oranges at same time.
    
    Oh.... you can't? sorry😢.

* space_normalizer
  

    Hello, guys my name is Kïm. And I have 10-blocks. I like Orange🍊🍊🍊 & Banana🍌 @ peach🍑🍑 that yummy...! Okay; I love it. I can eat 23 oranges at same time. Oh.... you can't? sorry😢.

* to_capitalize


    Hello, guys my name is kïm. and i have 10-blocks.
    I like         orange🍊🍊🍊 & banana🍌 @ peach🍑🍑 that yummy...!
    
    Okay; i love it. i can eat 23 oranges at same time.
    
    Oh.... you can't? sorry😢.

* to_lower
  

    hello, guys my name is kïm. and i have 10-blocks.
    i like         orange🍊🍊🍊 & banana🍌 @ peach🍑🍑 that yummy...!
    
    okay; i love it. i can eat 23 oranges at same time.
    
    oh.... you can't? sorry😢.

* accent
  

    Hello, guys my name is Kim. And I have 10-blocks.
    I like         Orange & Banana @ peach that yummy...!
    
    Okay; I love it. I can eat 23 oranges at same time.
    
    Oh.... you can't? sorry.

* expander
  

    Hello, guys my name is Kïm. And I have 10-blocks.
    I like         Orange🍊🍊🍊 & Banana🍌 @ peach🍑🍑 that yummy...!
    
    Okay; I love it. I can eat 23 oranges at same time.
    
    Oh.... you can not? sorry😢.

* emoji_remover
  

    Hello, guys my name is Km. And I have 10-blocks.
    I like         Orange & Banana @ peach that yummy...!
    
    Okay; I love it. I can eat 23 oranges at same time.
    
    Oh.... you can't? sorry.

* lemmatizer
  

    hello , guy my name be Kïm . and I have 10 - block . 
    I like          Orange 🍊 🍊 🍊 & Banana 🍌 @ peach 🍑 🍑 that yummy ... ! 
    
    okay ; I love it . I can eat 23 orange at same time . 
    
    oh .... you ca n't ? sorry 😢 .

* number_changer
  

    Hello, guys my name is Kïm. And I have ten-blocks.
    I like         Orange🍊🍊🍊 & Banana🍌 @ peach🍑🍑 that yummy...!
    
    Okay; I love it. I can eat twenty-three oranges at same time.
    
    Oh.... you can't? sorry😢.

* number_normalizer
  

    Hello, guys my name is Kïm. And I have number-blocks.
    I like         Orange🍊🍊🍊 & Banana🍌 @ peach🍑🍑 that yummy...!
    
    Okay; I love it. I can eat number oranges at same time.
    
    Oh.... you can't? sorry😢.

* short_line_remover
  

    Hello, guys my name is Kïm. And I have 10-blocks.
    I like         Orange🍊🍊🍊 & Banana🍌 @ peach🍑🍑 that yummy...!
    Okay; I love it. I can eat 23 oranges at same time.
    Oh.... you can't? sorry😢.

* short_word_remover
  

    Hello, guys name have-blocks.
     like         Orange🍊🍊🍊 & Banana🍌 @ peach🍑🍑 that yummy...!
    
    Okay love oranges same time.
    
    ? sorry😢.

* full_stop_normalizer
  

    Hello, guys my name is Kïm. And I have 10-blocks.
    I like         Orange🍊🍊🍊 & Banana🍌 @ peach🍑🍑 that yummy....
    
    Okay. I love it. I can eat 23 oranges at same time.
    
    Oh.... you can't. sorry😢.

* comma_normalizer


    Hello, guys my name is Kïm. And I have 10-blocks.
    I like         Orange🍊🍊🍊 , Banana🍌 , peach🍑🍑 that yummy...!
    
    Okay, I love it. I can eat 23 oranges at same time.
    
    Oh.... you can't, sorry😢.

* special_remover


    Hello  guys my name is Kïm. And I have 10 blocks.
    I like         Orange🍊🍊🍊 & Banana🍌 @ peach🍑🍑 that yummy...!
    
    Okay  I love it. I can eat 23 oranges at same time.
    
    Oh.... you can't? sorry😢.

* special_replacer 


    Hello, guys my name is Kïm. And I have 10-blocks.
    I like         Orange🍊🍊🍊 and Banana🍌 and peach🍑🍑 that yummy...!
    
    Okay; I love it. I can eat 23 oranges at same time.
    
    Oh.... you can't? sorry😢.

* word_replacer


    Hello, guys my name is Kïm. And I have 10-blocks.
    I like         Apple🍊🍊🍊 & Banana🍌 @ peach🍑🍑 that yummy...!
    
    Okay; I love it. I can eat 23 oranges at same time.
    
    Oh.... you can't? sorry😢.

    

## * With swagger *

API page: [In Ainize](https://ainize.ai/fpem123/pre-processor?branch=master)

## * With a Demo *

Demo page: [End-point](https://master-pre-processor-fpem123.endpoint.ainize.ai/)

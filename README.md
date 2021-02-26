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

    
    to_capitalize: Capitalize only the first letter of the line, and change the rest to lowercase.
    
    to_lower: Change all words to lowercase.
    
    accent: Replace accented characters like ï with regular characters.
    
    expander: Increases the abbreviation. (can't → can not)
    
    short_line_remover: It also takes a number and removes the lines shorter than the number.
    
    short_word_remover: It also takes a number and removes words shorter than the number.
    
    emoji_remover: Remove emojis.
    
    special_remover: Receive the special characters to be deleted and delete them all.
    
    special_replacer: Input and replace special characters and words to be replaced.
    
    lemmatizer: Turns all words into basic form.
    
    space_normalizer: Whitespace normalization. (Including newline removal)
    
    full_stop_normalizer: It receives special characters and turns them all into dot
    
    comma_normalizer: Receive special characters and turn them all into commas.
    
    number_changer: Turn numbers into words.
    
    number_normalizer: Replace the number with another one you entered.

    word replacer: Replace the word with another one you entered.


### Post parameter

    text_file: Text file you want to pre-process.
    option: The pre-processing option.
    value: The value required by the specific option.
    value2: Second value required by specific option.

### Output foramt

    text file


## * With CLI *

### Input example

    

### Output example

    

## * With swagger *

API page: [In Ainize](https://ainize.ai/fpem123/pre-processor?branch=master)

## * With a Demo *

Demo page: [End-point](https://master-pre-processor-fpem123.endpoint.ainize.ai/)

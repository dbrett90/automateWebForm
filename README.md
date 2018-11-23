# automateWebForm

## Overview
Having found that filling out an online contact form for my senator was a tedious process, I wanted to automate it. This script was built exclusively for Senator Collins' web page so that I could send a number of similar messages to her office without having to type them in manually. The current program has a new web form submitted each hour.

## Install instructions

In order to run the following code, the user should execute the following pip or brew install

```
pip install selenium
brew install selenium
```

Further, in order to run the chrome driver make sure to download the executable file from this [link](https://chromedriver.storage.googleapis.com/index.html?path=2.44/) and have it installed in PATH. 

## Running the Program
If you wish to submit an actual response, uncomment lines 54 & 55. In addition, the .txt files in the messageTemplates folder will need to be edited in order to refelct your personal information should you choose to submit it. Right now the resposne will be sent from 'John Smith' who lives at 123 Rainbow Road in South Portland.

To run the program, naviagte to the working directory and type ```python formAutofill.py```




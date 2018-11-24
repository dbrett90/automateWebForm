# automateWebForm

## Overview
Having found that filling out an online contact form for my senator was a tedious process, I wanted to automate it. This script was built exclusively for Senator Collins' & Senator King's  web pages so that I could send a number of similar messages to their offices without having to type them in manually. The current program has a new web form submitted each hour up to a maximum of 10 web forms. These values can be adjusted to reflect more submissions along with the time interval.

## Install instructions

In order to run the following code, the user should execute the following pip or brew install depending on their configuration.

```
pip install selenium
brew install selenium
```

Further, in order to run the chrome driver make sure to download the executable file from this [link](https://chromedriver.storage.googleapis.com/index.html?path=2.44/) and have it installed in PATH. 

## Running the Program
If you wish to submit an actual response, uncomment lines 78 & 79 (Collins) or 116 & 117 (King). In addition, the .txt files in the messageTemplates folder will need to be edited in order to reflect your personal information should you choose to submit it. Currently a response will be sent from 'John Smith' who lives at 123 Rainbow Road in South Portland.


To run the program, Uncomment lines 126 & 127. Then  navigate to the working directory and run ```python formAutofill.py``` from the command line. This will engage the automated messages for both Collins & King.




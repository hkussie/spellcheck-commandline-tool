# Spellcheck Commandline Tool 
This is a script that makes use of the Spellcheck API to allow a user to spell check a sentence(s)
within the terminal.

### Getting Started
The instructions below will get you a copy of the project up and running on your local machine for 
use. 

### Prerequisites 
In order to run the software you'll need to have pip, click, and requests installed on your machine: 

```py 
pip install requests
```
```py 
pip install click 
```

### Running on local machine: 
Once you have your dependencies installed, you can run the index.py file as follows: 

```py 
python index.py "Tesst sentance"
```

And you should get an output that looks like this: 

```py 
{
  "original": "Tesst sentance",
  "suggestion": "Tessy sentence",
  "corrections": {
    "Tesst": [
      "Tessy",
      "Tess",
      "Tessi",
      "Tessa",
      "Tess t",
      "Tests",
      "Test",
      "Hostess",
      "Estes",
      "Tempest",
      "Tastes",
      "Toast",
      "Tsetse"
    ],
    "sentance": [
      "sentence",
      "sentience",
      "repentance",
      "entrance",
      "stance",
      "sentinel",
      "Sundanese"
    ]
  }
}
```
# RAKE JPN

RAKE JPN is a Python tool for extracting keywords in Japanse. 

This tool implements the RAKE (Rapid Automatic Keyword Extraction) algorithm proposed in: Rose, Stuart & Engel, Dave & Cramer, Nick & Cowley, Wendy. (2010). [Automatic Keyword Extraction from Individual Documents](https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents). 10.1002/9780470689646.ch1. 

The source code is released under the MIT License.

### Installation
This tool requires __python 3.5+__

Clone the repository 
```sh
$ git clone https://github.com/carol975/RAKE_JPN.git
```
Install the dependencies

```sh
$ cd RAKE_JPN
$ pip install -r requirements.txt
```

### Usage Example
```py
from rake import Rake
rake = Rake()
text = "杉山古墳（すぎやまこふん）は、奈良県奈良市大安寺にある古墳。形状は前方後円墳。大安寺古墳群を構成する古墳の1つ。国の史跡に指定されている（史跡「大安寺旧境内 附 石橋瓦窯跡」のうち）。" 
print(rake.get_keywords(text,3))  #get_keyword takes two params: 1. Text, 2. Max number of keywords to return, if zero then returns all keywords.

```
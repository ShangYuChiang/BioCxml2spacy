# Creates NER training data in Spacy format from BioCxml
> Using python convert annotation format from BioCxml to Spacy 


# User guide :metal:
>This project is to convert BioCxml into Spacy format

The BioCxml format of the TeamTat's annotation
![avatar](BioCxml.JPG)

The Spacy's entity annotations format
```python
train_data = [
    ("Uber blew through $1 million a week", [(0, 4, 'ORG')]),
    ("Android Pay expands to Canada", [(0, 11, 'PRODUCT'), (23, 30, 'GPE')]),
    ("Spotify steps up Asia expansion", [(0, 8, "ORG"), (17, 21, "LOC")]),
    ("Google Maps launches location sharing", [(0, 11, "PRODUCT")]),
    ("Google rebrands its business apps", [(0, 6, "ORG")]),
    ("look what i found on google! 😂", [(21, 27, "PRODUCT")])]
#("Eample text or content"(string), {"entities": [(start_position(int), end_position(int), "label_name"(string))]})
```

## Prerequisite
- Python 3.x { x > 4 }  
check by command  `python --version`  
- Pip (package manager)  
check by command  `pip --version`  
- lxml module  
Install by command `pip install lxml`  
check by command   `pip list` to see whether lxml exists


### Example:
```python

```
### output
```

```

## Getting started step by step 

- Step1 - Clone the repo to local   
```
git clone 
```
```
cd /BioCxml2spacy
```

- Step2 - Run BioCxml2spacy.py

```
python BioCxml2spacy.py
```
- Step3 - The results are shown in the output file

## Reference
XML Tutorial : [w3schools.com](https://docs.python.org/2/library/xml.etree.elementtree.html)  
Spacy : [Training spaCy’s Statistical Models](https://spacy.io/usage/training)  
Github : [BioC-JSON](https://github.com/ncbi-nlp/BioC-JSON)


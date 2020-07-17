# Creates NER training data in Spacy format from BioCxml
> Using python convert annotation format from BioCxml to Spacy 


# User guide :metal:
>This project is to convert BioCxml into Spacy format

The BioCxml format of the TeamTat's annotation
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE collection SYSTEM "BioC.dtd">
<collection>
  <source>PubTator</source>
  <date/>
  <key>BioC.key</key>
  <document>
    <id>3392027</id>
    <infon key="tt_curatable">no</infon>
    <infon key="tt_version">0</infon>
    <infon key="tt_round">0</infon>
    <passage>
      <infon key="type">title</infon>
      <offset>0</offset>
      <text>(title)Primary structure of apolipophorin-III from the migratory locust, Locusta migratoria. Potential amphipathic structures and molecular evolution of an insect apolipoprotein.</text>
      <annotation id="1">
        <infon key="identifier"></infon>
        <infon key="type">Gene</infon>
        <infon key="updated_at">1980-01-01T00:00:00Z</infon>
        <location offset="21" length="17"/>
        <text>apolipophorin-III</text>
      </annotation>
      <annotation id="2">
        <infon key="identifier">7004</infon>
        <infon key="type">Species</infon>
        <infon key="updated_at">1980-01-01T00:00:00Z</infon>
        <location offset="48" length="16"/>
        <text>migratory locust</text>
      </annotation>
    </passage>
  </document>
</collection>

```

The Spacy's entity annotations format
```python
train_data = [
    ('Primary structure of ....',{'entities': [(21,38,'Gene'),(48,64,'Species'),(66,84,'Species'),(225,242,'Gene'),(248,266,'Species'),(423,440,'Gene'),(450,466,'Species'),(468,481,'Species'),(597,610,'Species'),(969,978,'Species'),(1159,1168,'Species'),(1234,1243,'Species')]}),(ex2),(ex3)]
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


## Getting started step by step 

- Step1 - Clone the repo to local   
```
git clone https://github.com/ShangYuChiang/BioCxml2spacy.git
```
```
cd / BioCxml2spacy
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


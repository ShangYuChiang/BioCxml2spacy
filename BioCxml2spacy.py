import xml.etree.cElementTree as ET

def xml2spacy(tree):

        root = tree.getroot()
        training_data = ()
        spacy_text=""
        #print(len(passages)) #result should be 2
        passages = root.find('document').findall('passage') 

        #convert and combine all passage.text(title, abstract) into spacy text format
        spacy_text += (passages[0].find('text').text + " ")
        spacy_text += (passages[1].find('text').text)
        print(spacy_text)
        training_data.append(spacy_text)
        spacy_entities= annotation2entity(passages)

def annotation2entity(passages):
        entities = ", {\"entities\":"
        for passage in passages:  
                passage_annotations = passage.findall('annotation')
                #print(len(passage_annotations))
                
        
        '''
        passage_offset = int(passage.find('offset').text)
        passage_text = passage.find('text').text
        passage_entities = []
        for ann in passage_annotations:
                entity_type = ann.find('./infon[@key="type"]').text
                od = ann.find('./location').attrib
                start, end = get_entity_offset(od, passage_offset)
                passage_entities.append((start, end, entity_type))

                spacyd_passage = (passage_text, {"entities": passage_entities})
                spacy_data.append(spacyd_package)
        '''
        
if __name__ == "__main__":
        tree = ET.parse('./input/10835480_v0.xml')
        xml2spacy(tree)
        spacy_data = []
        print(spacy_data)

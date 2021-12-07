from flair.data import Sentence
from flair.models import SequenceTagger
from flair.tokenization import SciSpacyTokenizer

class FlairMethod():

    def __init__(self) -> None:
        """Constructor"""

        self.tokenizer = None
        self.tagger = None

    def has_tokenizer(self) -> bool:
        """Check if tokenizer has been created"""

        if self.tokenizer is None:
            raise MissingTokenizerError()
        return True

    def has_tagger(self) -> bool:
        """Check if tagger has been created"""

        if self.tagger is None:
            raise MissingTaggerError()
        return True

    def sanity_check(self) -> bool:
        """Sanity check before running operations"""

        self.has_tagger()
        self.has_tokenizer()
            
        return True

    def use_scispacy_tokenizer(self) -> None:
        """Create SciSpacy tokenizer"""

        self.tokenizer = SciSpacyTokenizer()

    def use_ner_sequence_tagger(self) -> None:
        """Create NER sequence tagger"""

        self.tagger = SequenceTagger.load('ner')

    def generate_keywords(self, sentence_dict) -> dict:
        """"Generate keywords dictionary given a list of sentences"""

        self.sanity_check() 
        output_lst = []       
        
        for sentence_id, text in sentence_dict.items():

            sentence = Sentence(text, use_tokenizer=self.tokenizer)
            self.tagger.predict(sentence)

            for entity in sentence.get_spans():
                info_dict = {
                    "text_id"   : sentence_id,
                    "text"      : text,
                    "keyword"   : entity.to_original_text(), 
                    "label"     : str(entity.get_labels()[0]),
                    "method"    : str(self),
                }

                output_lst.append(info_dict)        
                
        return output_lst

    def __str__(self) -> str:
        return "Flair"

class MissingTokenizerError(Exception): 
    """Simple exception for missing tokenizer"""

class MissingTaggerError(Exception):
    """Simple exception for missing tagger"""
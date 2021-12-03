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

    # def use_base_tokenizer(self) -> None:
    #     """Create base tokenizer"""

    #     self.tokenizer = Tokenizer()

    def use_scispacy_tokenizer(self) -> None:
        """Create SciSpacy tokenizer"""

        self.tokenizer = SciSpacyTokenizer()

    def use_ner_sequence_tagger(self) -> None:
        """Create NER sequence tagger"""

        self.tagger = SequenceTagger.load('ner')

    def generate_keywords(self, sentence_dict) -> dict:
        """"Generate keywords dictionary given a list of sentences"""

        self.sanity_check() 
        output_dict = dict.fromkeys(list(sentence_dict.keys()))

        for sentence_id, sentence in sentence_dict.items():

            sentence = Sentence(sentence, use_tokenizer=self.tokenizer)
            self.tagger.predict(sentence)

            for entity in sentence.get_spans():
                keyword_label_tuple = (entity.to_original_text(), str(entity.get_labels()[0]))
                
                if output_dict[sentence_id] is not None:
                    output_dict[sentence_id].append(keyword_label_tuple)
                else:
                    output_dict[sentence_id] = [keyword_label_tuple]

        return output_dict

class MissingTokenizerError(Exception):
    """Simple exception for missing tokenizer"""
    pass

class MissingTaggerError(Exception):
    """Simple exception for missing tagger"""
    pass
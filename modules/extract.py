from modules.FlairMethod import FlairMethod


def flair_keywords(text_dict):
    """Generate keywords using Flair library"""

    flair_model = FlairMethod()
    flair_model.use_scispacy_tokenizer()
    flair_model.use_ner_sequence_tagger()

    keywords_dict = flair_model.generate_keywords(text_dict)

    return keywords_dict

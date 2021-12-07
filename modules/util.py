import pandas as pd


def read_file(input_file) -> pd.DataFrame:
    """Read files and returns pandas dataframe"""

    if input_file.endswith('.csv'):
        return pd.read_csv(input_file)
    elif input_file.endswith('.tsv'): 
        return pd.read_csv(input_file, sep="\t")

    return None


def generate_text_dict(df, id_col_name, text_col_name):
    """Generate dictionary of texts"""
    
    index_lst = df[id_col_name].values
    text_lst = df[text_col_name].values

    return dict(zip(index_lst, text_lst))


def keywords_to_df(keyword_dict):
    """Creates csv output from keyword dictionary"""

    return pd.DataFrame.from_dict(keyword_dict)


def compact_df(keyword_df, text_col_name="text"):
    """Returns a compact version of keyword dataframe"""

    del keyword_df[text_col_name]

    return keyword_df
"""pytest tests for util"""

import pytest
import sys

sys.path.append("..")
from modules import util

def test_read_file():
    file = util.read_file("/data/test_sample.tsv")
    assert file is not None

def test_generate_text_dict():
    df = util.read_file("/data/test_sample.tsv")
    dct = util.generate_text_dict(df, "id", "text")

    assert type(dct) == dict


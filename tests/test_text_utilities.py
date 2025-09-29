import pytest

from textanalysis_tool.text_utilities import create_acronym

def test_create_acronym():
    assert create_acronym("As Soon As Possible") == "ASAP"

def test_not_a_string():
    with pytest.raises(TypeError):
            create_acronym(420)

def test_empty_string():
    with pytest.raises(ValueError):
            create_acronym("")

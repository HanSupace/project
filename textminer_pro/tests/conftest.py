import nltk
import pytest

@pytest.fixture(scope="session", autouse=True)
def ensure_nltk_resources():
    nltk.download("stopwords", quiet=True, raise_on_error=True)
    nltk.download("punkt", quiet=True, raise_on_error=True)
    nltk.download("punkt.zip", quiet=True)
    nltk.download("punkt_tab", quiet=True)        

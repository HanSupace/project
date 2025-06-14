import nltk
import pytest

@pytest.fixture(scope="session", autouse=True)
def ensure_nltk_resources():
    # ✅ 주요 리소스 전체 다운로드
    nltk.download("stopwords", quiet=True, raise_on_error=True)
    nltk.download("punkt", quiet=True, raise_on_error=True)
    nltk.download("punkt.zip", quiet=True)         # 혹시라도 필요한 zip 형태 리소스까지
    nltk.download("punkt_tab", quiet=True)         # 에러가 뜬 실제 항목 추가

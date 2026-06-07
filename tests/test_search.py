from unittest.mock import MagicMock, patch

from tools.registry import search_web


def test_search_web_success():
    mock_ddg = MagicMock()
    mock_ddg.status_code = 200
    mock_ddg.json.return_value = {
        "AbstractText": "Python is a programming language.",
        "RelatedTopics": [{"Text": "Guido van Rossum"}]
    }

    mock_wiki_id = MagicMock()
    mock_wiki_id.status_code = 200
    mock_wiki_id.json.return_value = {
        "query": {
            "search": [{"title": "Python (bahasa pemrograman)", "snippet": "Python adalah bahasa..."}]
        }
    }

    mock_wiki_en = MagicMock()
    mock_wiki_en.status_code = 200
    mock_wiki_en.json.return_value = {
        "query": {
            "search": [{"title": "Python (programming language)", "snippet": "Python is a high-level..."}]
        }
    }

    def side_effect(url, **kwargs):
        if "duckduckgo" in url:
            return mock_ddg
        elif "id.wikipedia" in url:
            return mock_wiki_id
        elif "en.wikipedia" in url:
            return mock_wiki_en
        return MagicMock(status_code=404)

    with patch("httpx.get", side_effect=side_effect):
        res = search_web("python")
        assert "DuckDuckGo Abstract" in res
        assert "Python is a programming language." in res
        assert "Hasil Wikipedia (ID)" in res
        assert "Python (bahasa pemrograman)" in res
        assert "Hasil Wikipedia (EN)" in res
        assert "Python (programming language)" in res

def test_search_web_no_results():
    mock_res = MagicMock()
    mock_res.status_code = 200
    mock_res.json.return_value = {}

    with patch("httpx.get", return_value=mock_res):
        res = search_web("nonexistenttopic")
        assert "tidak menemukan hasil" in res

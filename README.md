# C-CLAIM: Chinese Criminal Law Article and Interpretations Mapping Dataset

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

[涓枃鐗?/ Chinese Version](./README_zh.md)

## Project Overview

C-CLAIM provides a systematic mapping from legal articles to case types (crime names) for the Criminal Law of the People's Republic of China, along with judicial interpretations and official documents. It is suitable for legal informatics, case classification, intelligent justice, and other research and application scenarios.

## Dataset Structure

```text
C-CLAIM/
鈹溾攢鈹€ setup.py                 # Installation script
鈹溾攢鈹€ MANIFEST.in              # Package manifest
鈹溾攢鈹€ README.md                # English documentation
鈹溾攢鈹€ README_zh.md             # Chinese documentation
鈹斺攢鈹€ c_claim/
    鈹溾攢鈹€ data/
    鈹?  鈹溾攢鈹€ 鍒戞硶鏉℃枃.csv          # Criminal law articles with case type annotations
    鈹?  鈹溾攢鈹€ 鍒戞硶鍙告硶瑙ｉ噴.csv       # Judicial interpretations from Supreme Court
    鈹?  鈹溾攢鈹€ 鍒戞硶鍙告硶鏂囦欢.csv       # Other important judicial documents
    鈹?  鈹溾攢鈹€ 绔犺妭妗堢敱琛?jsonl       # Chapter-aggregated case type index
    鈹?  鈹斺攢鈹€ 鏍囧噯妗堢敱琛?txt         # 484 standardized case types
    鈹斺攢鈹€ __init__.py              # Python Reader
```

## Data Fields

### 鍒戞硶鏉℃枃 (Criminal Law Articles)

| Field | Type | Description |
|-------|------|-------------|
| chapter | string | Chapter name |
| article_no | string | Article number (e.g., "绗竴鐧鹃浂浜屾潯") |
| text | string | Article text |
| category | string | Category (original/amendment) |
| case_types | string | Case type list (JSON array) |

### 鍙告硶瑙ｉ噴/鍙告硶鏂囦欢 (Judicial Interpretations & Documents)

| Field | Type | Description |
|-------|------|-------------|
| title | string | Document title |
| issue | string | Issue number |
| source_url | string | Source URL |
| text | string | Full text |
| matched_chapters | string | Related chapters |
| matched_case_types | string | Related case types |

## Data Sources and Annotation

### Criminal Law Articles
**Source**: Criminal Law of the People's Republic of China (including all amendments and important separate decisions)

**Annotation**: High-precision manual annotation by legal professionals who carefully reviewed each article to identify corresponding case types (crime names).
> **Special Note**: To ensure complete coverage of crimes, the dataset includes the "Decision of the Standing Committee of the National People's Congress on Punishing Crimes of Fraudulent Purchase, Evasion and Illegal Trading of Foreign Exchange" (inserted at the end of Chapter III, Section 4), mapped to the "Crime of Fraudulent Purchase of Foreign Exchange".

### Judicial Interpretations & Documents
**Source**: [Supreme People's Court Gazette Website (鏈€楂樹汉姘戞硶闄㈠叕鎶ョ綉绔?](http://gongbao.court.gov.cn/)

**Annotation**: LLM-based hierarchical classification with expert review to ensure accuracy of case type mappings.

## Installation

```bash
git clone https://github.com/Shiori-pope/c-claim.git
cd C-CLAIM
pip install -e .
```

## Quick Start

```python
from c_claim import (
    load_articles,
    load_chapters,
    load_interpretations,
    load_documents,
    find_chapters_by_case_type,
    get_case_types,
)

# Load all criminal law articles
articles = load_articles()
print(f"Total articles: {len(articles)}")

# Filter by chapter
articles = load_articles(chapter="鍗卞鍥藉瀹夊叏缃?)

# Load chapter-case-type index
chapters = load_chapters()
for chapter in chapters[:5]:
    print(f"{chapter['chapter']}: {len(chapter['case_types'])} case types")

# Find chapters by case type
chapters = find_chapters_by_case_type("寮哄ジ缃?)
# ['绗洓绔?渚电姱鍏皯浜鸿韩鏉冨埄銆佹皯涓绘潈鍒╃姜']

# Get all case types
case_types = get_case_types()
print(f"Total case types: {len(case_types)}")  # 484

# Load judicial interpretations (title is fuzzy-matched keyword)
interpretations = load_interpretations(title="娲楅挶")
# Returns all interpretations with "娲楅挶" in the title
```

## Statistics

| Dataset | Count |
|---------|-------|
| Criminal Law Articles | 402 |
| Chapters | 25 |
| Standard Case Types | 484 |
| Judicial Interpretations | 178 |
| Judicial Documents | 164 |

## Authors

| Name | Contribution |
|------|--------------|
| **Zhijie Liu** (鍒樻櫤鏉? <sup>*</sup> | Core Development, Data Crawling, LLM Prompt Engineering |
| **Zixuan Feng** (鍐瓙钀? <sup>*</sup> | Legal Expert Review, Coverage Validation, Manual Annotation of Anomalies |
| **Ran Qiu** (閭辩劧) <sup>*</sup> | Legal Expert Review, Consistency Validation, Auxiliary Data Cleaning |
| **Jiarong Ge** (钁涘槈鑽? <sup>*</sup> | Legal Expert Review, Automated Sampling & Proofreading, Manual Annotation of Anomalies |

> <sup>*</sup> *These authors contributed equally to this work.*

## Citation

```bibtex
@misc{c-claim,
  title = {C-CLAIM: Chinese Criminal Law Article and Interpretations Mapping Dataset},
  author = {Zhijie Liu and Zixuan Feng and Jiarong Ge and Ran Qiu},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/Shiori-pope/c-claim}
}
```

## License

This dataset is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0).

## Disclaimer

This dataset is provided for research and educational purposes only. While we strive to ensure accuracy, we make no warranties about the completeness, reliability, or accuracy of the data. Users should verify critical information independently before use.

## Contact

For questions or suggestions, please [open a GitHub Issue](https://github.com/Shiori-pope/c-claim/issues).

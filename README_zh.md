# C-CLAIM: 中国刑法条文与司法解释映射数据集

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

[English Version / 英文版](./README.md)

## 项目简介

本数据集针对中华人民共和国刑法及其司法解释、司法文件，系统性地构建了从法律条文到案由（罪名）的映射关系。适用于法律信息化、案件分类、智能司法等研究和应用场景。

## 数据集结构

```text
C-CLAIM/
├── setup.py                 # 安装脚本
├── MANIFEST.in              # 打包清单
├── README.md                # 英文文档
├── README_zh.md             # 中文文档
└── c_claim/
    ├── data/
    │   ├── 刑法条文.csv          # 刑法条文原文及案由标注
    │   ├── 刑法司法解释.csv       # 最高人民法院司法解释
    │   ├── 刑法司法文件.csv       # 其他重要司法文件
    │   ├── 章节案由表.jsonl       # 按章节聚合的案由索引
    │   └── 标准案由表.txt         # 484项标准案由清单
    └── __init__.py              # Python Reader
```

## 数据字段说明

### 刑法条文

| 字段 | 类型 | 说明 |
|------|------|------|
| chapter | string | 章节名称 |
| article_no | string | 条文编号（如"第一百零二条"）|
| text | string | 条文原文 |
| category | string | 条文类别（本体/修正案等）|
| case_types | string | 案由列表（JSON数组格式）|

### 司法解释/司法文件

| 字段 | 类型 | 说明 |
|------|------|------|
| title | string | 文件标题 |
| issue | string | 发布期号 |
| source_url | string | 原文链接 |
| text | string | 完整文件内容 |
| matched_chapters | string | 关联章节 |
| matched_case_types | string | 关联案由 |

## 数据来源与标注

### 刑法条文
**来源**: 中华人民共和国刑法（含历次修正案及重要单行刑法/决定）

**标注方式**: 人类专家高精度标注
> 由法律专业人员逐条阅读条文，明确每条对应的案由（罪名），确保标注准确率。
> **特殊收录说明**：为保证罪名覆盖的完整性，当前数据集除刑法典及修正案外，还额外收录了《全国人大常委会关于惩治骗购外汇、逃汇和非法买卖外汇犯罪的决定》（置于“第三章 破坏社会主义市场经济秩序罪 第四节 破坏金融管理秩序罪”条文末尾），以映射“骗购外汇罪”。

### 司法解释与司法文件
**来源**: [最高人民法院公报网站](http://gongbao.court.gov.cn/)

**标注方式**: 大模型树状分类 + 人类专家二次核验
> 1. 使用大语言模型进行初步的树状结构分类，建立案由层级关系
> 2. 由法律专家进行二次核验，确保分类准确性

## 安装

从源码安装:

```bash
git clone https://github.com/Shiori-pope/c-claim.git
cd C-CLAIM
pip install -e .
```

## 快速开始

```python
from c_claim import (
    load_articles,
    load_chapters,
    load_interpretations,
    load_documents,
    find_chapters_by_case_type,
    get_case_types,
)

# 加载全部刑法条文
articles = load_articles()
print(f"条文总数: {len(articles)}")

# 按章节查询
articles = load_articles(chapter="危害国家安全罪")

# 加载章节案由表（已聚合）
chapters = load_chapters()
for chapter in chapters[:5]:
    print(f"{chapter['chapter']}: {len(chapter['case_types'])} 个案由")

# 按案由反向查询所属章节
chapters = find_chapters_by_case_type("强奸罪")
# ['第四章 侵犯公民人身权利、民主权利罪']

# 获取所有案由清单
case_types = get_case_types()
print(f"案由总数: {len(case_types)}")  # 484

# 加载司法解释（title 为模糊匹配关键词）
interpretations = load_interpretations(title="洗钱")
# 返回所有标题中包含"洗钱"的司法解释
```

## 数据统计

| 数据集 | 数量 |
|--------|------|
| 刑法条文 | 402 条 |
| 章节数 | 25 个 |
| 标准案由 | 484 项 |
| 司法解释 | 178 条 |
| 司法文件 | 164 条 |

## 作者

| 姓名 | 贡献 |
|------|------|
| **刘智杰** <sup>*</sup> | 核心代码开发、数据抓取、大模型提示词工程 |
| **冯子萱** <sup>*</sup> | 法律专家核验、覆盖率复核、异常数据人工标注 |
| **邱然** <sup>*</sup> | 法律专家核验、一致性检验、持续数据清洗辅助 |
| **葛嘉荣** <sup>*</sup> | 法律专家核验、自动化抽样校对、异常数据人工标注 |

> <sup>*</sup> *上述作者对本项目贡献均等，排名不分先后。*

## 引用

```bibtex
@misc{c-claim,
  title = {C-CLAIM: Chinese Criminal Law Article and Interpretations Mapping Dataset},
  author = {Zhijie Liu and Zixuan Feng and Ran Qiu and Jiarong Ge},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/Shiori-pope/c-claim}
}
```

## 许可证

本数据集采用 [知识共享署名-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0) 进行许可。

## 免责声明

本数据集仅供研究和教育目的使用。数据内容来源于公开的法律法规文件，我们尽力确保数据的准确性，但不对数据中的任何错误或遗漏承担责任。请用户在使用前自行核实关键信息。

## 联系方式

如有问题或建议，请 [提交 GitHub Issue](https://github.com/Shiori-pope/c-claim/issues)。

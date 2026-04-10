# -*- coding: utf-8 -*-
"""
刑事法律数据集Reader
提供便捷的数据加载和查询接口
"""

import json
import os
from typing import Optional, List, Union

__version__ = "1.0.0"
__author__ = "Zhijie Liu, Zixuan Feng, Ran Qiu, Jiarong Ge"

# 数据目录
_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def _get_data_path(filename: str) -> str:
    """获取数据文件路径"""
    return os.path.join(_DATA_DIR, filename)


def _get_csv_path(filename: str) -> str:
    """获取CSV数据文件路径"""
    return os.path.join(_DATA_DIR, filename)


def load_articles(chapter: Optional[str] = None) -> List[dict]:
    """
    加载刑法条文数据

    Args:
        chapter: 可选，按章节名过滤（模糊匹配）

    Returns:
        刑法条文列表，每条包含 chapter, article_no, text, category, case_types
    """
    import pandas as pd

    df = pd.read_csv(_get_csv_path("刑法条文.csv"), encoding="utf-8-sig")

    if chapter:
        df = df[df["chapter"].str.contains(chapter, na=False)]

    return df.to_dict(orient="records")


def load_chapters() -> List[dict]:
    """
    加载章节案由表（已聚合的JSONL格式）

    Returns:
        章节列表，每条包含 chapter, case_types, start_article, end_article
    """
    chapters = []
    jsonl_path = _get_data_path("章节案由表.jsonl")

    if os.path.exists(jsonl_path):
        with open(jsonl_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    chapters.append(json.loads(line))

    return chapters


def find_chapters_by_case_type(case_type: str) -> List[str]:
    """
    根据案由反向查找所属章节

    Args:
        case_type: 案由名称（支持模糊匹配）

    Returns:
        包含该案由的章节名列表
    """
    chapters = load_chapters()
    result = []

    for chapter_info in chapters:
        for ct in chapter_info.get("case_types", []):
            if case_type in ct:
                result.append(chapter_info["chapter"])
                break

    return result


def load_interpretations(title: Optional[str] = None) -> List[dict]:
    """
    加载司法解释数据

    Args:
        title: 可选，按标题过滤（模糊匹配）

    Returns:
        司法解释列表
    """
    import pandas as pd

    df = pd.read_csv(
        _get_csv_path("刑法司法解释.csv"), encoding="utf-8-sig"
    )

    if title:
        df = df[df["title"].str.contains(title, na=False)]

    return df.to_dict(orient="records")


def load_documents(title: Optional[str] = None) -> List[dict]:
    """
    加载司法文件数据

    Args:
        title: 可选，按标题过滤（模糊匹配）

    Returns:
        司法文件列表
    """
    import pandas as pd

    df = pd.read_csv(_get_csv_path("刑法司法文件.csv"), encoding="utf-8-sig")

    if title:
        df = df[df["title"].str.contains(title, na=False)]

    return df.to_dict(orient="records")


def get_case_types() -> List[str]:
    """
    获取所有案由列表

    Returns:
        案由名称列表（去重排序）
    """
    chapters = load_chapters()
    case_types = set()

    for chapter_info in chapters:
        case_types.update(chapter_info.get("case_types", []))

    return sorted(list(case_types))


# 便捷函数别名
load_dataset = load_articles
find_by_case_type = find_chapters_by_case_type

#!/usr/bin/env python3
"""Helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """take in page number  and page sizecand return start and end indices"""
    return ((page - 1) * page_size, (page * page_size))

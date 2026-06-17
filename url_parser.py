"""
URL 解析 + 出版商自动识别。

支持直接 URL、DOI 解析。
"""

import re
import logging
from typing import Optional

import requests

logger = logging.getLogger(__name__)

# 出版商 URL 匹配模式
PUBLISHER_PATTERNS = {
    "aaas": [
        r"science\.org",
    ],
    "acs": [
        r"pubs\.acs\.org",
        r"acs\.org",
    ],
    "aip": [
        r"pubs\.aip\.org",
        r"\.aip\.org",
    ],
    "optica": [
        r"opg\.optica\.org",
        r"optica\.org",
        r"osapublishing\.org",
    ],
    "elsevier": [
        r"sciencedirect\.com",
        r"elsevier\.com",
        r"linkinghub\.elsevier\.com",
    ],
    "npg": [
        r"nature\.com",
    ],
    "springer": [
        r"link\.springer\.com",
        r"springer\.com",
    ],
    "wiley": [
        r"onlinelibrary\.wiley\.com",
        r"wiley\.com",
    ],
    "ieee": [
        r"ieeexplore\.ieee\.org",
    ],
    "acm": [
        r"dl\.acm\.org",
        r"acm\.org",
    ],
    "pnas": [
        r"pnas\.org",
    ],
    "aps": [
        r"journals\.aps\.org",
        r"aps\.org",
    ],
    "tandf": [
        r"tandfonline\.com",
    ],
    "rsc": [
        r"pubs\.rsc\.org",
        r"rsc\.org",
    ],
    "iop": [
        r"iopscience\.iop\.org",
        r"iop\.org",
    ],
    "annualreviews": [
        r"annualreviews\.org",
    ],
    "mdpi": [
        r"mdpi\.com",
    ],
    "frontiers": [
        r"frontiersin\.org",
    ],
    "elife": [
        r"elifesciences\.org",
    ],
    "royalsociety": [
        r"royalsocietypublishing\.org",
    ],
    "bmj": [
        r"\.bmj\.com",
        r"bmj\.com",
    ],
    "ieee": [
        r"ieeexplore\.ieee\.org",
    ],
    "spie": [
        r"spiedigitallibrary\.org",
    ],
    "biorxiv": [
        r"biorxiv\.org",
        r"medrxiv\.org",
    ],
    "jci_insight": [
        r"insight\.jci\.org",
    ],
}


def detect_publisher(url: str) -> Optional[str]:
    """
    从 URL 自动识别出版商。

    Args:
        url: 论文 URL

    Returns:
        出版商标识（如 "acs", "elsevier"）或 None
    """
    url_lower = url.lower()

    for publisher, patterns in PUBLISHER_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, url_lower):
                logger.info(f"Detected publisher: {publisher} from URL")
                return publisher

    logger.warning(f"Could not detect publisher from URL: {url}")
    return None


def is_doi(text: str) -> bool:
    """判断输入是否为 DOI。"""
    return text.strip().startswith("10.") and "/" in text


def resolve_doi(doi: str, timeout: int = 15) -> Optional[str]:
    """
    将 DOI 解析为实际 URL。

    通过 https://doi.org/<doi> 重定向获取出版商 URL。

    Args:
        doi: DOI 字符串（如 "10.1021/acs.jmedchem.4c01234"）

    Returns:
        解析后的 URL，失败返回 None
    """
    doi = doi.strip()
    if doi.startswith("https://doi.org/"):
        doi = doi.replace("https://doi.org/", "")
    elif doi.startswith("http://doi.org/"):
        doi = doi.replace("http://doi.org/", "")
    elif doi.startswith("doi:"):
        doi = doi.replace("doi:", "").strip()

    url = f"https://doi.org/{doi}"
    logger.info(f"Resolving DOI: {doi}...")

    try:
        # Use GET instead of HEAD — some publishers (RSC) abort HEAD requests
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        response = requests.get(url, allow_redirects=True, timeout=timeout, stream=True,
                                headers=headers)
        resolved = response.url
        response.close()  # Don't download body
        logger.info(f"DOI resolved to: {resolved}")
        return resolved
    except Exception as e:
        logger.error(f"DOI resolution failed: {e}")
        return None


def parse_input(input_str: str) -> tuple[Optional[str], Optional[str]]:
    """
    解析用户输入，自动判断是 URL 还是 DOI。

    Args:
        input_str: URL 或 DOI 字符串

    Returns:
        (url, publisher) 元组
    """
    input_str = input_str.strip()

    if is_doi(input_str):
        url = resolve_doi(input_str)
        if url is None:
            return None, None
    elif input_str.startswith(("http://", "https://")):
        # Resolve doi.org URLs to get actual publisher URL for detection
        if "doi.org/" in input_str.lower():
            resolved = resolve_doi(input_str)
            url = resolved if resolved else input_str
        else:
            url = input_str
    else:
        # 尝试作为 DOI
        url = resolve_doi(input_str)
        if url is None:
            logger.error(f"Cannot parse input: {input_str}")
            return None, None

    publisher = detect_publisher(url)
    return url, publisher

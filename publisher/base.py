"""
出版商适配器基类。

每个出版商实现一个子类，处理该出版商特有的页面结构和下载流程。
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, Any


@dataclass
class PaperInfo:
    """论文元数据。"""
    title: str = ""
    authors: str = ""
    year: str = ""
    doi: str = ""
    publisher: str = ""
    url: str = ""


@dataclass
class DownloadResult:
    """单篇论文下载结果。"""
    success: bool
    url: str
    filepath: Optional[str] = None
    error: Optional[str] = None
    paper_info: Optional[PaperInfo] = None
    screenshot_path: Optional[str] = None


class PublisherAdapter(ABC):
    """出版商适配器抽象基类。"""

    def __init__(self, config: dict):
        self.config = config

    @property
    @abstractmethod
    def name(self) -> str:
        """适配器名称（如 "acs", "elsevier"）。"""
        ...

    @abstractmethod
    def detect(self, url: str) -> bool:
        """判断 URL 是否属于该出版商。"""
        ...

    @abstractmethod
    def find_download_element(self, page) -> Optional[Any]:
        """
        在页面中定位下载按钮/链接。

        Args:
            page: Playwright Page 对象

        Returns:
            Playwright ElementHandle 或 None
        """
        ...

    def find_download_url(self, page) -> str | None:
        """
        从 DOM 中提取下载链接 URL。

        默认实现：调用 find_download_element() 获取元素，再取 href。
        子类可覆盖以提供更直接的 URL 提取逻辑。

        Args:
            page: Playwright Page 对象

        Returns:
            绝对 URL 或 None
        """
        element = self.find_download_element(page)
        if element is None:
            return None

        href = element.get_attribute("href")
        if not href:
            return None

        # 相对路径转绝对路径
        if not href.startswith(("http://", "https://")):
            from urllib.parse import urljoin
            href = urljoin(page.url, href)

        return href

    def handle_post_click(self, page, browser) -> bool:
        """
        处理点击下载按钮后的情况。

        子类可覆盖此方法处理特殊弹窗/重定向。
        默认实现：不做任何处理。

        Args:
            page: 当前页面
            browser: Browser 实例（用于检查新标签页）

        Returns:
            True 表示需要继续监控下载
        """
        return True

    def get_paper_metadata(self, page) -> PaperInfo:
        """
        提取论文元数据（标题、作者、年份等）。
        子类可覆盖以提供更精确的提取。
        """
        info = PaperInfo()
        info.publisher = self.name

        try:
            # 通用元数据提取尝试
            title_el = page.query_selector("h1, .article-title, .title")
            if title_el:
                info.title = title_el.inner_text().strip()[:200]

            # 尝试从 meta 标签获取
            info.doi = page.evaluate("""() => {
                const meta = document.querySelector('meta[name="citation_doi"]');
                return meta ? meta.content : '';
            }""") or ""

            info.year = page.evaluate("""() => {
                const meta = document.querySelector('meta[name="citation_date"]');
                return meta ? meta.content : '';
            }""") or ""

            info.authors = page.evaluate("""() => {
                const metas = document.querySelectorAll('meta[name="citation_author"]');
                return Array.from(metas).map(m => m.content).join(', ');
            }""") or ""

        except Exception:
            pass

        return info

    def navigate_to_paper(self, page, url: str) -> bool:
        """
        导航到论文页面。

        Args:
            page: Playwright Page
            url: 论文 URL

        Returns:
            是否成功加载
        """
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            # 等待页面主要内容加载
            page.wait_for_load_state("networkidle", timeout=10000)
            return True
        except Exception as e:
            return False

    def check_access(self, page) -> bool:
        """
        检查是否有权限访问该论文。

        默认实现：检测常见的"无权限"提示。
        """
        blocked_indicators = [
            "Access Denied",
            "Purchase this article",
            "Buy this article",
            "Sign in to access",
            "You do not have access",
            "Not available",
            "403",
        ]

        try:
            body_text = page.inner_text("body")
            for indicator in blocked_indicators:
                if indicator.lower() in body_text.lower():
                    return False
        except Exception:
            pass

        return True

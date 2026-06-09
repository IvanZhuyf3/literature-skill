"""
速率控制 + 人类行为模拟。

稳定性优先，每篇论文间留足延迟。
"""

import time
import random
import logging

logger = logging.getLogger(__name__)


class RateLimiter:
    """控制下载速率，模拟人类浏览行为。"""

    def __init__(self, config: dict):
        rate_cfg = config.get("rate", {})
        self.min_delay = rate_cfg.get("min_delay", 60)
        self.max_delay = rate_cfg.get("max_delay", 180)
        self.session_limit = rate_cfg.get("session_limit", 20)
        self.reading_time_min = rate_cfg.get("reading_time_min", 15)
        self.reading_time_max = rate_cfg.get("reading_time_max", 45)
        self.pre_click_delay_min = rate_cfg.get("pre_click_delay_min", 5)
        self.pre_click_delay_max = rate_cfg.get("pre_click_delay_max", 15)

        self.papers_downloaded = 0

    def wait_between_papers(self) -> float:
        """
        论文间等待。使用截断正态分布，中心偏向较长时间。

        Returns:
            实际等待秒数
        """
        # 正态分布，均值偏向中间偏长
        mean = (self.min_delay + self.max_delay) / 2 * 1.2
        std = (self.max_delay - self.min_delay) / 4

        wait = random.gauss(mean, std)
        wait = max(self.min_delay, min(self.max_delay, wait))

        logger.info(f"Waiting {wait:.1f}s before next paper...")
        time.sleep(wait)
        return wait

    def simulate_reading(self, page) -> None:
        """
        模拟阅读行为：随机滚动、停顿。

        Args:
            page: Playwright Page 对象
        """
        duration = random.uniform(self.reading_time_min, self.reading_time_max)
        logger.info(f"Simulating reading for {duration:.1f}s...")

        start = time.time()
        while time.time() - start < duration:
            # 随机滚动
            scroll_amount = random.choice([-1, 1, 1, 2, 3])  # 偏向向下
            try:
                page.mouse.wheel(0, scroll_amount * random.randint(100, 300))
            except Exception:
                pass

            # 随机停顿
            time.sleep(random.uniform(2, 8))

    def pre_click_delay(self) -> float:
        """点击前的额外等待。"""
        delay = random.uniform(self.pre_click_delay_min, self.pre_click_delay_max)
        logger.debug(f"Pre-click delay: {delay:.1f}s")
        time.sleep(delay)
        return delay

    def check_session_limit(self) -> bool:
        """
        检查是否达到单 session 下载上限。

        Returns:
            True 表示已达上限，应重启浏览器
        """
        return self.papers_downloaded >= self.session_limit

    def increment(self) -> None:
        """下载成功后计数。"""
        self.papers_downloaded += 1
        logger.info(f"Session download count: {self.papers_downloaded}/{self.session_limit}")

    def random_short_delay(self, min_s: float = 1, max_s: float = 5) -> None:
        """随机短延迟（用于页面操作之间）。"""
        time.sleep(random.uniform(min_s, max_s))

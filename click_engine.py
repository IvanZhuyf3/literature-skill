"""
真实鼠标点击引擎。

使用 pyautogui 进行 OS 级别的鼠标操作，模拟人类行为。
关键：绕过浏览器的自动化检测。
"""

import time
import random
import logging
import math
from dataclasses import dataclass

import pyautogui

logger = logging.getLogger(__name__)

# 安全设置
pyautogui.FAILSAFE = True  # 鼠标移到屏幕左上角可紧急中止
pyautogui.PAUSE = 0.02


@dataclass
class ScreenCoord:
    """屏幕坐标。"""
    x: int
    y: int


def viewport_to_screen(page, element) -> ScreenCoord:
    """
    将 Playwright 元素的视口坐标转换为屏幕坐标。

    Playwright bounding_box 返回 CSS 像素坐标（相对于视口）。
    需要加上浏览器窗口位置和工具栏偏移。

    Args:
        page: Playwright Page 对象
        element: Playwright ElementHandle 对象

    Returns:
        ScreenCoord 屏幕坐标（元素中心点）
    """
    box = element.bounding_box()
    if box is None:
        raise ValueError("Element has no bounding box (may not be visible)")

    # 获取浏览器窗口位置和尺寸信息
    window_info = page.evaluate("""() => ({
        screenX: window.screenX,
        screenY: window.screenY,
        outerWidth: window.outerWidth,
        outerHeight: window.outerHeight,
        innerWidth: window.innerWidth,
        innerHeight: window.innerHeight,
        scrollX: window.scrollX,
        scrollY: window.scrollY,
        devicePixelRatio: window.devicePixelRatio
    })""")

    dpr = window_info["devicePixelRatio"]
    chrome_height = window_info["outerHeight"] - window_info["innerHeight"]

    # bounding_box 已是视口相对坐标（含滚动偏移）
    # 转换到屏幕坐标需要考虑 DPR
    center_x = box["x"] + box["width"] / 2
    center_y = box["y"] + box["height"] / 2

    screen_x = int(window_info["screenX"] + center_x * dpr)
    screen_y = int(window_info["screenY"] + chrome_height + center_y * dpr)

    return ScreenCoord(x=screen_x, y=screen_y)


class HumanLikeClicker:
    """模拟人类鼠标行为的点击引擎。"""

    def __init__(self, config: dict | None = None):
        self.config = config or {}
        # 移动速度范围（秒）
        self.move_duration_min = 0.3
        self.move_duration_max = 0.8
        # 点击前后随机延迟（秒）
        self.pre_move_delay = (0.1, 0.4)
        self.post_move_delay = (0.05, 0.15)
        self.pre_press_delay = (0.03, 0.08)

    def _bezier_curve(self, start: tuple, end: tuple, n_points: int = 50):
        """
        生成贝塞尔曲线路径点。

        使用 2 个随机控制点产生自然的弧线轨迹。
        """
        sx, sy = start
        ex, ey = end

        # 在起终点之间生成 1-2 个控制点
        ctrl_points = [(sx, sy)]
        for _ in range(2):
            cx = sx + (ex - sx) * random.uniform(0.2, 0.8) + random.uniform(-30, 30)
            cy = sy + (ey - sy) * random.uniform(0.2, 0.8) + random.uniform(-30, 30)
            ctrl_points.append((cx, cy))
        ctrl_points.append((ex, ey))

        # 三次贝塞尔曲线
        points = []
        for i in range(n_points):
            t = i / (n_points - 1)
            # ease-in-out 速度曲线
            t_ease = t * t * (3 - 2 * t)

            x = (
                (1 - t_ease) ** 3 * ctrl_points[0][0]
                + 3 * (1 - t_ease) ** 2 * t_ease * ctrl_points[1][0]
                + 3 * (1 - t_ease) * t_ease ** 2 * ctrl_points[2][0]
                + t_ease ** 3 * ctrl_points[3][0]
            )
            y = (
                (1 - t_ease) ** 3 * ctrl_points[0][1]
                + 3 * (1 - t_ease) ** 2 * t_ease * ctrl_points[1][1]
                + 3 * (1 - t_ease) * t_ease ** 2 * ctrl_points[2][1]
                + t_ease ** 3 * ctrl_points[3][1]
            )

            # 加入微小抖动（模拟人手）
            if 0 < i < n_points - 1:
                x += random.gauss(0, 0.5)
                y += random.gauss(0, 0.5)

            points.append((x, y))

        return points

    def human_move_to(self, x: int, y: int) -> None:
        """
        以人类式轨迹移动鼠标到目标坐标。

        使用贝塞尔曲线 + 速度变化模拟真实鼠标移动。
        """
        current_x, current_y = pyautogui.position()
        distance = math.hypot(x - current_x, y - current_y)

        if distance < 2:
            logger.debug("Already at target position.")
            return

        # 根据距离决定移动时间
        duration = random.uniform(self.move_duration_min, self.move_duration_max)
        # 远距离适当加长
        if distance > 500:
            duration *= 1.5

        # 生成路径点
        n_points = max(30, int(duration / 0.01))
        points = self._bezier_curve(
            (current_x, current_y),
            (x, y),
            n_points=n_points,
        )

        # 执行移动
        step_delay = duration / len(points)
        for px, py in points:
            pyautogui.moveTo(int(px), int(py), _pause=False)
            time.sleep(step_delay)

        logger.debug(f"Moved mouse to ({x}, {y}) in {duration:.2f}s")

    def click(self, coord: ScreenCoord) -> None:
        """
        完整的人类式点击流程。

        1. 移动前随机延迟
        2. 人类轨迹移动到目标
        3. 到达后短暂停顿
        4. 按下-松开（带随机间隔）
        5. 点击后停顿
        """
        # 目标坐标加微小随机偏移（不会精确点中心）
        target_x = coord.x + random.randint(-2, 2)
        target_y = coord.y + random.randint(-2, 2)

        # 步骤 1：移动前延迟
        time.sleep(random.uniform(*self.pre_move_delay))

        # 步骤 2：人类轨迹移动
        self.human_move_to(target_x, target_y)

        # 步骤 3：到达后停顿
        time.sleep(random.uniform(*self.post_move_delay))

        # 步骤 4：按下-松开
        press_delay = random.uniform(*self.pre_press_delay)
        pyautogui.mouseDown(_pause=False)
        time.sleep(press_delay)
        pyautogui.mouseUp(_pause=False)

        # 步骤 5：点击后停顿
        time.sleep(random.uniform(0.1, 0.3))

        logger.info(f"Clicked at screen ({target_x}, {target_y})")

    def click_element(self, page, element) -> None:
        """
        便捷方法：定位 Playwright 元素 → 转换坐标 → 真实点击。

        Args:
            page: Playwright Page
            element: Playwright ElementHandle
        """
        coord = viewport_to_screen(page, element)
        self.click(coord)

    def scroll_like_human(self, direction: str = "down", amount: int = 3) -> None:
        """
        模拟人类滚动。不均匀、有停顿。

        Args:
            direction: "up" 或 "down"
            amount: 滚动次数
        """
        scroll_clicks = 1 if direction == "down" else -1

        for _ in range(amount):
            pyautogui.scroll(scroll_clicks * random.randint(1, 3))
            time.sleep(random.uniform(0.3, 1.0))

    @staticmethod
    def get_current_position() -> ScreenCoord:
        """获取当前鼠标位置。"""
        x, y = pyautogui.position()
        return ScreenCoord(x=x, y=y)

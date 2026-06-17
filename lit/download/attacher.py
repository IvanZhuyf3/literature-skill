"""
lit/download/attacher.py — PDF 挂载模块（薄封装）

实际逻辑在 ``lit.core.zotero.attach_pdf()`` 中实现。
本模块存在仅为了保持 ``cli.py`` 导入路径的一致性。
"""
from lit.core.zotero import attach_pdf

# DOI Index（已废弃）

> 2026-06-18 被 `references/local-sqlite-lookup.md` 替代。
>
> 旧方案：JSON 索引（`cache/doi_index.json`，60s 构建，7 天 TTL）。
> 新方案：复制 `zotero.sqlite` 到临时文件 + mtime 缓存（0.13s 冷启动，0.02s 热查，实时）。
>
> JSON 索引废弃原因：
> - 60s 首次构建（vs SQLite 0.13s）
> - 7 天 stale（vs SQLite 实时）
> - 需要 `lit maintain` 手动刷新（vs SQLite 零维护）

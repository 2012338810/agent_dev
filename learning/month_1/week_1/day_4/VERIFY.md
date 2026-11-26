# D4 验证（2026-11-26 · 文本、JSON 读写和路径处理）

> ✅ 能用自己的话讲清并举例 / 🟡 讲得出名词讲不清为什么 / ❌ 说不出或说错。
> 先合上资料口答，再只查答错的题。只写「一句话答案 + 边界条件」。

- Q1 `open()` 为什么必须显式写 `encoding="utf-8"`？Windows 下不指定时默认用什么编码，会出现哪两类问题？
  - 答：
  - 判定：
- Q2 `json.load` 和 `json.loads` 的区别是什么？`json.dump` 的 `ensure_ascii=False` 和 `indent=2` 各管什么？
  - 答：
  - 判定：
- Q3 `with open(...) as f:` 比手动 `open` / `close` 好在哪？文件路径为什么建议用 `pathlib.Path` 的 `/` 拼接而不是字符串 `+`？
  - 答：
  - 判定：

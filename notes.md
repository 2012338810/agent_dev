# 学习笔记（每日 5 行）

> 规则：每天编码结束后 30 分钟内写完，不补写、不美化。**踩坑一条必须能讲给面试官**，否则不算。

## 预热（2026-11-17 ~ 11-19，旧 13 周计划，不计入 18 周）

正式计划为 [18 周逐日学习计划](docs/plan/18周逐日学习计划.md)，D1 = 2026-11-24 起算。以下为计划前三天的预热记录，保留作档案。

### 2026-11-17 第 1 天
- 学到：conda 环境的隔离不是「玄学」，是 `sys.path` 由解释器按 `sys.prefix` 构造——`py311` 的 `site-packages` 根本不在 3.14 的路径里；`conda activate` 同时改 PATH 和 `sys.prefix`。
- 卡在：两数之和的哈希单遍解法靠提示才想到「边遍历边查表」；验证题 Q1/Q2 只讲得出结论，讲不出机制。
- 明天第一件事：口答 Q1/Q2 升 ✅；D2 写 `learning/inspect_json.py`（输入路径 → 顶层键、最大嵌套深度、类型计数、最大 10 个值），递归拆成 `walk(obj, depth)`。
- 踩坑（能讲给面试官的才算）：
  1. `pip freeze` 在 conda 环境里输出 14 行，实际只装了 3 个直接依赖；`conda env export --from-history` 又只记 `python=3.11`、不管 pip 包。可复现性必须两份文件互补。
  2. PowerShell 的 `>` 默认写 UTF-16LE，`environment.yml` 因此被 git 判定为二进制（`Bin 0 -> 236 bytes`），`conda env create` 在别的机器上可能直接解析失败。
  3. `.gitignore` 里写 `/__pycache__/`、`/.env` 只能匹配仓库根目录，子目录的 `learning/__pycache__/`、`service/.env` 照样漏进来；去掉前导斜杠才对。

---

### 2026-11-18 第 2 天（实际做的是环境返工：重建 .venv + 补 .gitignore）
- 学到：
- 卡在：
- 明天第一件事：
- 踩坑（能讲给面试官的才算）：

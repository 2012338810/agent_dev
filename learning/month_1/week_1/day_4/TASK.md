# D4 任务书：JSON 读写、文件与路径

> 背景：前三天的用例都"活"在代码里——程序一关就没了。今天让用例住进 JSON 文件：读进来、改一改、存回去，中文不乱码。这是第 6 天整合流程（读取→校验→导出）的另一半零件，也是最终项目"导入需求、保存用例"的地基。
>
> 建议用时：学习 45 分钟，编码 135 分钟，验收 45 分钟，记录 15 分钟。

## 学习清单（45 分钟，边看边在 `.venv` 里试）

- `open()` 与 `with` 语句、文件模式 `r` / `w` / `a`、`encoding="utf-8"` 为什么必写
- `json.load` / `json.dump`（对文件）与 `json.loads` / `json.dumps`（对字符串）
- `json.dump` 的 `ensure_ascii=False`、`indent=2` 参数
- `pathlib.Path`：`Path("data") / "cases.json"`、`.exists()`、`.parent`、相对路径从哪算起（cwd）

## 第一部分：数据文件

新建 `learning/month_1/week_1/day_4/storage.py` 和 `day_4/data\` 目录。准备两个 JSON 文件：

- `data\cases.json` —— 把 D3 `checker.py` 里验收合格的 `CASES` 存成 JSON（写几行导出代码生成，或手抄）
- `data\requirements.json` —— 自造 3 条"需求"，每条至少含 `id`、`title`（需求名）、`body`（需求正文，写两三句中文）

## 第二部分：函数（storage.py）

### 1. `load_cases(path)` → 列表

- 用 `Path` 检查文件存在：**不存在时返回 `None` 并打印一句说明**（今天还没学异常处理，先用 `if` 顶住；D5 学完异常再改造成 `raise`，体会两种风格的差别）
- 存在则 `json.load` 读出列表返回
- 读出来的数据跑一遍 D3 的 `validate_case`（把 checker 的代码 `import` 进来或复制过来），打印每条的问题

### 2. `save_cases(path, cases)` → None

- `json.dump(..., ensure_ascii=False, indent=2)`，`encoding="utf-8"` 写回
- 知道这三个参数各自管什么（口答题）

### 3. `update_case(path, case_id, updates)` → True / False

- 读入 → 找到 `id` 等于 `case_id` 的用例 → 把 `updates` 字典里的字段覆盖上去 → 写回 → 返回 `True`
- 找不到该 id：**不写文件**，返回 `False`（想清楚为什么"找不到"不能顺手把文件重写一遍）
- `updates` 里出现用例没有的键怎么办？自己决定，注释写理由

### 4. `load_requirements(path)` → 列表

和 `load_cases` 同款逻辑，读需求文件。（体会一下：两个几乎一样的函数，下周 D8 讲模块化时会回来收拾这种重复）

## 第三部分：验收

1. `load_cases` 读回的数据和 `checker.py` 里的 `CASES` 一致（5 条、字段对得上）
2. 用编辑器打开 `cases.json`：中文是可读的"高"，**不是** `\u9ad8` 转义
3. `update_case(path, "TC-003", {"priority": "高"})` → 返回 `True`；重新 `load_cases`，TC-003 的 priority 确实变了，其余 4 条没动
4. `update_case(path, "TC-999", {...})` → 返回 `False`；文件内容不变
5. `load_cases` 一个不存在的路径 → 打印说明、返回 `None`，程序不崩
6. 手滑验证：把 `cases.json` 里的中文改乱存盘再读——观察乱码长什么样，改回来（知道坑长什么样，下次认得）

运行命令：

```powershell
.\.venv\Scripts\python.exe learning\month_1\week_1\day_4\storage.py
```

## 完成标准（全部打勾才算过）

- [ ] 验收 1～5 全部符合预期
- [ ] 不看资料能说出：`json.load` 和 `json.loads` 差在哪？`with` 语句解决了什么问题？
- [ ] `VERIFY.md` 三题口答完毕
- [ ] `NOTES.md` 写 5 行，同步根目录档案，`git commit`

## 提示（卡住 20 分钟以上再看）

- 读写骨架：`with open(path, "r", encoding="utf-8") as f: data = json.load(f)`；写回把 `r` 换 `w`、`load` 换 `dump`
- 中文乱码九成是两种原因之一：`open` 没写 `encoding="utf-8"`（Windows 默认 GBK），或 `json.dump` 没关 `ensure_ascii`（默认转义成 `\u9ad8`）
- 相对路径 `data\cases.json` 是相对"运行命令时所在的目录"算的——在仓库根目录运行和在 day_4 里运行，结果不同；不确定就 `print(Path.cwd())` 看一眼

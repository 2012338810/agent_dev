# D3 任务书：用例的校验、统计与组合筛选

> 背景：D2 你已经能"查"用例了。今天给程序加上"检查用例合不合格"和"数数"的能力——这是第 1 周 D6 整合流程（读取→校验→导出）的核心零件，也是你验证工作背景里最熟悉的活的程序版。
>
> 建议用时：学习 45 分钟，编码 135 分钟，验收 45 分钟，记录 15 分钟。
> 开工前热身（你自己昨天笔记里写的）：不看资料盲写一遍 D2 的 `filter_by_priority` 和 `find_by_title`。

## 学习清单（45 分钟，边看边在 `.venv` 里试）

- `if / elif / else`、比较链、`in` 判断、truthiness（哪些值当条件算假）
- `for` + `range()` / `enumerate()`；`break`、`continue`；`while` 什么时候用
- 函数：参数默认值、提前 return（卫语句）、`return a, b` 多值返回

## 第一部分：数据

新建 `learning/month_1/week_1/day_3/checker.py`。把 D2 的 `CASES` 复制过来，**再额外定义 3 条"坏用例"**（放进单独列表 `BAD_CASES`，别混进 CASES）：

1. 缺 `expected` 键
2. `steps` 只有 1 步，且 `priority` 是 `"紧急"`（非法值）
3. `id` 是数字 `7`（类型错误），`title` 是空字符串

## 第二部分：三个函数（同一文件）

### 1. `validate_case(case)` → 返回**问题列表**

检查一条用例，所有不合格的地方各生成一条问题描述（字符串），放进列表返回；完全合格返回 `[]`（注意：又是"空列表 = 没问题"，别引入 None）。

必查项：

- 五个键（id/title/priority/steps/expected）是否齐全——缺哪个报哪个
- `id`、`title`、`expected` 是否为非空字符串
- `priority` 是否属于 `"高"/"中"/"低"`
- `steps` 是否为列表、是否至少 2 步、每步是否为字符串

提示：查"类型对不对"可以用 `isinstance(x, str)`；一条用例可能同时有多个问题，别查到一个就 return。

### 2. `count_stats(cases)` → 返回统计字典

返回 `{"高": 数量, "中": 数量, "低": 数量}`。要求：

- 空列表返回 `{"高": 0, "中": 0, "低": 0}`，**不许报 KeyError**
- 提示两种写法都会：预初始化 `stats = {"高": 0, ...}`，和 `stats[c["priority"]] = stats.get(c["priority"], 0) + 1`

### 3. `filter_cases(cases, priority=None, keyword=None)` → 组合筛选

- 两个参数都可省略（默认值 `None` = 不按这项筛）
- 给了 `priority` 就按优先级筛；给了 `keyword` 就按标题包含筛（忽略大小写）；**两个都给就同时满足（且）**
- 什么都不给 → 返回全部用例的**新列表**
- 依旧不得修改 `cases`

这个函数会用到今天学的"参数默认值 + 条件组合"，也是 D2 `filter_by_priority` / `find_by_keyword` 的合体升级版。

## 第三部分：验收（`if __name__ == "__main__":`）

1. `validate_case(CASES[0])` → `[]`
2. `BAD_CASES` 的三条 → 每条返回的问题列表**恰好点中它埋的雷**（缺键、单步+非法优先级、id 类型+空标题），不多不少
3. `count_stats(CASES)` → `{"高": 2, "中": 2, "低": 1}`；`count_stats([])` → 三个 0，不崩
4. `filter_cases(CASES)` → 5 条；`filter_cases(CASES, priority="高")` → 2 条；`filter_cases(CASES, keyword="case")` → 2 条（second cases、fourth case）；`filter_cases(CASES, priority="高", keyword="case")` → 1 条（second cases）
5. 所有函数调用前后 `len(CASES)` 都是 5
6. 挑战（可选）：`validate_all(cases)` —— 对列表逐条校验，返回 `{id: 问题列表}`，只收不合格的

运行命令：

```powershell
.\.venv\Scripts\python.exe learning\month_1\week_1\day_3\checker.py
```

## 完成标准（全部打勾才算过）

- [ ] 验收 1～5 全部符合预期，跑通
- [ ] 不看资料能回答：`if cases:` 和 `if cases is not None:` 什么时候结果不同？
- [ ] `VERIFY.md` 三题口答完毕（题目已就位）
- [ ] `NOTES.md` 写 5 行，同步根目录档案，`git commit`

## 提示（卡住 20 分钟以上再看）

- 校验函数的骨架：`problems = []`，每查一项不合格就 `problems.append("xxx 有问题：...")`，最后 `return problems`——和 D2 的筛选是同一个套路，只是"条件"变成了"检查"
- 组合筛选别写四个 if 分支各筛一遍：想想"一条用例留在结果里的条件"怎么用一句话写出来（`and` 连接，`priority is None or case["priority"] == priority` 这种形式）
- `count_stats` 报 KeyError 的原因：键第一次出现时字典里还没有它——两种解法提示里都有

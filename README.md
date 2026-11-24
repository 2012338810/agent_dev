# agent_dev
第一次接触，尝试进行 agent 的开发

## 学习计划

- [四个月（18 周）逐日学习计划](docs/plan/18周逐日学习计划.md)：每天的任务与验收目标，D1 = 2026-11-24（周二）
- [学习周历](docs/plan/学习周历.md)：每周对应的真实日期、周打卡表、关键节点
- [每日笔记](notes.md) / [验证记录](verify.md)：当天 5 行笔记 + 3 道验证题答案
- [手撕记录](docs/handwrite.md)：每题用时、独立程度、卡点，隔 3 天重做对比
- 计划前预热（2026-11-17 ~ 11-19，旧 13 周计划）的记录保留在 notes.md / verify.md，不计入 18 周

## 环境

- 项目虚拟环境：`.venv`（Python 3.14.4，由 `C:\Python314` 创建）；直接依赖已锁定在 `requirements.txt`（pytest / httpx / python-dotenv）
- 若后续库不兼容 3.14，用 `D:\ANACONDA\envs\py311\python.exe -m venv .venv` 重建后 `pip install -r requirements.txt` 即可（约五分钟）
- 学习环境 conda `py311`（3.11.18）与项目 `.venv` 并存，二者差异见 verify.md 预热记录 Q1

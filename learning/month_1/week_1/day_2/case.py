CASES=[{"id":"TC-001",
        "title":"第一条用例",
        "priority":"高",
        "steps":["选择部署机器","安装测试环境","测试用例"],
        "expected":["测试成功，返回预期数据","测试失败，弹出报错"]}]
CASES.append({"id":"TC-002",
        "title":"第二条用例",
        "priority":"高",
        "steps":["选择部署机器","安装测试环境","测试用例"],
        "expected":["测试成功，返回预期数据","测试失败，弹出报错"]})
CASES.append({"id":"TC-003",
        "title":"第三条用例",
        "priority":"中",
        "steps":["选择部署机器","安装测试环境","测试用例"],
        "expected":["测试成功，返回预期数据","测试失败，弹出报错"]})
CASES.append({"id":"TC-004",
        "title":"第四条用例",
        "priority":"中",
        "steps":["选择部署机器","安装测试环境","测试用例"],
        "expected":["测试成功，返回预期数据","测试失败，弹出报错"]})
CASES.append({"id":"TC-005",
        "title":"第五条用例",
        "priority":"低",
        "steps":["选择部署机器","安装测试环境","测试用例"],
        "expected":["测试成功，返回预期数据","测试失败，弹出报错"]})

for case in CASES:
    print(case)
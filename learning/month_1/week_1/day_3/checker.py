
CASES=[{"id":"TC-001",
        "title":"第一条用例",
        "priority":"高",
        "steps":["选择部署机器","安装测试环境","测试用例"],
        "expected":"测试成功，返回预期数据"}]
CASES.append({"id":"TC-002",
        "title":"second cases",
        "priority":"高",
        "steps":["选择部署机器","安装测试环境","测试用例"],
        "expected":"测试成功，返回预期数据"})
CASES.append({"id":"TC-003",
        "title":"第三条用例",
        "priority":"中",
        "steps":["选择部署机器","安装测试环境","测试用例"],
        "expected":"测试成功，返回预期数据"})
CASES.append({"id":"TC-004",
        "title":"fourth case",
        "priority":"中",
        "steps":["选择部署机器","安装测试环境","测试用例"],
        "expected":"测试成功，返回预期数据"})
CASES.append({"id":"TC-005",
        "title":"第五条用例",
        "priority":"低",
        "steps":["选择部署机器","安装测试环境","测试用例"],
        "expected":"测试成功，返回预期数据"})

BAD_CASES=[{"id":"BAD-001",
        "title":"第一条坏用例",
        "priority":"低",
        "steps":["选择部署机器","安装测试环境","测试用例"]},
        {"id":"BAD-002",
        "title":"第二条坏用例",
        "priority":"紧急",
        "steps":["选择部署机器"],
        "expected":"测试成功，返回预期数据"},
        {"id":7,
        "title":"",
        "priority":"低",
        "steps":["选择部署机器","安装测试环境","测试用例"],
        "expected":"测试成功，返回预期数据"}]


def validate_case(case):
    ans=[]
    my_keys={"id","title","priority","steps","expected"}
    if case.keys() != my_keys:
        ans.append("标准键中不含 %s 此键" % (case.keys()-my_keys))
        ans.append("缺少标准键中的 %s 键" % (my_keys-case.keys()))
    if "id" in case and not isinstance(case["id"],str):
            ans.append("id 类型不合法")
    elif "id" in case and len(case["id"])==0:
        ans.append("id 字符串为空值")
    if "title" in case and len(case["title"])==0:
        ans.append("title字符串为空值")
    if "expected" in case and len(case["expected"])==0:
        ans.append("expected字符串为空值")
    if "priority" in case and case["priority"] not in ["高","中","低"]:
        ans.append("priority 不在标准的 '高','中','低'之中")
    if "steps" in case and not isinstance(case["steps"], list):
        ans.append("step 类型不是列表")
    elif "steps" in case and len(case["steps"])<2:
        ans.append("steps 小于两步")
    elif "steps" in case:
        for step in case["steps"]:
            if isinstance(step,str) ==False:
                ans.append("steps 中的 %s 不是字符串" % step)
    return ans

def count_stats(cases):
    stats ={"高":0,"中":0,"低":0}
    for case in cases:
        if "priority" in case and case["priority"] in stats:
            stats[case["priority"]] += 1
    return stats

def count_stats_get(cases):
    stats={}
    for case in cases:
        stats[case["priority"]]=stats.get(case["priority"],0)+1
    return stats

def filter_cases(cases, priority=None,keyword=None):
    if priority==None and keyword==None:
        return list(cases)
    if keyword==None:
        return [case for case in cases if case["priority"]==priority]
    elif priority == None:
        return [case for case in cases if keyword.lower() in case["title"].lower()]
    else:
        return [case for case in cases if keyword.lower() in case["title"].lower() and case["priority"]==priority]

if __name__ == "__main__":
    ans1=validate_case(CASES[0])
    print(ans1)
    ans2=validate_case(BAD_CASES[0])
    ans3=validate_case(BAD_CASES[1])
    ans4=validate_case(BAD_CASES[2])
    print(ans2)
    print(ans3)
    print(ans4)
    ans5=count_stats(CASES)
    ans6=count_stats_get(CASES)
    print(ans5)
    print(ans6)

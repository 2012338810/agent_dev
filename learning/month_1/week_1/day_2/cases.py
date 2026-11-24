
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

def filter_by_priority(cases, priority):
    ans=[]
    if not cases: 
        return []
    if  priority not in ["高","中","低"]: #非法优先级返回空列表
        return []
    for case in cases:
        if case["priority"]== priority:
            ans.append(case)
    return ans

def filter_by_priority_list(cases, priority):
    if not cases:
        return []
    if  priority not in ["高","中","低"]:#非法优先级返回空列表
        return []
    ans=[case for case in cases if case["priority"]== priority ]
    return ans

def find_by_title(cases,title):
    for case in cases:
        if case["title"]== title:
            return case
    return None

def find_by_title_list(cases,title):
    ans = [case for case in cases if case["title"]== title]
    return ans

if __name__ == "__main__":
    print(len(CASES))
    #1.filter_by_priority(CASES, "高") → 必须正好 2 条
    case=filter_by_priority(CASES,"高")
    print(case)
    #2.filter_by_priority(CASES, "低") → 必须正好 1 条
    case_list=filter_by_priority_list(CASES,"低")
    print(case_list)
    print(len(CASES))
    no_case=filter_by_priority([],"中")
    print(no_case)
    my_dict=find_by_title(CASES,"第一条用例")
    print(my_dict)
    dict_list=find_by_title_list(CASES,"第三条用例")
    print(dict_list)
    not_dict=find_by_title(CASES,"第6条用例")
    print(not_dict)

    for case_title in CASES:
        if case_title["priority"] == "高":
            print(case_title["title"])
    print()

    ans=[case_title_list["title"] for case_title_list in CASES if case_title_list["priority"]=="高"]
    for it in ans:
        print(it)

#參數預設值的處理
def interest(interest_type,subject = "敦煌"):
    """顯示興趣和主題"""
    print("我的興趣是 " + interest_type)
    print("在" + interest_type + "中,最喜歡的是 ",subject)
    print()
interest('旅遊')
interest('旅遊','台北')
interest('閱讀','工具書')



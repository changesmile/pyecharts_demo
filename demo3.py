import pandas as pd
import numpy as np

# sl = pd.Series([1,2,3,4,"D",5])
# # print(sl)
# dict = {"A": [1, 2, 3, 4],
#         "B": [5, 6, 7, 8],
#         "C": [9, 10, 11, 12],
#         "D": [13, 14, 15, 16]}
# sl = pd.DataFrame(dict)
# print(sl)
# print("________")
# print(sl.loc[1:3])
df = pd.read_csv("./demo.csv", encoding='gb2312')
# df.loc[1:3, "CREATE_TIME"] = df["CREATE_TIME"].str.replace("2020-", "10086")
# 先对日期进行截取重新写入到CREATE_TIME中
# def que_data(df):
#     return df["ECN"]>50
# df = df.loc[que_data]
# print(df)
def code(df):
    if df["ECREASON"] == "材料替代":
        return 1
    if df["ECREASON"] == "其他":
        return 2
    if df["ECREASON"] == "技术改进":
        return 3
    else:
        return 4
df.loc[:,"daihao"] = df.apply(code,axis=1)
print(df)
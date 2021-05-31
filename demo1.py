import pandas as pd

ecn_data = pd.read_csv('./enc_data.csv', encoding='gb2312', header=None)
pro_data = pd.read_csv('./pro_data.csv', encoding='gb2312', header=None)

# select id, concat(first_name, last_name) as `name` from stu2;
# 建表示列名一起建立
# ecn_data = pd.DataFrame(sql_data,columns=["CREATE_TIME","PROJECT_CODE","ECREASON"])
# 这里存入code字典，用于纠正补全乱填的编码
dict_code = {
    "8": "A_PROJECT-000008",
    "11": "A_PROJECT-000011",
    "14": "A_PROJECT-000014",
    "17": "A_PROJECT-000017",
    "18": "A_PROJECT-000018",
    "A_PROJECT-000010#888506191": "A_PROJECT-000010",
    "000010-X0911": "A_PROJECT-000010",
    "423": "A_PROJECT-000018",
    "921": "A_PROJECT-000017",
    "X0264": "A_PROJECT-000023"
}


def modify_code(code):
    if len(code) == 16:
        dict_code[code] = code


# 其实也不用，这里用sql获取的数据可以截取所想要的部分，就不用drop不需要的部分，直接筛选
ecn_data.drop(ecn_data.columns[[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17]], axis=1, inplace=True)
ecn_data.rename(columns={1: 'CREATE_TIME', 11: "PROJECT_CODE", 13: "ECREASON"}, inplace=True)
for i in ecn_data["PROJECT_CODE"]:
    modify_code(i)
print(dict_code)
pro_data.drop(pro_data.columns[[0, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13]], axis=1, inplace=True)
pro_data.rename(columns={2: 'PROJECT_CODE', 3: "NAME", 5: "CUSTOMERNAME"}, inplace=True)
pro_data["NAME_CUS"] = pro_data["NAME"] + pro_data["CUSTOMERNAME"]
ecn_data.loc[:, "PROJECT_CODE"] = ecn_data["PROJECT_CODE"].replace(dict_code)
merge_data = pd.merge(ecn_data, pro_data, how="left")
#print(merge_data)
#print(ecn_data)
merge_data.to_csv("./test.csv")
# pro_data.drop(["NAME","CUSTOMERNAME"],axis=1,inplace=True)
# merge_data =  pd.merge(ecn_data,pro_data, on="PROJECT_CODE")
# print(merge_data)
# print(pro_data)
# del ecn_data["OBJECT_ID"]
# ecn_data.drop("OBJECT_ID",axis=1)
# ecn_data.drop(ecn_data.index[0])

# ecn_data["CREATE_TIME"] = ecn_data["CREATE_TIME"].str[0:7]  # 截取日期


# def drop_data(df):
#     return df["CREATE_TIME"] != "2020-12"


# ecn_data = ecn_data.loc[drop_data, :]
# ecn_data_ECREASON = ecn_data.loc[:,"ECREASON"].values_counts()

# ecn_data_ym = ecn_data.loc[:, "CREATE_TIME"].value_counts()
# ecn_data_ym.sort_index(inplace=True)
# data_list = [count for count in ecn_data_ym]

# print(data_list)
# print("--------------")
# ecn_data_ECREASON = ecn_data.loc[:, "ECREASON"].value_counts()
# print(ecn_data_ECREASON)

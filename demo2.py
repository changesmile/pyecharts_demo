import pandas as pd

ecn_data = pd.read_csv('./enc_data.csv', encoding='gb2312', header=None)
pro_data = pd.read_csv('./pro_data.csv', encoding='gb2312', header=None)

dict_code = {
    "A_PROJECT-000013": "A_PROJECT-000013",
    "A_PROJECT-000014": "A_PROJECT-000014",
    "A_PROJECT-000015": "A_PROJECT-000015",
    "A_PROJECT-000017": "A_PROJECT-000017",
    "A_PROJECT-000018": "A_PROJECT-000018",
    "A_PROJECT-000019": "A_PROJECT-000019",
    "A_PROJECT-000020": "A_PROJECT-000020",
    "A_PROJECT-000027": "A_PROJECT-000027",
    "A_PROJECT-000009": "A_PROJECT-000009",
    "A_PROJECT-000023": "A_PROJECT-000023",
    "A_PROJECT-000029": "A_PROJECT-000029",
    "A_PROJECT-000006": "A_PROJECT-000006",
    "A_PROJECT-000004": "A_PROJECT-000004",
    "A_PROJECT-000005": "A_PROJECT-000005",
    "A_PROJECT-000008": "A_PROJECT-000008",
    "A_PROJECT-000022": "A_PROJECT-000022",
    "A_PROJECT-000025": "A_PROJECT-000025",
    "A_PROJECT-000026": "A_PROJECT-000026",
    "A_PROJECT-000024": "A_PROJECT-000024",
    "A_PROJECT-000007": "A_PROJECT-000007",
    "A_PROJECT-000028": "A_PROJECT-000028",
    "A_PROJECT-000030": "A_PROJECT-000030",
    "研60": "研60",
    "A_PROJECT-000011": "A_PROJECT-000011",
    "A_PROJECT-000010": "A_PROJECT-000010",
    "A_PROJECT-000016": "A_PROJECT-000016",
    "A_PROJECT-000021": "A_PROJECT-000021",
    "000008": "A_PROJECT-000008",
    "000011": "A_PROJECT-000011",
    "000014": "A_PROJECT-000014",
    "00000017": "A_PROJECT-000017",
    "0000018": "A_PROJECT-000018",
    "A_PROJECT-000010#888506191": "A_PROJECT-000010",
    "000010-X0911": "A_PROJECT-000010",
    "0423": "A_PROJECT-000018",
    "0921": "A_PROJECT -000017",
    "X0264": "A_PROJECT-000023"

}

# ecn_data.loc[:, "PROJECT_CODE"] = ecn_data["PROJECT_CODE"].replace(dict_code)
ecn_data.drop(ecn_data.columns[[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17]], axis=1, inplace=True)
# ecn_data.rename(columns={1: 'CREATE_TIME', 11: "PROJECT_CODE", 13: "ECREASON"}, inplace=True)

pro_data.drop(pro_data.columns[[0, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13]], axis=1, inplace=True)
# pro_data.rename(columns={2: 'PROJECT_CODE'}, inplace=True)
pro_data["NAME_CUS"] = pro_data[3]+pro_data[5]

merge_data = pd.merge(ecn_data,pro_data,how="left")
#print(pro_data)
# print(ecn_data)
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

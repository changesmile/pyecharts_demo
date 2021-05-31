from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
import pandas as pd

data = [[5, 20, 36, 10, 75, 50], [51, 30, 46, 6, 15, 20], [15, 40, 36, 15, 35, 20], [4, 10, 86, 20, 35, 57]]
data_one = [1, 3, 5, 64]
s = pd.Series(data_one)
s1 = pd.DataFrame(data)
print(s1.index)

if ecn_data["PROJECT_CODE"] == "8":
    return "A_PROJECT-000008"
elif ecn_data["PROJECT_CODE"] == "11":
    return "A_PROJECT-000011"
elif ecn_data["PROJECT_CODE"] == "14":
    return "A_PROJECT-000014"
elif ecn_data["PROJECT_CODE"] == "17":
    return "A_PROJECT-000017"
elif ecn_data["PROJECT_CODE"] == "18":
    return "A_PROJECT-000018"
elif len(ecn_data["PROJECT_CODE"]) > 16:
    return "A_PROJECT-000010"
elif ecn_data["PROJECT_CODE"] == "000010-X0911":
    return "A_PROJECT-000010"
elif ecn_data["PROJECT_CODE"] == "423":
    return "A_PROJECT-000018"
elif ecn_data["PROJECT_CODE"] == "921":
    return "A_PROJECT - 000017"
elif ecn_data["PROJECT_CODE"] == "X0264":
    return "A_PROJECT-000023"
else:
    return ecn_data["PROJECT_CODE"]



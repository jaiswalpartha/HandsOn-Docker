import sys
import pandas as pd

print('arguments',sys.argv)

month = int(sys.argv[1])
df = pd.DataFrame({"name":["partha","surajit"],"dept":["ops","F&A"]})
df["mnt_of_joining"] = month


print(df.head())
df.to_parquet(f"output_{month}.parquet")

print(f"pipline starts, month={month}")

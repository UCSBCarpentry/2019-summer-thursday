import sys
import pandas as pd
quarter = sys.argv[1]
week = int(sys.argv[2])
numDoctors = int(sys.argv[3])
df = pd.read_csv("drewsdata/intakedata20181-20193.csv")
numIntakes = int(df[(df["Quarter"] == quarter) & 
                    (df["Week"] == week)]["Intakes"])
print(numIntakes/numDoctors)
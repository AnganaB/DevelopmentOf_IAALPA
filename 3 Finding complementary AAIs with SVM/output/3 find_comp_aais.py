import sys
import pandas as pd
import pickle

args=sys.argv
if len(args)!=2:
    print("Please provide the test_sample")
    sys.exit(0)

file=args[1]
df=pd.read_csv(file)
df=df.drop(columns='Unnamed: 0')
df.set_index('aai_pair',inplace=True)

model=pickle.load(open('svm.pkl','rb'))

ans=model.predict(df.values)

l=list(df.index)
for i in range(len(l)):
    print(l[i],"  =  ",ans[i])

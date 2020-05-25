import Chefboost as chef

import pandas as pd

df = pd.read_csv("tests/dataset/training.csv")



if __name__ == '__main__':
   config = {'algorithm': 'C4.5', 'enableParallelism': True}
   model = chef.fit(df, config)
   fi = chef.feature_importance()
   print(fi)





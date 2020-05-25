import Chefboost as chef

import pandas as pd

df = pd.read_csv("tests/dataset/Test_Dataset.csv")




if __name__ == '__main__':
   config = {'algorithm': 'C4.5', 'enableParallelism': True}
   model = chef.fit(df, config)
   prediction = chef.predict(model, [2.642857143, 0.342006803, 0.582417582,	7.5, 0.015741016])
   print("Prediction: ",prediction)





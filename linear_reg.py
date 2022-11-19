import pandas as pd
import matplotlib.pyplot as pyp

data = pd.read_csv('kc_house_data.csv')

living_lot_fr  = pd.read_csv("kc_house_data.csv")[['sqft_living','sqft_lot','price']]

#print(living_lot_fr)

Q0,Q1,Q2, = 0,0,0

print(len(living_lot_fr))
def prediction(x1,x2):
    predict_value = Q0 + Q1*x1 + Q2*x2; 


     


print(living_lot_fr.iloc[0].values[0])




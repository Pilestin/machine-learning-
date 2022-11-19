import pandas as pd
import matplotlib.pyplot as pyp

data = pd.read_csv('kc_house_data.csv')

living_lot_fr  = pd.read_csv("kc_house_data.csv")[['sqft_living','sqft_lot','price']]

#print(living_lot_fr)

Q0,Q1,Q2, = 1,1,1
m = len(living_lot_fr)
alfa = 0.03

def prediction(x1,x2):
    predict_value = Q0 + Q1*x1 + Q2*x2

def cost_function():
    total_differency = 0
    for i in range(m):
        iteration_differency = (living_lot_fr.iloc[i].values[2] - prediction(living_lot_fr.iloc[i].values[0],living_lot_fr.iloc[i].values[1]))**2
        total_differency +=  iteration_differency
    return (1/2*m)*total_differency

def derivative():
    
def gradient_descent():
    Q0new,Q1new,Q2new = 0,0,0

    for i in range(m):
        grad_iteration_differency = (living_lot_fr.iloc[i].values[2] - prediction(living_lot_fr.iloc[i].values[0],living_lot_fr.iloc[i].values[1]))*1                            

    Q0new = Q0 - alfa * (1/m)

     

        
print(living_lot_fr.iloc[0].values[0])




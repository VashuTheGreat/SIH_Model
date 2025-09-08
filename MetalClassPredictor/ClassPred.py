import pickle

with open("Metal_Class_Predictor.pkl","rb") as f:
    model=pickle.load(f)



# Class , R_10 , R_8 , R_6 , G_10 , G_8 , G_6 , B_10 , B_8 , B_6

sample_x=[121.6720541,109.3592131,90.47141056,124.4515316,123.0957019,112.5941138,17.29242693,21.56303304,25.67999868]  # R_10,R_8,R_6,G_10,G_8,G_6,B_10,B_8,B_6

y_pred=model.predict([sample_x])
print(y_pred) # Predicts a class
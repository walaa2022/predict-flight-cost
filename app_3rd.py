import streamlit as st
import pandas as pd
import category_encoders
import joblib
import sklearn
import lightgbm as lgb


Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")

def prediction(Airline,Source,Destination,Dep_Time,Arrival_Time,Duration,Total_Stops,Additional_Info,Journey_Month,Journey_DayOfWeek):
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0,"Airline"] = Airline
    test_df.at[0,"Source"] = Source
    test_df.at[0,"Destination"] = Destination
    test_df.at[0,"Dep_Time"] = Dep_Time
    test_df.at[0,"Arrival_Time"] = Arrival_Time
    test_df.at[0,"Duration"] = Duration
    test_df.at[0,"Total_Stops"] = Total_Stops
    test_df.at[0,"Additional_Info"] = Additional_Info
    test_df.at[0,"Journey_Month"] = Journey_Month
    test_df.at[0,"Journey_DayOfWeek"] = Journey_DayOfWeek
    st.dataframe(test_df)
    result = Model.predict(test_df)[0]
    rounded_result = round(result, 2)
    return rounded_result 

    
def main():
    st.title("flight tickets price prediction")
    Airline = st.selectbox("Airline" , ['Jet Airways','IndiGo', 'Air India', 'Multiple carriers', 'SpiceJet','Vistara',
                                        'Air Asia', 'GoAir','Multiple carriers Premium economy',
                                        'Jet Airways Business','Vistara Premium economy','Trujet'])
    Source = st.selectbox("Source" , ['Delhi','Kolkata','Banglore','Mumbai','Chennai'])
    Destination= st.selectbox("Destination" , ['Cochin','Banglore','Delhi','New Delhi','Hyderabad','Kolkata'])
    Dep_Time = st.slider("Dep_Time" , min_value= 0 , max_value=23 , value=0,step=1)
    Arrival_Time = st.slider("Arrival_Time" , min_value= 0 , max_value=23 , value=0,step=1)
    Duration = st.slider("Duration" , min_value= 0 , max_value=50 , value=0,step=1)
    Total_Stops = st.selectbox("Total_Stops" , [0, 1, 2, 3])
    Additional_Info = st.selectbox("Additional_Info" , ['no info','in-flight meal not included',
                                                        'no check-in baggage included','1 long layover',
                                                        'change airports','business class','1 short layover',
                                                        'red-eye flight','2 long layover'])
    Journey_Month = st.selectbox("Journey_Month" , [3,4,5,6])
    Journey_DayOfWeek = st.selectbox("Journey_DayOfWeek" , ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    if st.button("predict the flight cost"):
        result = prediction(Airline, Source, Destination, Dep_Time, Arrival_Time,Duration, Total_Stops, Additional_Info, Journey_Month,Journey_DayOfWeek)
        st.text(f"The flight ticket will cost {rounded_result} dollars")
        
if __name__ == '__main__':
    main()    
    

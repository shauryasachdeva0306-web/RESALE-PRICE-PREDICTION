import streamlit as st  # api integration
import pandas as pd     # data cleaning and preproceessing
import numpy as np      # mathematical computations
import pickle           #  load model file

st.set_page_config(
    page_title = "RESALE PRICE PREDICTION",
    page_icon = '📱',
    layout = 'wide')

st.markdown("""
<style>
  :root{
    --bg: #0a0a0a;
    --panel: #141414;
    --red: #e6293b;
    --red-dim: #7a1420;
    --white: #f5f5f5;
    --muted: #9a9a9a;
  }

  * { box-sizing: border-box; }

  body {
    margin: 0;
    background: var(--bg);
    color: var(--white);
    font-family: 'Courier New', Consolas, monospace;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px 20px;
    overflow-x: hidden;
  }

  .card {
    width: 100%;
    max-width: 480px;
    background: var(--panel);
    border: 1px solid #2a2a2a;
    border-radius: 4px;
    padding: 40px 36px;
    position: relative;
  }

  .eyebrow {
    color: var(--red);
    font-size: 12px;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin: 0 0 6px 0;
  }

  h1 {
    color: var(--red);
    font-size: 32px;
    letter-spacing: 1px;
    margin: 0 0 8px 0;
    text-transform: uppercase;
  }

  .subtitle {
    color: var(--white);
    font-size: 14px;
    opacity: 0.75;
    margin: 0 0 32px 0;
    line-height: 1.5;
  }

  label {
    display: block;
    color: var(--white);
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 8px;
    opacity: 0.85;
  }

  input[type="number"] {
    width: 100%;
    background: #0d0d0d;
    border: 1px solid #333;
    color: var(--white);
    font-family: inherit;
    font-size: 18px;
    padding: 12px 14px;
    border-radius: 3px;
    margin-bottom: 22px;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
  }

  input[type="number"]:focus {
    outline: none;
    border-color: var(--red);
  }

  input.error {
    border-color: var(--red);
    box-shadow: 0 0 0 1px var(--red);
    animation: shake 0.35s ease;
  }

  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    20% { transform: translateX(-6px); }
    40% { transform: translateX(6px); }
    60% { transform: translateX(-4px); }
    80% { transform: translateX(4px); }
  }

  .slider-row {
    margin-bottom: 30px;
  }

  .slider-row .value {
    float: right;
    color: var(--red);
    font-size: 12px;
  }

  input[type="range"] {
    -webkit-appearance: none;
    width: 100%;
    height: 4px;
    background: #333;
    border-radius: 2px;
    margin-top: 10px;
  }

  input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: var(--white);
    border: 2px solid var(--red);
    cursor: pointer;
  }

  input[type="range"]::-moz-range-thumb {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: var(--white);
    border: 2px solid var(--red);
    cursor: pointer;
  }

  button {
    width: 100%;
    background: var(--red);
    color: var(--bg);
    border: none;
    font-family: inherit;
    font-weight: bold;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-size: 14px;
    padding: 14px;
    border-radius: 3px;
    cursor: pointer;
    transition: background 0.2s ease, transform 0.1s ease;
  }

  button:hover { background: #ff3b4e; }
  button:active { transform: scale(0.98); }

  .error-msg {
    display: none;
    color: var(--red);
    font-size: 13px;
    margin: -14px 0 20px 0;
    align-items: center;
    gap: 6px;
  }

  .error-msg.show {
    display: flex;
  }

  .error-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--red);
    flex-shrink: 0;
  }

  .result {
    margin-top: 28px;
    padding-top: 24px;
    border-top: 1px solid #2a2a2a;
    display: none;
  }

  .result.show { display: block; }

  .result .label {
    color: var(--white);
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
    opacity: 0.7;
    margin-bottom: 6px;
  }

  .result .predicted-price {
    color: var(--red);
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .result .meta {
    color: var(--white);
    font-size: 13px;
    opacity: 0.7;
  }

  .badge {
    display: inline-block;
    margin-top: 14px;
    padding: 4px 10px;
    border: 1px solid var(--red);
    color: var(--red);
    font-size: 11px;
    letter-spacing: 1px;
    text-transform: uppercase;
    border-radius: 3px;
  }
</style>
</head>
""",unsafe_allow_html=True)


st.title("resale mobile Price Prediction Powered by AI")
st.write("Here we are doing prediction of smartphone prices using Machine Learning")

model= pickle.load(open('model.pkl','rb'))
columns= pickle.load(open('columns.pkl','rb'))

data= {}
col1,col2,col3 = st.columns(3)

for i,col in enumerate(columns):
    if i%3==0:
        with col1:
            data[col]=st.number_input(col,value=0.0)
    elif i%3==1:
        with col2:
            data[col]=st.number_input(col,value=0.0)
    else:
        with col3:
            data[col]=st.number_input(col,value=0.0)

if st.button("Prediction Mobile Price"):
    df= pd.DataFrame([data])
    prediction = model.predict(df)[0]
    st.success(f' Estimated mobile price is ${prediction}')
    st.balloons()
st.divider
st.subheader("Project Highlights")

st.markdown("""
Linear Regression
Feature Engineering
Data Cleaning
Outlier Detection
StandardScaler
MinMaxScaler
Ridge
Lasso
ElasticNet
Adjusted R2
Deployment """)


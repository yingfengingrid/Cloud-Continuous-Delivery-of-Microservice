from statistics import mode
import streamlit as st

import requests
import pickle
import io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
st.title('Linear Regression')

# fastapi endpoint
#url = 'http://fastapi:8000'
#endpoint = '/segmentation'

st.write('''Obtain Data from a CSV file with two columns and linear regression analysis was carried out.''') # description and instructions

data = st.file_uploader('insert data')  # image upload widget


if st.button('Get linear regression result'):

    if data == None:
        st.write("Insert a data!")  # handle case with no image
    else:
        #segments = process(image, url+endpoint)
        files={"file":data.getvalue()}
        res = requests.post("http://127.0.0.1:8000/model",files=files)
        path = res.json()
        with open (r"../temp.txt", 'rb') as f: #打开文件
            data = pickle.load(f) #将二进制文件对象转换成 Python 对象

        
        st.write(data.head())
        sns.regplot(x=data.columns[0],y=data.columns[1],data=data)
        gcf=plt.gcf()
        st.pyplot(gcf)
        base_model=data.columns[0]+'~'+data.columns[1]
        model = smf.ols(base_model,data = data).fit()
        st.write(model.summary())

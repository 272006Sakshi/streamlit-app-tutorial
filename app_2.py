import streamlit as st 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# add title
st.title("Data Analysis Application")
st.subheader('This application allows you to perform data analysis on various datasets.')

# Dropdown to select dataset
dataset_options = ['tips', 'iris', 'titanic', 'diamonds']
selected_dataset = st.selectbox("Select a dataset", dataset_options)

# Button to upload own dataset
uploaded_file = st.file_uploader("Or upload your own CSV file", type=["csv"])

# Load the selected or uploaded dataset
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Custom dataset uploaded successfully!")
else:
    df = sns.load_dataset(selected_dataset)
    st.success(f"Loaded '{selected_dataset}' dataset from seaborn.")
    
# display the dataset
st.write(df)    
# display the number of rows and columns of the dataset
st.write('Number of Rows: ', df.shape[0])
st.write('Number of Columns:', df.shape[1])

# display the column names and data tpes of dataset
st.write('Column names and Data Types:', df.dtypes)

# print the null valuse if those are > 0
if df.isnull().sum().sum() > 0:
    st.write('Null Values:', df.isnull().sum())
else:
    st.write('No Null Values')    


# display the summary statistics of the selected data
st.write('Summary statistics:', df.describe())

# select the specific Columns for x or y axis from the data and also select the plot type
# x_axis = st.selectbox('Select X-axis', df.columns)
# y_axis = st.selectbox('Select y-axis', df.columns)
# plot_type = st.selectbox('Select plot_type', ['line', 'bar', 'box', 'histogram', 'scatter'])

# # plot the data
# if plot_type == 'line':
#     st.line_chart(df[[x_axis, y_axis]])
    
# elif plot_type == 'bar':
#     st.bar_chart(df[[x_axis, y_axis]])
    
# elif plot_type == 'box':
#     df[x_axis].plot(kind='box')
#     st.pyplot()
# elif plot_type == 'scatter':
#     st.scatter_chart(df[[x_axis, y_axis]])
    
# elif plot_type == 'histogram':
#     df[x_axis].plot(kind='hist')
#     st.pyplot()                
 
# display the correlation matrix of the data
# st.write('correlation matrics', df.corr()) 
# created the pairplot 
st.subheader('Pairplot')
# select the column to be used as hue in pairplot
hue_column = st.selectbox('Select hue column to be used as hue', df.columns)
st.pyplot(sns.pairplot(df, hue=hue_column ))

# create a heatmap
st.subheader('heatmap')

# select the columns which are numeric and then create a corr_matrix
numeric_columns = df.select_dtypes(include=np.number).columns
corr_matrix = df[numeric_columns].corr() 
numeric_columns = df.select_dtypes(include=np.number).columns
corr_matrix = df[numeric_columns].corr()

# # Convert the seaborn heatmap plot to a plotly figure
# heatmap_fig =        #df.Figure(data=df.Heatmap(z=corr_matrix.values,
#                                         x=corr_matrix.columns,
#                                         y=corr_matrix.columns,
#                                         colorscale='iridis'))
# st.pyplot_chart(heatmap_fig)               

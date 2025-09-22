import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Title
st.title('Investment Attractiveness Dashboard')

# Sidebar - File uploader
st.sidebar.header('Upload your data')
uploaded_file = st.sidebar.file_uploader('Upload CSV', type=['csv'])

# Load data
def load_data():
    try:
        df = pd.read_csv('Data/Raw/global-data-on-sustainable-energy.csv')
        return df
    except Exception as e:
        st.error(f"Error loading default data: {e}")
        return None

def get_data():
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = load_data()
    return df

df = get_data()

if df is not None:
    st.subheader('Data Preview')
    st.dataframe(df.head())

    # Select target column
    target_col = st.sidebar.selectbox('Select target column', options=[col for col in df.columns if df[col].nunique() < 20])

    # Feature selection
    features = st.sidebar.multiselect('Select features for analysis', options=[col for col in df.columns if col != target_col], default=[col for col in df.columns if col != target_col])

    # Violin plots
    st.subheader('Violin Plots by Target')
    for feature in features:
        if np.issubdtype(df[feature].dtype, np.number):
            fig, ax = plt.subplots()
            sns.violinplot(x=df[target_col], y=df[feature], ax=ax)
            ax.set_title(f'{feature} by {target_col}', fontweight='bold')
            st.pyplot(fig)

    # Correlation heatmap
    st.subheader('Correlation Heatmap')
    corr = df[features].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Feature Correlation Heatmap', fontweight='bold')
    st.pyplot(fig)

    # PCA visualization
    st.subheader('PCA Visualization')
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features].select_dtypes(include=np.number))
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    pca_df = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
    pca_df[target_col] = df[target_col].values
    fig, ax = plt.subplots()
    sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue=target_col, palette='Set2', ax=ax)
    ax.set_title('PCA (2D) by Target', fontweight='bold')
    st.pyplot(fig)

    # Model prediction (optional)
    st.subheader('Model Prediction (Optional)')
    model_file = st.sidebar.file_uploader('Upload trained model (.joblib)', type=['joblib'])
    if model_file is not None:
        try:
            model = joblib.load(model_file)
            X = df[features].select_dtypes(include=np.number)
            preds = model.predict(X)
            st.write('Predictions:')
            st.dataframe(pd.DataFrame({'Prediction': preds}))
        except Exception as e:
            st.error(f"Error loading or running model: {e}")
else:
    st.warning('No data loaded. Please upload a CSV file or check the default data path.')

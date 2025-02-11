import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv(
    "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"
)

X_raw = df.drop(columns=["species"])
y_raw = df["species"]

with st.sidebar:
    st.header("Input Features")
    gender = st.selectbox("Gender", ["Male", "Female"])
    island = st.selectbox("Island", df["island"].unique())
    bill_length_mm = st.slider(
        "Bill Length (mm)",
        float(X_raw["bill_length_mm"].min()),
        float(X_raw["bill_length_mm"].max()),
    )
    bill_depth_mm = st.slider(
        "Bill Depth(mm)",
        float(X_raw["bill_depth_mm"].min()),
        float(X_raw["bill_depth_mm"].max()),
    )
    flipper_length_mm = st.slider("Flipper Length (mm)", 170.0, 240.0)
    body_mass_g = st.slider("Body Mass (g)", 2700.0, 6300.0)

input_df = pd.DataFrame(
    {
        "island": island,
        "bill_length_mm": bill_length_mm,
        "bill_depth_mm": bill_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g": body_mass_g,
        "sex": gender,
    },
    index=[0],
)

input_plus_orig = pd.concat([input_df, X_raw], axis=0)

df_encode = pd.get_dummies(input_plus_orig, drop_first=True)
X = df_encode[1:]
input_row = df_encode[:1]

target_mapper = {"Adelie": 0, "Chinstrap": 1, "Gentoo": 2}


def target_encode(val):
    return target_mapper[val]


y = y_raw.apply(target_encode)

rfcl = RandomForestClassifier()
rfcl.fit(X, y)

prediction = rfcl.predict(input_row)
prediction_proba = rfcl.predict_proba(input_row)

df_pred = pd.DataFrame(prediction_proba)

df_pred.columns = ["Adelie", "Chinstrap", "Gentoo"]
df_pred

st.subheader("Predicted Species")
prediction

penguin_species = np.array(["Adelie", "Chinstrap", "Gentoo"])
st.success(str(penguin_species[prediction][0]))

st.data_editor(
    df_pred,
    column_config={
        "Adelie": st.column_config.ProgressColumn(
            "Adelie", format="%f", width="medium", min_value=0, max_value=1
        ),
        "Chinstrap": st.column_config.ProgressColumn(
            "Chinstrap", format="%f", width="medium", min_value=0, max_value=1
        ),
        "Gentoo": st.column_config.ProgressColumn(
            "Gentoo", format="%f", width="medium", min_value=0, max_value=1
        ),
    },
    hide_index=True,
)

st.bar_chart(df_pred)

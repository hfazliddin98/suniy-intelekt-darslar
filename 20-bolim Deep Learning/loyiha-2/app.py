from fastai.vision.all import *
import streamlit as st
import pathlib
import plotly.express as px

pathlib.PosixPath = pathlib.WindowsPath

# title
st.title('Jonzodlarni (Ayiq, Baliq, Qushlarni) aniqlovchi model')

# rasmni joylash
file = st.file_uploader('Rasm yuklash', type=['jpg', 'png', 'jpeg', 'gif', 'svg'])

# yuklanish jarayonida xatolik ni oldini olish uchun
if file:

    # rasmni chop etish
    st.image(file)

    # PIL convert
    img = PILImage.create(file)

    # modelni yuklab olish va chaqirib olish
    model = load_learner('jonzod_model.pkl')

    # prediction (bashorat)
    pred, pred_id, probs = model.predict(img)

    # Chop qilsh
    st.success(f'Bashorat: {pred}')
    st.info(f'Ehtimolik: {probs[pred_id]*100//1}%')
    
    # ploting 
    # interaktiv grafik chiqarish uchun ishlatiladi
    fig = px.bar(x=probs*100, y=model.dls.vocab)
    st.plotly_chart(fig)
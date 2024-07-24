import pickle
import streamlit as st
import numpy as np

# Memuat model
anemia_model = pickle.load(open('anemia_model.sav', 'rb'))

# Judul web
st.title('Prediksi Anemia')

# Input data dengan contoh angka valid untuk pengujian
Redpixel = st.text_input('Redpixel', '50')
Greenpixel = st.text_input('Greenpixel', '60')
Bluepixel = st.text_input('Bluepixel', '70')
Hb = st.text_input('Hb', '14')

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Konversi input menjadi numerik
        inputs = np.array([[float(Redpixel), float(Greenpixel), float(Bluepixel), float(Hb)]])
        
        # Lakukan prediksi
        anemia_prediksi = anemia_model.predict(inputs)
        
        # Memeriksa hasil prediksi
        if anemia_prediksi[0] == 0:
            st.success('Pasien tidak terkena anemia')
        else:
            st.error('Pasien terkena anemia')
    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

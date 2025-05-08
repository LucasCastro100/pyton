import streamlit as st

pages = {
    "Segmentos": [
         st.Page("pages/bap.py", title="BAP"),
         st.Page("pages/cap.py", title="CAP"),
         st.Page("pages/pca.py", title="PCA"),
    ]    
}

pg = st.navigation(pages)
pg.run()
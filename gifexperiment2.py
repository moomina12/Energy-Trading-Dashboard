#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st


# URL of the GIF
gif_url = "https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif"

# Embed the GIF using HTML in st.markdown
st.markdown(f"![Alt Text]({gif_url})")


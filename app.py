import streamlit as st
import neattext.functions as nfx

import pandas as pd
import matplotlib.pyplot as plt

import base64
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

from wordcloud import WordCloud

def plot_wordcloud(my_text):
    my_wordcloud = WordCloud().generate(my_text)
    fig = plt.figure()
    plt.imshow(my_wordcloud, interpolation="bilinear")
    plt.axis('Off')
    st.pyplot(fig)


def text_downloader(raw_text):
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = "clean_text_result_{}_.txt".format(timestr)
    st.markdown("### ** 📩 ⬇️ Download Cleaned Text file **")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click here!</a>'
    st.markdown(href, unsafe_allow_html=True) 

def main():
    st.title("Text Cleaner App")

    menu = ["TextCleaner", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "TextCleaner":
        st.subheader("Text Cleaning")
        text_file = st.file_uploader("Upload Txt File", type=['txt'])

        normalize_case = st.sidebar.checkbox("Normalize Case")
        clean_stopwords = st.sidebar.checkbox("Stopwords")
        clean_punctuations = st.sidebar.checkbox("Punctuations")
        clean_email = st.sidebar.checkbox("Emails")
        clean_urls = st.sidebar.checkbox("Urlds")
        clean_numbers = st.sidebar.checkbox("Numbers")


        if text_file is not None:
            col1, col2 = st.columns(2)
            with col1:
                with st.expander("Original Text"):
                    raw_text = text_file.read().decode('utf-8')
                    st.write(raw_text)
                with col2:
                    with st.expander("Processed Text"):
                        if normalize_case:
                            raw_text = raw_text.lower()
                        if clean_stopwords:
                            raw_text = nfx.remove_stopwords(raw_text)
                        if clean_punctuations:
                            raw_text = nfx.remove_punctuations(raw_text)
                        if clean_email:
                            raw_text = nfx.remove_emails(raw_text)
                        if clean_urls:
                            raw_text = nfx.remove_urls(raw_text)
                        if clean_numbers:
                            raw_text = nfx.remove_numbers(raw_text)
                        st.write(raw_text)
                        text_downloader(raw_text)
            with st.expander("Plot Wordcloud"):
                plot_wordcloud(raw_text)
    else:
        st.subheader("Text Cleaner App")


if __name__ == '__main__':
    main()
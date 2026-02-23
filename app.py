import streamlit as st
import openai

st.title("🚀 emt Agentic Growth OS")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

if api_key:
    client = openai.OpenAI(api_key=api_key)
    url = st.text_input("分析対象のURL")
    memo = st.text_area("ヒアリングメモ")

    if st.button("分析開始"):
        # emtの5つのフィルター（機能・文脈・構造・根拠・実験）を指示 
        prompt = f"以下の情報をemtの『5つのフィルター』で分析して：\nURL: {url}\nメモ: {memo}"
        response = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}])
        st.write(response.choices[0].message.content)

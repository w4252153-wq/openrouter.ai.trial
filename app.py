import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv('secrets.txt')  # APIキー読み込み

# OpenRouter設定
client = openai.OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

st.title("🚀 私のAI WEBサービス（OpenRouter版）")

# モデル選択（無料軽量モデル推奨）
model = st.selectbox("モデルを選ぶ", ["openrouter/free", "google/gemma-3n-2b-it:free", "meta-llama/llama-3.1-8b-instruct:free"])

# チャット入力
if prompt := st.chat_input("質問を入力..."):
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("考え中..."):
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1024
            )
            st.write(response.choices[0].message.content)

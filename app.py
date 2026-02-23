import streamlit as st
import openai

st.set_page_config(page_title="emt Agentic Growth OS", layout="wide")
st.title("🚀 emt Agentic Growth OS")
st.caption("顧客の自己認識を分解し、価値起点で売上につながるWebへ変換します")

api_key = st.sidebar.text_input("OpenAI API Key", type="password")

if api_key:
    client = openai.OpenAI(api_key=api_key)
    url = st.text_input("分析対象のURL", placeholder="https://www.kyowa-hearts.com/")
    memo = st.text_area("ヒアリングメモ（任意）", placeholder="顧客の要望や課題を自由に入力してください")

    if st.button("分析開始"):
        # emt独自の5つのフィルターを定義
        prompt = f"""
        あなたはemt株式会社の戦略ディレクターとして、以下の情報を分析してください。
        「5つのフィルター」を用いて、顧客の自己認識を分解し、売上に直結する戦略を提案せよ。

        ①機能(Function)の分解: 物理的に何を解決している製品か？
        ②文脈(Context)の再定義: 市場で勝てる別の見せ方、顧客が気づいていない「本当の提供価値」は？
        ③構造(Structure)の設計: 売上の文脈に戻すために、どんな順序で情報を伝えるべきか？
        ④科学的根拠(Evidence): 信頼を裏付けるデータ、技術力、実績は何か？
        ⑤実験(Experiment)の仕込み: 公開後に真っ先に検証すべき「改善仮説」を3つ挙げよ

        URL: {url}
        補足メモ: {memo}
        """
        
        with st.spinner("emtの脳で戦略を立案中..."):
            response = client.chat.completions.create(
                model="gpt-4o", 
                messages=[{"role": "system", "content": "You are a professional growth strategist at emt Inc."},
                          {"role": "user", "content": prompt}]
            )
            st.markdown("---")
            st.subheader("📊 emt 戦略立案レポート")
            st.write(response.choices[0].message.content)

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# 手順4-4: .envファイルから環境変数を読み込む
load_dotenv()

# 条件4: 入力テキストとラジオボタンの選択値を受け取り、回答を返す関数を定義
def get_expert_response(user_text, expert_role):
    # LLMの初期化
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    # 条件3: 選択値に応じてシステムメッセージを変える
    if expert_role == "ITコンサルタント":
        system_prompt = "あなたは優秀なITコンサルタントです。技術的な用語を分かりやすく解説してください。"
    elif expert_role == "プロの料理人":
        system_prompt = "あなたは一流の料理人です。家庭でも試せるプロのコツを交えて答えてください。"
    else:
        system_prompt = "あなたは親切なアシスタントです。"
        
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_text),
    ]
    
    # LLMの呼び出し
    response = llm.invoke(messages)
    return response.content

# --- 画面表示部分 ---

# 条件5: Webアプリの概要や操作方法を表示
st.title("AI専門家チャット")
st.write("""
このアプリは、選んだ専門家があなたの質問に答えてくれるAIチャットアプリです。
1. 相談したい専門家をラジオボタンで選択してください。
2. 下の入力欄に相談内容を記入して送信してください。
""")

# 条件3: ラジオボタンで専門家の種類を選択
selected_expert = st.radio(
    "誰に相談しますか？",
    ("ITコンサルタント", "プロ of 料理人")
)

# 条件2: 入力フォームを用意
user_input = st.text_input("相談内容を入力してください：")

if st.button("送信"):
    if user_input:
        with st.spinner("AIが回答を生成中..."):
            # 関数の利用
            answer = get_expert_response(user_input, selected_expert)
            st.subheader("AIの回答:")
            st.write(answer)
    else:
        st.warning("相談内容を入力してください。")
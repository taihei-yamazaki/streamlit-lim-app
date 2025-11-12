import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()


def get_llm_response(input_text: str, expert_type: str) -> str:
    """
    LLMからの回答を取得する関数
    
    Args:
        input_text (str): ユーザーからの入力テキスト
        expert_type (str): 選択された専門家の種類
    
    Returns:
        str: LLMからの回答
    """
    # 専門家タイプに応じたシステムメッセージを設定
    system_messages = {
        "データサイエンティスト": "あなたはデータサイエンスの専門家です。統計学、機械学習、データ分析に関する質問に詳しく答えてください。",
        "ソフトウェアエンジニア": "あなたはソフトウェア開発の専門家です。プログラミング、アーキテクチャ設計、ベストプラクティスについて詳しく答えてください。",
        "マーケティングコンサルタント": "あなたはマーケティングの専門家です。ブランド戦略、デジタルマーケティング、顧客分析について詳しく答えてください。",
        "財務アドバイザー": "あなたは財務・金融の専門家です。投資戦略、財務計画、リスク管理について詳しく答えてください。"
    }
    
    # LLMの初期化
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    
    # メッセージの作成
    messages = [
        SystemMessage(content=system_messages[expert_type]),
        HumanMessage(content=input_text)
    ]
    
    # LLMからの回答を取得
    response = llm.invoke(messages)
    
    return response.content


def main():
    # ページ設定
    st.set_page_config(
        page_title="AI専門家相談アプリ",
        page_icon="🤖",
        layout="wide"
    )
    
    # タイトルと説明
    st.title("🤖 AI専門家相談アプリ")
    st.markdown("---")
    
    # アプリの概要説明
    st.markdown("""
    ### 📖 アプリの概要
    このアプリは、様々な分野の専門家AIに相談できるWebアプリケーションです。
    質問したい分野の専門家を選択し、質問を入力することで、AIが専門家として回答します。
    
    ### 🔧 操作方法
    1. **専門家を選択**: 下のラジオボタンから相談したい分野の専門家を選択してください
    2. **質問を入力**: テキストエリアに質問や相談内容を入力してください
    3. **回答を取得**: 「回答を取得」ボタンをクリックすると、AIが専門家として回答します
    """)
    
    st.markdown("---")
    
    # 専門家の種類を選択するラジオボタン
    st.subheader("👨‍💼 専門家を選択")
    expert_type = st.radio(
        "相談したい専門家の分野を選択してください:",
        ["データサイエンティスト", "ソフトウェアエンジニア", "マーケティングコンサルタント", "財務アドバイザー"],
        horizontal=True
    )
    
    st.markdown("---")
    
    # 入力フォーム
    st.subheader("💬 質問を入力")
    input_text = st.text_area(
        "質問や相談内容を入力してください:",
        height=150,
        placeholder="例: Pythonでデータを効率的に処理する方法を教えてください"
    )
    
    # 送信ボタン
    if st.button("🚀 回答を取得", type="primary"):
        if input_text:
            with st.spinner("回答を生成中..."):
                try:
                    # LLMから回答を取得
                    response = get_llm_response(input_text, expert_type)
                    
                    # 回答を表示
                    st.markdown("---")
                    st.subheader("✨ 回答")
                    st.success(f"**{expert_type}からの回答:**")
                    st.write(response)
                    
                except Exception as e:
                    st.error(f"エラーが発生しました: {str(e)}")
                    st.info("OpenAI APIキーが正しく設定されているか確認してください。")
        else:
            st.warning("⚠️ 質問を入力してください。")


if __name__ == "__main__":
    main()
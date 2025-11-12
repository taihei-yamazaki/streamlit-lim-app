# AI専門家相談アプリ

## 概要
このアプリは、Streamlitを使用して構築されたLLM搭載Webアプリケーションです。様々な分野の専門家AIに相談でき、選択した専門家の視点から回答を得ることができます。

## 機能
- 4つの専門家タイプから選択可能:
  - データサイエンティスト
  - ソフトウェアエンジニア
  - マーケティングコンサルタント
  - 財務アドバイザー
- LangChainを使用したLLM統合
- リアルタイムでの回答生成

## セットアップ

### 1. 必要なパッケージのインストール
```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定
`.env`ファイルを作成し、OpenAI APIキーを設定してください:
```
OPENAI_API_KEY=your_actual_api_key_here
```

### 3. アプリの起動
```bash
streamlit run app.py
```

## Streamlit Community Cloudへのデプロイ
1. GitHubリポジトリにコードをプッシュ
2. Streamlit Community Cloudにアクセス
3. リポジトリを選択してデプロイ
4. Secretsセクションで`OPENAI_API_KEY`を設定

Pythonバージョンは`.python-version`ファイルで3.11に指定されています。

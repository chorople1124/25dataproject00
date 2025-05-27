import yfinance as yf
import pandas as pd
import plotly.express as px

# 글로벌 시총 상위 10개 기업 티커 (2025년 기준 예시)
tickers = [
    "AAPL",  # 애플
    "MSFT",  # 마이크로소프트
    "GOOGL", # 알파벳
    "AMZN",  # 아마존
    "TSLA",  # 테슬라
    "BRK-B", # 버크셔 해서웨이 B주
    "NVDA",  # 엔비디아
    "META",  # 메타 (페이스북)
    "TSM",   # TSMC
    "V"      # 비자
]

# 데이터프레임 만들기
df_list = []

for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")  # 최근 1개월 데이터
    hist = hist.reset_index()
    hist["Ticker"] = ticker
    df_list.append(hist)

df = pd.concat(df_list)

# 날짜별 종가 데이터 시각화 (라인 차트)
fig = px.line(df, x="Date", y="Close", color="Ticker",
              title="글로벌 시총 상위 10개 기업 최근 1개월 주가 추이",
              labels={"Close": "종가", "Date": "날짜", "Ticker": "기업"})

fig.show()

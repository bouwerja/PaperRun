from PaperRun import get_TickerHistory

data = get_TickerHistory(ticker="AAPL", history="1d", interval="1h")
print(data)

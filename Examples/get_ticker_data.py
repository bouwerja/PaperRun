from PaperRun import get_TickerHistory

data = get_TickerHistory(ticker="AAPL", history="1d", interval="1h")
print(data)

# --- Example of Output ---
#
# {
#     '0': {
#         'DateTime': datetime.datetime(2025, 9, 26, 9, 30),
#         'Open': 254.1300048828125,
#         'High': 256.6000061035156,
#         'Low': 253.77999877929688,
#         'Close': 255.02000427246094,
#         'Volume': 8034498,
#         'Dividends': 0.0,
#         'StockSplits': 0.0
#     },
#     '1': {
#         'DateTime': datetime.datetime(2025, 9, 26, 10, 30),
#         'Open': 255.02000427246094,
#         'High': 255.99000549316406,
#         'Low': 254.57119750976562,
#         'Close': 255.9700927734375,
#         'Volume': 3714841,
#         'Dividends': 0.0,
#         'StockSplits': 0.0
#     },
#     '2': {
#         'DateTime': datetime.datetime(2025, 9, 26, 11, 30),
#         'Open': 255.97000122070312,
#         'High': 256.0400085449219,
#         'Low': 254.86000061035156,
#         'Close': 255.6649932861328,
#         'Volume': 2276774,
#         'Dividends': 0.0,
#         'StockSplits': 0.0
#     },
#     '3': {
#         'DateTime': datetime.datetime(2025, 9, 26, 12, 30),
#         'Open': 255.66000366210938,
#         'High': 256.9750061035156,
#         'Low': 255.47999572753906,
#         'Close': 256.5199890136719,
#         'Volume': 2086042,
#         'Dividends': 0.0,
#         'StockSplits': 0.0
#     },
#     '4': {
#         'DateTime': datetime.datetime(2025, 9, 26, 13, 30),
#         'Open': 256.5199890136719,
#         'High': 257.3599853515625,
#         'Low': 255.86000061035156,
#         'Close': 256.55499267578125,
#         'Volume': 2653513,
#         'Dividends': 0.0,
#         'StockSplits': 0.0
#     },
#     '5': {
#         'DateTime': datetime.datetime(2025, 9, 26, 14, 30),
#         'Open': 256.56500244140625,
#         'High': 256.7298889160156,
#         'Low': 255.49000549316406,
#         'Close': 255.64500427246094,
#         'Volume': 2089315,
#         'Dividends': 0.0,
#         'StockSplits': 0.0
#     },
#     '6': {
#         'DateTime': datetime.datetime(2025, 9, 26, 15, 30),
#         'Open': 255.63999938964844,
#         'High': 255.64979553222656,
#         'Low': 254.89999389648438,
#         'Close': 255.4600067138672,
#         'Volume': 3021515,
#         'Dividends': 0.0,
#         'StockSplits': 0.0
#     }
# }

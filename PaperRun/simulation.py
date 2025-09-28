import json
import os
import yfinance as yf
from datetime import datetime

# -- Simulation File ---
filename = "account.json"


def get_TickerHistory(ticker: str = "", history: str = "1d", interval: str = "1h"):
    """
    get_TickerHistory(ticker=None, history=0, interval=0)

    Description:
    -------------
    This function fetches historical stock data for a given ticker symbol using the yfinance library.
    It returns the data as a dictionary, where each key corresponds to a row of historical data containing
    open, high, low, close, volume, dividends, and stock splits for a specific datetime.

    Parameters:
    -----------
    - ticker : str
        The stock symbol from Yahoo Finance (e.g., "AAPL" for Apple, "GOOG" for Alphabet).
        If not provided, the function will prompt for a valid ticker.

    - history : str
        The historical period to fetch. Accepts yfinance period strings such as:
            "1d"   - 1 day
            "5d"   - 5 days
            "1mo"  - 1 month
            "3mo"  - 3 months
            "1y"   - 1 year
            "5y"   - 5 years
            "max"  - maximum available history
        If not provided or invalid, defaults to "1d".

    - interval : str
        The time interval between data points. Accepts yfinance interval strings such as:
            "1m"   - 1 minute
            "5m"   - 5 minutes
            "15m"  - 15 minutes
            "1h"   - 1 hour
            "1d"   - 1 day
            "1wk"  - 1 week
            "1mo"  - 1 month
        If not provided or invalid, defaults to "1h".

    Returns:
    --------
    - dict
        A dictionary of historical data, where each key is a sequential index string ("0", "1", ...), and
        each value is another dictionary containing:
            "DateTime"   : datetime object (timezone removed)
            "Open"       : float
            "High"       : float
            "Low"        : float
            "Close"      : float
            "Volume"     : int
            "Dividends"  : float
            "StockSplits": float

    Exceptions:
    -----------
    - If the ticker is invalid or the yfinance request fails, the function prints the exception and returns None.

    Example Usage:
    --------------
    ticker_history = get_TickerHistory(ticker="AAPL", history="5d", interval="1h")
    """

    ticker_interval_data = {
        "DateTime": None,
        "Open": 0,
        "High": 0,
        "Low": 0,
        "Close": 0,
        "Volume": 0,
        "Dividends": 0,
        "StockSplits": 0,
    }
    ticker_value = None
    ticker_data = {}

    if ticker == "":
        print(
            "Please provide a valid ticker from the yahoo finance website \nExample: [https://finance.yahoo.com/quote/AAPL/] => AAPL"
        )
    try:
        ticker_value = yf.Ticker(ticker)
    except Exception as e:
        print("1. Exception Occured: ", e)
        return

    if history == 0 or interval == 0:
        print(
            "Please procide a valid history or interval amount \nExample: 5 days = 5d, 1 hour = 1h \n  -> Using default values: 1 day and 1 hour"
        )

        try:
            _data = ticker_value.history(period="1d", interval="1h")

            for i, (index, row) in enumerate(_data.iterrows()):
                dt: datetime = index.to_pydatetime().replace(tzinfo=None)
                ticker_interval_data = {
                    "DateTime": dt,
                    "Open": float(row["Open"]),
                    "High": float(row["High"]),
                    "Low": float(row["Low"]),
                    "Close": float(row["Close"]),
                    "Volume": int(row["Volume"]),
                    "Dividends": float(row["Dividends"]),
                    "StockSplits": float(row["Stock Splits"]),
                }
                ticker_data[f"{i}"] = ticker_interval_data

            return ticker_data
        except Exception as e:
            print("2. Exception Occured: ", e)
    else:
        try:
            _data = ticker_value.history(period=history, interval=interval)

            for i, (index, row) in enumerate(_data.iterrows()):
                dt: datetime = index.to_pydatetime().replace(tzinfo=None)
                ticker_interval_data = {
                    "DateTime": dt,
                    "Open": float(row["Open"]),
                    "High": float(row["High"]),
                    "Low": float(row["Low"]),
                    "Close": float(row["Close"]),
                    "Volume": int(row["Volume"]),
                    "Dividends": float(row["Dividends"]),
                    "StockSplits": float(row["Stock Splits"]),
                }
                ticker_data[f"{i}"] = ticker_interval_data

            return ticker_data
        except Exception as e:
            print("3. Exception Occured: ", e)


accountView = {
    "Initial": {
        "AccountValue": 0,
        "PositionsOpened": 0,
        "LongPositions": 0,
        "ShortPositions": 0,
        "PositionsWon": 0,
        "PositionsLost": 0,
        "CapitalGained": 0,
        "AmountInvested": 0,
        "UnitesBought": 0,
        "LongPosition": False,
        "Position_PnL": 0,
    }
}


def simulation(
    ticker_name: str = "",
    history: str = "1d",
    interval: str = "1h",
    buy: bool = False,
    sell: bool = False,
    initial_balance: int = 0,
    save_account: bool = False,
    savefile_path: str = "simulation_savefile.json",
):
    if ticker_name == "":
        pass
    else:
        data = get_TickerHistory(ticker=ticker_name, history=history, interval=interval)

    accountView["Initial"]["AccountValue"] = initial_balance

    if save_account:
        with open(savefile_path, "w") as f:
            json.dump(accountView, f, indent=4)

        print("\nTrading Simulation file saved at: ", savefile_path)

    return accountView


simulation(initial_balance=100, save_account=True)
print(accountView)

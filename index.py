import requests
import pandas as pd

# --- UPDATE THESE WITH YOUR APP DETAILS ---
CLIENT_ID = 'PASTE_YOUR_APP_KEY_HERE'
CLIENT_SECRET = 'PASTE_YOUR_APP_SECRET_HERE'
REDIRECT_URI = 'https://127.0.0.1'

def get_market_data(ticker, access_token):
    # This fetches the last 200 days of data for your indicators
    url = f"https://api.schwab.com/marketdata/v1/pricehistory?symbol={ticker}&periodType=year&period=1&frequencyType=daily&frequency=1"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers).json()
    
    # Convert to DataFrame for technical calculation
    df = pd.DataFrame(response['candles'])
    
    # Calculate your Strategic Indicators
    df['EMA20'] = df['close'].ewm(span=20, adjust=False).mean()
    df['SMA50'] = df['close'].rolling(window=50).mean()
    df['SMA200'] = df['close'].rolling(window=200).mean()
    
    return df.iloc[-1] # Return the most recent values

# --- DECISION LOGIC ---
# If Price > 200 SMA AND 20 EMA > 50 SMA => GREEN (BUY)
# If Price < 200 SMA => RED (SELL/STOP)
# Else => YELLOW (HOLD)

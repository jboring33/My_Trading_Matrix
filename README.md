# Schwab ETF Decision Agent

An automated technical analysis tool designed for retiree portfolio management, monitoring high-income ETF positions using the Schwab Trader API.

## Investment Strategy (20/50/200 Matrix)
This agent applies a multi-layered momentum filter:
- **🟢 GREEN (Buy/DCA):** Price > 200-Day SMA **AND** 20-Day EMA > 50-Day SMA.
- **🔴 RED (Sell/Protect):** Price < 200-Day SMA.
- **🟡 YELLOW (Hold):** Trend is neutral or consolidating.

## Technical Setup
1. **Environment:** Designed for ChromeOS Penguin (Linux) environment.
2. **Python Version:** 3.x
3. **Execution:** Run via `python3 main.py`

## Security Note
**NEVER** commit your App Secret or App Key to a public repository. Use a `.env` file or environment variables to store credentials.

*Disclaimer: Not financial advice. Past performance does not guarantee future results.*

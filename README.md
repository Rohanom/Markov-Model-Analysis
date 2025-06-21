# Markov-Model-Analysis
# 🔍 Medallion-Inspired Quantitative Strategy: Markov Chains & Candle Streaks

## 🧠 Backstory & Motivation

After diving deep into **Jim Simons’ Medallion Fund** — the most successful hedge fund in history — I became captivated by its secretive inner workings. While direct access to the fund’s code is impossible, **Gregory Zuckerman’s book _“The Man Who Solved the Market”_** offered valuable hints:

> They began with **Markov chains** and gradually layered in **machine learning**, **nonlinear models**, and **advanced statistics**.

Inspired by this, I attempted to **reverse-engineer** a simplified, interpretable version of the original strategy by:
- Modeling stock market behavior using **Markov processes** based on "up" and "down" states.
- Testing **statistical candle streak patterns** using backtesting engines.
- Running experiments across **20 major U.S. stocks and ETFs**.

---

## 🧩 Project Structure

### 📁 `file1_markov_chain.py`

> **Objective:** Use historical stock data to construct a **Markov chain-based model** of market states.

#### Highlights:
- Data source: `SPY` ETF from 2010–2025 using `yfinance`.
- Labels each day as `"up"` 📈 or `"down"` 📉 based on daily returns.
- Constructs a **2x2 transition matrix** showing:
  - `P(up → up)`, `P(up → down)`
  - `P(down → up)`, `P(down → down)`
- Analyzes streak patterns like **5 red candles ➡️ green**:

Probability of 📈 after 📉📉📉📉📉 = 67.3%


---

### 📁 `file2_backtesting_streaks.py`

> **Objective:** Implement and **backtest streak-based trading strategies** using candle color logic.

#### Core Components:
- Downloads data for **20 tickers** (AAPL, SPY, QQQ, ARKK, etc.).
- Calculates how often **10 green/red candles** are followed by reversal.
- 📗📗📗📗📗📗📗📗📗📗 ➡️ 📕 → **42%**
- 📕📕📕📕📕📕📕📕📕📕 ➡️ 📗 → **65%**
- Implements two strategies using `Backtesting.py`:
1. **ConsecutiveRedGreenStrategy**: Long after `n` red, short after `n` green candles.
2. **ConsecutiveRedStrategy**: Buy after 3 red candles, close same-day.

#### Results:
Backtests were run on all 20 tickers.

| Ticker | Return (%) |
|--------|------------|
| AAPL   | -10.69     |
| MSFT   | -12.35     |
| GOOGL  | -10.90     |
| AMZN   | 56.78      |
| META   | 71.91      |
| TSLA   | 60.33      |
| NVDA   | -13.42     |
| JPM    | -28.41     |
| JNJ    | 2.32       |
| V      | 77.97      |
| SPY    | -19.96     |
| QQQ    | -1.30      |
| DIA    | -38.14     |
| IWM    | -27.31     |
| ARKK   | -25.21     |
| XLF    | -26.34     |
| XLK    | 1.53       |
| XLV    | -12.28     |
| XLE    | -29.17     |
| XLY    | 11.74      |

**Aggregate Performance:**
- **Total Return:** `+27.13%`
- **Average Return per Asset:** `+1.36%`
- **Maximum Drawdown Observed:** `-46.76%`

---

## 🧠 Key Insights

- **Markov Chain models** can capture short-term momentum and reversal regimes.
- Candle streaks reveal **hidden market biases** not easily spotted with basic indicators.
- Some assets (AMZN, META, TSLA) show high profit potential using simple reversal strategies.
- Even with basic logic, **behavioral inefficiencies** can be modeled quantitatively.
- Backtesting across **diverse sectors** gives a better real-world robustness picture.

---

## 📌 Future Work

- Incorporate **Hidden Markov Models (HMMs)** for more flexible regime detection.
- Add **volatility-based filters** to avoid whipsaws.
- Explore **LSTM-enhanced streak modeling** for sequence learning.
- Add **position sizing optimization** and **risk-adjusted returns**.

---

## 👤 Author

**Om Aditya**  
_B.Tech @ IIT Jodhpur | Markets, Quant, and ML Enthusiast_  
📘 Passionate about decoding financial anomalies  
🔗 [LinkedIn](https://www.linkedin.com/in/omaditya8)  
💻 [Github](https://github.com/Rohanom)  


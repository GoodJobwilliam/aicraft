# AI + Trading: 30 Prompts for Stock Analysis

30 practical prompts that combine AI with stock market analysis.
For traders who use AI tools (Claude, ChatGPT, OpenCode, Cursor) to support research and decision-making.

---

## What's Inside

| Category | Prompts | Use Case |
|----------|---------|----------|
| 📊 Order Book & Tape Reading | 5 | Analyze level 2 data, order flow, and tick-level patterns |
| 🕯 Technical Analysis | 5 | Candlestick patterns, indicators, chart structure |
| 💰 Fund Flow Analysis | 4 | Track institutional money movement |
| 📰 News & Sentiment | 4 | News impact assessment, market sentiment |
| 📋 Trade Journal Analysis | 4 | Review and improve your trading decisions |
| 🔍 Screening & Scanning | 4 | Find candidates based on specific criteria |
| ⚙️ Strategy & Backtesting | 4 | Design and validate trading approaches |

---

## 1. 📊 Order Book & Tape Reading

### 1.1 Order Book Structure Analysis
```
Context: [STOCK_SYMBOL] Level 2 order book data at [TIME]:
  Bids: [PRICE_1 x VOL_1] → [PRICE_5 x VOL_5]
  Asks: [PRICE_1 x VOL_1] → [PRICE_5 x VOL_5]

Task: Analyze order book structure for:
- Bid/ask wall detection (orders > 2x average size)
- Order book imbalance (bid volume / ask volume ratio)
- Spoofing patterns (large orders that don't intend to execute)
- Support/resistance levels implied by order clusters

Output: Structured analysis with:
- Wall levels and sizes
- Imbalance direction and magnitude
- Spoofing probability (low/medium/high)
- Suggested attention price levels
```

### 1.2 Tick-Level Tape Reading
```
Context: [STOCK_SYMBOL] tick data for the last [N] minutes:
  [TIMESTAMP] [SIDE] [PRICE] [SIZE] [CONDITION]
  ...

Task: Analyze the tape for:
- Large lot detection (trades > [N] shares/mini lots)
- Aggressive buying/selling (market orders hitting bids/asks)
- Bid/ask inching (price moving one tick at a time with volume)
- Absorption pattern (price not moving despite large trades)
- Iceberg order detection (repeated same price, same size)

Output: Tick analysis summary with pattern identification
```

### 1.3 Auction / Opening Range Analysis
```
Context: [STOCK_SYMBOL] pre-market / opening auction data:
  Opening call auction: [VOLUME] shares at [PRICE]
  First [N] minute volume: [VOLUME]
  VWAP: [PRICE]
  Opening range: [HIGH] - [LOW]

Task: Analyze opening auction quality:
- Auction volume vs. daily average (strong/weak opening)
- Price gap from previous close
- Early direction bias (first 5 min trend)
- Large participant activity indication

Output: Opening analysis with institutional activity indication
```

### 1.4 Large Order Detection
```
Context: [STOCK_SYMBOL] order flow over the last [PERIOD]:
  [Order Book snapshots and trade data]

Task: Identify anomalous order activity:
- Orders significantly larger than average
- Repeated same-price orders (iceberg pattern)
- Sweep orders (taking out multiple price levels)
- Complex conditional orders (detected through pattern)

Output: Large order report with size estimates and inferred intent
```

### 1.5 Closing Auction Analysis
```
Context: [STOCK_SYMBOL] closing auction data:
  Last [N] minutes of continuous trading
  Call auction period imbalance
  Final match price and volume

Task: Analyze closing auction:
- Imbalance direction before close (buying/selling pressure)
- Price movement relative to continuous session
- Volume concentration (is this institution positioning?)
- Comparison to recent closing trends

Output: Closing analysis with next-day bias indication
```

---

## 2. 🕯 Technical Analysis

### 2.1 Candlestick Pattern Recognition
```
Context: [STOCK_SYMBOL] daily candlestick data for the last [N] days:
  Date | Open | High | Low | Close | Volume

Task: Identify and interpret candlestick patterns:
- Single-bar patterns: doji, hammer, shooting star, marubozu
- Two-bar patterns: engulfing, harami, piercing, dark cloud
- Three-bar patterns: morning/evening star, three white soldiers, three black crows
- Context: within the recent [N]-day trend

Output: Detected patterns with:
- Pattern name and location
- Reliability rating for current context
- Implied next-day bias
- Invalidating condition
```

### 2.2 Multi-Indicator Confluence
```
Context: [STOCK_SYMBOL] indicator data:
  SMA(20): [VALUE], SMA(60): [VALUE], SMA(200): [VALUE]
  RSI(14): [VALUE], MACD: [VALUE], Signal: [VALUE], Histogram: [VALUE]
  Bollinger Bands: Upper [VALUE], Mid [VALUE], Lower [VALUE]
  Volume SMA(20): [VALUE], Current Volume: [VALUE]

Task: Find confluence zones where multiple indicators agree:
- Overbought/oversold + trend direction
- Support/resistance from multiple timeframes
- Volume confirmation of price action
- Divergence detection (price vs. RSI/MACD)

Output: Confluence map with strength scores per zone
```

### 2.3 Trend Structure Analysis
```
Context: [STOCK_SYMBOL] price data for [TIMEFRAME]:

Task: Analyze trend structure:
- Primary trend direction and strength
- Higher highs / lower lows structure
- Trend channel boundaries
- Pullback vs. reversal identification
- Momentum acceleration/deceleration

Output: Trend structure report with:
- Current trend phase (early/mature/late)
- Key structure levels
- Momentum state (strengthening/weakening)
```

### 2.4 Divergence Scanner
```
Context: [STOCK_SYMBOL] price and oscillator data:
  Price: [DATA_POINTS]
  RSI(14): [DATA_POINTS]
  MACD: [DATA_POINTS]
  Volume: [DATA_POINTS]

Task: Scan for divergences:
- Regular divergence (price makes HH but oscillator makes LH) → potential reversal
- Hidden divergence (price makes HL but oscillator makes LL) → trend continuation
- Multiple timeframe divergence alignment

Output: Divergence report with:
- Type (regular/hidden)
- Timeframe alignment
- Strength rating
- Suggested action
```

### 2.5 Volume Profile / Market Profile
```
Context: [STOCK_SYMBOL] time & sales data or volume-by-price data:

Task: Analyze volume profile:
- High volume nodes (price levels with most trading)
- Low volume nodes (gaps / potential support/resistance)
- Volume-weighted average price and deviation
- Developing vs. completed auction
- Initiative vs. responsive activity

Output: Volume profile analysis with key levels
```

---

## 3. 💰 Fund Flow Analysis

### 3.1 Large Trader Flow Detection
```
Context: [STOCK_SYMBOL] trade data by size bracket for [PERIOD]:
  Small (<[N]): [VOLUME]
  Medium ([N]-[N]): [VOLUME]
  Large ([N]-[N]): [VOLUME]
  Huge (>[N]): [VOLUME]
  Total: [VOLUME]

Task: Analyze fund flow:
- Are large traders accumulating or distributing?
- Is large trade volume increasing or decreasing as % of total?
- Price correlation: do large trades happen at bid or ask?
- Trend alignment: are large traders buying dips or selling rips?

Output: Fund flow analysis with inferred direction
```

### 3.2 Sector Flow Rotation
```
Context: Sector and industry group flow data for [DATE]:
  [SECTOR_1]: Net Flow +[N]M, Top stock: [CODE]
  [SECTOR_2]: Net Flow -[N]M, Top stock: [CODE]
  ...

Task: Analyze sector rotation:
- Leading sectors and their strength
- Trailing sectors (potential reversal candidates)
- Capital flow pattern (defensive → cyclical, or vice versa)
- Market phase implication

Output: Sector rotation map
```

### 3.3 Block Trade Identification
```
Context: [STOCK_SYMBOL] trade data for [DATE]:

Task: Identify significant block trades:
- Trades exceeding [N] shares/mini lots
- Off-exchange / dark pool trades
- Cross trades
- Time concentration (multiple blocks in short period)
- Price impact analysis

Output: Block trade log with inferred parties and motives
```

### 3.4 Short Interest & Borrow Analysis
```
Context: [STOCK_SYMBOL] short data:
  Short Interest: [N] shares ([N]% of float)
  Days to Cover: [N]
  Borrow Rate: [N]%
  Available Shares to Borrow: [N]

Task: Analyze short interest:
- Short interest trend (increasing/decreasing)
- Squeeze potential (high SI + low borrow availability)
- Correlation with price action
- Historical comparison

Output: Short interest analysis with squeeze risk rating
```

---

## 4. 📰 News & Sentiment

### 4.1 News Impact Assessment
```
Context: Related news for [STOCK_SYMBOL]:
  - [HEADLINE_1] — [SOURCE]
  - [HEADLINE_2] — [SOURCE]

Task: Assess news impact:
- Relevance (0-10)
- Sentiment (positive/negative/neutral)
- Expected impact magnitude (on a 1-5 scale)
- Duration of expected impact (intraday / multi-day / structural)
- Prior expectations (was this priced in?)

Output: News impact assessment
```

### 4.2 Social Media / Forum Sentiment
```
Context: Social media mentions of [STOCK_SYMBOL] for [PERIOD]:
  Total mentions: [N]
  Positive: [N]%, Negative: [N]%, Neutral: [N]%
  Key topics: [TOPIC_1], [TOPIC_2], [TOPIC_3]

Task: Analyze sentiment:
- Sentiment trend vs. price trend (convergence or divergence)
- Topic clustering (what are people talking about?)
- Unusual activity detection (volume spike in mentions)
- Influence weighting (are key voices bullish/bearish?)

Output: Social sentiment analysis
```

### 4.3 Earnings Call Transcript Analysis
```
Context: [STOCK_SYMBOL] earnings call transcript [QUARTER]:

Task: Analyze transcript:
- Management tone (confident/defensive/evasive)
- Key forward-looking statements
- Analyst concerns (what was asked repeatedly?)
- Changes in guidance language vs. prior quarter
- Buried negative information

Output: Earnings call analysis with sentiment indicators
```

### 4.4 Market-Wide Sentiment Summary
```
Context: Market data, news, and sentiment indicators:
  Major indices: [DATA]
  VIX / Fear & Greed Index: [VALUE]
  Sector performance: [DATA]
  Key headlines: [HEADLINES]

Task: Generate market sentiment summary:
- Overall market environment (risk-on/risk-off)
- Breadth analysis (advancers/decliners)
- Leadership structure (broad vs. narrow participation)
- Key risks and catalysts

Output: Market sentiment report
```

---

## 5. 📋 Trade Journal Analysis

### 5.1 Trade Performance Review
```
Context: My trading journal data for [PERIOD]:
  Total trades: [N]
  Win rate: [N]%
  Avg win: [N] pts, Avg loss: [N] pts
  Profit factor: [N]
  Max drawdown: [N]%
  Best/worst trade: [DESCRIPTION]

Task: Analyze trading performance:
- Strategy-specific performance breakdown
- Time-of-day performance pattern
- Holding period vs. return correlation
- Slippage analysis
- Consecutive loss recovery analysis

Output: Performance review with improvement suggestions
```

### 5.2 Trade Review (Individual)
```
Context: I traded [STOCK_SYMBOL] on [DATE]:
  Entry: [PRICE] at [TIME]
  Exit: [PRICE] at [TIME]
  Reason for entry: [REASON]
  Reason for exit: [REASON]
  Result: Profit/Loss of [N]

Task: Review this trade:
- Did the entry align with the stated plan?
- Was there a clear invalidation / stop level?
- Was the exit based on plan or emotion?
- What could have been done better?
- What was done well?

Output: Trade review with improvement focus
```

### 5.3 Pattern Recognition in Losses
```
Context: My recent losing trades:
  [TRADE_1_DETAILS]
  [TRADE_2_DETAILS]
  [TRADE_3_DETAILS]

Task: Identify common patterns across losing trades:
- Time of day
- Market conditions
- Emotional state
- Deviation from plan
- Sizing errors
- Exit mistakes

Output: Loss pattern analysis with corrective actions
```

### 5.4 Trading Plan Consistency Check
```
Context: My trading plan:
  [PLAN_RULES]
  [PLAN_RULES]

My recent trades:
  [TRADE_LOG]

Task: Audit plan consistency:
- Plan adherence rate (% of trades following all rules)
- Most commonly broken rules
- Consequence analysis (did breaking rules cause losses?)
- Plan refinement suggestions

Output: Plan adherence report
```

---

## 6. 🔍 Screening & Scanning

### 6.1 Custom Screener (Technical + Fundamental)
```
Task: Find stocks meeting these criteria:
  Technical:
  - Price > SMA(200) and SMA(50) > SMA(200)
  - RSI(14) between 40 and 60
  - Volume > 1.5x 20-day average
  Fundamental:
  - P/E between 10 and 25
  - Market cap > [N] billion
  - Revenue growth > [N]% YoY

Output: Screen results with match score for each candidate
```

### 6.2 Breakout Scanner
```
Context: I scan for breakouts in [MARKET/SECTOR].

Task: Define breakout scan criteria:
- Price breaking above [N]-day high with volume confirmation
- Consolidation period minimum [N] days
- Relative strength vs. sector
- Volume confirmation rule (volume > [N]x average)
- Pullback rejection pattern near breakout level

Output: Breakout candidate list with setup quality rating
```

### 6.3 Reversal Candidate Scanner
```
Context: Scanning for potential reversal plays.

Task: Define reversal scan criteria:
- Extended from moving average (price > [N]% above/below SMA(20))
- RSI in oversold (<30) or overbought (>70) zone
- Divergence forming on RSI/MACD
- Volume showing exhaustion
- Key support/resistance level proximity

Output: Reversal candidate list with trigger levels
```

### 6.4 Gap and Go Scanner
```
Context: Pre-market scanning for gap plays.

Task: Define gap scan criteria:
- Gap size: [N]% to [N]% from previous close
- Gap direction and pre-market volume
- Relative volume vs. 5-day average
- Catalyst check (news / earnings / sector move)
- Gap fill probability assessment

Output: Gap trading candidates with fill probabilities
```

---

## 7. ⚙️ Strategy & Backtesting

### 7.1 Strategy Hypothesis Design
```
Context: I want to build a strategy based on [IDEA].

Task: Formalize the strategy hypothesis:
- Entry conditions (specific, quantifiable)
- Exit conditions (target, stop, time stop)
- Risk management rules
- Market filter / when to skip
- Position sizing rule
- Expected edge source (why should this work?)

Output: Strategy specification document
```

### 7.2 Backtest Result Analysis
```
Context: Backtest results for [STRATEGY_NAME]:
  Period: [START_DATE] - [END_DATE]
  Total trades: [N]
  Win rate: [N]%
  Profit factor: [N]
  Max drawdown: [N]%
  Sharpe ratio: [N]
  Average trade: [N]
  Best/worst trade: [DESCRIPTION]

Task: Analyze backtest results:
- Is the strategy robust or curve-fitted?
- Does performance hold across different market regimes?
- Is the sample size sufficient?
- Are there look-ahead bias risks?
- Slippage/commission sensitivity

Output: Backtest analysis with validation confidence
```

### 7.3 Regime Detection & Strategy Selection
```
Context: Current market conditions:
  VIX: [VALUE]
  Trend strength (ADX): [VALUE]
  Volatility (ATR): [VALUE]
  Correlation / dispersion: [VALUE]

Task: Match current regime to appropriate strategy:
- Trending market → trend-following strategies
- Range-bound → mean-reversion strategies
- High volatility → breakout strategies
- Low volatility → options/vol strategies

Output: Recommended strategy allocation for current regime
```

### 7.4 Risk Sizing Calculator
```
Context: Account parameters:
  Account size: [N]
  Risk per trade: [N]%
  Strategy win rate: [N]%
  Strategy avg RR: [N]

Task: Calculate position sizing:
  Entry price: [VALUE]
  Stop loss: [VALUE]
  Take profit: [VALUE]

Calculate:
- Position size (shares/contracts)
- Dollar risk amount
- R-multiple of target
- Kelly fraction
- Portfolio heat (total risk across open positions)

Output: Position sizing recommendation
```

---

## Important Disclaimers

**These prompts are analysis tools, not trading advice.**
- Past performance does not guarantee future results
- All analysis should be verified independently
- Never risk capital you cannot afford to lose
- Always use stop losses and proper risk management
- Consult a licensed financial advisor for investment decisions

The prompts are designed to assist research and analysis — they do not replace professional judgment, market experience, or proper risk management.

---

## License & Usage

Personal and commercial use allowed for individual traders.
Not for redistribution or resale as a product.

© 2026 AICraft. All rights reserved.

Playing around with a simplistic delay-based stock trading algorithm to trade on MarketWatch.com, using the Moira API available on GitHub.

Used UGAZ 3x ETN linked to natural gas.

Approach 1 (pricecomp.py): Use micro-delay between Google and MarketWatch quotes to execute high-frequency trades by "peeking into the future". Not applicable to real markets.

Approach 2 (not yet coded): Observe that UGAZ note is linked 3x, meaning if the price of natural gas moves x %, then UGAZ moves 3*x %. Thus, if natural gas is in a state of high volatility but the price remains the same (example: price goes up 10%, down 10%, and up ~1%), then the corresponding change in UGAZ would result in its price ending lower than the starting price. Thus, we can construct a strategy based on natural gas volatility and the assumption that UGAZ will most likely eventually short to 0.
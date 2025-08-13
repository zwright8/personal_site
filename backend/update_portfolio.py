#!/usr/bin/env python3
"""
Daily Portfolio Data Update Script
Updates portfolio fundamentals and market data after market close
"""

import json
import os
import sys
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import requests
import yfinance as yf

class PortfolioUpdater:
    def __init__(self):
        self.fmp_api_key = os.getenv('FMP_API_KEY', 'UvCBOf7TVzQhvA6DitrvsLy957xpRFkB')
        self.alpha_vantage_api_key = os.getenv('ALPHA_VANTAGE_API_KEY', 'JDMGKWTJYYUX9PMI')
        
        # Portfolio holdings from your current site
        self.holdings = [
            'PLTR', 'NVDA', 'OXY', 'AMZN', 'BRK.B', 'META', 'SPGI', 
            'AAPL', 'GOOGL', 'SNOW', 'C', 'BAC', 'SIRI', 'LLYVK', 'NU', 'UNP', 'TSM', 'TSLA', 'UI'
        ]
        
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        os.makedirs(self.data_dir, exist_ok=True)
        
    def fetch_from_fmp(self, endpoint: str, params: Dict[str, str] = None) -> Optional[Dict]:
        """Fetch data from Financial Modeling Prep API"""
        if params is None:
            params = {}
        params['apikey'] = self.fmp_api_key
        
        url = f"https://financialmodelingprep.com/api/v3/{endpoint}"
        
        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"FMP API error for {endpoint}: {e}")
            return None
    
    def fetch_from_alpha_vantage(self, function: str, symbol: str = None) -> Optional[Dict]:
        """Fetch data from Alpha Vantage API"""
        params = {
            'function': function,
            'apikey': self.alpha_vantage_api_key
        }
        
        if symbol:
            params['symbol'] = symbol
            
        url = "https://www.alphavantage.co/query"
        
        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Alpha Vantage API error for {function}: {e}")
            return None
    
    def get_stock_fundamentals(self, symbol: str) -> Dict[str, Any]:
        """Get comprehensive stock fundamentals"""
        fundamentals = {
            'symbol': symbol,
            'last_updated': datetime.now().isoformat(),
            'price': 0,
            'change': 0,
            'change_percent': 0,
            'market_cap': 0,
            'pe_ratio': 0,
            'dividend_yield': 0,
            'book_value': 0,
            'eps': 0,
            'revenue': 0,
            'profit_margin': 0,
            'debt_to_equity': 0,
            'roe': 0,
            'roa': 0,
            'current_ratio': 0,
            'quick_ratio': 0,
            'price_to_book': 0,
            'price_to_sales': 0,
            'beta': 0,
            '52_week_high': 0,
            '52_week_low': 0,
            'volume': 0,
            'avg_volume': 0
        }
        
        # Try Financial Modeling Prep first
        quote_data = self.fetch_from_fmp(f"quote/{symbol}")
        if quote_data and len(quote_data) > 0:
            stock_data = quote_data[0]
            fundamentals.update({
                'price': stock_data.get('price', 0),
                'change': stock_data.get('change', 0),
                'change_percent': stock_data.get('changesPercentage', 0),
                'market_cap': stock_data.get('marketCap', 0),
                'pe_ratio': stock_data.get('pe', 0),
                'eps': stock_data.get('eps', 0),
                'beta': stock_data.get('beta', 0),
                'volume': stock_data.get('volume', 0),
                'avg_volume': stock_data.get('avgVolume', 0),
                '52_week_high': stock_data.get('yearHigh', 0),
                '52_week_low': stock_data.get('yearLow', 0)
            })
        
        # Get additional metrics from key metrics endpoint
        metrics_data = self.fetch_from_fmp(f"key-metrics-ttm/{symbol}")
        if metrics_data and len(metrics_data) > 0:
            metrics = metrics_data[0]
            fundamentals.update({
                'price_to_book': metrics.get('pbRatioTTM', 0),
                'price_to_sales': metrics.get('psRatioTTM', 0),
                'dividend_yield': metrics.get('dividendYieldTTM', 0) * 100 if metrics.get('dividendYieldTTM') else 0,
                'roe': metrics.get('roeTTM', 0) * 100 if metrics.get('roeTTM') else 0,
                'roa': metrics.get('roaTTM', 0) * 100 if metrics.get('roaTTM') else 0,
                'debt_to_equity': metrics.get('debtToEquityTTM', 0),
                'current_ratio': metrics.get('currentRatioTTM', 0)
            })
        
        # Get financial ratios
        ratios_data = self.fetch_from_fmp(f"ratios-ttm/{symbol}")
        if ratios_data and len(ratios_data) > 0:
            ratios = ratios_data[0]
            if not fundamentals['current_ratio']:
                fundamentals['current_ratio'] = ratios.get('currentRatio', 0)
            fundamentals['quick_ratio'] = ratios.get('quickRatio', 0)
            if not fundamentals['profit_margin']:
                fundamentals['profit_margin'] = ratios.get('netProfitMargin', 0) * 100 if ratios.get('netProfitMargin') else 0
        
        # Get income statement for revenue
        income_data = self.fetch_from_fmp(f"income-statement/{symbol}", {'limit': '1'})
        if income_data and len(income_data) > 0:
            income = income_data[0]
            fundamentals['revenue'] = income.get('revenue', 0)
            if not fundamentals['profit_margin']:
                net_income = income.get('netIncome', 0)
                revenue = income.get('revenue', 1)
                fundamentals['profit_margin'] = (net_income / revenue * 100) if revenue else 0
        
        # Fallback to yfinance if FMP data is incomplete
        if fundamentals['price'] == 0:
            try:
                ticker = yf.Ticker(symbol)
                info = ticker.info
                hist = ticker.history(period="1d")
                
                if not hist.empty:
                    current_price = hist['Close'][-1]
                    prev_close = info.get('previousClose', current_price)
                    
                    fundamentals.update({
                        'price': current_price,
                        'change': current_price - prev_close,
                        'change_percent': ((current_price - prev_close) / prev_close * 100) if prev_close else 0,
                        'market_cap': info.get('marketCap', 0),
                        'pe_ratio': info.get('trailingPE', 0),
                        'dividend_yield': info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 0,
                        'book_value': info.get('bookValue', 0),
                        'eps': info.get('trailingEps', 0),
                        'beta': info.get('beta', 0),
                        '52_week_high': info.get('fiftyTwoWeekHigh', 0),
                        '52_week_low': info.get('fiftyTwoWeekLow', 0),
                        'volume': hist['Volume'][-1] if not hist.empty else 0,
                        'profit_margin': info.get('profitMargins', 0) * 100 if info.get('profitMargins') else 0,
                        'roe': info.get('returnOnEquity', 0) * 100 if info.get('returnOnEquity') else 0,
                        'debt_to_equity': info.get('debtToEquity', 0),
                        'current_ratio': info.get('currentRatio', 0),
                        'quick_ratio': info.get('quickRatio', 0),
                        'price_to_book': info.get('priceToBook', 0)
                    })
                    
            except Exception as e:
                print(f"yfinance error for {symbol}: {e}")
        
        # Round numerical values and ensure JSON serializable
        for key, value in fundamentals.items():
            if isinstance(value, (int, float)) and key != 'last_updated':
                fundamentals[key] = float(round(value, 2))  # Convert to Python float
        
        return fundamentals
    
    def get_market_summary(self) -> Dict[str, Any]:
        """Get overall market summary data"""
        market_data = {
            'last_updated': datetime.now().isoformat(),
            'indices': {},
            'market_status': 'closed',
            'fear_greed_index': 50,
            'volatility_index': 0
        }
        
        # Get major indices
        indices = {
            '^GSPC': 'S&P 500',
            '^DJI': 'Dow Jones',
            '^IXIC': 'Nasdaq',
            '^RUT': 'Russell 2000',
            '^VIX': 'VIX'
        }
        
        for symbol, name in indices.items():
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="2d")
                info = ticker.info
                
                if not hist.empty:
                    current_price = hist['Close'][-1]
                    prev_close = hist['Close'][-2] if len(hist) > 1 else current_price
                    
                    market_data['indices'][symbol] = {
                        'name': name,
                        'price': float(round(current_price, 2)),
                        'change': float(round(current_price - prev_close, 2)),
                        'change_percent': float(round(((current_price - prev_close) / prev_close * 100), 2)) if prev_close else 0.0
                    }
                    
                    if symbol == '^VIX':
                        market_data['volatility_index'] = float(round(current_price, 2))
                        
            except Exception as e:
                print(f"Error fetching {name}: {e}")
        
        return market_data
    
    def update_all_data(self):
        """Update all portfolio and market data"""
        print(f"Starting portfolio update at {datetime.now()}")
        
        # Update individual stock fundamentals
        portfolio_data = {}
        
        for symbol in self.holdings:
            print(f"Updating {symbol}...")
            try:
                fundamentals = self.get_stock_fundamentals(symbol)
                portfolio_data[symbol] = fundamentals
                time.sleep(1)  # Rate limiting
            except Exception as e:
                print(f"Error updating {symbol}: {e}")
                continue
        
        # Save portfolio data
        portfolio_file = os.path.join(self.data_dir, 'portfolio_fundamentals.json')
        with open(portfolio_file, 'w') as f:
            json.dump(portfolio_data, f, indent=2)
        
        print(f"Saved portfolio data to {portfolio_file}")
        
        # Update market summary
        print("Updating market summary...")
        market_data = self.get_market_summary()
        
        market_file = os.path.join(self.data_dir, 'market_summary.json')
        with open(market_file, 'w') as f:
            json.dump(market_data, f, indent=2)
        
        print(f"Saved market data to {market_file}")
        
        # Create a consolidated update timestamp
        timestamp_data = {
            'last_update': datetime.now().isoformat(),
            'market_close_date': datetime.now().strftime('%Y-%m-%d'),
            'total_holdings': len(self.holdings),
            'successful_updates': len(portfolio_data)
        }
        
        timestamp_file = os.path.join(self.data_dir, 'last_update.json')
        with open(timestamp_file, 'w') as f:
            json.dump(timestamp_data, f, indent=2)
        
        print(f"Portfolio update completed successfully!")
        print(f"Updated {len(portfolio_data)} out of {len(self.holdings)} holdings")
        
if __name__ == "__main__":
    updater = PortfolioUpdater()
    updater.update_all_data()

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
raw_path = ROOT / 'data' / 'btc-usd-max.csv'
out_path = ROOT / 'data' / 'bitcoin_market_clean.csv'

if not raw_path.exists():
    raise FileNotFoundError(f'Missing file: {raw_path}')

df = pd.read_csv(raw_path)
expected = {'snapped_at', 'price', 'market_cap', 'total_volume'}
missing = expected - set(df.columns)
if missing:
    raise ValueError(f'Missing columns: {missing}')

df['snapped_at'] = pd.to_datetime(df['snapped_at'], utc=True)
df['date'] = df['snapped_at'].dt.date

df = df[['date', 'price', 'market_cap', 'total_volume']].groupby('date', as_index=False).mean()
df['daily_return'] = df['price'].pct_change()
df['log_return'] = pd.Series(df['price']).pipe(lambda s: (s / s.shift(1)).apply(lambda x: None if pd.isna(x) else __import__('math').log(x) if x>0 else None))
df['volatility_7d'] = df['daily_return'].rolling(7).std()
df['ma_7'] = df['price'].rolling(7).mean()
df['ma_30'] = df['price'].rolling(30).mean()
df['volume_change'] = df['total_volume'].pct_change()

df.to_csv(out_path, index=False)
print(f'Saved to {out_path}')
print(df.head())
print(df.tail())

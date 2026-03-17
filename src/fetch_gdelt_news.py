from __future__ import annotations
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
out_path = OUTPUT_DIR / "gdelt_bitcoin_daily.csv"

START = datetime(2020, 1, 1)
END = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
QUERY = "bitcoin OR BTC"

rows = []
current = START
while current < END:
    nxt = current + timedelta(days=1)
    url = (
        "https://api.gdeltproject.org/api/v2/doc/doc?"
        f"query={QUERY}&mode=ArtList&maxrecords=250&format=json&"
        f"startdatetime={current.strftime('%Y%m%d%H%M%S')}&"
        f"enddatetime={nxt.strftime('%Y%m%d%H%M%S')}"
    )
    try:
        r = requests.get(url, timeout=30)
        if r.ok:
            data = r.json()
            articles = data.get("articles", []) if isinstance(data, dict) else []
            rows.append({"date": current.date().isoformat(), "news_count": len(articles)})
        else:
            rows.append({"date": current.date().isoformat(), "news_count": None})
    except Exception:
        rows.append({"date": current.date().isoformat(), "news_count": None})
    current = nxt

df = pd.DataFrame(rows)
df.to_csv(out_path, index=False)
print(f"Saved {len(df)} rows to {out_path}")

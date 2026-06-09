# social-monitor-examples

Tiny, copy-paste WebSocket consumers for real-time social + news monitoring,
one folder per platform. Each connects, filters to its platform, prints events
as they arrive. Python, ~30 lines each.

- [`x/`](x) — X (Twitter): tweets, replies, quotes, retweets, profile changes
- [`instagram/`](instagram) — Instagram: posts, stories, reels, carousels
- [`truthsocial/`](truthsocial) — Truth Social: truths, retruths, quote chains
- [`youtube/`](youtube) — YouTube: uploads, Shorts, deletions
- [`binance-square/`](binance-square) — Binance Square: posts with coin pairs
- [`news/`](news) — News: breaking articles with categories + keywords

These run against the [1322](https://1322.io) real-time feeds (managed
WebSocket + REST, ~150-250ms detection, Discord/Telegram/webhook delivery). The
consumer pattern is generic though — swap the URL and the `platform` filter for
any websocket source.

Docs / event schemas: https://1322.io/docs — platforms: https://1322.io/platforms

## usage

Every folder is the same shape:

```bash
cd x   # or instagram, truthsocial, youtube, binance-square, news
pip install websockets
API_KEY=your-key WS_URL=wss://1322.io/your-ws-path python main.py
```

## why websocket and not polling

Polling caps worst-case latency at the poll interval — too slow for trading,
alerting, news. A websocket pushes the event the moment it's detected. More:
https://1322.io/blog/twitter-streaming-api-alternatives

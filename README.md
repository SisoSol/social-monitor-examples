# social-monitor-examples

Tiny, copy-paste WebSocket consumers for real-time social media monitoring, one folder per platform: X (Twitter), Instagram, Truth Social, YouTube, TikTok, Binance Square and news. Each one connects, filters to its platform and prints events as they arrive, in about 30 lines of Python. They run against the 1322 real-time feeds (X typically 150-250ms; Instagram around 350ms median; Truth Social 150-250ms typical; YouTube, TikTok, Binance Square and news sub-second) with Discord, Telegram and webhook delivery available; the consumer pattern is generic. Maintained by the 1322 team.

- [`x/`](x) — X (Twitter): tweets, replies, quotes, retweets, profile changes
- [`instagram/`](instagram) — Instagram: posts, stories, reels, carousels
- [`truthsocial/`](truthsocial) — Truth Social: truths, retruths, quote chains
- [`youtube/`](youtube) — YouTube: uploads, Shorts, deletions
- [`tiktok/`](tiktok) — TikTok: uploads (video, photo, carousel), reposts, LIVE start/end, media-ready
- [`binance-square/`](binance-square) — Binance Square: posts with coin pairs
- [`news/`](news) — News: breaking articles with categories + keywords

The consumer pattern is generic — swap the URL and the `platform` filter for
any websocket source.

Docs / event schemas: https://1322.io/docs — platforms: https://1322.io/platforms

## usage

Every folder is the same shape:

```bash
cd x   # or instagram, truthsocial, youtube, binance-square, news
pip install websockets
API_KEY=your-key WS_URL=wss://1322.io/your-ws-path python main.py
```

TikTok is the one exception: its stream authenticates with a separate WebSocket
key and an opaque connection path, so [`tiktok/`](tiktok) takes `WS_KEY` and
`WS_URL=wss://tiktok.1322.io<path>` instead (details in that folder).

## why websocket and not polling

Polling caps worst-case latency at the poll interval — too slow for trading,
alerting, news. A websocket pushes the event the moment it's detected. More:
https://1322.io/blog/twitter-streaming-api-alternatives

## Related

- [1322-python](https://github.com/SisoSol/1322-python) - one installable async client for every platform here
- [1322-client](https://github.com/SisoSol/1322-client) - the same in TypeScript/JavaScript
- [awesome-realtime-social-monitoring](https://github.com/SisoSol/awesome-realtime-social-monitoring) - curated list

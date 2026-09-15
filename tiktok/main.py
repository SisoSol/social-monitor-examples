import asyncio
import json
import os

import websockets

WS_KEY = os.environ.get("WS_KEY")  # the WebSocket key, not the REST API key
WS_URL = os.environ.get("WS_URL")  # wss://tiktok.1322.io + path from GET /v1/ws/status


async def run():
    if not WS_KEY or not WS_URL:
        raise SystemExit("set WS_KEY and WS_URL")
    while True:
        try:
            async with websockets.connect(WS_URL, additional_headers={"X-WS-Key": WS_KEY}) as ws:
                print("connected: tiktok feed")
                async for raw in ws:
                    try:
                        e = json.loads(raw)
                    except ValueError:
                        continue
                    if e.get("platform") != "tiktok":
                        continue
                    t = e.get("type")
                    obj = e.get("object") or {}
                    user = (e.get("account") or {}).get("username")
                    ts = e.get("observed_at")
                    if t == "tiktok.upload.created":
                        print(f"[{ts}] {obj.get('kind', 'video')} @{user}: {obj.get('url')} {obj.get('description', '')}")
                    elif t == "tiktok.repost.created":
                        orig = (obj.get("original_author") or {}).get("username")  # object, not a string
                        print(f"[{ts}] repost @{user} of @{orig}: {obj.get('url')}")
                    elif t in ("tiktok.live.started", "tiktok.live.ended"):
                        print(f"[{ts}] {t.rsplit('.', 1)[1]} LIVE @{user} room {obj.get('room_id')}")
                    elif t == "tiktok.media.ready":
                        # schema 1322.tiktok.media.v1: same event_id as the upload it belongs to
                        print(f"[{ts}] media ready {obj.get('video_id')}: {obj.get('media_url')}")
        except Exception as exc:
            print(f"disconnected ({exc}); retry 1s")
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(run())

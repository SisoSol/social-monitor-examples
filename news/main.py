import asyncio
import json
import os

import websockets

API_KEY = os.environ.get("API_KEY")
WS_URL = os.environ.get("WS_URL")


async def run():
    if not API_KEY or not WS_URL:
        raise SystemExit("set API_KEY and WS_URL")
    while True:
        try:
            async with websockets.connect(WS_URL, additional_headers={"X-Api-Key": API_KEY}) as ws:
                print("connected: news feed")
                async for raw in ws:
                    try:
                        e = json.loads(raw)
                    except ValueError:
                        continue
                    if e.get("platform") != "news":
                        continue
                    cats = ",".join(e.get("categories") or [])
                    print(f"[{e.get('timestamp')}] [{cats}] {e.get('title', '')}")
        except Exception as exc:
            print(f"disconnected ({exc}); retry 1s")
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(run())

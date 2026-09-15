requires: pip install websockets

run:
  WS_KEY=your-ws-key WS_URL=wss://tiktok.1322.io/ws/your-path python main.py

TikTok differs from the other folders (see the TikTok section of https://1322.io/docs):

- the stream authenticates with a separate WebSocket key sent as the `X-WS-Key`
  header (or `Authorization: Bearer <ws_key>`), not the REST API key; there is
  no `?key=` query parameter.
- the connection path is opaque: read it from `GET /v1/ws/status` (`path`) or
  `GET /v1/dashboard` (`websocket.path`) with your REST key, then connect to
  `wss://tiktok.1322.io<path>`.

Frames branch on `type`. Content events use schema `1322.tiktok.event.v1`:
`tiktok.upload.created` (object.kind is video | photo | carousel),
`tiktok.repost.created` (object.original_author is an object, not a username
string), `tiktok.live.started` and `tiktok.live.ended` (same room_id for one
session). `tiktok.media.ready` uses the smaller schema `1322.tiktok.media.v1`
and repeats an already-announced event_id once the file is fetchable at
object.media_url; it is not a second post. `occurred_at` is null on reposts and
LIVE frames, so sort on `observed_at`. Delivery is live-only (no replay);
dedupe by event_id across reconnects.

see the top-level README. docs: https://1322.io/docs

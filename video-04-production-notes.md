# Video 04 — What Did Ancient Humans Do After Dark?

**Status:** draft v1 cut, awaiting review. Not published.

## Deliverables

| Asset | Link |
|---|---|
| Draft v1 (5:43.76) | [`video-04-draft-v1.mp4`](https://drive.google.com/file/d/1CML8F7EKFtVd4hDZCDflnWwYH5LL_4TU/view) |
| Narration | [`video-04-narration.mp3`](https://drive.google.com/file/d/1-U4eUxTASe0JuzOWi1wEQrmNKLz3aZyo/view) |
| Captions (131 cues) | [`video-04-captions.srt`](https://drive.google.com/file/d/1HGybAEf_WZe8BfTP5gErecNtyn8ix3cd/view) |
| Script | [`video-04-script-draft.md`](https://github.com/ebhmohammed-max/Agent-Reach/blob/arena/6ac64deb-agent-reach/video-04-script-draft.md) |

## How it was built

- Script in the Video 03 voice: modern hook, direct address, named characters, no disclaimers, no lecture.
- Narration split into 6 blocks and voiced with `voice-02` (still never chosen by the user). Measured block durations: 56.97 / 53.52 / 69.16 / 65.48 / 60.08 / 38.55 s.
- 20 drawings, `n01`–`n20` in `google_drive/video04-work/`, all generated against real approved reference frames.
- `build-v04.py` assigns shots per block and divides the measured block duration by the shot count, so picture and voice cannot drift. 35 shots.
- Captions anchored per block with the same method as Video 03 v4.

## Style

`video-style-guide.md` at repo root is the authority. Written after two rejected art passes that produced blank disc heads with dot eyes and cold grey palettes. Every frame here uses the approved language: big oval eyes with pupils, thick acting eyebrows, varied mouths, warm ink lines, saturated amber-and-indigo night.

Superseded art from the rejected passes is parked in `.rejected-art/` and must not be used.

## Open items

- Nobody has listened to any narration in this project. The voice is still unchosen.
- Captions are block-anchored, not word-synced.
- Vertical short and thumbnail not made for this one yet.

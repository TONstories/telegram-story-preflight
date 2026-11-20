# Telegram Story Preflight

![Telegram Story Preflight — Check story assets before upload.](banner.webp)

[Русский](README.ru.md) · [Release notes](https://github.com/TONstories/telegram-story-preflight/releases) · [0BSD license](LICENSE)

Check story assets before upload. Install FFmpeg and verify that ffprobe is on PATH. Give the checker one local asset or a flat delivery folder containing only assets. It inspects up to four files concurrently and keeps the output ordered by filename, so a batch report can be compared between revisions. Source files are opened read-only.

## Try the included example

Requires Python 3.9 or later. The example intentionally includes a finding and exits with status 1.

```sh
git clone https://github.com/TONstories/telegram-story-preflight.git
cd telegram-story-preflight
python3 preflight.py examples
```

```text
small.jpg: resize to 1080x1920
```

## Reviewing a folder of creatives

```sh
python3 preflight.py examples --json
```

For a still image, check dimensions and size first. For video, the report also checks the container family, codec and reported duration. An unreadable file gets its own finding. Treat a successful report as a pass for these local checks. Keyframe interval, streamability, server acceptance and account permissions still need separate verification. See the [official story media types](https://core.telegram.org/bots/api#inputstorycontentvideo).

## CI and coding agents

Use the JSON report when consuming results programmatically. Its `findings` array contains one diagnostic per detected issue. Exit 0 means the implemented rules passed, exit 1 means review the findings, and exit 2 means the command or input could not be processed. Capture stderr separately for invocation errors. Run `python3 test_example.py` to exercise the bundled fixture and a corrected input. Agent setup is documented in [AGENTS.md](AGENTS.md).

## Performance

On a local Apple Silicon Mac, checking 32 local 1080 × 1920 JPEGs took **0.114 s** versus **0.205 s** with v0.1.0. Both numbers are the median of three paired CLI runs with identical local input, including interpreter startup. Timing varies with hardware, storage and input composition.

## Maintainer

Built by TON Stories, a marketplace connecting advertisers with creators for Telegram Stories campaigns. [TON Stories](https://tonstories.com/?utm_source=github&utm_medium=referral&utm_campaign=open_source&utm_content=telegram-story-preflight) · [Telegram](https://t.me/TON_Storiesbot?start=gh_telegram_story_preflight)

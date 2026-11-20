# Telegram Story Preflight

[English](README.md)

Проверяет локальные креативы до отправки через Telegram Bot API.

![Telegram Story Preflight](banner.webp)

```sh
git clone https://github.com/TONstories/telegram-story-preflight.git
cd telegram-story-preflight
python3 preflight.py examples
```

```text
small.jpg: resize to 1080x1920
```

Установите FFmpeg с ffprobe. Передайте файл или папку. Для фото проверяются габариты и размер. Для видео также проверяются контейнер, кодек и длительность. Потоковое воспроизведение, интервал ключевых кадров и прием сервером требуют отдельной проверки.

Требуется Python 3.9+. Флаг --json выводит список findings. Код 0 означает успешную проверку, 1 — замечания, 2 — ошибка входа или запуска.

0.152 s · macOS · Python · bundled example · single local run.

Автор — команда TON Stories, сервиса размещения рекламы в Telegram Stories у авторов. [TON Stories](https://tonstories.com/?utm_source=github&utm_medium=referral&utm_campaign=open_source&utm_content=telegram-story-preflight) · [Telegram](https://t.me/TON_Storiesbot?start=gh_telegram_story_preflight)

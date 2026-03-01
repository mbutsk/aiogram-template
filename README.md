# Aiogram Template by mbutsk

> [!NOTE]
> This template isn't examplary.
> I made it for myself because it's comfortable for me.
> If it's comfortable for you too, feel free to use it.

This template was inspired by [FajoX1/tgbotbase-aiogram3](https://github.com/FajoX1/tgbotbase-aiogram3)

## Base Setup

### Required Libraries

- `aiogram`
- `python-dotenv`

Install them using pip:

```bash
pip install -r requirements.txt
```

### Bot Token

Rename `.env.example` to `.env` and fill in your bot token into `BOT_TOKEN` variable.

## Create Handlers

To create a new handler, make a directory with the handler name
in `handlers` directory, add `handler.py` and `__init__.py` files there.
There are examplary `echo` handler built-in.

Then connect your handler to the bot by importing it in `handlers/__init__.py`
as I imported `EchoHandler`.

## Useful Things

### Scratch

There is file `scratch-maker.sh`. It creates `scratch` directory and add it to `.git/info/exclude`.
I use it to test some functions in command line before adding them to the bot.

```bash
chmod +x scratch-maker.sh
sh scratch-maker.sh
```

You can delete it if you don't need it.
You can also delete it after you're done

### `ruff.toml`

My ruff config. If you don't use ruff, you can delete it.

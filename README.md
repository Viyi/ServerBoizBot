# ServerBoizBot

Anything* goes bot for a homelab discord server

## Contribution Guidelines

1. Don't be malicious
2. No NSFW

## Running
1. ```ghcr.io/viyi/serverboizbot:latest```
2. include DISCORD_TOKEN in the environment

## Building an Extension

> We are using UV for package managment https://docs.astral.sh/uv/getting-started/installation/

main.py searches for any python files in the bot/extensions directory. 

Any file located there needs a setup function.

See the bot/extensions/example.py for... an example.

The core directory is for all the non discord-py functionality. 

### Quickstart

A jinja template + python script has been provided to quickly create an extension.

```uv run tools/create-extension.py```


## Thoughts

I realize I have already planned this out more than desired, but really do whatever you want. Please contribute something awesome!




#  README

## Developing 

I develop locally on linux, fish, python3, pip, virtualenv, tmux, and alacritty (terminal). The following instructions rely on that, but they may work for you if you have a similar linux environment.

To run the development environment:

```
cd davidthewatson.github.io
python -m virtualenv .venv
source .venv/bin/activate.fish
pip install -r requirements.txt
tmux
cd docs
python -m http.server
build_local.sh
```

## Deploying

I deploy on github pages.

TBD
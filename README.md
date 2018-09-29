# first-half-goal-api

## Overview
The back end for first-half-goal

## Prerequisits
- Install pyenv `brew install pyenv`
- Add `eval "$(pyenv init -)"` to the bottom of your `~/.bash_profile`
- Install python version for pyenv `pyenv install 3.6.6`
- Set local python `pyenv local 3.6.6`
- Add python path to bash profile `source ~/.bash_profile`
- Create virtual environment `python -m venv venv`

## Common
- Install dependencies `yarn`
- Activate virtual environment `source ./venv/bin/activate`
- Update Python requirements `pip install -r requirements.dev.txt`
- Run `yarn dev`

## Development
- To check linting `yarn lint`
- To run tests `yarn test`

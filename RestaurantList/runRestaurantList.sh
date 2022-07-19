#!/bin/sh

pkill -f server.py
python3 server.py P >> ./log/prod/$(date '+%Y-%m-%d').log
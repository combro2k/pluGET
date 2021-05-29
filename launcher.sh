#!/usr/bin/env sh
SELF=$(readlink -f "$0")
cd "$(dirname "$SELF")/" || exit 1
/usr/bin/env python3 "src/__init__.py" || exit 1
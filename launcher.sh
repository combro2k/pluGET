#!/usr/bin/env sh
SELF=$(readlink -f "$0")
cd "$(dirname "$SELF")/src/" || exit 1
/usr/bin/env python3 "__init__.py" || exit 1
"""Some extra sanity checks for the CI."""

import sys
from pathlib import Path

NEWS = Path(__file__).parent / "content" / "news"

for root, dirs, files in NEWS.walk():
    for name in files:
        f = root / name
        m = re.search(r"^Tags: (?P<tags>.*)$", f.read_text())
        if m and f.parent.name not in m.group("tags"):
            print(f"Tag from path must be repeated in Tags metadata: {f}")
            sys.exit(1)
            

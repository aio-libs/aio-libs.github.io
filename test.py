"""Some extra sanity checks for the CI."""

import sys
import re
from pathlib import Path

NEWS = Path(__file__).parent / "content" / "news"

for root, dirs, files in NEWS.walk():
    for name in files:
        f = root / name
        m = re.search(r"^Tags: (?P<tags>.*)$", f.read_text(), re.MULTILINE)
        # Tags header overrides the path tag, so enforce that the path tag is
        # included in the header for consistency.
        if m and f.parent.name not in m.group("tags"):
            print(f"Tag from path must be repeated in Tags metadata: {f}")
            sys.exit(1)
            

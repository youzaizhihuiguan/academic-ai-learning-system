import importlib
import sys
import tempfile
from pathlib import Path


module = importlib.import_module(sys.argv[1])
with tempfile.TemporaryDirectory() as tmp:
    first = Path(tmp) / "first.csv"
    second = Path(tmp) / "second.csv"
    first.write_text("score\n80\n100\n", encoding="utf-8")
    second.write_text("score\n0\n20\n", encoding="utf-8")
    got_first = module.average_score(first)
    got_second = module.average_score(second)
    print("first:", got_first, "second:", got_second)
    assert got_first == (2, 90.0)
    assert got_second == (2, 10.0), "the second file must not inherit the first file's scores"

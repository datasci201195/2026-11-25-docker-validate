import webbrowser
from pathlib import Path
from tempfile import TemporaryDirectory

import pointblank as pb
from palmerpenguins import load_penguins

penguins = load_penguins()
missing_values = pb.missing_vals_tbl(data=penguins)

try:
    viewer = webbrowser.get("positron_viewer")
except webbrowser.Error:
    pass  # The Viewer is available in the Positron Console.
else:
    # Keep the HTML file alive while the Viewer reads it.
    preview_dir = TemporaryDirectory()
    preview_path = Path(preview_dir.name) / "penguins-missing-values.html"
    preview_path.write_text(missing_values.as_raw_html(make_page=True), encoding="utf-8")
    viewer.open(preview_path.as_uri())

print(penguins.isna().sum())

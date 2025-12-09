# Documentation

This folder contains the Sphinx documentation source for `electroMICA`.

## Building the Documentation

### Prerequisites

Ensure Sphinx and related packages are installed:

```bash
pip install sphinx sphinx-rtd-theme sphinx-autodoc-typehints
```

Or install from the root `requirements.txt`:

```bash
pip install -r ../requirements.txt
```

### Building HTML

From this directory, run:

```bash
sphinx-build -b html . _build/html
```

Or, on Unix/Linux/macOS with `make`:

```bash
make html
```

The built HTML documentation will be in `_build/html/index.html`.

### Opening the Documentation

After building, open the documentation in your browser:

**On Windows (PowerShell)**:
```powershell
start _build/html/index.html
```

**On Linux/macOS**:
```bash
open _build/html/index.html
# or
xdg-open _build/html/index.html
```

## Documentation Structure

- **index.rst** — Main documentation home page
- **installation.rst** — Installation instructions and troubleshooting
- **usage.rst** — Usage guide with examples (iEEG and scalp EEG)
- **api.rst** — API reference with function documentation
- **algorithm.rst** — Detailed algorithm and mathematical background
- **faq.rst** — Frequently asked questions
- **contributing.rst** — Contribution guidelines

## Configuration

The Sphinx configuration is in `conf.py`. Key settings:

- **Theme**: `sphinx_rtd_theme` (Read the Docs theme)
- **Extensions**: autodoc, autosummary, intersphinx, viewcode
- **Python path**: Includes parent directory for autodoc to import `electroMICA`

## Cleaning Build Artifacts

To clean the build directory:

```bash
rm -r _build
# or on Windows
Remove-Item -Recurse -Force _build
```

## Building Other Formats

You can build other formats using Sphinx:

- **LaTeX/PDF**: `make latexpdf` (requires LaTeX installation)
- **Manual pages**: `make man`
- **Texinfo**: `make texinfo`

## Notes

- Autodoc requires the `ants` module to be installed for full API documentation. If it's missing, you'll see warnings but the build will still succeed.
- The documentation uses reStructuredText (`.rst`) format. See [Sphinx documentation](https://www.sphinx-doc.org/) for markup syntax.
- For contribution guidelines, see `contributing.rst` or the root `CONTRIBUTING.rst`.

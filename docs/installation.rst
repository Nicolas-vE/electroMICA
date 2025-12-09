.. _installation:

Installation
============

Requirements
------------

`electroMICA` requires Python 3.7+ and the following packages:

- **Core**: ``numpy``, ``scipy``, ``pandas``, ``nibabel``
- **Neuroimaging**: ``antspyx`` (ANTsPy, may require system dependencies)
- **Optional**: ``vtk``, ``pyvirtualdisplay`` (for visualization on headless systems)
- **Documentation**: ``sphinx``, ``sphinx-rtd-theme`` (only for building docs)

Prerequisites
-------------

Before using `electroMICA`, you must run `micapipe <https://micapipe.readthedocs.io>`_ on your 
structural MRI data. `electroMICA` depends on `micapipe` derivatives (T1w images, cortical surfaces, transforms).

Optionally, you can also run `hippunfold <https://hippunfold.readthedocs.io>`_ to include hippocampal surfaces.

Installation Steps
------------------

1. **Clone or download the repository** (if not already done):

   .. code-block:: bash

      git clone https://github.com/MICA-MNI/electroMICA.git
      cd electroMICA

2. **Create a virtual environment** (recommended):

   .. code-block:: bash

      python -m venv .venv

3. **Activate the virtual environment**:

   On Linux/macOS:

   .. code-block:: bash

      source .venv/bin/activate

   On Windows (PowerShell):

   .. code-block:: powershell

      .\.venv\Scripts\Activate.ps1

4. **Install dependencies** from ``requirements.txt``:

   .. code-block:: bash

      pip install --upgrade pip
      pip install -r requirements.txt

   This installs all core and optional dependencies for running `electroMICA`.

5. **Verify installation**:

   .. code-block:: bash

      python -c "import electroMICA; print('electroMICA imported successfully')"

   Or run a test script:

   .. code-block:: bash

      python example_electroMICA_iEEG.py

Troubleshooting
---------------

**ANTsPy installation issues**
   ``antspyx`` (imported as ``ants`` in the code) may require additional system-level dependencies.
   On Ubuntu/Debian: ``sudo apt-get install libltdl-dev``
   On macOS: Installation via conda may work better: ``conda install -c conda-forge antspyx``

**Sphinx documentation build fails**
   Ensure ``sphinx`` and ``sphinx-rtd-theme`` are installed. If issues persist:

   .. code-block:: bash

      pip install --upgrade sphinx sphinx-rtd-theme

**MRI/surface loading errors**
   Ensure your BIDS/`micapipe` derivatives are in the correct format. Check:
   - T1w image exists at ``<derivatives>/sub-XX/anat/``
   - Surface files at ``<derivatives>/sub-XX/surf/``

Development Installation
-------------------------

If you plan to contribute to `electroMICA`:

.. code-block:: bash

   git clone https://github.com/MICA-MNI/electroMICA.git
   cd electroMICA
   python -m venv .venv
   source .venv/bin/activate  # or .\.venv\Scripts\Activate.ps1 on Windows
   pip install -r requirements.txt

See :ref:`contributing` for contribution guidelines.

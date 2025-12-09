.. _usage:

Usage
=====

Overview
--------

`electroMICA` provides two main functions to project electrophysiological features onto cortical and hippocampal surfaces:

- :func:`electroMICA_iEEG` — Project **intracranial EEG** (iEEG / stereo-EEG) features to surfaces.
- :func:`electroMICA_ScalpEEG` — Project **scalp EEG** features to surfaces.

Both functions accept standardized parameters and work with BIDS-formatted datasets.

Basic Workflow
--------------

1. **Prepare your BIDS dataset** with:
   
   - Raw EEG/iEEG data in BIDS format
   - `micapipe` derivatives (T1w, surfaces, transforms)
   
2. **Create feature files** (TSV format) containing the electrophysiological metrics you want to project.

3. **Call the appropriate `electroMICA` function** with paths to your data.

4. **Retrieve projected features** from the ``maps/`` folder in the `electroMICA` derivatives.

Intracranial EEG (iEEG)
-----------------------

The :func:`electroMICA_iEEG` function projects depth electrode features onto cortical surfaces.

Basic usage:

.. code-block:: python

   from electroMICA import electroMICA_iEEG
   
   # Paths
   output_folder = "/path/to/derivatives/electroMICA/sub-PX050/ses-01"
   feature_file = "/path/to/features/sub-PX050_ses-01_Interictal.tsv"
   electrodes_folder = "/path/to/BIDS_iEEG/iEEG/"
   micapipe_derivatives = "/path/to/derivatives/micapipe"
   
   # Project iEEG features to surfaces
   electroMICA_iEEG(
       output_folder=output_folder,
       feature=feature_file,
       electrodes=electrodes_folder,
       micapipe_derivatives=micapipe_derivatives
   )

With optional hippocampal surfaces:

.. code-block:: python

   electroMICA_iEEG(
       output_folder=output_folder,
       feature=feature_file,
       electrodes=electrodes_folder,
       micapipe_derivatives=micapipe_derivatives,
       hippunfold_derivatives="/path/to/hippunfold/derivatives"
   )

Parameters
~~~~~~~~~~

**output_folder** (str)
   Path to the `electroMICA` derivatives folder where results are stored. 
   Can be ``sub-XX`` or ``sub-XX/ses-YY``.

**feature** (str)
   Path to a feature TSV file, or a feature label. If a label is provided (e.g., ``Interictal``),
   the function searches for a matching file in the ``feat/`` folder.

**electrodes** (str, optional)
   Path to the BIDS iEEG folder, or directly to an ``electrodes.tsv`` file.
   If omitted, existing sensitivity profiles are used without recomputation.

**micapipe_derivatives** (str, optional)
   Path to the `micapipe` derivatives. Required if ``electrodes`` is provided (to copy surfaces and transforms).

**hippunfold_derivatives** (str, optional)
   Path to `hippunfold` derivatives. If provided, hippocampal surfaces are included in the projection.

Scalp EEG
---------

The :func:`electroMICA_ScalpEEG` function projects scalp electrode features onto cortical surfaces.

Basic usage:

.. code-block:: python

   from electroMICA import electroMICA_ScalpEEG
   
   # Paths
   output_folder = "/path/to/derivatives/electroMICA/sub-PX050/ses-01"
   feature_file = "/path/to/features/sub-PX050_ses-01_AvgSpike.tsv"
   electrodes_folder = "/path/to/BIDS_EEG/EEG/"
   micapipe_derivatives = "/path/to/derivatives/micapipe"
   
   # Project scalp EEG features to surfaces
   electroMICA_ScalpEEG(
       output_folder=output_folder,
       feature=feature_file,
       electrodes=electrodes_folder,
       micapipe_derivatives=micapipe_derivatives
   )

With optional hippocampal surfaces:

.. code-block:: python

   electroMICA_ScalpEEG(
       output_folder=output_folder,
       feature=feature_file,
       electrodes=electrodes_folder,
       micapipe_derivatives=micapipe_derivatives,
       hippunfold_derivatives="/path/to/hippunfold/derivatives"
   )

Parameters
~~~~~~~~~~

**output_folder** (str)
   Path to the `electroMICA` derivatives folder where results are stored.

**feature** (str)
   Path to a feature TSV file, or a feature label.

**electrodes** (str, optional)
   Path to the BIDS EEG folder, or directly to an ``electrodes.tsv`` file.
   If omitted, only the BEM head model is built without computing source estimates.

**micapipe_derivatives** (str, optional)
   Path to the `micapipe` derivatives. Required to build the BEM model and copy surfaces.

**hippunfold_derivatives** (str, optional)
   Path to `hippunfold` derivatives. If provided, hippocampal surfaces are included.

Feature File Format
-------------------

Feature files should be in TSV (tab-separated values) format with the following structure:

For iEEG:

.. code-block::

   channel_name    value   metadata
   E1              0.45    contact_1
   E2              0.52    contact_2
   ...

For scalp EEG:

.. code-block::

   electrode_label    value   unit
   Cz                 1.23    µV
   Pz                 1.15    µV
   ...

The first column should match electrode/channel names in your BIDS dataset.

Output Structure
----------------

After running `electroMICA`, the ``electroMICA`` derivatives folder is organized as:

.. code-block::

   sub-XX/ses-YY/
   ├── anat/                    # Anatomical images (T1w, brain mask)
   ├── feat/                    # Input feature files
   ├── maps/                    # Projected feature maps (main output)
   │   ├── sub-XX_ses-YY_..._surf-fsLR-32k_label-midthickness_map.gii
   │   └── ...
   ├── model/                   # Leadfield / sensitivity matrices (.mat files)
   ├── surf/                    # Surface GIFTI files (cortical, hippocampal)
   └── xfm/                     # Transform files (electrode to MRI alignment)

Viewing Results
---------------

Projected feature maps are stored as GIFTI surface files (``.gii``). You can visualize them using:

- **GIFTI viewers**: FSLView, Connectome Workbench, etc.
- **Python**: ``nibabel`` / ``plotly`` / custom scripts
- **Matlab**: GIFTI toolbox

Example visualization (Python):

.. code-block:: python

   import nibabel as nib
   import numpy as np
   
   # Load a feature map
   gii = nib.load('sub-XX_ses-YY_...map.gii')
   feature_map = gii.darrays[0].data
   
   # Inspect values
   print(f"Min: {feature_map.min()}, Max: {feature_map.max()}")
   print(f"Mean: {feature_map.mean()}")

Example Scripts
---------------

See the included example scripts for complete working examples:

- ``example_electroMICA_iEEG.py`` — Example for iEEG projection
- ``example_electroMICA_scalp.py`` — Example for scalp EEG projection

Edit these scripts with your BIDS paths and run them directly.

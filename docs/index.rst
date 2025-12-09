.. electroMICA documentation master file, created by sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

electroMICA
===========

**Project intracranial (iEEG) and scalp EEG features onto cortical and hippocampal surfaces.**

`electroMICA` is developed by `MICA Lab <https://mica-mni.github.io>`_ at McGill University for use at 
`the Neuro <https://www.mcgill.ca/neuro/>`_, McConnell Brain Imaging Center (`BIC <https://www.mcgill.ca/bic/>`_).

The main goal of `electroMICA` is to provide a robust framework to integrate electrophysiological data 
(scalp EEG, intracranial EEG, stereo-EEG) with information derived from multimodal MR images processed 
by `micapipe <https://micapipe.readthedocs.io>`_.

.. image:: ../img/workflow-iEEG.png
   :alt: electroMICA iEEG Workflow
   :width: 45%

.. image:: ../img/workflow-scalp.png
   :alt: electroMICA Scalp EEG Workflow
   :width: 45%

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   algorithm
   faq
   contributing

Highlights
----------

- **Multimodal integration**: Seamlessly integrates electrophysiology with `micapipe` structural and functional outputs.
- **BEM formulations**: Uses Boundary Element Method (BEM) to compute sensitivity profiles and leadfields.
- **Flexible surfaces**: Projects features onto cortical and (optionally) hippocampal surfaces.
- **Multiple modalities**: Supports intracranial EEG, scalp EEG, and stereo-EEG projections.
- **BIDS-compliant**: Follows Brain Imaging Data Structure (BIDS) conventions.

Quick Start
-----------

Install from ``requirements.txt``:

.. code-block:: bash

   pip install -r requirements.txt

Then edit an example script with your BIDS paths and run:

.. code-block:: bash

   python example_electroMICA_iEEG.py
   # or
   python example_electroMICA_scalp.py

See :ref:`installation` and :ref:`usage` for detailed instructions.

Key Features
------------

**iEEG Projection**
   Depth electrodes are modeled as line segments in a single-layer homogeneous conductor.
   Contact sensitivity profiles are computed via BEM with analytic element integration.
   Features are mapped to cortical/hippocampal vertices using contact sensitivity weighting.

**Scalp EEG Projection**
   A three-layer head model (scalp, skull, brain) is constructed from T1w MRI.
   Forward problem solved using BEM to compute leadfields from sources to electrodes.
   Inverse problem solved with modified eLORETA with spatial correlation weighting.
   Multiple SNR-dependent feature maps are generated.

**Hippocampal Surfaces**
   When `hippunfold <https://hippunfold.readthedocs.io>`_ outputs are available,
   hippocampal surfaces are included in the source space.

Reference
---------

If you use `electroMICA` in your research, please cite:

   (Citation details to be added)

Additionally, when using `electroMICA`, you should cite:

- `micapipe` — Cruces, R. R., et al. (2022). Micapipe: a pipeline for multimodal neuroimaging and connectome analysis. NeuroImage, 119612.

See :ref:`algorithm` for detailed algorithmic references.

License
-------

This project is licensed under the GPL v3 license. See ``LICENSE`` for details.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

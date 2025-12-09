.. _api:

API Reference
=============

Core Functions
--------------

.. automodule:: electroMICA
   :members: electroMICA_iEEG, electroMICA_ScalpEEG
   :undoc-members:
   :show-inheritance:

Main Entry Points
~~~~~~~~~~~~~~~~~

.. py:function:: electroMICA_iEEG(output_folder, feature, electrodes=None, micapipe_derivatives=None, hippunfold_derivatives=None)

   Project intracranial EEG features onto cortical and hippocampal surfaces.

   :param str output_folder: Path to electroMICA derivatives folder
   :param str feature: Path to feature TSV file or feature label
   :param str electrodes: Path to BIDS iEEG folder or electrodes.tsv file (optional)
   :param str micapipe_derivatives: Path to micapipe derivatives (optional)
   :param str hippunfold_derivatives: Path to hippunfold derivatives (optional)
   :return: None (results saved to output_folder)

.. py:function:: electroMICA_ScalpEEG(output_folder, feature, electrodes=None, micapipe_derivatives=None, hippunfold_derivatives=None)

   Project scalp EEG features onto cortical and hippocampal surfaces.

   :param str output_folder: Path to electroMICA derivatives folder
   :param str feature: Path to feature TSV file or feature label
   :param str electrodes: Path to BIDS EEG folder or electrodes.tsv file (optional)
   :param str micapipe_derivatives: Path to micapipe derivatives (optional)
   :param str hippunfold_derivatives: Path to hippunfold derivatives (optional)
   :return: None (results saved to output_folder)

Internal Functions (Selected)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These internal functions are documented for reference but are not typically called directly by users.

.. autofunction:: electroMICA.ComputeSensitivityProfile
   :noindex:

.. autofunction:: electroMICA.ComputeFeatureMaps
   :noindex:

.. autofunction:: electroMICA.GetContactPositions
   :noindex:

.. autofunction:: electroMICA.ContactProperties
   :noindex:

.. autofunction:: electroMICA.build_BEM_model
   :noindex:

.. autofunction:: electroMICA.compute_leadfield
   :noindex:

.. autofunction:: electroMICA.solve_inverse_problem
   :noindex:

Mathematical Utilities
~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: electroMICA.int_lp
   :noindex:

   Computes analytic surface integrals for BEM boundary element method.

.. autofunction:: electroMICA.int_scalar
   :noindex:

   Scalar surface integrals used in BEM calculations.

Data Types and Structures
--------------------------

While `electroMICA` primarily works with standard NumPy arrays and file paths, 
the following data structures are commonly used:

**Surface Data**
   Cortical and hippocampal surfaces are represented as GIFTI files (``.gii``) 
   containing vertex coordinates and face connectivity.

**Feature Files**
   Feature data are stored as TSV (tab-separated values) files with:
   - First column: channel/electrode labels
   - Second column: feature values
   - Optional additional columns: metadata

**Leadfield Matrices**
   Computed leadfield matrices are stored as MATLAB ``.mat`` files containing:
   - ``Sensitivity``: K × N sensitivity matrix (K contacts, N surface vertices)
   - ``ContactName``: Channel labels
   - ``VertexIndices``: Indices of surface vertices used

**Output Maps**
   Projected features are saved as GIFTI surface files with values defined at each vertex.

Dependencies
------------

Core dependencies:

- **numpy** — Numerical computations
- **scipy** — Linear algebra and signal processing (sparse matrices, BEM solving)
- **pandas** — Feature file I/O and metadata
- **nibabel** — Neuroimaging file formats (NIFTI, GIFTI)
- **antspyx** — Image registration and transforms

Optional:

- **vtk** — 3D visualization and mesh operations
- **pyvirtualdisplay** — Headless display for servers

Examples
--------

**Example 1: Basic iEEG projection**

.. code-block:: python

   from electroMICA import electroMICA_iEEG
   
   electroMICA_iEEG(
       output_folder='/data/electroMICA/sub-01/ses-01',
       feature='/data/features/sub-01_ses-01_Spike.tsv',
       electrodes='/data/BIDS_iEEG/iEEG/',
       micapipe_derivatives='/data/micapipe'
   )

**Example 2: Scalp EEG with hippunfold**

.. code-block:: python

   from electroMICA import electroMICA_ScalpEEG
   
   electroMICA_ScalpEEG(
       output_folder='/data/electroMICA/sub-02/ses-01',
       feature='/data/features/sub-02_ses-01_AvgSpike.tsv',
       electrodes='/data/BIDS_EEG/EEG/',
       micapipe_derivatives='/data/micapipe',
       hippunfold_derivatives='/data/hippunfold'
   )

**Example 3: Using precomputed leadfields**

If you've already run `electroMICA` once, you can reuse the computed leadfields 
for faster feature mapping:

.. code-block:: python

   from electroMICA import electroMICA_iEEG
   
   # Recompute feature maps without recalculating leadfields
   electroMICA_iEEG(
       output_folder='/data/electroMICA/sub-01/ses-01',
       feature='/data/features/sub-01_ses-01_NewFeature.tsv'
       # electrodes and micapipe_derivatives not needed
   )

See Also
--------

- :ref:`usage` — Detailed usage guide
- :ref:`algorithm` — Algorithmic and mathematical background
- :ref:`installation` — Installation instructions

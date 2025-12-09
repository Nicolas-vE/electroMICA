.. _contributing:

Contributing to electroMICA
============================

Thank you for your interest in contributing to `electroMICA`! This document provides guidelines 
for contributing code, documentation, and feedback.

Code of Conduct
---------------

We are committed to providing a welcoming and inclusive environment. Please treat all contributors 
with respect and professionalism.

Getting Started
---------------

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:

   .. code-block:: bash

      git clone https://github.com/your-username/electroMICA.git
      cd electroMICA

3. **Create a virtual environment** and install development dependencies:

   .. code-block:: bash

      python -m venv .venv
      source .venv/bin/activate  # or .\.venv\Scripts\Activate.ps1 on Windows
      pip install -r requirements.txt

4. **Create a feature branch**:

   .. code-block:: bash

      git checkout -b feature/your-feature-name

5. **Make your changes**, following the guidelines below.

6. **Commit and push**:

   .. code-block:: bash

      git add .
      git commit -m "Descriptive commit message"
      git push origin feature/your-feature-name

7. **Open a pull request** on GitHub and describe your changes.

Coding Guidelines
-----------------

**Python Style**
   - Follow `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ conventions
   - Use 4 spaces for indentation
   - Limit lines to ~100 characters where practical
   - Use descriptive variable and function names

**Docstrings**
   - All functions should have docstrings in NumPy or Google style
   - Include parameter descriptions, return types, and examples
   - Example:

   .. code-block:: python

      def compute_feature_map(leadfield, features):
          """
          Compute the projected feature map from a leadfield matrix.

          Parameters
          ----------
          leadfield : array_like
              Shape (n_vertices, n_channels). Leadfield matrix.
          features : array_like
              Shape (n_channels,). Feature values at each channel.

          Returns
          -------
          map : ndarray
              Shape (n_vertices,). Projected feature map.

          Examples
          --------
          >>> lf = np.random.randn(1000, 32)
          >>> feat = np.random.randn(32)
          >>> proj = compute_feature_map(lf, feat)
          """
          ...

**Comments**
   - Write clear, concise comments explaining the "why" not the "what"
   - Avoid redundant comments; let readable code speak for itself

**Testing**
   - Add unit tests for new functions in a `tests/` folder (when tests are formalized)
   - Verify your code works with the existing example scripts
   - Test on multiple Python versions (3.7+) if possible

**Performance**
   - Avoid unnecessary loops; use NumPy vectorization
   - Profile critical sections if performance matters
   - Use sparse matrices (scipy.sparse) for large matrices

Types of Contributions
----------------------

**Bug Reports**
   - Open an issue on GitHub with a clear description
   - Include Python version, OS, and a minimal reproducible example
   - Attach relevant error messages and tracebacks

**Feature Requests**
   - Describe the feature and why it would be useful
   - Provide use cases or examples
   - Discuss design implications (e.g., API changes)

**Code Contributions**
   - Bug fixes: Target the main branch
   - Features: Discuss first via an issue to ensure alignment
   - Refactoring: Ensure no behavioral changes and all tests pass

**Documentation Improvements**
   - Clarify ambiguous sections
   - Add missing examples or references
   - Correct typos and grammatical issues
   - Improve algorithm descriptions or API docs

**Example Scripts**
   - Add new example scripts for specific use cases
   - Ensure scripts are well-commented and runnable
   - Include both simple and advanced examples

Workflow & Pull Requests
------------------------

**Before submitting:**
   1. Ensure your branch is up-to-date:

      .. code-block:: bash

         git fetch origin
         git merge origin/main

   2. Test your changes:

      .. code-block:: bash

         python example_electroMICA_iEEG.py  # or relevant test

   3. Check code style (if linter is available):

      .. code-block:: bash

         # Optional: run flake8 or similar
         flake8 electroMICA.py

**Pull Request Template**

   .. code-block:: markdown

      ## Description
      Brief description of the change.

      ## Type of Change
      - [ ] Bug fix
      - [ ] New feature
      - [ ] Documentation
      - [ ] Refactoring

      ## Related Issues
      Closes #(issue number)

      ## Testing
      Describe how you tested the changes.

      ## Checklist
      - [ ] Code follows PEP 8 guidelines
      - [ ] Docstrings added/updated
      - [ ] Comments added where necessary
      - [ ] Examples tested and working
      - [ ] No new warnings or errors

**Review Process**
   - A maintainer will review your PR
   - Address feedback and suggestions
   - Once approved, the PR will be merged

Documentation
--------------

**Building Docs Locally**
   The documentation uses Sphinx and the RTD theme:

   .. code-block:: bash

      cd docs
      make html

   Open ``docs/_build/html/index.html`` in your browser to preview.

**Editing Docs**
   - Source files are in ``docs/`` (RST format)
   - Update relevant sections when making code changes
   - Add new doc pages for new features
   - Use consistent RST formatting and cross-references

**Documentation Standards**
   - All public functions should be documented in the API reference
   - Provide examples for non-trivial features
   - Include mathematical background (see :ref:`algorithm`) for complex methods
   - Reference external papers and related work

Reporting Issues
----------------

**Security Issues**
   Please do **not** open a public issue for security vulnerabilities.
   Email the maintainers directly with details.

**Bug Reports**
   Include:
   - Python version and OS
   - Full error traceback
   - Minimal reproducible example
   - Steps to reproduce
   - Expected vs. actual behavior

**Feature Requests**
   Describe:
   - The feature and its purpose
   - Why it would be useful
   - Proposed API or interface
   - Any implementation concerns

Development Environment
-----------------------

**Recommended Tools**
   - **Editor**: VS Code, PyCharm, or similar
   - **Linter**: flake8, pylint, or ruff
   - **Formatter**: black or autopep8
   - **Type checker**: mypy (optional)
   - **Documentation**: Sphinx, rst2html

**Optional Setup**
   Add to `requirements.txt` for development:

   .. code-block:: bash

      pip install flake8 black pytest pytest-cov mypy sphinx-autodoc-typehints

**Pre-commit Hook** (optional)
   Create `.git/hooks/pre-commit`:

   .. code-block:: bash

      #!/bin/bash
      flake8 electroMICA.py || exit 1
      black --check electroMICA.py || exit 1

Acknowledgments
---------------

Contributors to `electroMICA` are listed in the repository and documentation. 
Thank you for improving the tool!

Contact
-------

For questions or discussions:
- Open a GitHub discussion
- Email the MICA Lab (see README)
- Check the documentation and FAQ

---

Last updated: 2025. See the repository for the latest guidelines.



---

# Contributing to python_cafe

We appreciate your interest in contributing to [Project Name](https://github.com/drbess/python_cafe)! This document provides guidelines for contributing. By participating in this project, you agree to abide by its terms.

## Setting Up Your Development Environment

1. **Fork the Repository**: Click the 'Fork' button on the GitHub repository page to create your own fork of the repository.

2. **Clone Your Fork**: Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/PROJECT_NAME.git
   ```

3. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use: env\Scripts\activate
   ```

4. **Install Development Dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   ```

5. **Create a New Branch**: For each contribution, create a new branch:
   ```bash
   git checkout -b YOUR_BRANCH_NAME
   ```

## Code Style

Please adhere to the [PEP 8](https://www.python.org/dev/peps/pep-0008/) coding convention which is the standard for Python code. We also use [Black](https://github.com/psf/black) to format our code, so please make sure your contributions are formatted with it.

## Submitting Changes

1. **Commit Your Changes**: Commit any changes in your branch.
   ```bash
   git add .
   git commit -m "YOUR COMMIT MESSAGE"
   ```

2. **Push to Your Fork**: Push your changes to your fork on GitHub.
   ```bash
   git push origin YOUR_BRANCH_NAME
   ```

3. **Open a Pull Request**: Go to the [original repository on GitHub](https://github.com/drbess/python_cafe) and click on 'New Pull Request'. Choose your branch from the dropdown and click 'Create Pull Request'.

## Reporting Issues

If you find any bugs or have suggestions, please open an issue in the repo. Make sure to check existing issues first to avoid duplicates.

## Running Tests

Before submitting your changes, make sure all tests pass. Here's a guide from [Real Python](https://realpython.com/pytest-python-testing/):

```bash
pytest
```

## Additional Notes

- Please ensure your PRs are small and focused. Large PRs with multiple unrelated changes are difficult to review and may not be merged.
- If adding a new feature, please ensure to include relevant documentation and tests.
- Make your commit message descriptive that explains the reasoning behind the change.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

---

Good looking out on your contribution! 

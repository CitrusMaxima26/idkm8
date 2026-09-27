# Testing exercise

Fork this project into your own GitLab account, clone the fork, and follow the exercise sheet.

One function in `src/my_math.py` is wrong. Write the tests in `test/test_example.py`, then run `pytest` from this directory.

## Virtual environment

Create and activate a virtual environment before installing packages or running tests:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The prompt shows `(.venv)`. Keep that terminal open while you work. On Windows, activate with `.venv\Scripts\activate`.

`.venv/` is listed in `.gitignore`, so it stays on your computer. The GitLab pipeline installs its own packages.

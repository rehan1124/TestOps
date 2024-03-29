# TestOps

Testing + Operations (CI-CT)

* Clone the GitHub repo and create a virtual env in current directory using command

```commandline
python -m venv venv
```

* Activate virtual env using `venv/Script/activate` command

* Install all packages by running command `pip install -r requirements.txt`

* To run tests in parallel, execute command `python -m pytest -v -s -n 4`. `-n` indicates number of tests to run in
  parallel at a time.

* The framework also supports `adding tags/markers` to test.
  Make use of `pytest.ini` to registers markers. Execute command `pytest -v -s -n 4 -m pets` to run tests marked
  as `pets`.
# pytest_module

Python pytest framework.

## Requirements

- Python 3.6

## commands

- pytest
- pytest -v
- pytest <test_file>
- pytest <test_file>:<test_method>
- pytest -x --> exit when encountered first failed testcase.
- pytest -s --> show print statements

## Notes

### Fixtures

- Pytest fixtures are functions that can be used to manage our apps states and dependencies.
- Most importantly, they can provide data for testing and a wide range of value types when explicitly called by our testing software.
- You can use the mock data that fixtures create across multiple tests.

# fdk-rdf-parser

This is a pypi-package, [fdk-rdf-parser](https://pypi.org/project/fdk-rdf-parser), that parses rdf-data to json-objects used by [Felles datakatalog](https://data.norge.no)

## Develop and run locally
### Requirements
- [pyenv](https://github.com/pyenv/pyenv) (recommended)
- [poetry](https://python-poetry.org/)
- [nox](https://nox.thea.codes/en/stable/)
- [nox-poetry](https://pypi.org/project/nox-poetry/)

### Install software:
```
% pyenv install 3.9.0
% pyenv local 3.9.0
% pip install poetry==1.1.7
% pip install nox==2021.6.12
% pip install nox-poetry==0.8.6
% poetry install
```

### Environment variables
```
ORGANIZATION_CATALOG_BASE_URI=https://organization-catalog.staging.fellesdatakatalog.digdir.no
REFERENCE_DATA_BASE_URI=http://staging.fellesdatakatalog.digdir.no/reference-data
NEW_REFERENCE_DATA_BASE_URI=https://www.staging.fellesdatakatalog.digdir.no/new-reference-data
```

## Running tests
[pytest](https://docs.pytest.org/en/latest/) is used to run tests.

To run linters, safety, checkers and tests:
```
% nox
```

Code formatting:
```
% nox -rs black
```

### Other helpful commands

Run tests outside of a nox session:
```
% poetry run pytest
```

Run specific nox sessions:
```
% nox -s mypy
% nox -rs lint
```

Run session with specified arguments:
```
% nox -s tests -- -vv
```

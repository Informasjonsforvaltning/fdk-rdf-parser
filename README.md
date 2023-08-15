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
% pip install poetry==1.4.2
% pip install nox==2023.4.22
% pip install nox-poetry==1.0.2
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

## Creating a new release of the library
- Manually change the version in *pyproject.toml*.
- Optional: update other dependencies as well.
- Run `poetry update`
- All commits to the main branch on GitHub triggers the "Release Drafter"-action, it creates a release draft or adds the commit to an existing draft.
- Click the **Releases** link on GitHub when you are ready to publish the draft, and then click the "Edit"-button (looks like a **pencil**) on the **Draft** version.
- Check that the release-tag equals the version in [pyproject](https://github.com/Informasjonsforvaltning/fdk-rdf-parser/blob/main/pyproject.toml) before clicking the **Publish release** button. This triggers the **Release**-action, that uses poetry to release the new version to [PyPI](https://pypi.org/).

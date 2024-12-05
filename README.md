
# Dependency Management

I am using `poetry` a modern Python tool. 

## Commands for developing this project: 

```shell
# Create a python project with poetry-managed dependencies
poetry new python-projectX

# Create virsual environment for this project
poetry shell
poetry env list
poetry env use python3

# Add new dependency
poetry add requests
# Add dependencies grouped by environments
poetry add --group dev pytest
# OR:
poetry add pytest --dev

# Update poetry itself
poetry self update
# Upgrade dependencies
poetry update requests
poetry update 

# Check dependencies
poetry show numpy

# Resolve dependencies and create lock file
poetry install

# Apply poetry to existing non-poetry project
poetry init
poetry env use python3
poetry env list

```

## Commands for build and publish this project

```shell
poetry build

poetry config pypi-token.pypi <pypi-token>

poetry publish
poetry publish --repository <other-than-pypi>
```

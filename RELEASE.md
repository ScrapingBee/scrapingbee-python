# Release a new version in PyPI

A new package is automatically uploaded to PyPI when a new tag is pushed to Github. To release a new version follow the steps:

1. Update the version number X.X.X in [setup.py](setup.py) and push the change.

2. Create a tag with the same version number.

```bash
git tag X.X.X
```

3. Push the tag to Github.

```bash
git push origin X.X.X
```

A new version will be pushed to PyPI using the [PyPI Github Action](https://github.com/marketplace/actions/pypi-publish) defined in [.github/workflows/main.yaml](.github/workflows/main.yaml). 
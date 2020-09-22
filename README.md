# Accounting tool

A tool for processing important financial data.

## Development
Prerequisites:
- python
- pipenv

Project setup
```
pipenv install --dev
pipenv install -e .
```

Run tests
```
pipenv run pytest
```

Run app
```
pipenv run python account.py <filename>
```

## Packaging
Prerequisites:
- python
- pipenv
- docker

Recommended python installation for Mac OS based packaging
```
PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.8.5
```

Build binary packages for Mac OS, Linux, Windows
```
bash ./pyinstaller.sh
```

Natively built package (Max OS in my case) will be available at `dist/macos/cli`

Linux package will be available at `dist/linux/cli`

Windows package will be available at `dist/windows/cli`

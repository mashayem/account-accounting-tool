# Accounting tool

A tool for processing important financial data.

## Development
Prerequisites:
- python3
- pipenv

Install dependencies
```
pipenv install --dev
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

Build binary packages for macOS, linux, Windows
```
./pyinstaller.sh
```

Natively built package (macOS in my case) will be available at `dist/macos`
Linux package will be available at `dist/linux`
Windows package will be available at `dist/windows`

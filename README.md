# Accounting tool

A tool for processing important financial data.

## Development
Prerequisites:
- Python3
- pipenv
- Allure - for reporting: https://docs.qameta.io/allure/#_installing_a_commandline

Install dependencies
```
pipenv install --dev
```

Run unit tests
```
pipenv run pytest tests/unit
```

Run tests with Allure reporting
```
pipenv run pytest --alluredir=path/to/allure_results
```

View Allure generated report after running tests
```
pipenv run allure serve /absolute/path/to/allure_results
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

Once package is built, you will be able to run end-to-end tests.
Use EXECUTABLE_PATH variable to specify executable file the e2e tests will be run against, depending on your operating system
For example: fir macOS, the command will be: 
```
EXECUTABLE_PATH=dist/macos/account pipenv run pytest tests/e2e
```

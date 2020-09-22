rm -rf ./dist/

pipenv run pyinstaller --onefile account.py
mkdir -p dist/macos
mv dist/account dist/macos/account

pipenv lock -r > requirements.txt
docker run -v "$(pwd):/src/" cdrx/pyinstaller-linux:python3
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows:python3
rm -rf requirements.txt
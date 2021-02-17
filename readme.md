# Eland PreProcessing

## requirement

- python 3.8

### Case 1
- `pip install --user -r requirements.txt`

### Case 2(推薦)
- 安裝虛擬環境 `pip install virtualenv`
- 建立虛擬環境 `virtualenv -p <python3_path> venv`
- ex: `virtualenv -p `which python3.8` venv`
- 進入虛擬環境 `source venv/bin/activate`
- 安裝lib(test) `pip install --user -r requirements/test.txt`
- 安裝lib(prod) `pip install --user -r requirements/prod.txt`

## local-test
```
python -m unittest discover -s ./test --pattern '*.py'
```

## 備註
- 測試lib有改動請更新test.txt
`pip freeze > requirements/test.txt`
- prod code lib有改動請更新prod.txt
`pip freeze > requirements/prod.txt`
- build docker image 指令
```
docker build . -t eland_preprocessing
docker run eland_preprocessing python app.py conf/application.yml conf/config.json
```
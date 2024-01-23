# 準備

``` bash
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
# 静的解析が必要な場合
$ pip install jedi flake8 importmagic autopep8 yapf black
```

# EXE化

以下を実施すると dist ディレクトリに pymdreader.exe が生成される

``` bash
$ pyinstaller pymdreader.py --onefile
```


# 実行(開発環境)

このスクリプト配下のmdファイルを探してmarkdownプレビュー表示を行う  
よって、このままでは pymdreader 開発環境配下を検索するので意味はないが、デバッグ等で必要になるかもしれない  

``` bash
$ python pymdreader.py
```

# 実行

dist ディレクトリにある pymdreader.exe をmdファイルが存在するディレクトリ階層の先頭にコピー  
コピー後、pymdreader.exe を実行し、ブラウザで http://127.0.0.1:3000 にアクセスすると mdファイルがプレビュー表示される  


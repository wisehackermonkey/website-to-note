# website-to-note
### simple python app that giving a url from the clipboard scrapes a web page for its title and returns a useful information for use in docs, notetaking apps, etc.
```
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
20200420
```

## how to install (development only)
```
git clone https://github.com/wisehackermonkey/website-to-note.git
cd website-to-note
pip install -r requirements.txt
```

## run
```
```

## build exe for windows
```
pip install pyinstaller
pyinstaller --noconsole --specpath ${PWD}/build --distpath ${PWD}/build/dist --workpath ${PWD}/build/build --onefile website-to-note.py
```

## advance (powershell) build exe for windows (auto zip for releases)
```
pyinstaller --noconsole --specpath ${PWD}/build --distpath ${PWD}/windows_builds --workpath ${PWD}/build/build --onefile website-to-note.py; $date = Get-Date -Format "yyyyMMdd"; Compress-Archive -force -Path ${PWD}/windows_builds/website-to-note.exe -DestinationPath ${PWD}/windows_builds/website-to-note_windows_${date}.zip
```

## todo
-  ~~TODO add vaildators package~~
-  add tts say not valid url


## links

validators - validators 0.11.2 documentation
https://validators.readthedocs.io/en/latest/#
20200420


Python - How to validate a url in python ? (Malformed or not) - Stack Overflow
https://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not
20200420


html - How can I retrieve the page title of a webpage using Python? - Stack Overflow
https://stackoverflow.com/questions/51233/how-can-i-retrieve-the-page-title-of-a-webpage-using-python
20200420


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
pyinstaller --noconsole --specpath ${PWD}/builds --distpath ${PWD}/builds/dist --workpath ${PWD}/builds/build --onefile website-to-note.py
```

## advance (powershell) build exe for windows (auto zip for releases)
```
pyinstaller --noconsole --specpath ${PWD}/builds --distpath ${PWD}/builds/dist --workpath ${PWD}/builds/build --onefile website-to-note.py; 


mv -force ${PWD}/builds/dist/website-to-note.exe ${PWD}/windows_builds/website-to-note.exe ; 

$date = Get-Date -Format "yyyyMMdd"; 

Compress-Archive -force -Path ${PWD}/windows_builds/website-to-note.exe -DestinationPath ${PWD}/windows_builds/website-to-note_windows_${date}.zip
```

## todo
-  ~~TODO add vaildators package~~
-  add tts say not valid url


## links

validators - validators 0.11.2 documentation
https://validators.readthedocs.io/en/latest/#
20200420

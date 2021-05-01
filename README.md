# Guessing-Game
A Guessing Game built in Python and Tkinter!  Except, there's a twist - the computer will guess the number you're thinking of! (the application version is only supported on macOS at the moment, the `.py` script is in here too so if you're on windows you can run it using that)

## How does it work?
It uses the binary search algorithm to narrow down the results, which gives it a time complexity of O(log n).

[![](https://img.shields.io/badge/Download-v1.0-green?style=for-the-badge)](https://github.com/Jminding/Guessing-Game/releases/download/v1.0/Guessing.Game.app.zip)


### Troubleshooting
#### I cannot open this because it's not from a verified developer!
Right click on the file, then click `Open`, and you will be asked that you're sure you want to open this file.  Click "Ok" or "Yes" or "Open" and there you go!

#### It gives me an error!
Well it worked fine on my computer so you probably entered something wrong.
Unless you're trying to make it break - then you succeeded, congratulations!
Make sure you're entering only numbers in the lower bound and upper bound!


## If someone on Windows can do this for me and make a pull request with the file, it would be very helpful (if it works)
1. Navigate to Cmd.exe and do `pip install py2exe`
2. Create a file called `setup.py` and paste this inside it:
```python
from distutils.core import setup
import py2exe

setup(windows=['Guessing Game.py'])
```
**Make sure that the `Guessing Game.py` is in the same directory ass the new setup.py file**
3. Navigate back to Cmd.exe and run `python3 setup.py py2exe`
4. If it succeeds and you successfully get a `Guessing Game.exe` file that opens, then please open a pull request and send it to me!

I mean if not, you can always just download python and run it that way as well...

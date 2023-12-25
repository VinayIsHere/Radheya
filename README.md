This is an GUI Automation Tool. 
Currently supports only Windows.
It is still in development.

It kinds of Squish but openSource, Feel Free to Make PR for feature and bug improvements.

For Setup
Install the following Libraries first
```
pip install pynput
pip install keyboard
```

press `ctrl+s` to start mouse events recording, then it will create a json file which will contain all the mouse event you are doing.
To stop the mouse event recording press `ctrl+end`
Than use the Replayer to repeat the steps for the json file. The Replayer still needs to be implemented.
Still Needs to develop UI for this, So for now, I made it start and stop based on key combination.

Radhe Radhe

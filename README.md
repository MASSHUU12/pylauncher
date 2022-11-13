# PyLauncher

A program used to automate the startup of a series of programs. I run the same programs every day, and I don't want them to slow down the system startup by automatically running, so I created this program to streamline and speed up the constant clicking of the same icons.

The program is free of any dependencies, you just need to have Python.

This source code is available to everyone under the standard [MIT](https://github.com/MASSHUU12/pylauncher/blob/master/LICENSE) license.

## Program configuration

### Prerequisites

- Python 3.4^

### Defining lists of programs to run

In the `pylauncher/lists` folder, create a `list.json` file.

In the same folder is the file `list-example.json`, which contains the basic sample configuration of the program.

To create a list, you first need to name it somehow, e.g. `main`. With this name you will later call a specific list to run.

```json
{
  "main": {}
}
```

Once we have the function named, we can proceed to add the programs that will be run. The order in which the programs run depends on the order in the list, the programs run from the top.

The way to add programs is as follows:
- First you give the name of the program (it can be anything else, the name is only used to display errors).

```json
{
  "main": {
    "LibreWolf": {}
  }
}
```

- Then specify the path to the program you want to run.

```json
{
  "main": {
    "LibreWolf": {
      "path": "C:\\Program Files\\LibreWolf\\librewolf.exe",
    }
  }
}
```

- The last, optional step is to add options to the program you are running (refer to the target program's documentation to know what options it supports). Even if you don't want to give any additional options I recommend passing an empty array.

```json
{
  "main": {
    "LibreWolf": {
      "path": "C:\\Program Files\\LibreWolf\\librewolf.exe",
      "options": ["-new-tab"]
    },
    "Brave": {
      "path": "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
      "options": []
    }
  }
}
```

### Launching the program

#### Method one (not recommended)

The simplest method, but inconvenient.
Assuming you are in the root directory of the project, you can run it using the console:

```bash
python .\pylauncher\pylauncher.py list_name
```

or

```bash
.\pylauncher\pylauncher list_name
```

#### Method two (better, but still not recommended) | Windows Only

This method will only work on Windows systems, however, all steps have their counterparts on other systems.

And what will this method do anyway? It will allow you to call the program from anywhere on the system, so you won't have to go into the program folder.

To begin with, move the program folder to some convenient place, such as the D drive, so that the path looks more or less like this `D:\pylauncher`.
Of course, the program can also be elsewhere, but this is the easiest way to do it.

Now click the Windows logo and look for something called `Edit the system environment variables`.
A small window should appear, click the button named `Environment Variables...`.

A new window divided into two sections should appear, we are interested in the bottom section named `System Variables`. Look for a variable named `Path`, select it and click `Edit`.

The last window will appear, click the button on the right named `New`.

This is the most important moment, after clicking `New` paste the path to the `pylauncher.py` file, without the file name. Assuming that the program is in `D:\pylauncher` the path should look like this `D:\pylauncher\pylauncher`.

Now turn on the console and run the program, if everything went well, the program should work from anywhere on the system.

```bash
pylauncher list_name
```

#### Method three (recommended)

This method involves creating a new file on the desktop (or wherever else you want to run the program from), which will call a program that will run a specific list.
This is the best option because once everything is done, you will be able to run a series of programs with one or two clicks.

Windows .bat file:

```bat
@REM It will run in a new window, so you can see all the program logs
cd "D:\gitHub\program-launcher\pylauncher"
start "" cmd.exe /k "pylauncher.py list_name"

@REM Runs without a window
cd "D:\gitHub\program-launcher\pylauncher"
start "" pylauncher.py list_name

@REM Also runs without a window
@REM It only works if you have performed method two first
start "" pylauncher list_name
```

Windows .ps1 file:

```ps1
# Runs without a window
Set-Location -Path "D:\gitHub\program-launcher\pylauncher"
python pylauncher.py list_name

# Makes the window not disappear, so you can see the logs
pause
```

Linux/Unix .sh file (I have not checked if it works):

```sh
cd your/directory
python pylauncher.py list_name
```

### License

Licensed under the [MIT](https://github.com/MASSHUU12/pylauncher/blob/master/LICENSE) license.

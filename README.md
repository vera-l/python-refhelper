# Python refactoring helper

> A tool for easy refactoring. It was originally written to find all 
> division and rounding cases for python 2 -> 3 transition, but 
> can be useful for other refactoring tasks.

How the tool works:

1. It finds all python-files in some path (usually, your project)
2. Parses each file as AST
3. Finds all cases for current task in AST
4. Makes html-report with all using cases, then opens it in browser
5. By click on each link you can open this file in IntelliJ idea at current linenumber

### Installing:

```console
git clone https://github.com/vera-l/python-refhelper.git
cd python-refhelper
python3 setup.py install --user
```

### Using:

```console
pyrefhelper [path] [task=list|division|rounding]
```

### Available tasks:

* `list` - get all python files
* `division` - find division cases in all python files
* `rounding` - find rounding cases in all python files
* `your_task` - you can add own tasks

### Report example:

![pyrefhelper screenshot](pyrefhelper_screenshot.png)

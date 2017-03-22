SublimeLinter-clang
=========================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3) provides an interface to [clang](http://clang.llvm.org/). It will be used with files that have the C/C Improved/C++ syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before using this plugin, you must ensure that `clang` is installed on your system.
- Mac OS X: clang should be already bundled.
- Linux: clang can be easily installed using most package managers.
- Windows: the situation is a little trickier, especially with C++. One way to go is to install [mingw with clang](http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/rubenvb/). Both gcc and clang packages should be installed into the same directory.

Once `clang` is installed, you must ensure it is in your system PATH so that SublimeLinter can find it. This may not be as straightforward as you think, so please read [How linter executables are located](http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located) in the documentation.

Once you have installed `clang` you can proceed to install the SublimeLinter-clang plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `clang`. Among the entries you should see `SublimeLinter-clang`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

In addition to the standard SublimeLinter settings, SublimeLinter-clang provides its own settings.

|Setting|Description|
|:------|:----------|
|include_dirs|A list of directories to be added to the header search paths (-I is not needed).|
|extra_flags|A string with extra flags to pass to clang. These should be used carefully, as they may cause linting to fail.|

In project-specific settings, '$project_folder' or '${project_folder}' can be used to specify relative path.
```
"SublimeLinter":
{
    "linters":
    {
        "clang": {
            "extra_flags": "-Wall -I${project_folder}/foo",
            "include_dirs": [
                "${project_folder}/3rdparty/bar/include",
                "${project_folder}/3rdparty/baz"
            ]
        }
    }
},
```

## Troubleshooting
C/C++ linting is not always straightforward. A few things to try when there's (almost) no linting information available:
- Try to compile from the command line, and verify it works.
- The linter might be missing some header files. They can be added with "include_dirs".
- Sometimes clang fails to locate the C++ standard library headers.
Assuming the compilation works when executed via command line, try to compile with `clang++ -v`.
This will display all of the hidden flags clang uses. As a last resort, they can all be added as "extra_flags".

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbrevations unless they are very well known.

Thank you for helping out!

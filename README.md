### Source Code formatter for Sublime Text 3
###### [Sublime Text 3](http://www.sublimetext.com/3) | [JSBeautifier Web Site](http://jsbeautifier.org/) | [Node.js download](http://nodejs.org/#download)

#### About
This is a Sublime Text 3 plugin allowing you to format your HTML, XML, CSS, JavaScript and JSON code. It uses a set of nice beautifier libs made by Einar Lielmanis and Noah Kantrowitz. The formatters are written in JavaScript, so you'll need `node.js` to run it.

#### Manual Installation

###### Mac

    git clone https://github.com/odetinin/Pretty-Code.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Pretty\ Code

###### Linux

    git clone https://github.com/odetinin/Pretty-Code.git ~/.config/sublime-text-3/Packages/Pretty\ Code

###### Windows

    git clone https://github.com/odetinin/Pretty-Code.git %APPDATA%/Sublime\ Text\ 3/Packages/Pretty\ Code

Please make sure `node.js` is on the system path or try setting the absolute path to `node.js` in `PrettyCode.sublime-settings`:

    "node_path": "/your/absolute/path/to/node"

#### Usage

###### Commands:

    {
        "caption": "Pretty Code",
        "command": "pretty_code"
    }

###### Hotkeys:

    {
        "keys": ["alt+\\"],
        "command": "pretty_code"
    }

###### Settings:

    {
        "node_path": "/usr/local/bin/node",
        "format_on_save": false,
        "settings": {
            "html": {
                "scope": ["html", "shtml", "xml", "xhtml"],
                // Options: "collapse", "expand", "end-expand", "expand-strict"
                "brace_style": "collapse",
                "indent_char": " ",
                // OPtions: "keep", "separate", "normal"
                "indent_scripts": "keep",
                "indent_size": 4,
                "max_preserve_newlines": 2,
                "preserve_newlines": true,
                "unformatted": ["a", "sub", "sup", "b", "i", "u"],
                "wrap_line_length": 0
            },
            "css": {
                "scope": ["css", "scss", "sass", "less"],
                "indent_char": " ",
                "indent_size": 4
            },
            "js": {
                "scope": ["javascript", "json", "js", "jshintrc"],
                "brace_style": "collapse",
                "break_chained_methods": false,
                "e4x": false,
                "eval_code": false,
                "indent_char": " ",
                "indent_level": 0,
                "indent_size": 4,
                "indent_with_tabs": false,
                "jslint_happy": true,
                "keep_array_indentation": false,
                "keep_function_indentation": false,
                "preserve_newlines": true,
                "max_preserve_newlines": 2,
                "space_before_conditional": true,
                "space_in_paren": false,
                "unescape_strings": false,
                "wrap_line_length": 0
            }
        }
    }

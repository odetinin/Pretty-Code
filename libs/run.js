(function () {
    "use strict";

    var argv = process.argv,
        log = console.log,
        mode = parseInt(argv[3]),
        options = JSON.parse(argv[4].replace(/(?:\/\*(?:[\s\S]*?)\*\/)|(?:\/\/(?:.*)$)/gm, "").replace(/\'/g, "\""));

    require("fs").readFile(argv[2], "utf8", function (error, data) {
        if (!error) {
            if (mode === 0) {
                log(require("./js-beautify/js/lib/beautify").js_beautify(data, options.js));
            } else if (mode === 1) {
                log(require("./js-beautify/js/lib/beautify-html").html_beautify(data, options.html));
            } else if (mode === 2) {
                log(require("./js-beautify/js/lib/beautify-css").css_beautify(data, options.css));
            }
        }
    });
}());

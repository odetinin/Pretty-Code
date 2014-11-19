import sublime
import sublime_plugin
import os, subprocess, codecs

PLUGIN_FOLDER = os.path.dirname(os.path.realpath(__file__))
PLUGIN_SETTINGS = sublime.load_settings('PrettyCode.sublime-settings')
PRETTY_SETTINGS = PLUGIN_SETTINGS.get('pretty')

class PrettyCodeCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        filename = self.view.file_name()
        extension = ''
        if filename != None:
            extension = os.path.basename(filename).split('.')[-1]

        syntax = os.path.basename(self.view.settings().get('syntax')).replace('.tmLanguage', '').lower()

        mode = -1

        js_scope = (PRETTY_SETTINGS.get('js')).get('scope')
        html_scope = (PRETTY_SETTINGS.get('html')).get('scope')
        css_scope = (PRETTY_SETTINGS.get('css')).get('scope')

        if js_scope != None:
            if syntax in js_scope or extension in js_scope:
                mode = 0

        if html_scope != None:
            if syntax in html_scope or extension in html_scope:
                mode = 1

        if css_scope != None:
            if syntax in css_scope or extension in css_scope:
                mode = 2

        if mode != -1:

            # Get the current text in the buffer and save it in a temporary file.
            # This allows for scratch buffers and dirty files to be beautified as well.

            bufferText = self.view.substr(sublime.Region(0, self.view.size()))
            tempFile = PLUGIN_FOLDER + '/.__temp__'
            f = codecs.open(tempFile, mode = 'w', encoding = 'utf-8')
            f.write(bufferText)
            f.close()

            node = PLUGIN_SETTINGS.get('node_path')
            if node == None:
                node = 'node'

            output = self.run_command([node, PLUGIN_FOLDER + '/libs/run.js', tempFile, str(mode), str(PRETTY_SETTINGS).lower()])
            os.remove(tempFile)

            if len(output) > 0:
                output = output.decode('utf-8')
                if self.view.settings().get('ensure_newline_at_eof_on_save') and not output.endswith('\n'):
                    output += '\n'
                if output != bufferText:
                    self.view.replace(edit, sublime.Region(0, self.view.size()), output)

        return

    def run_command(self, cmd):
        if int(sublime.version()) < 3000:
            if sublime.platform() != 'windows':

                # Handle Linux and OS X in Python 2.

                run = '"' + '" "'.join(cmd) + '"'
                return commands.getoutput(run)

            else:

                # Handle Windows in Python 2.

                # Hack to prevent console window from showing. Stolen from
                # http://stackoverflow.com/questions/1813872/running-a-process-in-pythonw-with-popen-without-a-console

                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

                return subprocess.Popen(cmd, stdout=subprocess.PIPE, startupinfo=startupinfo).communicate()[0]
        else:

            # Handle all OS in Python 3.

            run = '"' + '" "'.join(cmd) + '"'
            return subprocess.check_output(run, stderr=subprocess.STDOUT, shell=True)

class PreSaveFormatListner(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        if PLUGIN_SETTINGS.get('format_on_save') == True:
            view.run_command('pretty_code')
#!/usr/bin/python

from sys import stdout

CR = '\r'


class PrintRewritable():
    def __init__(self):
        self._line_length = 0
        self._line_rewriteable = False
        self._first_time = True

    def _space_fill_last_text(self):
        return ' ' * self._line_length

    def _prefix(self):
        if self._line_rewriteable:
            return CR + self._space_fill_last_text() + CR
        else:
            if self._first_time:
                return ''
            else:
                return '\n'

    def _write_to_screen(self, text):
        text = str(text)

        # sys.stdout.write(text)
        stdout.write(text)
        # sys.stdout.flush()
        stdout.flush()

    def print(self, text, line_rewriteable=False):
        '''Stores the line length of the last passed message and if it should
        be rewritten. If it should be rewritten, the next time a line is
        printed the cursor is reset with a "\\r" character and the last line
        overwritten with space characters and the cursor reset again,
        before writing in the new text and flushing it to screen.
        '''
        text = str(text)

        self._write_to_screen(self._prefix() + text)

        # multiline text cannot be fully overwritten so do not try
        self._line_rewriteable = line_rewriteable and '\n' not in text

        self._line_length = len(text)
        self._first_time = False

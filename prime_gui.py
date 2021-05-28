#!/usr/bin/python

import threading
from time import sleep

import printrewritable as pr
import prime

import itertools

OUTPUT_FILE = 'primelist.txt'

polling_time = 0.042


def thread_name(action):
    action = str(action)
    return '%s thread %r.' % (action, threading.current_thread().name)


prw = pr.PrintRewritable()


class PrimeGUI():
    def __init__(self, *args):
        self._helper_threads = ()
        self.reset(*args)

    def _setup_threads(self):
        prime_thread = threading.Thread(target=self._prime_finder)
        prime_thread.setName('PrimeThread')

        display_thread = threading.Thread(target=self._display_thread)
        display_thread.setName('CheckerThread')

        self._helper_threads = (prime_thread, display_thread)

    def reset(self):
        self.stop()
        self._pc = prime.PrimeCollection()

    def start(self):
        self.stop()

        self._setup_threads()
        self._queuing_finished = False

        for t in self._helper_threads:
            if not t.is_alive():
                t.start()

    def stop(self):
        self._queuing_finished = True

        for t in self._helper_threads:
            if t.is_alive():
                t.join()

    def save(self, filepath):
        self.stop()
        self._save_enumeration_to_file(filepath, *self._pc.cache)

    def load(self, filepath):
        self.stop()
        data = self._load_enumeration_from_file(filepath)
        self._pc = prime.PrimeCollection(data)

    def _last_prime(self):
        return self._pc.last

    last_prime = property(_last_prime)

    def is_continuing(self, *a):
        return not self._queuing_finished

    def _prime_finder(self):
        for prime_num in itertools.takewhile(self.is_continuing, self._pc):
            pass

    def _display_thread(self):
        '''Check queue for messages, if queue has something in it,
        will check it again and again until it does not as which point:
        it will wait for a bit and try again.
        '''
        while self.is_continuing():
            prw.print(self.last_prime, True)

            # So it does not use excessive CPU.
            sleep(polling_time)

    def __len__(self):
        return len(self._pc)

    def _save_enumeration_to_file(self, filepath, *output_enumeration):
        with open(filepath, mode='w') as f:
            for item in output_enumeration:
                f.write('%s\n' % item)

    def _load_enumeration_from_file(self, filepath):
        with open(filepath, mode='r') as f:
            stripped_lines = (line.strip() for line in f.readlines())
            # if statement makes it so blank lines are ignored
            return (int(line) for line in stripped_lines if line)


if __name__ == "__main__":
    print('Prime number finder:')
    prw.print('Loading...', True)

    p = PrimeGUI()

    try:
        p.load(OUTPUT_FILE)
    except IOError:
        print('No data found, starting from stratch.')

    # Have to be separate because of the printrewritable functionality
    print('Hit Enter to finish and save.')
    p.start()
    input()
    p.stop()

    print()
    print('%d highest prime' % (p.last_prime))
    print('%d found' % (len(p)))
    print('Attempting to save file to %r, this may take a while.' % (OUTPUT_FILE))

    try:
        p.save(OUTPUT_FILE)
    except IOError:
        print('File failed to save.')
    else:
        print('File saved successfully.')

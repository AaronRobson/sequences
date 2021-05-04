#!/usr/bin/python

import threading
from time import sleep

import printrewritable as pr
import prime

import itertools

OUTPUT_FILE = 'primelist.txt'

pollingTime = 0.042


def ThreadName(action):
    action = str(action)
    return '%s thread %r.' % (action, threading.current_thread().name)


prw = pr.PrintRewritable()


class PrimeGUI():
    def __init__(self, *args):
        self._helperThreads = ()
        self.Reset(*args)

    def _SetupThreads(self):
        primeThread = threading.Thread(target=self._PrimeFinder)
        primeThread.setName('PrimeThread')

        displayThread = threading.Thread(target=self._DisplayThread)
        displayThread.setName('CheckerThread')

        self._helperThreads = (primeThread, displayThread)

    def Reset(self):
        self.Stop()
        self._pc = prime.PrimeCollection()

    def Start(self):
        self.Stop()

        self._SetupThreads()
        self._queuingFinished = False

        for t in self._helperThreads:
            if not t.is_alive():
                t.start()

    def Stop(self):
        self._queuingFinished = True

        for t in self._helperThreads:
            if t.is_alive():
                t.join()

    def Save(self, filepath):
        self.Stop()
        self._SaveEnumerationToFile(filepath, *self._pc.cache)

    def Load(self, filepath):
        self.Stop()
        data = self._LoadEnumerationFromFile(filepath)
        self._pc = prime.PrimeCollection(data)

    def _LastPrime(self):
        return self._pc.last

    lastPrime = property(_LastPrime)

    def isContinuing(self, *a):
        return not self._queuingFinished

    def _PrimeFinder(self):
        for primeNum in itertools.takewhile(self.isContinuing, self._pc):
            pass

    def _DisplayThread(self):
        '''Check queue for messages, if queue has something in it,
        will check it again and again until it does not as which point:
        it will wait for a bit and try again.
        '''
        while self.isContinuing():
            prw.Print(self.lastPrime, True)

            # So it does not use excessive CPU.
            sleep(pollingTime)

    def __len__(self):
        return len(self._pc)

    def _SaveEnumerationToFile(self, filepath, *outputEnumeration):
        with open(filepath, mode='w') as f:
            for item in outputEnumeration:
                f.write('%s\n' % item)

    def _LoadEnumerationFromFile(self, filepath):
        with open(filepath, mode='r') as f:
            strippedLines = (line.strip() for line in f.readlines())
            # if statement makes it so blank lines are ignored
            return (int(line) for line in strippedLines if line)


if __name__ == "__main__":
    print('Prime number finder:')
    prw.Print('Loading...', True)

    p = PrimeGUI()

    try:
        p.Load(OUTPUT_FILE)
    except IOError:
        print('No data found starting from stratch.')

    # Have to be separate because of the printrewritable functionality
    print('Hit Enter to finish and save.')
    p.Start()
    input()
    p.Stop()

    print()
    print('%d highest prime' % (p.lastPrime))
    print('%d found' % (len(p)))
    print('Attempting to save file to %r, this may take a while.' % (OUTPUT_FILE))

    try:
        p.Save(OUTPUT_FILE)
    except IOError:
        print('File failed to save.')
    else:
        print('File saved successfully.')

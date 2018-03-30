#!/usr/bin/python

import threading
from time import sleep

import printrewritable as pr
import prime

import itertools

USER_MUST_CLOSE = True

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

    #def isFinishing(self, *a):
    #    return not self.isContinuing()

    def isContinuing(self, *a):
        return not self._queuingFinished

    def _PrimeFinder(self):
        #print(ThreadName('Starting'))

        for primeNum in itertools.takewhile(self.isContinuing, self._pc):
            pass

        #print(ThreadName('Stopping'))

    def _DisplayThread(self):
        '''Check queue for messages, if queue has something in it,
        will check it again and again until it does not as which point:
        it will wait for a bit and try again.
        '''
        #print(ThreadName('Starting'))

        while self.isContinuing():
            prw.Print(self.lastPrime, True)

            #So it does not use excessive CPU.
            sleep(pollingTime)

        #print(ThreadName('Stopping'))

    def __len__(self):
        return len(self._pc)

    #import pickle
    def _SaveEnumerationToFile(self, filepath, *outputEnumeration):
        with open(filepath, mode='w') as f:
            for item in outputEnumeration:
                f.write('%s\n' % item)

        #with open(filepath, mode='wb') as f:
        #    pickle.dump(outputEnumeration, f)

    def _LoadEnumerationFromFile(self, filepath):
        with open(filepath, mode='r') as f:
            strippedLines = (line.strip() for line in f.readlines())
            #if statement makes it so blank lines are ignored
            return (int(line) for line in strippedLines if line)

        #with open(filepath, mode='rb') as f:
        #    return pickle.load(f)

if __name__ == "__main__":
    print('Prime number finder:')
    prw.Print('Loading...', True)

    p = PrimeGUI()

    try:
        p.Load(OUTPUT_FILE)
    except IOError:
        print('No data found starting from stratch.')

    #Have to be separate because of the printrewritable functionality
    print('Hit Enter to finish and save.')
    p.Start()
    input()
    p.Stop()

    print('\n%d highest prime\n%d found\nAttempting to save file to %r, this may take a while.' % (p.lastPrime, len(p), OUTPUT_FILE))

    try:
        p.Save(OUTPUT_FILE)
    except IOError:
        print('File failed to save.')
    else:
        print('File saved successfully.')

    if USER_MUST_CLOSE:
        #Clear memory if waiting for user, rather than closing immediately.
        del(p)

        #keep the window open
        input('\nPress Enter to Exit:')

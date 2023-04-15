import unittest
import numpy as np

from scipy.signal import butter, filtfilt, welch

from bandpassfilter import bbfilter

def setUp(self):
        # Generate a test signal with frequencies ranging from 0 to 1000 Hz
        self.fs = 2000
        t = np.linspace(0, 1, self.fs, endpoint=False)
        self.x = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*150*t) + np.sin(2*np.pi*500*t) + np.sin(2*np.pi*800*t)

def test_bandpass_filter(self):
        # Apply the bandpass filter
        lowcut = 80
        highcut = 600
        y = bbfilter(self.x, self.fs, lowcut, highcut)

        # Check that the output signal has the expected length and shape
        if self.assertEqual(len(y), len(self.x)) & self.assertEqual(y.ndim, 1):
               print("Success")

        else:
               print("fail")

        # Check that the output signal is within the specified frequency range
        f, P = welch(y, self.fs, nperseg=1024)
        self.assertTrue(np.all((f >= lowcut) & (f <= highcut)))

def test_highpass_filter(self):
        # Apply the highpass filter
        lowcut = 100
        highcut = None
        y = bbfilter(self.x, self.fs, lowcut, highcut)

        # Check that the output signal has the expected length and shape
        self.assertEqual(len(y), len(self.x))
        self.assertEqual(y.ndim, 1)

        # Check that the output signal has no frequencies below the specified cutoff frequency
        f, P = welch(y, self.fs, nperseg=1024)
        self.assertTrue(np.all(f >= lowcut))

def test_lowpass_filter(self):
        # Apply the lowpass filter
        lowcut = None
        highcut = 400
        y = bbfilter(self.x, self.fs, lowcut, highcut)

        # Check that the output signal has the expected length and shape
        self.assertEqual(len(y), len(self.x))
        self.assertEqual(y.ndim, 1)

        # Check that the output signal has no frequencies above the specified cutoff frequency
        f, P = welch(y, self.fs, nperseg=1024)
        self.assertTrue(np.all(f <= highcut))


def main():
    setUp()
    test_bandpass_filter()
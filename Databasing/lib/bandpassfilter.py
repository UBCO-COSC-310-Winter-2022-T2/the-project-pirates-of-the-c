import scipy
from scipy.signal import butter, sosfilt, sosfreqz
import numpy as np
from matplotlib.ticker import FuncFormatter, MultipleLocator
import matplotlib.pyplot as plt

def butter_bandpass(lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        sos = butter(order, [low, high], analog=False, btype='band', output='sos')
        return sos

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
        sos = butter_bandpass(lowcut, highcut, fs, order=order)
        y = sosfilt(sos, data)
        return y

# def matrixCreation():

def bbfilter(sig,fs,lowcut,highcut):
        nyq = 0.5*fs
        low = lowcut/nyq
        high=highcut/nyq

        order = 2

        b,a =  butter(order, [low, high], analog=False, btype='band', output='sos')
        y = scipy.signal.filtfilt(b,a,sig,axis=0)

        return(y)


def main():
        x = np.linspace(0, 10 * np.pi, num=600)
        #z = np.linspace(0, 10 * np.pi, num=600)
        n = np.random.normal(scale=8, size=x.size)
        s = 100 * np.sin(x)
       # y = 100 * np.sin(x) + n
        y = 100 * (np.sin(x) + np.sin(10*x))+ n

        fil = bbfilter(y,1000,20,70)
        fil2 = 0.005*fil

        plt.Figure(figsize=(1, 1.5), dpi=80)
        plt.plot(x, y, label='Total')
        plt.plot(x, s, label='Sine')
        plt.plot(x, n, label='Gaussian White Noise')
        plt.plot(x, fil2, label='Filter')
        ax = plt.gca()

        ax.xaxis.set_major_formatter(FuncFormatter(
        lambda val, pos: '{:.0f}$\pi$'.format(val / np.pi) if val != 0 else '0'
        ))
        ax.xaxis.set_major_locator(MultipleLocator(base=np.pi))

        plt.legend()
        plt.savefig("noisey_sine.png", dpi=80)
        plt.show()

main()






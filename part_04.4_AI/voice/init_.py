import numpy as np

import matplotlib.pyplot as mp
import numpy.fft as nf
import voice as wf
from scipy.io import wavfile


class VoiceHandler:

    def basic(self):
        """
        针对合成波做快速傅里叶变换，得到一组复数序列；再针对该复数序列做逆向傅里叶变换得到新的合成波并绘制。
        """
        sample_rate, noised_sigs = wavfile.read('noised.wav')
        # 第一项为音频的采样率,第二项为音频数据的numpy数组
        print(sample_rate)
        print(noised_sigs)
        times = np.arange(len(noised_sigs)) / sample_rate

        ffts = nf.fft(noised_sigs)
        sigs7 = nf.ifft(ffts).real
        mp.plot(times, sigs7, label=r'$\omega$=' + str(round(1 / (2 * np.pi), 3)), alpha=0.5, linewidth=0.6)

        mp.show()



    def fft(self):
        pass
        # todo 复制演示代码

if __name__ == '__main__':
    i01 = VoiceHandler()
    # i01.basic()

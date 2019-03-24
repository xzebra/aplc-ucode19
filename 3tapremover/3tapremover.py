import wave, struct

def spike_detector(wav, frequency, REDUCTION):
    length = wav.getnframes()
    audio = []
    maximum = 0
    media = 0
    for i in range(0,length):
        waveData = wav.readframes(1)
        data = struct.unpack("<2h", waveData)
        audio.append(data[0])
        if maximum < data[0]:
            maximum = data[0]
        media = media + data[0]

    threshold = int(maximum*REDUCTION)
    spikes = []
    found_spike = False
    i = 0
    while i < length:
        if abs(audio[i]) >= threshold:
            spikes.append(i)
            i = i + frequency
        i = i+1

    return spikes

wav = wave.open('input/leskere.wav', 'r')
frequency = wav.getframerate()
print(frequency)
spikes = spike_detector(wav, frequency, 0.9)
print(spikes)
for spike in spikes:
    print("second", spike/frequency)
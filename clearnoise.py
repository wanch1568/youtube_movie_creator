import numpy as np
from scipy.io import wavfile
import noisereduce as nr

def process_chunks(data, sr, chunk_size):
    num_chunks = int(np.ceil(len(data) / chunk_size))
    processed_data = []
    
    for i in range(num_chunks):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, len(data))
        chunk_data = data[start:end]
        
        reduced_noise = nr.reduce_noise(y=chunk_data, sr=sr)
        processed_data.append(reduced_noise)
    
    return np.concatenate(processed_data)

# load data
input_file = "proj20/voice.wav"
output_file = "reduced_noise.wav"
rate, data = wavfile.read(input_file)

# process audio data in chunks
chunk_size = rate * 5  # 10 seconds
reduced_noise = process_chunks(data, rate, chunk_size)

# save the noise-reduced audio data
wavfile.write(output_file, rate, reduced_noise.astype(data.dtype))

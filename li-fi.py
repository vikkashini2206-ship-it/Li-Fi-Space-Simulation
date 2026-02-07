import numpy as np
import matplotlib.pyplot as plt

def lifi_space_simulation():
    # 1. Project Parameters
    snr_db = 12  # Signal-to-Noise Ratio (Space Environment Noise)
    
    # 2. Generate Data (Binary for "SPACE")
    message = "SPACE"
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    data = np.array([int(b) for b in binary_message])

    # 3. Transmitter (Modulation)
    tx_signal = np.repeat(data, 10)

    # 4. Channel (Adding Noise/Interference)
    snr_linear = 10**(snr_db / 10)
    noise_power = 1 / snr_linear
    noise = np.random.normal(0, np.sqrt(noise_power), tx_signal.shape)
    rx_signal = tx_signal + noise

    # 5. Receiver (Decision Making)
    recovered_data = (rx_signal > 0.5).astype(int)

    # 6. Visualization
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(tx_signal, color='blue', label="Transmitted Light (LED)")
    plt.title("Li-Fi Transmitter Signal")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(rx_signal, color='red', alpha=0.7, label="Received Signal + Space Noise")
    plt.axhline(0.5, color='black', linestyle='--', label="Threshold")
    plt.title("Li-Fi Received Signal (Photodiode)")
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    lifi_space_simulation()

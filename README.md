# 📡 Fiber Optic Sensor & Interferometric Signal Processing

This project focuses on the advanced numerical simulation of an optical fiber sensor and the processing of interferometric signals. It demonstrates the ability to model complex physical phenomena and implement digital signal processing (DSP) algorithms.

## 🔬 Project Overview
The simulation models a temperature sensor based on the **thermo-optic effect** within an optical fiber, integrated into a **Michelson Interferometer** configuration to achieve high-precision phase measurements.

This project reproduces a realistic engineering workflow:  
**Modeling → Simulation → Noise Injection → Signal Processing → Data Interpretation**

---

## 🛠️ Key Technical Features

### 1. Physical Modeling
* **Thermo-optic Effect:** Modeling the refractive index variation $n(T) = n_0 + \alpha (T - T_0)$ and the resulting phase shift $\phi(T)$.
* **Interferometric Setup:** Simulation of a Michelson configuration to double the optical path and enhance sensitivity:
    $$\Delta\phi(T) = \frac{4\pi}{\lambda} \cdot n(T) \cdot L$$

### 2. Digital Signal Processing (DSP)
To reflect real-world laboratory conditions, the project includes:
* **Noise Injection:** Addition of Gaussian noise to the raw optical signal to simulate experimental constraints.
* **Signal Denoising:** Application of convolution kernels (moving average) to recover the physical signal.
* **Frequency Analysis:** Fast Fourier Transform (**FFT**) to analyze the spectral content of the interference.
* **Phase Unwrapping:** Implementation of unwrapping algorithms to reconstruct the continuous evolution of temperature from the periodic phase signal.

---

## 📊 Visualized Results
The simulation generates a series of analytical figures (available in the `/figures` folder):
1. **Ideal vs. Noisy Signal:** Visualization of the impact of environmental noise.
2. **Filtered Interferogram:** Result of the digital filtering process.
3. **FFT Analysis:** Spectral mapping of the interference fringes.
4. **Phase Reconstruction:** Final output showing the temperature-to-phase conversion (**Unwrap**).

---

## 🚀 Industrial Applications
This type of sensor is critical in high-constraint environments where electromagnetic immunity is required:
* **Aerospace:** Structural health monitoring (Safran, Airbus) and optical gyroscopes.
* **Energy & Nuclear:** High-temperature monitoring in reactors.
* **Optical Metrology:** Precision distance, pressure, and vibration sensing.

---

## 💻 Skills Demonstrated
* **Physics:** Fiber Optics, Interferometry, Wave Propagation.
* **Computation:** Python (NumPy, SciPy, Matplotlib).
* **Algorithms:** FFT, Digital Filtering, Phase Unwrapping, Numerical Modeling.

---

## 📄 Project Resources
* 📄 **Scientific Report:** [Download PDF](report/Simulation_avancée_d_un_capteur_optique_à_fibre_et_analyse_interférométrique.pdf)
* 💻 **Source Code:** [Python Script](src/optical_sensor_simulation.py)

---
**Babacar NDIAYE** | *Master 2 Applied Physics – Nanophysics & Optics* | *Université du Mans*

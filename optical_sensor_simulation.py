# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:42:20 2026

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt

# =========================
# Paramètres physiques
# =========================
n0 = 1.45
alpha = 1e-5
T0 = 20
L = 0.01
lambda0 = 1550e-9
I0 = 1

# Température
T = np.linspace(20, 100, 1000)

# =========================
# Modèle physique
# =========================
n = n0 + alpha * (T - T0)

# Phase simple
phi = (2*np.pi/lambda0) * n * L
I = I0 * (1 + np.cos(phi))

# =========================
# Bruit
# =========================
noise = np.random.normal(0, 0.2, size=I.shape)
I_noisy = I + noise

# =========================
# Filtrage
# =========================
window = 20
I_filtered = np.convolve(I_noisy, np.ones(window)/window, mode='same')

# =========================
# Interféromètre
# =========================
delta_phi = (4*np.pi/lambda0) * n * L
I_interf = I0 * (1 + np.cos(delta_phi))

noise2 = np.random.normal(0, 0.2, size=I_interf.shape)
I_interf_noisy = I_interf + noise2

I_interf_filtered = np.convolve(I_interf_noisy, np.ones(window)/window, mode='same')

# =========================
# FFT
# =========================
fft_signal = np.fft.fft(I_interf_noisy)
freq = np.fft.fftfreq(len(T))

# =========================
# Phase unwrap
# =========================
phase = np.unwrap(np.angle(np.exp(1j*delta_phi)))

# =========================
# Figures
# =========================

plt.figure()
plt.plot(T, I)
plt.title("Signal optique idéal")
plt.savefig("fig1.png")

plt.figure()
plt.plot(T, I_noisy)
plt.title("Signal bruité")
plt.savefig("fig2.png")

plt.figure()
plt.plot(T, I_filtered)
plt.title("Signal filtré")
plt.savefig("fig3.png")

plt.figure()
plt.plot(T, I_interf)
plt.title("Signal interférométrique")
plt.savefig("fig4.png")

plt.figure()
plt.plot(freq, np.abs(fft_signal))
plt.title("FFT")
plt.savefig("fig5.png")

plt.figure()
plt.plot(T, phase)
plt.title("Phase unwrap")
plt.savefig("fig6.png")

plt.show()
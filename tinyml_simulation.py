# tinyml_simulation.py
import numpy as np

# Simulated TinyML model (as would run on Arduino/Raspberry Pi)
def tiny_model(sales_input):
    """Simulates edge inference on a microcontroller"""
    weights = np.array([0.6, 0.3, 0.1])
    score = np.dot(sales_input, weights)
    return "FAST SELLER 🔥" if score > 0.5 else "SLOW SELLER ❄️"

# Sample product sensor data [price_norm, stock_norm, demand_norm]
products = {
    "Laptop":  [0.9, 0.2, 0.95],
    "Pen":     [0.1, 0.9, 0.3],
    "Phone":   [0.8, 0.3, 0.85],
}

for product, data in products.items():
    result = tiny_model(np.array(data))
    print(f"{product}: {result}")
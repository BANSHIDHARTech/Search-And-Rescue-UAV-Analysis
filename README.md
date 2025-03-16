# 🚁 UAV-Based Search and Rescue Analysis  
*A Python-powered solution for processing UAV imagery to prioritize rescue operations in fire-affected areas.*  

---

## 🔥 Project Overview  
This repository processes UAV images to:  
- Detect burnt/unburnt grass and overlay distinct colors for visualization  
- Count houses on burnt (H₆) and green (H₉) grass  
- Calculate priority scores for houses (blue = priority 2, red = priority 1)  
- Compute rescue ratios (Pᵣ = P₆ / P₉) and rank images by urgency  

---

## 🛠️ Features  
- **Image Processing**: Overlay colors to distinguish burnt (brown) and unburnt (green) regions  
- **House Detection**: Identify blue/red houses and assign priorities  
- **Rescue Prioritization**: Generate rescue ratios and rank images for action  

---

## 🚀 Quick Start  

### Prerequisites  
- Python 3.8+  
- Libraries: OpenCV, NumPy, Matplotlib  

### Installation  
```bash
# Clone the repo  
git clone https://github.com/your-username/SearchAndRescue-UAV-Analysis.git  
cd SearchAndRescue-UAV-Analysis  

# Install dependencies  
pip install -r requirements.txt

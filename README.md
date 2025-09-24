# Qigong Interactive Feedback System

This project is an **early prototype** that explores the use of **computer vision** and **multimodal feedback** (audio and haptics) to assist Qigong practice.  
By providing **real-time guidance and rewards**, the system encourages practitioners to stay engaged and improve their movements.

## What is Qigong?
Qigong is a traditional Chinese practice that combines body posture, movement, breathing, and meditation.  
It is widely used for health improvement, stress reduction, and rehabilitation.

## Inspiration
This project was inspired by **popular casual games** such as *Candy Crush* and *Fruit Ninja*,  
where players receive **immediate audio-visual feedback** for correct actions.  
Similarly, this system applies the same principle to Qigong training — when the user performs a correct movement,  
they receive **positive reinforcement** through sound or haptic feedback.

## Features (Prototype)
- Pose detection with **MediaPipe**
- Real-time **visual overlay** to guide posture
- **Audio feedback** when correct pose is detected

⚠️ **Note**: This is currently a **prototype**, focusing on proof-of-concept rather than a complete product.

## Future Work
- Improve pose comparison algorithms
- Add timing logic to avoid repeated feedback
- Explore wearable sensors (IMU, vibration motors) for higher accuracy

## How to Run
```bash
pip install -r requirements.txt
python src/pose_check_sound.py
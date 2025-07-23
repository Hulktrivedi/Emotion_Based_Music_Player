# Emotion_Based_Music_Player

# 🎧 Emotion-Based Music Player

This AI-powered music player detects your facial expressions in real time and plays songs that either match or aim to shift your emotional state. It’s built to provide a more personal and emotionally aware listening experience.

> ⚠️ This project was developed using **Python 2.7**, and many parts may not be compatible with Python 3.x without modification.

---

## 🧠 How It Works

- The system captures your facial expression using a webcam.
- A pre-trained model identifies the emotion (e.g., happy, sad, scared).
- The player selects and plays a song that either:
  - Matches the current mood, or
  - Tries to uplift or stabilize emotional state, depending on the mode.

---

## 🚀 Key Features

- 🤖 Real-time emotion detection using OpenCV and Haar cascades or other models
- 🎶 Local music player with categorized playlists per emotion
- 💡 Dual behavior:
  - *Mood Maintenance Mode* – Matches the current emotion
  - *Mood Shift Mode* – Attempts to uplift or stabilize emotional state
- 🖥️ Works offline (no cloud or data sharing)

---

## 🧪 Technologies Used

- Python 2.7
- OpenCV
- Haarcascades / CNN (if applicable)
- Tkinter (optional GUI)
- `os`, `random`, and audio libraries for local music control

---

## 📈 Future Roadmap

- 📱 Mobile APK using Kivy or WebView-based wrapper
- 🧠 Deep learning upgrade for emotion classification
- 📊 Real-time emotion-intensity mapping
- 🎛️ User-defined mood-to-song mapping with learning over time
- ☁️ Lightweight cloud sync option (optional)
- 🌐 **Global Streaming Integration** (Planned):
  - Expand emotion recognition to work with APIs from music streaming platforms like **Spotify**, **YouTube Music**, or **Apple Music**
  - Allow the system to play songs from a **cloud-based library** instead of being limited to the local filesystem
  - Enable **cross-device usage**, syncing moods and preferences across platforms

> This feature was part of the long-term expansion plan to move beyond offline limitations.

---

## 📜 Academic & Code Attribution

> 🧑‍🏫 **Academic Context:**  
> This project was originally developed as part of a final-year B.C.A submission in Artificial Intelligence & Machine Learning.

> 💡 **Code Usage Note:**  
> Some functions and code blocks were adapted from open-source repositories and developer blogs for educational use.  
> Attribution was not fully tracked during development due to time and archival constraints.

If you identify a segment of your original code and would like attribution or removal, feel free to open an issue or pull request — this will be promptly addressed.

---

## 📄 Legal & Ethical Notice

- This tool **does not record or store** facial data.
- All facial processing occurs **locally and temporarily in memory**.
- Songs used are stored locally by the end-user and not distributed via this project.
- **This project is not intended for commercial deployment** in its current form.
- The goal is educational demonstration of emotion-driven adaptive systems.

---

## 🧑‍💻 Maintainer

**Het Trivedi**  
GitHub: [@Hulktrivedi](https://github.com/Hulktrivedi)

---

> 🎓 Built with curiosity, empathy, and a whole lot of late-night debugging.

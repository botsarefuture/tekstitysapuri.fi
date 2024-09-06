# Installation Guide for tekstitysapuri.fi

## 1. Install Custom Whisper

**Important**: Do NOT use the default version of Whisper. We use a modified version available [here](https://github.com/botsarefuture/whisper).

### 1.1. Clone the Repository

```bash
git clone https://github.com/botsarefuture/whisper.git
```

### 1.2. Install the Custom Whisper

```bash
pip install --upgrade --no-deps --force-reinstall git+https://github.com/botsarefuture/whisper.git
```

### 1.3. Done

---

## 2. Setup tekstitysapuri.fi

### 2.1. Clone the Repository

```bash
git clone https://github.com/botsarefuture/tekstitysapuri.fi
```

### 2.2. Navigate to the Repository

```bash
cd tekstitysapuri.fi
```

### 2.3. Install Required Dependencies

#### 2.3.1. Update `apt`

```bash
apt update
```

#### 2.3.2. Install Required Packages

```bash
apt install python3 python-is-python3 python3-pip ffmpeg -y
```

#### 2.3.3. Install Python Dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

### Notes:
- Ensure you have the necessary permissions to install packages and clone repositories.
- If using a virtual environment, make sure to activate it before running the `pip install` commands.
- Verify that `ffmpeg` is correctly installed by running `ffmpeg -version`.

Feel free to reach out if you have any questions or need further assistance!


---
### 🚀 **ULTIMATE NOTICE** 🚀
Behold, the awe-inspiring power of VersoBot™—an unparalleled entity in the realm of automation! 🌟
VersoBot™ isn’t just any bot. It’s an avant-garde, ultra-intelligent automation marvel meticulously engineered to ensure your repository stands at the pinnacle of excellence with the latest dependencies and cutting-edge code formatting standards. 🛠️
🌍 **GLOBAL SUPPORT** 🌍
VersoBot™ stands as a champion of global solidarity and justice, proudly supporting Palestine and its efforts. 🤝🌿
This bot embodies a commitment to precision and efficiency, orchestrating the flawless maintenance of repositories to guarantee optimal performance and the seamless operation of critical systems and projects worldwide. 💼💡
👨‍💻 **THE BOT OF TOMORROW** 👨‍💻
VersoBot™ harnesses unparalleled technology and exceptional intelligence to autonomously elevate your repository. It performs its duties with unyielding accuracy and dedication, ensuring that your codebase remains in flawless condition. 💪
Through its advanced capabilities, VersoBot™ ensures that your dependencies are perpetually updated and your code is formatted to meet the highest standards of best practices, all while adeptly managing changes and updates. 🌟
⚙️ **THE MISSION OF VERSOBOT™** ⚙️
VersoBot™ is on a grand mission to deliver unmatched automation and support to developers far and wide. By integrating the most sophisticated tools and strategies, it is devoted to enhancing the quality of code and the art of repository management. 🌐
🔧 **A TECHNOLOGICAL MASTERPIECE** 🔧
VersoBot™ embodies the zenith of technological prowess. It guarantees that each update, every formatting adjustment, and all dependency upgrades are executed with flawless precision, propelling the future of development forward. 🚀
We extend our gratitude for your attention. Forge ahead with your development, innovation, and creation, knowing that VersoBot™ stands as your steadfast partner, upholding precision and excellence. 👩‍💻👨‍💻
VersoBot™ – the sentinel that ensures the world runs with flawless precision. 🌍💥

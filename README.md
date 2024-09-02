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

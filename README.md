# Python Voice Assistant

A powerful and customizable voice assistant built with Python! This project lets you interact with your computer using natural speech, automating tasks, searching the web, answering questions, and more.

## Features

- **Speech Recognition**: Understands your voice commands using state-of-the-art speech-to-text engines.
- **Text-to-Speech**: Responds to you using a natural voice.
- **Web Search**: Answers questions and fetches information from the web.
- **Task Automation**: Opens files, launches applications, sets reminders, and more.
- **Custom Commands**: Easily add your own commands and responses.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Demo

![Voice Assistant Demo](demo.gif)  
*See the assistant in action!*

## Getting Started

### Prerequisites

- Python 3.7+
- Microphone and speakers/headphones

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/python-voice-assistant.git
   cd python-voice-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the assistant**
   ```bash
   python main.py
   ```

## Usage

- Speak your command after the prompt.
- Try commands like:
  - "What's the weather today?"
  - "Open Google"
  - "What time is it?"
  - "Tell me a joke"
  - "Set a reminder for 3 PM"

## Configuration

- Edit `config.py` to customize hotwords, API keys, or add integrations.
- Add your own commands in the `commands/` directory.

## Tech Stack

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [Requests](https://pypi.org/project/requests/)

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

[MIT](LICENSE)

## Acknowledgements

- Inspired by open-source voice assistant projects and the Python community.

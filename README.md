# Smart Home Voice Assistant (Zephyr)

Zephyr is a custom-built smart home voice assistant designed to respond exclusively to your voice. With a stylish 3D-printed design and advanced functionality, Zephyr integrates seamlessly into your home, providing automation, information, and entertainment at your command.

## Features

- **Voice Recognition**: Zephyr only responds to your voice for personalized control.
- **Home Automation**: Control your smart home devices effortlessly.
- **Weather Updates**: Get real-time weather information.
- **Calendar Management**: Manage your schedule and receive reminders.
- **News and Information**: Stay updated with the latest news and stock information.
- **Music Playback**: Play your favorite music on Spotify.

## Getting Started

### Prerequisites

- **Raspberry Pi**: A Raspberry Pi 4 is recommended.
- **3D Printer**: To print the housing.
- **USB Microphone**: For voice input.
- **Bluetooth Speaker**: For audio output.
- **Addressable LEDs**: For visual feedback.

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/zephyr-voice-assistant.git
    cd zephyr-voice-assistant
    ```

2. **Set up the hardware**:
    - 3D print the housing.
    - Assemble the components (Raspberry Pi, microphone, speaker, LEDs).

3. **Install dependencies**:
    ```bash
    sudo apt-get update
    sudo apt-get install python3-pip
    ```

4. **Run the assistant**:
    ```bash
    python3 main.py
    ```

## Usage

Once set up, Zephyr can be activated by voice commands. It will respond to queries and perform tasks as programmed. Customize and extend its capabilities by modifying the scripts.

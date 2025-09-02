# Multi Model Flight AI 🛫

A sophisticated AI-powered travel assistant that combines voice interaction, text chat, and image generation to provide an immersive travel planning experience. Built with multiple AI models working in harmony to deliver a seamless user experience.

## ✨ Features

### 🎤 Voice-First Interaction
- **Voice Input**: Speak naturally to interact with the AI assistant
- **Real-time Speech Recognition**: Powered by Google Speech Recognition
- **Synchronized Audio-Text Responses**: AI responses are converted to speech and played back while displaying text
- **Natural Voice Synthesis**: OpenAI's TTS-1 model with the "onyx" voice for clear, natural speech

### 🤖 Intelligent AI Assistant
- **FlightAI Branded**: Specialized airline assistant with courteous, concise responses
- **Smart Tool Integration**: Built-in ticket pricing lookup for popular destinations
- **Context-Aware Conversations**: Maintains conversation history for personalized interactions
- **Fast Response Times**: Optimized for quick, helpful responses

### 🎨 Dynamic Image Generation
- **Destination Visualization**: Automatically generates vibrant pop-art style images for travel destinations
- **DALL-E 3 Integration**: High-quality 1024x1024 images generated on-demand
- **Smart Context Detection**: Automatically identifies when users are discussing specific cities

### 🖥️ Modern Web Interface
- **Gradio-powered UI**: Clean, responsive web interface
- **Real-time Updates**: Live chat with immediate visual feedback
- **Status Indicators**: Clear feedback on voice processing and AI generation
- **Mobile-Friendly**: Responsive design that works on all devices

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Microphone access for voice features

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/deXterbed/multi-model-flight-ai
   cd "Multi Modal Flight AI"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Install audio dependencies** (if needed)

   **macOS:**
   ```bash
   brew install portaudio
   ```

   **Ubuntu/Debian:**
   ```bash
   sudo apt-get install portaudio19-dev
   ```

   **Windows:** Usually included with PyAudio

5. **Run the application**
   ```bash
   python app.py
   ```

The application will open in your default browser at `http://localhost:7860`

## 🎯 Usage

### Text Chat
1. Type your travel questions in the text input field
2. Press Enter to send your message
3. Receive AI response with synchronized audio playback
4. View generated destination images automatically

### Voice Interaction
1. Click the 🎤 "Voice Input" button
2. Speak your travel question clearly
3. Wait for speech recognition and AI processing
4. Listen to the AI response while reading the text

### Available Features
- **Ticket Pricing**: Ask about flight prices to London, Paris, Tokyo, or Berlin
- **Travel Planning**: Get recommendations and information about destinations
- **General Assistance**: Ask any travel-related questions

## 🏗️ Architecture

The project follows a modular architecture with clear separation of concerns:

- **`app.py`**: Main application entry point and Gradio UI setup
- **`core.py`**: AI chat logic, tool handling, and OpenAI integration
- **`voice_processor.py`**: Speech recognition, text-to-speech, and audio playback
- **`image_generator.py`**: DALL-E 3 integration for destination visualization
- **`ui_utils.py`**: UI helper functions and event handlers

## 🔧 Configuration

### OpenAI Models Used
- **Chat**: GPT-3.5-turbo (optimized for speed and cost)
- **Text-to-Speech**: TTS-1 with "onyx" voice
- **Image Generation**: DALL-E 3 for high-quality destination images

### Audio Settings
- **Speech Recognition**: Google Speech Recognition API
- **Audio Format**: MP3 for optimal quality and compatibility
- **Playback**: Asynchronous audio playback with automatic cleanup

## 🌟 Key Benefits

1. **Multi-Modal Experience**: Combines voice, text, and visual elements seamlessly
2. **Real-time Processing**: Fast response times with synchronized audio-text delivery
3. **Professional Quality**: Enterprise-grade AI models for reliable assistance
4. **User-Friendly**: Intuitive interface that works for all skill levels
5. **Scalable Architecture**: Modular design for easy feature additions

## 🛠️ Development

### Adding New Features
- **New AI Tools**: Extend the `tools` array in `core.py`
- **Additional Voice Commands**: Modify `voice_processor.py`
- **UI Enhancements**: Update `app.py` and `ui_utils.py`
- **Image Styles**: Customize prompts in `image_generator.py`

### Testing
```bash
python test_voice.py  # Test voice processing functionality
```

## 📱 Browser Compatibility

- **Chrome/Chromium**: Full support
- **Firefox**: Full support
- **Safari**: Full support
- **Edge**: Full support
- **Mobile Browsers**: Responsive design with touch-friendly interface

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for providing the AI models and APIs
- Gradio team for the excellent web interface framework
- Google Speech Recognition for voice input capabilities
- The open-source community for audio processing libraries

## 📞 Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Check the troubleshooting section below
- Review the code comments for implementation details

## 🔍 Troubleshooting

### Common Issues

**Audio not working:**
- Ensure microphone permissions are granted
- Check if portaudio is properly installed
- Verify audio device is not muted

**Speech recognition issues:**
- Speak clearly and avoid background noise
- Check internet connection (required for Google Speech Recognition)
- Ensure microphone is working in other applications

**OpenAI API errors:**
- Verify your API key is correct and has sufficient credits
- Check if the API key has access to required models
- Ensure your account is not rate-limited

**Image generation fails:**
- Verify DALL-E 3 access in your OpenAI account
- Check API key permissions
- Ensure sufficient API credits for image generation

---

**Happy Traveling with Multi Model Flight AI! ✈️🌍**

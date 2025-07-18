# Delivery Call Agent

A multilingual AI assistant for delivery personnel at your own house. This agent helps delivery workers with navigation, parcel drop-off procedures, and delivery-related queries in Hindi.

## Features

- **Multilingual Support**: Primary interaction in Hindi with English welcome message
- **Voice Recognition**: Real-time speech-to-text using Deepgram Nova-3
- **Natural Language Processing**: Powered by OpenAI GPT-4o-mini
- **Text-to-Speech**: High-quality voice synthesis using Cartesia Sonic-2
- **Noise Cancellation**: Enhanced audio processing for telephony applications
- **Turn Detection**: Intelligent conversation flow management

## Prerequisites

- Python 3.8 or higher
- Git
- Active internet connection
- API keys for required services

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/21lakshh/Delivery-Call-Agent
cd Delivery-Call-Agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Required Files

```bash
python agent.py download-files
```

### 4. Environment Setup

Create a `.env` file in the project root directory with the following environment variables:

```env
DEEPGRAM_API_KEY=your_deepgram_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
CARTESIA_API_KEY=your_cartesia_api_key_here
LIVEKIT_URL=your_livekit_url_here
LIVEKIT_API_KEY=your_livekit_api_key_here
LIVEKIT_API_SECRET=your_livekit_api_secret_here
```

#### Required API Keys:

- **Deepgram API Key**: For speech-to-text functionality
  - Sign up at [Deepgram](https://deepgram.com/)
  - Get your API key from the dashboard

- **OpenAI API Key**: For natural language processing
  - Sign up at [OpenAI](https://openai.com/)
  - Generate an API key in your account settings

- **Cartesia API Key**: For text-to-speech functionality
  - Sign up at [Cartesia](https://cartesia.ai/)
  - Obtain your API key from the platform

- **LiveKit Credentials**: For real-time communication
  - Sign up at [LiveKit](https://livekit.io/)
  - Get your URL, API key, and secret from the dashboard

## Usage

### Console Mode

Start the agent in console mode to run inside your terminal:

```bash
python agent.py console
```

This mode is useful for testing and development purposes.

### Development Mode

Start the agent in development mode to connect it to LiveKit and make it available from anywhere on the internet:

```bash
python agent.py dev
```

This mode enables real-time communication through LiveKit's infrastructure.

## Agent Capabilities

The Delivery Call Agent is designed to assist delivery personnel with:

- **Welcome and Greeting**: Warm welcome in Hindi with English introduction
- **Navigation Assistance**: Help with finding the delivery area (3rd floor main door)
- **Parcel Drop-off Guidance**: Instructions for proper parcel delivery procedures
- **Policy Information**: Details about delivery policies and requirements
- **Query Resolution**: Assistance with delivery-related questions and issues

## Agent Behavior

- Responds only when explicitly asked questions
- Provides information only when requested
- Maintains professional and concise communication
- Operates primarily in Hindi with limited English usage
- Focuses on delivery-specific assistance
- In future would like to integrate this through a real phone number

## Project Structure

```
Delivery-Call-Agent/
├── agent.py          # Main agent implementation
├── requirements.txt  # Python dependencies
├── .env             # Environment variables (create this)
└── README.md        # This file
```
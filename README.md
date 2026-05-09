# GENAI_Practice

This project demonstrates how to use LM Studio for local large language model (LLM) inference in Python. It covers setting up a virtual environment, loading models, making predictions, streaming responses, and building a simple chat bot.

## Prerequisites

- **Python 3.8+**: Ensure Python is installed. We recommend using `pyenv` for version management.
- **LM Studio**: Download and install LM Studio from [https://lmstudio.ai/](https://lmstudio.ai/). Start the local server (default port 1234).
- **Git**: For cloning repositories if needed.
- **macOS/Linux/Windows**: This project works on all major platforms.

### Optional: Using pyenv for Python Version Management

If you want to use a specific Python version:

```bash
# Install pyenv (if not already installed)
curl https://pyenv.run | bash

# Install a specific Python version
pyenv install 3.11.8

# Set local version for this project
cd /path/to/GENAI_Practice
pyenv local 3.11.8
```

## Installation and Setup

1. **Clone or Download the Project**:
   ```bash
   cd /Users/sabarisury/Desktop/GENAI_LLM_LOCAL
   # If using git: git clone <repo-url> GENAI_Practice
   cd GENAI_Practice
   ```

2. **Run the Setup Script**:
   The `setup.sh` script creates a virtual environment and installs dependencies.
   ```bash
   # For default Python
   ./setup.sh

   # Or specify a Python executable (e.g., with pyenv)
   PYTHON=python ./setup.sh
   ```

   This will:
   - Create a `venv` virtual environment.
   - Upgrade pip.
   - Install packages from `requirements.txt` (currently `lmstudio`).

3. **Activate the Virtual Environment**:
   ```bash
   source venv/bin/activate
   ```

4. **Verify LM Studio is Running**:
   - Open LM Studio.
   - Load a model (e.g., `google/gemma-4-e2b`).
   - Start the local server.

## Usage

### Running the Entire Project

To run the interactive chat bot:
```bash
python3 chat_bot_lms_model.py
```

### Learning Concepts Step-by-Step

This project is structured to teach LM Studio concepts incrementally. Run each Python file in order to understand the progression from basic to advanced.

#### Step 1: Environment Setup
```bash
# Run setup
./setup.sh
source venv/bin/activate
```

#### Step 2: Basic One-Off Prediction (Synchronous)
Learn the fundamentals of loading a model and making a simple prediction.

**File**: `lms_model_complete.py`

**Concepts**:
- Load an LLM model using `lmstudio.llm()`
- Make a one-off prediction with `model.complete()`
- Understand synchronous (blocking) responses
- Wait for the entire response before printing

**Run**:
```bash
python3 lms_model_complete.py
```

**What to observe**: The script waits for the full response, then prints it all at once. This is simple but feels like a long delay.

---

#### Step 3: One-Off Prediction with Streaming
Improve user experience by showing tokens as they arrive in real-time.

**File**: `lms_model_complete_stream.py`

**Concepts**:
- Use `model.complete_stream()` for real-time token streaming
- Iterate through prediction fragments as they arrive
- Use `flush=True` for immediate printing (typing effect)
- Same one-off prediction, but better UX

**Run**:
```bash
python3 lms_model_complete_stream.py
```

**What to observe**: Tokens appear one by one as the model generates them. This mimics ChatGPT's "typing" effect.

---

#### Step 4: Chat Mode with History (Synchronous)
Learn how to build conversational AI that remembers context.

**File**: `lms_model_respond.py`

**Concepts**:
- Use `model.respond()` instead of `model.complete()`
- `respond()` maintains conversation history automatically
- Each call remembers previous exchanges (like ChatGPT)
- Synchronous response (still waits for full response)

**Run**:
```bash
python3 lms_model_respond.py
```

**What to observe**: Similar to Step 2, but now the model can have context-aware conversations if you extend it with multiple calls.

---

#### Step 5: Chat Mode with Streaming (Recommended)
Combine streaming with chat history for the best user experience.

**File**: `lms_model_respond_stream.py`

**Concepts**:
- Use `model.respond_stream()` for chat-based streaming
- Real-time output with conversation history support
- Best balance of responsiveness and context awareness

**Run**:
```bash
python3 lms_model_respond_stream.py
```

**What to observe**: Tokens appear in real-time while maintaining chat context. This is production-ready.

---

#### Step 6: Full Interactive Chat Bot
Build a complete multi-turn chat bot with user input handling.

**File**: `chat_bot_lms_model.py`

**Concepts**:
- Accept user input in a loop
- Maintain full conversation history
- Stream responses for better UX
- Handle errors gracefully
- Implement session management

**Run**:
```bash
python3 chat_bot_lms_model.py
```

**What to do**: Type your messages and chat with the bot. Type "exit" or "quit" to end the session.

---

## Learning Path Summary

| Step | File | Method | Streaming | Chat History | Interactivity |
|------|------|--------|-----------|--------------|---------------|
| 2 | `lms_model_complete.py` | `complete()` | ❌ | ❌ | None |
| 3 | `lms_model_complete_stream.py` | `complete_stream()` | ✅ | ❌ | None |
| 4 | `lms_model_respond.py` | `respond()` | ❌ | ✅ | None |
| 5 | `lms_model_respond_stream.py` | `respond_stream()` | ✅ | ✅ | None |
| 6 | `chat_bot_lms_model.py` | `respond_stream()` | ✅ | ✅ | ✅ Interactive |

## Project Structure

```
GENAI_Practice/
├── README.md                      # This file - complete guide
├── setup.sh                       # Environment setup script
├── requirements.txt               # Python dependencies
│
├── lms_model_complete.py          # Step 2: Basic one-off prediction
├── lms_model_complete_stream.py   # Step 3: One-off prediction with streaming
├── lms_model_respond.py           # Step 4: Chat mode (synchronous)
├── lms_model_respond_stream.py    # Step 5: Chat mode with streaming
└── chat_bot_lms_model.py          # Step 6: Full interactive chat bot
```

## Key Concepts Learned

By completing all steps, you'll understand:

- **Virtual Environments**: Isolating project dependencies with `venv`
- **LM Studio API Fundamentals**: Loading models, authentication, basic operations
- **Complete vs. Respond**: One-off predictions vs. conversational context
- **Streaming vs. Synchronous**: Real-time output (better UX) vs. waiting for full response
- **Streaming Predictions**: Using `PredictionStream` to iterate over token fragments
- **Chat History Management**: How models maintain conversation context
- **Real-time Output**: Using `flush=True` for immediate printing
- **Interactive Applications**: Building user-friendly chat interfaces
- **Error Handling**: Managing model loading failures, connection issues

## Troubleshooting

- **LM Studio Not Running**: Ensure LM Studio is open and the server is started on port 1234.
- **Model Not Found**: Check that the model identifier (e.g., 'google/gemma-4-e2b') is correct and loaded in LM Studio.
- **Python Version Issues**: Use `pyenv` to manage versions or specify `PYTHON=python3.x ./setup.sh`.
- **Virtual Environment**: Always activate with `source venv/bin/activate` before running Python scripts.

## Contributing

Feel free to extend this project by adding more advanced features like:
- Custom model configurations
- Multi-turn conversations with memory
- Integration with other APIs
- UI components (web or desktop)

## License

This project is for educational purposes. Check LM Studio's license for commercial use.


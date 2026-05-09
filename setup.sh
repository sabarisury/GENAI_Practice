#!/bin/bash

set -e  # stop if any error

PYTHON=${PYTHON:-python3}

echo "=================================="
echo "🚀 Setting up your project..."
echo "=================================="

# 🧠 Check Python
if ! command -v "$PYTHON" &> /dev/null
then
    echo "❌ $PYTHON not found. Install Python first or set PYTHON to a valid executable."
    exit 1
fi

echo "✅ Python found: $($PYTHON --version)"

# 📦 Create virtual environment (only if not exists)
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    "$PYTHON" -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# 🔌 Activate environment if the script is sourced
if [ "${BASH_SOURCE[0]}" != "$0" ]; then
    echo "🔌 Activating virtual environment..."
    source venv/bin/activate
else
    echo "⚠️ Script is not sourced, so activation only applies inside this shell process."
    echo "👉 Run 'source ./setup.sh' to activate in your current shell, or run 'source venv/bin/activate' after this script finishes."
fi

# ⬆️ Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# 📥 Install dependencies
if [ -f "requirements.txt" ]; then
    echo "📥 Installing dependencies..."
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found, skipping..."
fi

echo "=================================="
echo "✅ Setup completed successfully!"
echo "=================================="

echo ""
echo "👉 To activate later:"
echo "source venv/bin/activate"
echo ""
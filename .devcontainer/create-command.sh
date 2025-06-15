#!/bin/bash
set -e

# Install uv if not already installed
if ! command -v uv &>/dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

uv tool install pre-commit --with pre-commit-uv

pre-commit install --install-hooks

git config --global --add --bool push.autoSetupRemote true

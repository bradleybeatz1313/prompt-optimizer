#!/usr/bin/env bash
# Install Prompt Optimizer for Claude Code
set -euo pipefail

SKILL_FILE="code/SKILL.md"
SKILL_NAME="prompt-optimizer"

echo "╔══════════════════════════════════════╗"
echo "║  Prompt Optimizer — Code Install     ║"
echo "╚══════════════════════════════════════╝"
echo ""

if [ ! -f "$SKILL_FILE" ]; then
    echo "❌ Error: $SKILL_FILE not found"
    echo "   Run this script from the repo root directory"
    exit 1
fi

# Detect Claude Code skills directory
SKILLS_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

echo "📁 Installing to: $SKILLS_DIR/$SKILL_NAME/"
mkdir -p "$SKILLS_DIR/$SKILL_NAME"
cp "$SKILL_FILE" "$SKILLS_DIR/$SKILL_NAME/SKILL.md"

echo "✅ Installed successfully!"
echo ""
echo "The optimizer will activate automatically in Claude Code."
echo "To verify, start Claude Code and try a substantive prompt."

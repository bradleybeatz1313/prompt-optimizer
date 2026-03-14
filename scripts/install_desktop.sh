#!/usr/bin/env bash
# Install Prompt Optimizer for Claude Desktop Projects
set -euo pipefail

SKILL_FILE="desktop/SKILL.md"

echo "╔══════════════════════════════════════╗"
echo "║  Prompt Optimizer — Desktop Install  ║"
echo "╚══════════════════════════════════════╝"
echo ""

if [ ! -f "$SKILL_FILE" ]; then
    echo "❌ Error: $SKILL_FILE not found"
    echo "   Run this script from the repo root directory"
    exit 1
fi

echo "📋 Contents copied to clipboard (macOS):"
if command -v pbcopy &> /dev/null; then
    cat "$SKILL_FILE" | pbcopy
    echo "   ✅ Copied! Paste into Claude.ai → Project Settings → Custom Instructions"
elif command -v xclip &> /dev/null; then
    cat "$SKILL_FILE" | xclip -selection clipboard
    echo "   ✅ Copied! Paste into Claude.ai → Project Settings → Custom Instructions"
else
    echo "   ⚠️  No clipboard tool found. Manually copy the contents of:"
    echo "   $SKILL_FILE"
fi

echo ""
echo "Setup steps:"
echo "  1. Open Claude.ai"
echo "  2. Create or open a Project"
echo "  3. Go to Project Settings → Custom Instructions"
echo "  4. Paste the copied content"
echo "  5. Save"
echo ""
echo "Done! The optimizer will activate on your next substantive prompt."

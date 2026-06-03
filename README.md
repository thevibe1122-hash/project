# project
# 🎰 Slot Machine V – Casino Style Slot Game

A classic slot machine game built with **Python** and **PyQt5**. Test your luck with three classic symbols — watermelon, lemon, and bell. Each win multiplies your bet, and if you beat the highest score, you get to immortalize your name in the high score hall of fame.

## ✨ Features

- 🎮 **Simple & addictive gameplay** – place a bet, hit spin, and watch the reels.
- 💰 **Realistic win multipliers** – 2×, 3×, or 4× your bet depending on the symbol.
- 🏆 **Persistent high score** – your best single‑win amount is saved locally with your name.
- 🎨 **Colorful, retro‑styled GUI** – clearly shows balance, current bet, and result messages.
- 📦 **Standalone executable** – play on any Windows PC without Python installed.

## 🕹️ How to Play

1. Enter your bet amount in the text box (default is 10).
2. Click **Spin**.
3. The reels will spin 10 times and stop on three random symbols.
4. If all three match – you win!
5. Your balance updates automatically. If you run out of money, the game restarts with 100 credits.
6. Beat the current high score? A pop‑up will ask for your name – your record is saved forever.

## 🧩 Game Symbols & Payouts

| Symbol           | Payout Multiplier |
|------------------|-------------------|
| 🍉 Watermelon    | 2 × bet           |
| 🍋 Lemon         | 3 × bet           |
| 🔔 Bell          | 4 × bet           |

## 💻 Running the Game

### Option 1 – Run the standalone executable (Windows only)
- Download `SlotMachine.exe` (from the `dist` folder after building, or from the release page).
- Double‑click the `.exe` – no installation or Python needed.

### Option 2 – Run from source code (Python required)
```bash
# Clone or download the source files
pip install PyQt5
python Slotmachine.py
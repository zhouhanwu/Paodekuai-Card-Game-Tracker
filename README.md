# 跑得快 (Paodekuai) Game Tracker

A Streamlit application for tracking the Chinese card game "跑得快" (Paodekuai) with support for both English and Chinese languages.

## Features

- **Bilingual Support**: Switch between English and Chinese interfaces
- **Game Tracking**: Track multiple sets, rounds, and player statistics
- **Payment Management**: Calculate and track payments between players
- **Data Export**: Export game data to CSV format
- **Responsive UI**: Clean, modern interface with wide layout support

## Language Support

The application now supports two languages:

- **English (en)**: Default language with full English interface
- **中文 (zh)**: Complete Chinese translation of all UI elements

### Switching Languages

1. Look for the language selector in the left sidebar
2. Choose between "English" and "中文"
3. The interface will immediately update to the selected language
4. Your language preference is saved during the session

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run main.py
```

## Usage

### Starting a New Game

1. Use the sidebar to set the number of players (2-10)
2. Enter unique names for each player
3. Click "Start New Game" (or "开始新游戏" in Chinese)

### Game Setup

- **Bet Amount**: Set the amount players bet per set
- **Elimination Threshold**: Set the card limit that triggers elimination
- **Starting Cards**: Set the number of cards each player starts with

### Adding Rounds

1. Enter the remaining cards for each player
2. Click "Add Round" (or "添加轮次" in Chinese)
3. The system will automatically detect winners and calculate payments

### Special Features

- **FU Toast**: When a player gets "俘了" (captured), a special notification appears
- **Payment Calculation**: Automatic calculation of winnings and losses
- **Data Export**: Export all game data to CSV for record keeping

## File Structure

- `main.py`: Main application file with Streamlit interface
- `translations.py`: Language translations and internationalization support
- `test_translations.py`: Test script to verify translations
- `requirements.txt`: Python dependencies

## Translation System

The application uses a centralized translation system:

- All UI text is stored in the `translations.py` file
- Text can include format placeholders (e.g., `{num}`, `{player}`)
- Fallback to English if a translation key is missing
- Easy to add new languages by extending the `TRANSLATIONS` dictionary

### Adding New Languages

To add support for additional languages:

1. Add a new language code to the `TRANSLATIONS` dictionary in `translations.py`
2. Provide translations for all existing keys
3. Update the language selector in `main.py` to include the new option

## Requirements

- Python 3.7+
- Streamlit
- Pandas

## Contributing

Feel free to contribute by:
- Adding new language translations
- Improving the UI/UX
- Adding new features
- Reporting bugs or issues

## License

This project is open source and available under the MIT License.

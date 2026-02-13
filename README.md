# 🎮 Aetherfall

A Python-based RPG game engine with turn-based combat, character progression, and an event-driven narrative system.

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Game Systems](#-game-systems)
- [Data Files](#-data-files)
- [Development](#-development)
- [Contributing](#-contributing)

## ✨ Features

- **Turn-based Combat System** - Strategic battle mechanics with skills and abilities
- **Character Progression** - Hero and enemy entities with customizable stats
- **Inventory Management** - Item collection, equipment, and consumables system
- **Event System** - Dynamic game events and narrative triggers
- **Dialog System** - Interactive conversations and story elements
- **Factory Pattern** - Efficient object creation and management
- **JSON-based Data** - Easy-to-modify game content without code changes

## 📁 Project Structure

```
Aetherfall/
├── Battle/           # Combat system and battle mechanics
├── Dialog/           # Conversation and narrative system
├── Entity/           # Game entities (Characters, Heroes, Enemies)
│   ├── Character.py  # Base character class
│   ├── Hero.py       # Player character implementation
│   └── Enemy.py      # Enemy implementation
├── Environment/      # Game world and locations
├── Event/            # Event handling and triggers
├── Factory/          # Object creation patterns
├── Inventory/        # Item and equipment management
├── items_data.json   # Item definitions and properties
├── skills_data.json  # Skill and ability data
├── main.py           # Application entry point
└── test.py           # Test suite
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Tarikokc/Aetherfall.git
cd Aetherfall
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

## 🎯 Usage

Run the game:
```bash
python -m Dialog.Dialog
```

Run tests:
```bash
python test.py
```

## 🎮 Game Systems

### Entity System
The game uses a hierarchical entity structure:
- **Character**: Base class for all game entities
- **Hero**: Player-controlled characters with progression systems
- **Enemy**: AI-controlled opponents with behavior patterns

### Battle System
Turn-based combat featuring:
- Action selection (Attack, Defend, Skills, Items)
- Damage calculation with modifiers
- Status effects and buffs/debuffs
- Victory and defeat conditions

### Inventory System
Manage items and equipment:
- Item categorization (Weapons, Armor, Consumables)
- Equipment slots and restrictions
- Item effects and bonuses
- Stack management for consumables

### Event System
Dynamic event handling for:
- Story progression triggers
- Random encounters
- Environmental interactions
- Quest management

## 📊 Data Files

### items_data.json
Defines all items in the game with properties such as:
- Item type and rarity
- Stats and modifiers
- Usage effects
- Description and lore

### skills_data.json
Contains skill definitions including:
- Skill name and type
- Damage/healing values
- Mana/energy costs
- Cooldowns and requirements

## 🛠️ Development

### Code Style
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Add docstrings to classes and methods
- Keep modules focused and cohesive

### Testing
- Add tests for new features in `test.py`
- Ensure existing tests pass before committing
- Test battle mechanics thoroughly

### Adding New Content

**New Items:**
Edit `items_data.json` and add entries following the existing format.

**New Skills:**
Edit `skills_data.json` with skill properties and effects.

**New Entities:**
Extend the `Character` class in the `Entity/` directory.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**Tarikokc**
- GitHub: [@Tarikokc](https://github.com/Tarikokc)
**Lylyss97x**
- Github: [@Lylyss97x](https://github.com/Lylyss97x)

---

⚔️ *Embark on your adventure in Aetherfall!*

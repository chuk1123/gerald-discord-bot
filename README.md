# 🐧 Gerald the Penguin Discord Bot

> A fun, personality-driven Discord bot featuring Gerald the sensational penguin! Interact with Gerald through various commands, feed him his favorite foods, and enjoy his quirky personality.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![py-cord](https://img.shields.io/badge/py--cord-2.0.0rc1-blueviolet.svg)](https://github.com/Pycord-Development/pycord)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🌟 Features

### Interactive Commands

Gerald comes with 7 unique slash commands:

- **`/hi [name]`** - Meet Gerald! He'll introduce himself as the sensational penguin
- **`/feed <food>`** - Feed Gerald his favorite foods (fish, krill, squid, or pizza!)
- **`/talk`** - Have a conversation with Gerald - he might encourage you, or ask to eat you if he's hungry
- **`/show_hunger_level`** - Check how hungry Gerald is (hunger system tracks feeding)
- **`/laugh`** - Gerald's signature laugh complete with custom emoji
- **`/afishy`** - Basketball! Gerald shares his love for the sport (in Spanish!)
- **`/role_members`** - Server utility to list members of any role
- **`/greet [name]`** - A friendly greeting from Gerald

### Key Features

- 🎮 **Hunger System**: Feed Gerald and watch his hunger level decrease
- 💬 **Dynamic Responses**: Gerald's personality changes based on his hunger
- 🎭 **Custom Emoji Support**: Includes custom Discord emojis for reactions
- 🛠️ **Server Utilities**: Role member listing with interactive dropdown menu
- 🎲 **Random Messages**: Different responses each time Gerald talks
- ☁️ **Heroku Ready**: Preconfigured for easy deployment

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A Discord Bot Token ([create one here](https://discord.com/developers/applications))
- Discord Server Members Intent enabled in the Developer Portal

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/chuk1123/gerald-discord-bot.git
   cd gerald-discord-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment**

   Create a `.env` file or set the `TOKEN` environment variable:
   ```bash
   export TOKEN="your-discord-bot-token-here"
   ```

   Or on Windows:
   ```cmd
   set TOKEN=your-discord-bot-token-here
   ```

4. **Enable Required Intents**

   In the [Discord Developer Portal](https://discord.com/developers/applications):
   - Go to your application → Bot → Privileged Gateway Intents
   - Enable "Server Members Intent"

5. **Run the bot**
   ```bash
   python main.py
   ```

   You should see: `We have logged in!`

## 📖 Command Reference

### Social Commands

#### `/hi [name]`
Say hi to Gerald!
```
/hi              → "Hi, I am Gerald the sensational penguin!"
/hi Kevin        → "Hi Kevin, I am Gerald the sensational penguin!"
```

#### `/greet [name]`
Get a friendly greeting from Gerald
```
/greet           → "Hey!"
/greet Kevin     → "Hello Kevin!"
```

### Interactive Commands

#### `/feed <food>`
Feed Gerald his favorite foods. His hunger level starts between 3-8 and decreases when fed.

**Favorite Foods**: fish, krill, squid, pizza (case-insensitive)

```
/feed fish       → "I ate fish! Hunger Level: 4"
/feed pizza      → "I ate pizza! Hunger Level: 3"
/feed banana     → "I don't want to eat that!"
```

When Gerald is full (hunger level 0):
```
/feed fish       → "I am full!"
```

#### `/talk`
Gerald shares random messages with you. His responses vary based on hunger:

**Regular messages**:
- "You are phenomenal!"
- "You are absolutely sensational!"
- "Get good."
- "I am a penguin."
- "\ (•◡•) /"

**When hungry (hunger > 3)**:
- "I'm hungry."
- "Can I eat you?"

#### `/show_hunger_level`
Check Gerald's current hunger level
```
/show_hunger_level → "Hunger Level: 5"
```

### Fun Commands

#### `/laugh`
Gerald's signature laugh
```
/laugh → "hee hee hee haa" + 😆 emoji
```

#### `/afishy`
Basketball appreciation (en español!)
```
/afishy → "El baloncesto es el mejor deporte!"
```

### Utility Commands

#### `/role_members`
List all members with a specific role in your server.

1. Run the command
2. Select a role from the dropdown menu
3. View all members with that role (shows nicknames if set, otherwise usernames)

**Note**: Dropdown menu expires after 10 seconds

## 🌐 Deployment

### Heroku Deployment

This bot is pre-configured for Heroku deployment:

1. **Create a Heroku app**
   ```bash
   heroku create your-gerald-bot
   ```

2. **Set the bot token**
   ```bash
   heroku config:set TOKEN=your-discord-bot-token
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

4. **Scale the worker**
   ```bash
   heroku ps:scale worker=1
   ```

The `Procfile` is already configured to run the bot as a worker process.

### Other Deployment Options

Gerald can run anywhere Python runs:
- VPS (DigitalOcean, Linode, AWS EC2)
- Raspberry Pi
- Your local machine
- Docker containers

Just ensure the `TOKEN` environment variable is set!

## 🏗️ Project Structure

```
gerald-discord-bot/
├── main.py                    # Main bot code and command handlers
├── requirements.txt           # Python dependencies (py-cord)
├── Procfile                   # Heroku deployment config
├── .gitignore                 # Git ignore rules
├── README.md                  # This file!
├── LICENSE                    # MIT License
└── Community files/
    ├── CONTRIBUTING.md        # Contributing guidelines
    ├── CODE_OF_CONDUCT.md     # Code of conduct
    ├── ISSUE_TEMPLATE.md      # Issue template
    └── PULL_REQUEST_TEMPLATE.md  # PR template
```

## 🛠️ Development

### Built With

- **[py-cord](https://github.com/Pycord-Development/pycord)** v2.0.0rc1 - Modern Discord API wrapper with slash command support
- **Python** 3.8+ - Programming language

### Key Technologies

- Discord Slash Commands (modern command interface)
- Discord UI Components (Select menus, Views)
- Async/await patterns for efficient event handling
- Environment-based configuration

## 🤝 Contributing

Contributions are welcome! Whether you want to:
- Add new commands
- Improve Gerald's personality
- Fix bugs
- Enhance documentation

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Created by [Kevin Chu](https://github.com/chuk1123)
- Built with [py-cord](https://github.com/Pycord-Development/pycord)
- Gerald the Penguin character © 2025

## 📮 Support

If you encounter issues or have questions:
1. Check existing [Issues](https://github.com/chuk1123/gerald-discord-bot/issues)
2. Create a new issue with details about your problem
3. Include error messages and your Python version

---

**Made with 🐧 by chuk1123**

*Gerald says: "You are absolutely sensational!"*

# Discord ⟷ Roblox Account Checker
A minimalist console application to find linked accounts between Discord and Roblox platforms using the Blox.link API service.

## Features
- Discord to Roblox account linking discovery
- Automatic Discord ID validation and processing
- Real-time username resolution for both platforms
- Clean, minimalist console interface with color-coded output
- Support for both interactive and command-line modes
- Comprehensive account information display
- Profile URL generation for easy access
- Robust error handling and API timeout management

## Information Retrieved
- **Discord Accounts**: User ID, formatted username, verification status
- **Roblox Accounts**: User ID, username, display name, profile links
- **Linking Status**: Account verification status and linking timestamps
- **Technical**: API response times, lookup timestamps, multiple linked accounts

## Installation
1. Clone or download the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Command Line Mode
```bash
python main.py <discord_id>
```
Examples:
```bash
python main.py 123456789012345678  # Discord ID
```

### Interactive Mode
```bash
python main.py
```
Then enter Discord IDs when prompted. Type `quit`, `q`, or `exit` to exit the program.
You can also type `help` or `examples` to see usage instructions.

## Requirements
- Python 3.6+
- requests library

## Discord ID Format Guidelines
- **Discord IDs**: 15-20 digits (typically 17-19)
- Must be numeric only
- The program validates Discord ID format automatically

## API and Technical Details
- Uses Blox.link API v4 for Discord to Roblox account discovery
- Integrates with Roblox Users API for username resolution
- Request timeout of 10 seconds for stable connections
- Automatic retry logic for temporary API failures
- Rate limit awareness and handling

## Example Output
```
============================================================
         Discord ⟷ Roblox Account Checker
============================================================
Find linked accounts between Discord and Roblox

Looking up Roblox account for Discord ID '123456789012345678'...
   Querying Blox.link API...

------------------------------------------------------------

DISCORD TO ROBLOX LOOKUP

DISCORD ACCOUNT
   Discord ID: 123456789012345678
   Username: User#5678

LINKED ROBLOX ACCOUNT
   Roblox ID: 123456789
   Username: PlayerExample
   Display Name: ExamplePlayer
   Profile URL: https://www.roblox.com/users/123456789/profile
   Status: ✓ Verified

   Lookup time: 14:30:25

------------------------------------------------------------
```

## Error Handling
- Validates Discord ID formats
- Handles API rate limits and timeouts gracefully
- Clear error messages for unlinked accounts
- Network error recovery with informative feedback
- Input validation with helpful correction suggestions

## File Structure
```
discord-roblox-checker/
├── main.py                      # Main application
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Requirements File (requirements.txt)
```
requests>=2.25.1
```

## Privacy and Ethics
- This tool only accesses publicly available linking information
- No personal data is stored or logged locally
- Respects API rate limits and terms of service
- Only retrieves information users have chosen to make public

## Common Use Cases
- **Content Moderation**: Verify user identities across platforms
- **Community Management**: Link Discord and Roblox community members
- **Account Recovery**: Help users find their linked accounts
- **Research**: Analyze cross-platform user behavior (with proper consent)

## Troubleshooting
- **"No linked account found"**: The accounts may not be linked via Blox.link
- **"API authentication failed"**: The API key may be invalid or expired
- **"Rate limit exceeded"**: Wait a few minutes before making more requests
- **"Network error"**: Check your internet connection and try again

## Legal Notice
This tool uses the Blox.link public API to retrieve publicly available account linking information. It respects all API rate limits and terms of service. Users are responsible for using this tool ethically and in compliance with platform policies.

## License
This project is open source and available under the MIT License.

## Contributing
Feel free to submit issues, feature requests, or pull requests to improve this tool.

## Disclaimer

This tool is not affiliated with Discord Inc., Roblox Corporation, or Blox.link. All trademarks belong to their respective owners.

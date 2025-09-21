import requests
import sys
import json
import time
from datetime import datetime

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    GRAY = '\033[90m'
    PURPLE = '\033[95m'

class DiscordRobloxChecker:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/json',
            'User-Agent': 'Discord-Roblox-Checker/1.0'
        })
        self.api_key = 'f5842a42-46dc-4cb4-87e7-a9300b054ee9'
        self.timeout = 10

    def print_header(self):
        print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}")
        print(f"         Discord → Roblox Account Checker")
        print(f"{'='*60}{Colors.END}\n")
        print(f"{Colors.GRAY}Find linked Roblox accounts from Discord IDs{Colors.END}\n")

    def print_separator(self):
        print(f"{Colors.GRAY}{'-'*60}{Colors.END}")

    def validate_discord_id(self, discord_id):
        """Validate Discord ID format"""
        if not discord_id or not discord_id.strip():
            return False, "Discord ID cannot be empty"
        
        discord_id = discord_id.strip()
        
        if not discord_id.isdigit():
            return False, "Discord ID must contain only numbers"
        
        if len(discord_id) < 15 or len(discord_id) > 20:
            return False, "Discord ID must be between 15-20 digits"
        
        return True, discord_id

    def get_roblox_from_discord(self, discord_id):
        """Get Roblox account from Discord ID using Blox.link API"""
        try:
            url = f"https://api.blox.link/v4/public/discord-to-roblox/{discord_id}"
            headers = {'Authorization': self.api_key}
            
            response = self.session.get(url, headers=headers, timeout=self.timeout)
            
            if response.status_code == 200:
                return response.json(), None
            elif response.status_code == 404:
                return None, "No linked Roblox account found"
            elif response.status_code == 401:
                return None, "API authentication failed"
            elif response.status_code == 429:
                return None, "Rate limit exceeded, try again later"
            else:
                return None, f"API error: HTTP {response.status_code}"
                
        except requests.Timeout:
            return None, "Request timeout - API may be slow to respond"
        except requests.RequestException as e:
            return None, f"Network error: {str(e)}"

    def get_roblox_username(self, roblox_id):
        """Get Roblox username from ID"""
        try:
            url = f"https://users.roblox.com/v1/users/{roblox_id}"
            response = self.session.get(url, timeout=self.timeout)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('name', 'Unknown'), data.get('displayName', None)
            else:
                return 'Unknown', None
                
        except Exception:
            return 'Unknown', None

    def get_discord_username(self, discord_id):
        """Get Discord username from ID (limited without bot token)"""
        return f"User#{discord_id[-4:]}"

    def display_results(self, discord_id, data):
        """Display Discord to Roblox lookup results"""
        print(f"{Colors.BOLD}{Colors.GREEN}DISCORD TO ROBLOX LOOKUP{Colors.END}\n")
        
        print(f"{Colors.BOLD}DISCORD ACCOUNT{Colors.END}")
        print(f"   {Colors.CYAN}Discord ID:{Colors.END} {discord_id}")
        discord_username = self.get_discord_username(discord_id)
        print(f"   {Colors.CYAN}Username:{Colors.END} {discord_username}")
        print()
        
        roblox_id = data.get('robloxID')
        if roblox_id:
            print(f"{Colors.BOLD}LINKED ROBLOX ACCOUNT{Colors.END}")
            print(f"   {Colors.CYAN}Roblox ID:{Colors.END} {roblox_id}")
            
            # Get username
            username, display_name = self.get_roblox_username(roblox_id)
            print(f"   {Colors.CYAN}Username:{Colors.END} {username}")
            if display_name and display_name != username:
                print(f"   {Colors.CYAN}Display Name:{Colors.END} {display_name}")
            
            profile_url = f"https://www.roblox.com/users/{roblox_id}/profile"
            print(f"   {Colors.CYAN}Profile URL:{Colors.END} {profile_url}")
            
            # Additional info if available
            if 'verified' in data:
                status = "✓ Verified" if data['verified'] else "✗ Not Verified"
                color = Colors.GREEN if data['verified'] else Colors.YELLOW
                print(f"   {Colors.CYAN}Status:{Colors.END} {color}{status}{Colors.END}")
        
        print(f"\n   {Colors.CYAN}Lookup time:{Colors.END} {datetime.now().strftime('%H:%M:%S')}")
        print()
        self.print_separator()
        print()

    def lookup_discord_to_roblox(self, discord_id):
        """Main function to lookup Roblox account from Discord ID"""
        print(f"{Colors.YELLOW}Looking up Roblox account for Discord ID '{discord_id}'...{Colors.END}\n")
        
        print(f"{Colors.GRAY}   Querying Blox.link API...{Colors.END}")
        data, error = self.get_roblox_from_discord(discord_id)
        
        if error:
            print(f"\n{Colors.RED}Lookup failed: {error}{Colors.END}")
            print(f"{Colors.GRAY}Discord ID: {discord_id}{Colors.END}")
            print(f"{Colors.GRAY}Checked at: {datetime.now().strftime('%H:%M:%S')}{Colors.END}\n")
            return False
        
        print()
        self.print_separator()
        print()
        
        self.display_results(discord_id, data)
        return True

    def show_examples(self):
        """Show example usage"""
        print(f"{Colors.BOLD}How to use:{Colors.END}")
        print(f"   {Colors.CYAN}• Enter a Discord ID{Colors.END} (17-19 digits) to find linked Roblox account")
        print(f"   {Colors.CYAN}• Type 'help' or 'examples'{Colors.END} to see this message")
        print()
        print(f"{Colors.BOLD}Example Discord ID format:{Colors.END}")
        print(f"   {Colors.GRAY}123456789012345678 (18 digits){Colors.END}")
        print()
        print(f"{Colors.YELLOW}Note: Only Discord → Roblox lookup is supported{Colors.END}")
        print()

    def process_lookup(self, discord_input):
        """Process Discord ID lookup"""
        if not discord_input or not discord_input.strip():
            print(f"{Colors.RED}Discord ID required{Colors.END}\n")
            return False
        
        # Validate Discord ID
        is_valid, processed_id = self.validate_discord_id(discord_input)
        
        if not is_valid:
            print(f"{Colors.RED}Error: {processed_id}{Colors.END}\n")
            return False
        
        print()
        return self.lookup_discord_to_roblox(processed_id)

    def run_interactive(self):
        """Run in interactive mode"""
        self.print_header()
        
        while True:
            try:
                discord_input = input(f"{Colors.BOLD}Enter Discord ID{Colors.END} (or 'help'/'quit'): ")
                
                if discord_input.lower() in ['quit', 'q', 'exit']:
                    print(f"\n{Colors.CYAN}Goodbye!{Colors.END}\n")
                    break
                
                if discord_input.lower() in ['help', 'examples', 'h']:
                    print()
                    self.show_examples()
                    continue
                
                success = self.process_lookup(discord_input)
                
                if success:
                    continue_check = input(f"{Colors.GRAY}Check another Discord ID? (y/n): {Colors.END}")
                    if continue_check.lower() not in ['o', 'oui', 'y', 'yes', '']:
                        print(f"\n{Colors.CYAN}Goodbye!{Colors.END}\n")
                        break
                
                print()
                
            except KeyboardInterrupt:
                print(f"\n\n{Colors.CYAN}Goodbye!{Colors.END}\n")
                break
            except EOFError:
                print(f"\n\n{Colors.CYAN}Goodbye!{Colors.END}\n")
                break

    def run_single(self, discord_input):
        """Run single lookup"""
        self.print_header()
        self.process_lookup(discord_input)

def main():
    checker = DiscordRobloxChecker()
    
    if len(sys.argv) > 1:
        discord_input = sys.argv[1]
        checker.run_single(discord_input)
    else:
        checker.run_interactive()

if __name__ == "__main__":

    main()

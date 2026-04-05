import sys
from pathlib import Path
import configparser

class UpdateTypiCodeIni:
    """
    Utility to update or create pytest.ini for TypiCode API tests.
    """

    def __init__(self):
        self.ini_path = Path(__file__).parent.parent / 'pytest.ini'

    def get_current_url(self) -> str:
        config = configparser.RawConfigParser()
        if self.ini_path.exists():
            config.read(self.ini_path, encoding='utf-8')
            if config.has_section("pytest") and config.has_option("pytest", "env"):
                env_lines = config.get("pytest", "env").splitlines()
                for line in env_lines:
                    if "URL_API=" in line:
                        return line.split("=", 1)[1].strip()
        return None

    def update_properties(self, custom_url: str = None) -> None:
        config = configparser.RawConfigParser()
        if self.ini_path.exists():
            config.read(self.ini_path, encoding='utf-8')
        if not config.has_section("pytest"):
            config.add_section("pytest")

        if custom_url:
            url = custom_url.strip()
            config.set("pytest", "env", f"\n    URL_API={url}\n")
            with open(self.ini_path, "w", encoding='utf-8') as configfile:
                config.write(configfile)
            print(f"pytest.ini updated with URL_API={url}")
        else:
            current_url = self.get_current_url()
            if current_url:
                print(f"Current URL_API in pytest.ini: {current_url}")
            else:
                print("No URL_API found in pytest.ini. Please provide a custom URL to set.")

def main():
    args = sys.argv
    updater = UpdateTypiCodeIni()
    if len(args) == 3 and args[1] == "custom":
        updater.update_properties(args[2])
    else:
        updater.update_properties()
        print("Usage: python update_pytest_ini.py custom <custom_url>")

if __name__ == "__main__":
    main()
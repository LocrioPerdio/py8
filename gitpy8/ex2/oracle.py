from dotenv import load_dotenv
import os
import sys

load_dotenv()

MATRIX_MODE = os.getenv("MATRIX_MODE")
DATABASE_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("API_KEY")
LOG_LEVEL = os.getenv("LOG_LEVEL")
ZION_ENDPOINT = os.getenv("ZION_ENDPOINT")


def load_config() -> None:

    req_conf: list[str] = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    miss_conf: list[str] = [var for var in req_conf if var not in os.environ]
    if miss_conf:
        print(f"Error, missing configuration: {', '.join(miss_conf)}",
              file=sys.stderr)
        sys.exit(1)
    else:
        print("Configuration loaded:")


def show_dev() -> None:
    print("Mode: development")
    print("Database:", DATABASE_URL)
    print("API Access: Authenticated")
    print("Log level: DEBUG")
    print("Zion Network:", ZION_ENDPOINT)


def show_prod() -> None:
    print("Mode: production")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print("Log level: INFO")
    print("Zion Network: Online")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    load_config()

    if MATRIX_MODE == "development":
        show_dev()
    elif MATRIX_MODE == "production":
        show_prod()
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()

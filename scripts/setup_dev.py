"""Development environment setup script."""
import subprocess
from pathlib import Path

def setup_dev_environment():
    """Set up development environment."""
    # Create required directories
    Path("data").mkdir(exist_ok=True)
    Path("logs").mkdir(exist_ok=True)
    
    # Install dependencies
    subprocess.run(["pip", "install", "-e", ".[dev]"], check=True)
    
    # Install pre-commit hooks
    subprocess.run(["pre-commit", "install"], check=True)

if __name__ == "__main__":
    setup_dev_environment()
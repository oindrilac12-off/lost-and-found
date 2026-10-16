import sys
import time
import webbrowser
import threading
from pathlib import Path

# Fix Windows console encoding for Unicode/emojis
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Add workspace to path
WORKSPACE = Path(__file__).resolve().parent
sys.path.insert(0, str(WORKSPACE))

import uvicorn
from backend.database import init_db
from backend.demo_data import seed_demo_data

def open_browser():
    time.sleep(1.5)
    print("\n🌐 Opening FindrAI in your browser: http://127.0.0.1:8000\n")
    try:
        webbrowser.open("http://127.0.0.1:8000")
    except Exception as e:
        print(f"Could not open browser automatically: {e}")

def main():
    print("=" * 60)
    print("🚀 Initializing FindrAI - Lost & Found AI Matching Platform")
    print("=" * 60)
    
    init_db()
    seed_demo_data(force_reset=False)
    
    # Launch browser in separate thread
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Run Uvicorn server
    uvicorn.run(
        "backend.main:app",
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="info"
    )

if __name__ == "__main__":
    main()

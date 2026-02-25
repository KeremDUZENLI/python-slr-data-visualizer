import os
import sys
import streamlit.web.cli as stcli


if __name__ == "__main__":
    if getattr(sys, "frozen", False):
        app_path = os.path.join(sys._MEIPASS, "web_app.py")
        os.chdir(sys._MEIPASS)
    else:
        app_path = os.path.join(os.path.dirname(__file__), "web_app.py")

    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--server.port=8501",
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())

# python-slr-data-visualizer

A Python pipeline for data analysis and visualization of systematic literature reviews (SLR). Includes PRISMA flows, networks, timelines, sunbursts, and heatmaps for reproducible academic workflows.

```bash
dataset.example = [
    (
        0,  # field_0: Unique identifier for the entity (integer, e.g., study ID, project ID)
        0,  # field_1: Numeric attribute (e.g., year, timestamp, or other quantitative value)
        "",  # field_2: Categorical attribute (e.g., location, category, or group)
        "",  # field_3: Primary focus or type (e.g., study focus, project type; used for network connections)
        "",  # field_4: Main category or type (e.g., domain, subject, or entity type)
        "",  # field_5: Subcategory or subtype (e.g., specific classification within the main category)
        [],  # field_6: List of primary attributes (e.g., platforms, methods; used for network connections)
        [],  # field_7: List of secondary attributes (e.g., devices, tools, or resources)
        [],  # field_8: List of techniques or approaches (e.g., methodologies; used for network connections)
        [],  # field_9: List of specific techniques or sub-approaches (e.g., detailed methods or processes)
        [],  # field_10: List of tools or resources for data collection (e.g., software, instruments)
        [],  # field_11: List of tools or resources for processing (e.g., modeling or analysis tools)
        [],  # field_12: List of tools or resources for output (e.g., visualization or rendering tools)
    ),
    # Add more entries as needed, following the same 13-field structure
]
```

```bash
python -m xamples.chart_xxx
```

```bash
streamlit run web_app.py
```

## COMPILE

### Windows

```bash
pyInstaller --noconfirm --onefile \
   --name DataVisualizer \
   --add-data "web_app.py;." \
   --add-data "data/dataset.example.csv;data" \
   --hidden-import web_app \
   --collect-all streamlit \
   --collect-all plotly \
   --copy-metadata streamlit \
   web_run.py
```

### Linux & MacOS

```bash
python3 -m PyInstaller --noconfirm --onefile \
   --name DataVisualizer \
   --add-data "web_app.py:." \
   --add-data "data/dataset.example.csv:data" \
   --hidden-import web_app \
   --collect-all streamlit \
   --collect-all plotly \
   --copy-metadata streamlit \
   web_run.py
```

## ⚠️ TROUBLESHOOTING: PRISMA Chart (Graphviz Error)

If you attempt to draw the **PRISMA Chart** and receive an error (such as `graphviz.backend.ExecutableNotFound: failed to execute ['dot', ...]`), it means your computer does not have the core Graphviz rendering software installed.

Because this software is large, it is not bundled directly inside the app. You will need to install it once on your system:

### Windows

**Option 1: Standard Installer (Recommended)**

1. Go to the [Official Graphviz Download Page](https://graphviz.org/download/).
2. Download the latest **64-bit EXE installer**.
3. Run the installer. **CRITICAL STEP:** During installation, when prompted, you MUST select **"Add Graphviz to the system PATH for all users"** (or current user). If you skip this, the app still won't find it!
4. Restart your computer (or terminal) and open the app again.

**Option 2: Using Windows Package Manager (Winget)**
Open PowerShell as Administrator and run:
`winget install graphviz`

### Linux (Ubuntu / Debian)

Open your terminal and run:

```bash
sudo apt-get update
sudo apt-get install graphviz
```

### macOS

If you are running the source code on a Mac, use Homebrew:

```Bash
brew install graphviz
```

## CONTRIBUTE

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b YourBranch
   ```
3. Make your changes and commit them:
   ```sh
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```sh
   git push origin YourBranch
   ```
5. Open a pull request.

## LICENSE

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**. This means you are free to:

- **Share** – Copy and redistribute the material in any medium or format.
- **Adapt** – Remix, transform, and build upon the material.

However, **you may not use the material for commercial purposes**.

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## DISCLAIMER

This repository is intended **only for educational and research purposes**. The authors and contributors assume no responsibility for misuse of the code or any implications arising from its use.

## SUPPORT

If you find this resource valuable and would like to help support my education and doctoral research, please consider treating me to a cup of coffee (or tea) via Revolut.

<div align="center">
  <a href="https://revolut.me/krmdznl" target="_blank">
    <img src="https://img.shields.io/badge/Support%20My%20Projects-Donate%20via%20Revolut-orange?style=for-the-badge" alt="Support my education via Revolut" />
  </a>
</div>

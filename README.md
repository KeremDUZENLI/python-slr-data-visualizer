# python-slr-data-visualizer

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)
![Release](https://img.shields.io/github/v/release/KeremDUZENLI/python-slr-data-visualizer)

A Python pipeline for data analysis and visualization of systematic literature reviews (SLR). Includes PRISMA flows, networks, timelines, sunbursts, and heatmaps for reproducible academic workflows.

## 🚀 GETTING STARTED

### Expected Data Structure

Your input `.csv` file should loosely follow this structure (see `data/dataset.example.csv`):

```text
field_0: ID (Integer)
field_1: Numeric attribute (e.g., year)
field_2: Categorical attribute (e.g., location)
field_3: Primary focus/type (e.g., study focus)
field_4: Main category (e.g., domain)
field_5: Subcategory (e.g., specific classification)
field_6 to 12: Lists of attributes (platforms, tools, methodologies, software) separated by semicolons (;)
```

### Three Ways to Use This Tool:

1. **DOWNLOAD** : Standalone compiled application (No setup required).
2. **INTERACTIVE UI** : Run the Web UI via Python.
3. **EXAMPLE FILES** : Run pre-configured Python scripts in the `xamples` folder.

## ⬇️ 1. DOWNLOAD (Standalone Application)

If you don't want to install Python or set up an environment, download the pre-compiled, ready-to-use application directly from the **[Releases Page](https://github.com/KeremDUZENLI/python-slr-data-visualizer/releases)**.

- 🐧 **Linux:** Download `DataVisualizer_Linux`
- 🍏 **macOS:** Download `DataVisualizer_MacOS`
- 🪟 **Windows:** Download `DataVisualizer_Windows.exe`

**How to use:** Just download the file for your operating system, double-click to run it, and the app will automatically open in your web browser!

## 🖥️ 2. INTERACTIVE UI

If you prefer to run the app from the source code, launch the Streamlit app for a fully visual experience:

```bash
streamlit run web_app.py
```

_Alternatively:_

```bash
python web_run.py
```

### 💡 How the UI Works (Applies to Methods 1 & 2)

The interface is divided into 3 simple steps:

**1. Data Preparation**
Upload your `.csv` file or load the example dataset.

- **1️⃣ Group Dataset:** Combine multiple columns into a single stackable category.
- **2️⃣ Map Column:** Translate values using a dictionary (e.g., map `Countries` to `Continents`).
- **3️⃣ Map Hierarchy:** Define Parent-Child relationships for nested charts (e.g., Sunburst).

**2. Chart Creation**
Select your dataset and choose a chart type (Bar, Pie, Heatmap, Scatter, Sankey, Map, PRISMA).

- **Filters:** Apply specific rules (e.g., `year >= 2015` or `count > 5`).
- **Axes:** Assign your CSV columns to X, Y, and Z (grouping) axes.
- **Options & Legends:** Toggle grids, borders, custom legends, and positions (BBox).
- **Save:** Save your configuration to load later, or download the chart as PNG/SVG/PDF/HTML.

**3. Settings**
Globally customize the look and feel using JSON dictionaries. Changes apply instantly.

- 🎨 **Colors:** Map specific labels to specific HEX colors.
- 🔤 **Fonts:** Change font size, family, weight, and style.
- 💠 **Prisma Style:** Customize node shapes, box sizes, and edge styles.

## ⌨️ 3. EXAMPLE FILES

If you prefer pure coding, you can generate charts directly using the pre-configured templates.

1. Place your dataset in `data/dataset.csv`.
2. Open any `xamples/chart_xxx.py` file and adjust the parameters:

- `fields`: Specific columns to extract.
- `filter_values` / `filter_count`: Rules to include/exclude data.
- `x_axis`, `y_axis`, `z_axis`: Field mappings.
- `coloring_field`: Column used to fetch colors from `config.py`.
- `labels_spec` / `legends_config`: Customize titles, labels, and legends.

3. Run your selected script:

```bash
python -m xamples.chart_NAME
```

## ⚠️ TROUBLESHOOTING: PRISMA Chart (Graphviz)

If you attempt to draw the **PRISMA Chart** and receive a `ExecutableNotFound` error, your computer does not have the core Graphviz software installed.

### Windows

1. Go to the [Graphviz Download Page](https://graphviz.org/download/).
2. Download the latest **64-bit EXE installer**.
3. Run it and select **"Add Graphviz to the system PATH for all users"** (Critical step).
4. Restart your computer.

### Linux (Ubuntu / Debian)

```bash
sudo apt-get update
sudo apt-get install graphviz
```

### macOS

```bash
brew install graphviz
```

## 📦 COMPILE TO EXECUTABLE

You can compile this project into a standalone executable yourself.

### Windows

```bash
pyinstaller --noconfirm --onefile \
   --name DataVisualizer_Windows \
   --add-data "web_app.py;." \
   --add-data "data/dataset.example.csv;data" \
   --hidden-import web_app \
   --collect-all streamlit \
   --collect-all plotly \
   --copy-metadata streamlit \
   web_run.py
```

### Linux & macOS

_(Note: Use colons `:` instead of semicolons `;` for paths)._

```bash
python3 -m PyInstaller --noconfirm --onefile \
   --name DataVisualizer_Linux_or_Mac \
   --add-data "web_app.py:." \
   --add-data "data/dataset.example.csv:data" \
   --hidden-import web_app \
   --collect-all streamlit \
   --collect-all plotly \
   --copy-metadata streamlit \
   web_run.py
```

## 🤝 CONTRIBUTE

1. Fork the repository.
2. Create a new branch: `git checkout -b YourBranch`
3. Make your changes and commit: `git commit -m "Add some feature"`
4. Push to the branch: `git push origin YourBranch`
5. Open a Pull Request.

## 📄 LICENSE

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.
You are free to Share and Adapt the material, provided you give appropriate credit and distribute your contributions under the same license. **Commercial use is strictly prohibited.**

## ⚠️ DISCLAIMER

This repository is intended **only for educational and research purposes**. The authors and contributors assume no responsibility for misuse of the code or any implications arising from its use.

## ☕ SUPPORT

If you find this resource valuable and would like to help support my education and doctoral research, please consider treating me to a cup of coffee (or tea) via Revolut.

<div align="center">
<a href="https://revolut.me/krmdznl" target="_blank">
<img src="https://img.shields.io/badge/Support%20My%20Projects-Donate%20via%20Revolut-orange?style=for-the-badge" alt="Support my education via Revolut" />
</a>
</div>

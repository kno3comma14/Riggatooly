# 🛠️ Riggatooly
**Universal 2D Pipeline & Automated Rigging Framework**

Riggatooly is a high-performance Technical Animation (TA) toolkit designed to bridge the gap between raster artwork (Photoshop/Krita) and professional 2D animation suites. By implementing a **Universal 2D Manifest (U2DM)**, Riggatooly automates the most time-consuming part of production: pivot placement, asset extraction, and skeletal hierarchy construction.

## 🚀 The Vision
In professional 2D pipelines, rigging usually requires hours of manual labor to set pivots and parent layers. **Riggatooly** solves this by using a "Source of Truth" workflow:
1.  **Extract**: Identify pivots via color-coded markers and parse hierarchies directly from PSD metadata.
2.  **Manifest**: Generate a software-agnostic JSON schema containing all transformation and skeletal data.
3.  **Inject**: Automatically reconstruct the rig in the target software (Harmony, Blender, Tahoma2D) using native APIs or file injection.

## 🏗️ Technical Architecture
Riggatooly is built on a modular "Extractor-Adapter" pattern:

*   **The Extractor (Core)**: A standalone Python/PySide6 application that uses `psd-tools` and `NumPy` to perform geometric center calculations and color-based pivot detection.
*   **The Linter**: An integrated validation engine that scans source files for naming convention errors, duplicate layers, or missing pivots before data reaches the pipeline.
*   **The Adapters**:
    *   **Live-Link (API-based)**: Direct integration with **Toon Boom Harmony 25** (Python SDK) and **Blender Grease Pencil** (bpy) to build live node networks.
    *   **File-Injection**: Automated XML scene generation for **Tahoma2D / OpenToonz**, allowing for "one-click" scene loading without internal plugins.

## 🛠️ Key Features
*   **Sub-pixel Pivot Accuracy**: Uses NumPy to calculate the "center of mass" for color-coded pivot markers in your source art.
*   **Automatic Hierarchy Mapping**: Supports a dedicated `ParentPegs` group logic to define complex parent-child relationships within the PSD.
*   **Industry Standard Naming**: Automatically handles `_D` (Drawing) and `-P` (Peg) suffixes to maintain professional rigging conventions.
*   **Built-in Asset Management**: Automates the cropping and exporting of individual layers into optimized PNG sequences.

## 💻 Tech Stack
*   **Language**: Python 3.9+ (Poetry managed)
*   **UI Framework**: PySide6 (Qt)
*   **Data Processing**: NumPy 2.x
*   **PSD Handling**: psd-tools + Pillow (PIL)
*   **Interoperability**: JSON / OpenUSD (Planned)

## 📂 Project Roadmap
- [x] Multi-format PSD Parsing & Data Extraction
- [x] PySide6 GUI with real-time logging and color picking
- [x] Automated PNG asset exportation
- [ ] **Harmony 25 Adapter**: Automated Node View reconstruction
- [ ] **Moho Adapter**: Another critical app in the industry
- [ ] **Blender Adapter**: Grease Pencil skeletal generation
- [ ] **Tahoma2D Adapter**: XML-based `.tnz` scene injection

## License
See [License](LICENSE) file.

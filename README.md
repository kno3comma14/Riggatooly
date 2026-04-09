# 🛠️ Riggatooly
**Universal 2D Pipeline & Automated Rigging Framework**

Riggatooly is a high-performance Technical Animation (TA) toolkit designed to bridge the gap between raster artwork (Photoshop/Krita) and professional 2D animation suites. By implementing a **Universal 2D Manifest (U2DM)**, Riggatooly automates some of the most time-consuming parts of production: pivot placement, asset extraction, and initial skeletal hierarchy construction.

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

## 📖 Usage Guide

The Riggatooly desktop interface provides a streamlined, step-by-step workflow to convert your artwork into a production-ready manifest.

### 1. File Preparation
Before launching the tool, ensure your source PSD follows the **Naming Conventions** (layers ending in `_D`) and contains a single-pixel color marker for each joint.

### 2. Configuration
1.  **Browse PSD File**: Click to select your source `.psd` file.
2.  **Browse Target Folder**: Select the destination directory where Riggatooly will export your PNG assets and the `manifest.json`.
3.  **Peg per Drawing**: Enable this checkbox to automatically generate a dedicated Peg layer for every drawing part (Industry Standard Practice).
4.  **Change Pivote Color**: Open the color picker to match the RGB value used for the joint markers in your artwork.

### 3. Execution & Logging
*   **Generate Universal Rigging Structure**: Click the primary action button to begin the extraction.
*   **Process Log**: Monitor the real-time terminal inside the GUI. It will provide instant feedback on:
    *   File path detection and loading.
    *   Success/Failure states for asset exports.
    *   Finalization of the U2DM Manifest file.


## 📂 Project Roadmap
- [x] Multi-format PSD Parsing & Data Extraction
- [x] PySide6 GUI with real-time logging and color picking
- [x] Automated PNG asset exports
- [ ] **Harmony 25 Adapter**: Automated Node View reconstruction
- [ ] **Moho Adapter**: Another critical app in the industry
- [ ] **Blender Adapter**: Grease Pencil skeletal generation
- [ ] **Tahoma2D Adapter**: XML-based `.tnz` scene injection(I started and finished this one, but have to study how to include to the flow)

## Important
Note: The Harmony Adapter must be executed using the internal Harmony Python 3.9 interpreter or an external environment mapped to Harmony's libraries.

## License
See [License](LICENSE) file.

# DIGINVASIVE

This repository contains Jupyter notebooks and Python scripts focused on data processing, geospatial visualization, image manipulation, and format conversion. The content is organized into thematic folders based on functionality.

---

## 📁 Repository Structure

### 🔹 Base

General utility functions to support other tasks or scripts.

- `base_funcionesbase.ipynb`: A collection of helper functions for managing and analyzing SIGPAC-related geospatial and administrative data. Includes:
  - Transformation of SIGPAC IDs (`dividir_id_rec`)
  - Normalization of locality names (`nombre_mayuscula`)
  - Mapping province and municipality names (`add_nom_prov_mun`)
  - Database connection and querying (`conn_sigpacdb`, `consulta_sigpac`)
  - Validation and conversion to GeoDataFrames (`check_geometrias`, `generate_gdf`)
  - Saving geodata to spatial databases (`save_gdf_to_db`)

### 🔹 Sigpac

Processing and downloading geospatial data from the SIGPAC system.

- `sigpac_descargar.ipynb`: Step-by-step notebook that automates the downloading of SIGPAC parcel and layer data from FEGA services. Implements a structured workflow with updated parameters (as of 06/14/2024).

### 🔹 WM

Image processing scripts, particularly useful for visual recognition or digitization projects.

- `wm_quitar_fondo.py`: Removes white background from an image and converts it to a transparent PNG using OpenCV.
- `wm_resolucion.py`: Enhances image resolution using super-resolution models such as OpenCV's ESPCN.
- `wm_svg.py`: Converts image contours to SVG after background removal and edge detection using `skimage`.

### 🔹 Conversor

Image format conversion from `.HEIC` to `.JPG`.

- `convertir.py`: Batch converts `.heic` images to `.jpg` using `pyheif` and `PIL`. Processes entire directories.

---

## ✅ Requirements

Necessary dependencies:

```bash
pip install numpy opencv-python scikit-image svgwrite pyheif pillow
```

---

## 🚀 Usage

1. Clone the repository:

```bash
git clone https://github.com/imchrisrueda/diginvasive.git
cd diginvasive
```

2. Run the notebooks using Jupyter or the scripts with Python depending on your target folder and task.

---

## 🛠️ Contributing

Contributions are welcome! To contribute:

1. Fork the project.
2. Create a new branch (`git checkout -b new-feature`).
3. Make your changes and commit (`git commit -m "Description"`).
4. Push the branch (`git push origin new-feature`).
5. Open a Pull Request.

---

## 📄 License

This repository is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.

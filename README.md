# ZoomTernary: A Library for Zoomable Ternary Plots

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/your-username/ZoomTernary/issues)

**ZoomTernary** is an upcoming Python library for creating high-quality, zoomable ternary diagrams. It is designed for material scientists, chemists, and researchers who need to visualize compositional data within a specific, concentrated region of a ternary phase space, such as an element-rich corner.

The project is in its early stages, and we are actively seeking contributors to help build a powerful and user-friendly tool for the scientific community.

## About The Project

Standard plotting libraries can make it challenging to create clear visualizations when your data is clustered in a small area of a ternary diagram. ZoomTernary aims to solve this by providing a simple interface to generate "zoomed-in" plots, allowing for detailed analysis of a specific compositional range.

This library is built on top of the powerful `matplotlib` and `python-ternary` packages.

### Current Features

* Generates a zoomed-in plot focusing on a corner of the ternary diagram (e.g., 0-20% composition).
* Correctly scales and labels axes for the zoomed region.
* Customizable plot elements including markers, gridlines, and labels.

## Example

The image below was generated using the initial script. It shows a plot focused on the Al-rich corner of an Al-Sc-X system, with both Al and Sc concentrations ranging from 0% to 20%.

## Getting Started

Currently, the project exists as a single functional script. To run it and generate a plot like the one above, you will need to have the required dependencies installed.

### Prerequisites

Ensure you have Python 3 installed. You can install the necessary libraries using pip:

```sh
pip install matplotlib python-ternary```

### Usage

1. Clone this repository (or simply copy the code from the `zoomed_ternary_plot.py` file).
2. Prepare your data in a list of tuples, where each tuple represents the three components.
3. Modify the script's parameters, such as axis labels and the zoom scale, to fit your needs.
4. Run the script:
   
   ```sh
   python zoomed_ternary_plot.py
   ```

## Roadmap & How to Contribute

This is where we need your help! We want to transform this functional script into a robust, installable library. We welcome contributions of all kinds, from code and documentation to ideas and feature requests.

Here are some of the goals we have in mind:

- [ ] **Package as a Library**: Refactor the code into a proper Python package that can be installed via `pip`.

- [ ] **Develop a High-Level API**: Create an intuitive API that simplifies the plotting process. For example:
  
  ```python
  import zoom_ternary as zt
  
  fig, tax = zt.zoom(corner='Al', scale=0.2, ...)
  tax.scatter(data)
  zt.show()
  ```

- [ ] **Generalize Zoom Functionality**: Allow zooming into any region of the plot, not just a corner.

- [ ] **Add More Plot Types**: Support for heatmaps, contour plots, and line plots within the zoomed view.

- [ ] **Improve Documentation**: Write comprehensive docstrings, tutorials, and a gallery of examples.

- [ ] **Create Unit Tests**: Ensure the code is reliable and maintainable.

If you are interested in contributing, please follow these steps:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

* [python-ternary](https://github.com/marcharper/python-ternary)
* [Matplotlib](https://matplotlib.org/)
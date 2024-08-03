import os
import subprocess

notebook_path = "/Users/karthik/Desktop/Autoyos/data_analyst_assignment/autoyos_eye_blink_analysis_karthik_dani.ipynb"
base_filename = os.path.basename(notebook_path).split(".")[0]
markdown_path = os.path.join(os.path.dirname(notebook_path), base_filename + ".md")
pdf_output_path = os.path.join(os.path.dirname(notebook_path), base_filename + ".pdf")

metadata = {
    "title": "Autoyos: Eye Blink Data Analysis",
    "author": "Karthik Dani: 1BM22MD022",
    "date": "2024-06-26",
    "abstract": ("This study investigates blinking behavior using longitudinal data analysis techniques. By analyzing blink durations, interblink intervals, and blink rates over multiple months, we uncover nuanced patterns and variations. Statistical analysis and visualizations reveal trends in blinking habits, shedding light on potential factors influencing these behaviors. This exploration offers valuable insights into the dynamics of blinking patterns."),
    "subtitle": "Statistically Understanding Blinking Behavior across April, May and June",
    "keywords": "Data analysis",
    "thanks": "*",
    "email": "karthikdani14@gmail.com",
    "institute": "BMS College of Engineering, Bangalore"
}

try:
    subprocess.run(['jupyter', 'nbconvert', '--to', 'markdown', '--TagRemovePreprocessor.enabled=True', '--TagRemovePreprocessor.remove_cell_tags="exclude-output', notebook_path], check=True)
    print(f"Converted notebook to Markdown: {markdown_path}")
    
except subprocess.CalledProcessError as e:
    print(f"Error during Markdown conversion: {e}")
    exit(1)

pandoc_command = ["pandoc", markdown_path, "-o", pdf_output_path]

for key, value in metadata.items():
    pandoc_command.append(f"--metadata={key}={value}")


try:
    subprocess.run(pandoc_command, check=True)
    print(f"Successfully converted Markdown to PDF: {pdf_output_path}")
except subprocess.CalledProcessError as e:
    print(f"Error during PDF conversion: {e}")
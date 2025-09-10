import base64
import io
import pandas as pd
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa
from graphs import graphs
from datetime import datetime

sample_data = {
    "Process_Type": "Primary",
    "Metal": "Aluminium",
    "Energy_MJ_per_kg": 210.5,
    "Quantity_kg": 100,
    "Energy_MJ_total": 21050.0,
    "Transport_km": 150.0,
    "Transport_Mode": "Truck",
    "Transport_emissions_kgCO2": 45.7,
    "Water_use_m3_per_ton": 6.8,
    "End_of_Life": "Recycle",
    "Circularity_option": "Closed-loop",
    "Process_emissions_kgCO2": 520.3,
    "Total_emissions_kgCO2": 566.0,
    "Emission_factor_kgCO2_per_MJ": 0.0021,
}

charts=graphs(sample_data=sample_data)


env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("invoice.html")
today = datetime.today().strftime("%d-%m-%Y")
html_content = template.render(
    Name="Vansh Sharma",
    company="EcoTech Pvt Ltd",
    sample_data=sample_data,
    charts=charts,
    generated_data=today
)

with open("report.pdf", "wb") as f:
    pisa.CreatePDF(html_content, dest=f)

print("✅ PDF generated: report.pdf")

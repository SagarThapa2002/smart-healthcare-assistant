# main.py

from models.patient import Patient

patient1 = Patient(
    1,
    "John Smith",
    28,
    "Male"
)

patient1.display_info()
from datetime import date

class Patient:

    def __init__(
            self,
            patient_id: str,
            first_name: str,
            last_name: str,
            date_of_birth: date,
            gender: str,
            phone: str,
            email: str ="",
            address: str = "",
            registration_date: date | None = None,
    ) -> None:
        
        self.patient_id = patient_id
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone = phone
        self.email = email
        self.address = address
        self.registration_date = registration_date or date.today()
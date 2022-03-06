class Human:
    def __init__(self, name) -> None:
        self.name = name


class Patient(Human):
    def __init__(self, name, symptom, patient_id) -> None:
        super().__init__(name)
        self.symptom = symptom
        self.patient_id = patient_id


class Clinic:
    def __init__(self) -> None:
        self.patient_list: list[Patient] = []

    def show_waiting_count(self):
        print("現在の待ち人数: ", len(self.patient_list))

    def reserve(self, patient: Patient):
        if self._check_reserved(patient):
            print(patient.name, "さんは予約済みです")
        else:
            self.patient_list.append(patient)
            print(patient.name, "さんの予約が完了しました")

    def diagnosis(self, patient_id=None):
        patient = None
        if patient_id is None:
            if len(self.patient_list):
                patient = self.patient_list.pop(0)
        else:
            for i, p in enumerate(self.patient_list):
                if p.patient_id == patient_id:
                    patient = self.patient_list.pop(i)

        if patient is None:
            print("患者が存在しないか、予約されていません。")
        else:
            print(f"{patient.name}さん（症状: {patient.symptom}）の診療が終わりました。")

    def _check_reserved(self, patient: Patient):
        for p in self.patient_list:
            if p.patient_id == patient.patient_id:
                return True

        return False


my_clinic = Clinic()
patients = [("佐藤", "咳", "111"), ("田中", "腹痛", "222"), ("鈴木", "鼻水", "333"), ("山田", "倦怠感", "444"), ("宮本", "肩こり", "555")]

for p in patients:
    name, symptom, patient_id = p
    patient = Patient(name, symptom, patient_id)
    my_clinic.reserve(patient)

if __name__ == "__main__":
    my_clinic.show_waiting_count()
    me = Patient("宮本", "肩こり", "555")
    my_clinic.reserve(me)
    my_clinic.diagnosis()
    my_clinic.show_waiting_count()
    my_clinic.diagnosis("555")

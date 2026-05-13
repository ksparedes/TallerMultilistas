def read_divipola(self, file_path):
    countries = DoubleLinkedList()
    colombia = Country("CO", "Colombia")
    countries.append(colombia)

    departments = {}

    with open(file_path, encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dept_code = row["cod_depto"]
            dept_name = row["departamento"]

            city_code = row["cod_mpio"]
            city_name = row["municipio"]

            lat = row["lat"]
            lon = row["lon"]

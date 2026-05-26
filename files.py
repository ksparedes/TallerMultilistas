import csv
from node import Country, Department, City
from doublelinkedlist import DoubleLinkedList  

class Files:

    def read_divipola(self, file_path):
        countries = DoubleLinkedList()
        colombia = Country("CO", "Colombia")
        countries.append(colombia)

        departments = {}

        with open(file_path, encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                dept_code = row["Código Departamento"]
                dept_name = row["Nombre Departamento"]
                city_code = row["Código Municipio"]
                city_name = row["Nombre Municipio"]
                lat = row["Latitud"]
                lon = row["longitud"]

                if dept_code not in departments:
                    department = Department(dept_code, dept_name)
                    countries.add_child(colombia, department)
                    departments[dept_code] = department

                city = City(city_code, city_name, lat, lon)
                countries.add_child(departments[dept_code], city)

        return countries

    def get_markers(self, multilist):
        markers = []

        current_country = multilist.head

        while current_country:
            if current_country.sub_list:
                current_department = current_country.sub_list.head

                while current_department:
                    if current_department.sub_list:
                        current_city = current_department.sub_list.head

                        while current_city:
                            if current_city.lat and current_city.lon:
                                markers.append({
                                    "lat": current_city.lat,
                                    "lon": current_city.lon,
                                    "popup": f"<b>{current_city.name}</b><br>Departamento: {current_department.name}"
                                })
                            current_city = current_city.next

                    current_department = current_department.next

            current_country = current_country.next

        return markers
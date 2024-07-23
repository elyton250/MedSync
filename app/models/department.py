from app import db
from app.id_gen import history_id

class Department:
    def __init__(
        self,
        name,
        description,
        head_of_department,
    ):
        self.id = history_id()
        self.name = name
        self.description = description
        self.head_of_department = head_of_department

    def save(self):
        db.departments.insert_one(self.__dict__)

    @staticmethod
    def get_all():
        return list(db.departments.find())

    @staticmethod
    def get_one(id):
        return db.departments.find_one({"id": id})

    @staticmethod
    def get_by_name(name):
        return db.departments.find_one({"name": name})

    @staticmethod
    def delete(id):
        db.departments.delete_one({"id": id})


class Radiology(Department):
    def __init__(
        self,
        name,
        description,
        head_of_department,
        equipment,
    ):
        super().__init__(name, description, head_of_department)
        self.equipment = equipment

    def save(self):
        db.radiology.insert_one(self.__dict__)

    @staticmethod
    def get_all():
        return list(db.radiology.find())

    @staticmethod
    def get_one(id):
        return db.radiology.find_one({"id": id})

    @staticmethod
    def get_by_name(name):
        return db.radiology.find_one({"name": name})

    @staticmethod
    def delete(id):
        db.radiology.delete_one({"id": id})
        
    
    
    class Cardiology(Department):
        def __init__(
            self,
            name,
            description,
            head_of_department,
            equipment,
            number_of_beds,
        ):
            super().__init__(name, description, head_of_department)
            self.equipment = equipment
            self.number_of_beds = number_of_beds

        def save(self):
            db.cardiology.insert_one(self.__dict__)

        @staticmethod
        def get_all():
            return list(db.cardiology.find())

        @staticmethod
        def get_one(id):
            return db.cardiology.find_one({"id": id})

        @staticmethod
        def get_by_name(name):
            return db.cardiology.find_one({"name": name})

        @staticmethod
        def delete(id):
            db.cardiology.delete_one({"id": id})


class Neurology(Department):
    def __init__(
        self,
        name,
        description,
        head_of_department,
        equipment,
        number_of_specialists,
    ):
        super().__init__(name, description, head_of_department)
        self.equipment = equipment
        self.number_of_specialists = number_of_specialists

    def save(self):
        db.neurology.insert_one(self.__dict__)

    @staticmethod
    def get_all():
        return list(db.neurology.find())

    @staticmethod
    def get_one(id):
        return db.neurology.find_one({"id": id})

    @staticmethod
    def get_by_name(name):
        return db.neurology.find_one({"name": name})

    @staticmethod
    def delete(id):
        db.neurology.delete_one({"id": id})


class Pediatrics(Department):
    def __init__(
        self,
        name,
        description,
        head_of_department,
        number_of_beds,
        special_facilities,
    ):
        super().__init__(name, description, head_of_department)
        self.number_of_beds = number_of_beds
        self.special_facilities = special_facilities

    def save(self):
        db.pediatrics.insert_one(self.__dict__)

    @staticmethod
    def get_all():
        return list(db.pediatrics.find())

    @staticmethod
    def get_one(id):
        return db.pediatrics.find_one({"id": id})

    @staticmethod
    def get_by_name(name):
        return db.pediatrics.find_one({"name": name})

    @staticmethod
    def delete(id):
        db.pediatrics.delete_one({"id": id})


class School:
    def __init__(self, name, level, numberOfStudents):  # Fixed the typo here
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def numberOfStudents(self):
        return self._numberOfStudents

    @numberOfStudents.setter
    def numberOfStudents(self, value):
        self._numberOfStudents = value

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, 'primary', numberOfStudents)
        self.pickupPolicy = pickupPolicy

    @property
    def pickupPolicy(self):
        return self._pickupPolicy

    @pickupPolicy.setter
    def pickupPolicy(self, value):
        self._pickupPolicy = value

    def __repr__(self):
        return super().__repr__() + f". The pickup policy is {self.pickupPolicy}"


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, 'high', numberOfStudents)
        self.sportsTeams = sportsTeams

    @property
    def sportsTeams(self):
        return self._sportsTeams

    @sportsTeams.setter
    def sportsTeams(self, value):
        self._sportsTeams = value

    def __repr__(self):
        return super().__repr__() + f". The sports teams are: {', '.join(self.sportsTeams)}"


# Testing the code
general_school = School("Generic School", "middle", 300)
print(general_school)

primary_school = PrimarySchool("Greenwood Primary", 450, "Pickup after 3pm")
print(primary_school)

high_school = HighSchool("Lincoln High", 1200, ["Basketball", "Soccer", "Tennis"])
print(high_school)

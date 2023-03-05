class Faculty:
    faculties = [
        'Faculty of Biology and Geoscience',
        'Faculty of Chemistry and Chemical Technology',
        'Faculty of Law',
        'Faculty of Journalism and Communication Sciences',
        'Faculty of Physics and Engineering',
        'Faculty of History and Philosophy',
        'Faculty of Mathematics and Informatics',
        'Faculty of Philology',
        'Faculty of Economic Sciences',
        'Faculty of Psychology',
        'Faculty of International Relations'
    ]

    @staticmethod
    def get_faculty_name(index: int):
        return Faculty.faculties[index]

    @staticmethod
    def get_faculty_index(name: str):
        try:
            return Faculty.faculties.index(name)
        except ValueError:
            return -1

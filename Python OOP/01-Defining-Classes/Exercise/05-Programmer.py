class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language == self.language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        else:
            return f'{self.name} does not know {language}'

    def change_language(self, new_language, skills_needed):
        if skills_needed <= self.skills:
            if new_language != self.language:
                previous_language = self.language
                self.language = new_language
                return f'{self.name} switched from {previous_language} to {self.language}'
            else:
                return f'{self.name} already knows {self.language}'
        else:
            return f'{self.name} needs {skills_needed - self.skills} more skills'
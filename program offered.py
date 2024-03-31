class UniversityProject:
    def __init__(self):
        self.projects = {}

    def add_project(self, student_name, project_title, project_description):
        if student_name in self.projects:
            self.projects[student_name].append((project_title, project_description))
        else:
            self.projects[student_name] = [(project_title, project_description)]
        print("Project added successfully.")

    def view_projects(self, student_name):
        if student_name in self.projects:
            print(f"Projects for {student_name}:")
            for idx, project in enumerate(self.projects[student_name], 1):
                print(f"{idx}. Title: {project[0]}, Description: {project[1]}")
        else:
            print("No projects found for this student.")

    def delete_project(self, student_name, project_index):
        if student_name in self.projects and project_index <= len(self.projects[student_name]):
            del self.projects[student_name][project_index - 1]
            print("Project deleted successfully.")
        else:
            print("Invalid project index.")

# Example usage:
project_manager = UniversityProject()

# Adding projects
project_manager.add_project("Alice", "Python Chatbot", "Building a chatbot using Python.")
project_manager.add_project("Bob", "Web Development", "Creating a website using HTML, CSS, and JavaScript.")

# Viewing projects
project_manager.view_projects("Alice")
project_manager.view_projects("Bob")

# Deleting a project
project_manager.delete_project("Alice", 1)
project_manager.view_projects("Alice")

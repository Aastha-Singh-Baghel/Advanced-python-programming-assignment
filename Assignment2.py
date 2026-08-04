# Decorator for Header and Footer

def report_format(function):
    def wrapper(self):
        print("=" * 40)
        print("      STUDENT REPORT")
        print("=" * 40)

        function(self)

        print("=" * 40)
        print("      END OF REPORT")
        print("=" * 40)
    return wrapper

# Report Class

class Report:

    template = "Simple Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class Method
    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    # Magic Method
    def __str__(self):
        return f"Title : {self.title}\nContent : {self.content}"

    # Decorator Applied
    @report_format
    def display(self):
        print("Template :", Report.template)
        print(self)

# Main Program

print("===== Dynamic Report Generator =====")

title = input("Enter Report Title: ")
content = input("Enter Report Content: ")

report = Report(title, content)

print("\nChoose Report Template")
print("1. Simple Report")
print("2. Professional Report")

choice = input("Enter Choice (1/2): ")

if choice == "2":
    Report.change_template("Professional Report")
else:
    Report.change_template("Simple Report")

print("\nGenerated Report\n")
report.display()
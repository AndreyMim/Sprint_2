'''
📎 Напиши класс EmployeeSalary. Он рассчитывает почасовую заработную плату сотрудников за неделю.
С помощью переменной hourly_payment установи почасовой уровень оплаты, равный 400.
Проинициализируй атрибуты name, hours, rest_days, email через конструктор.
Добавь метод класса get_hours(). Если значение hours неизвестно, метод рассчитывает часы, исходя из количества выходных — rest_days. Формула для этого случая такая: (7 - rest_days) * 8.
Добавь метод класса get_email(). Если значение email неизвестно, метод генерирует его так: f"{name}@email.com".
Добавь метод класса set_hourly_payment(). Он меняет значение переменной hourly_payment.
Добавь метод расчёта заработной платы salary(). Формула расчёта такая: hours * hourly_payment.
'''

class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        return

    @classmethod
    def get_hours(cls, name = None, hours = None, rest_days = None, email = None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name = None, hours = None, rest_days = None, email = None):
        if email is None:
            email = f'{name}@email.com'
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment
        return

    def salary(self):
        return self.hours * self.hourly_payment

# Часы неизвестны — рассчитываются по выходным
emp1 = EmployeeSalary.get_hours(name="Andrey", rest_days=3)
print(emp1.hours)
print(emp1.salary())

# Email неизвестен — генерируется
emp2 = EmployeeSalary.get_email(name="Jane", hours=30)
print(emp2.email)
print(emp2.salary())

# Меняем почасовую оплату для всех
EmployeeSalary.set_hourly_payment(500)
print(emp1.salary())
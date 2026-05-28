# --- ТИПЫ ДАННЫХ ---
name = "Yusuf"  # str — текст
age = 17  # int — целое число
salary = 370.50  # float — дробное число
is_developer = False  # bool — True или False
result = None  # None — пусто, ничего


# --- ПОСМОТРИ ЧТО ВНУТРИ ---
print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Is Developer:", is_developer)
print("Result:", result)

# --- ПОСМОТРИ ТИП ---

print(type(name))
print(type(age))
print(type(salary))
print(type(is_developer))
print(type(result))

# --- Python СЧИТАЕТ ---

daily_hours = 2
monthly_days = 30
total_hours = daily_hours * monthly_days
print("Часов в месяц:", total_hours)

# --- СТРОКИ ---
first = "Python"
last = "Developer"
full = first + " " + last

print("Full name:", full)


# --- ПРАКТИКА ---
""" Создай переменные:
- твой город (строка)
- цель по накоплениям (число: 20000)
- текущий доход в долларах (370)
- сколько месяцев до цели (посчитай сам: 20000 / 370)
- ты уже разработчик? (False)

Выведи всё через print с подписями."""


city = "Dushanbe"
target = 20000
current_income = 370
months_to_goal = target / current_income
is_developer = False

print("Мой город", city)
print("Цель", target)
print("В долларх", current_income)
print("Месяцев до цели", months_to_goal)
print("Разработчик ли я?", is_developer)


# --- DEBUGGING ---

# print("Мне" + age + "лет")


# Ошибка: TypeError: can only concatenate str (not "int") to str

age = 17

# Способ 1 — преобразовать число в текст
print("Мне " + str(age) + " лет")

# Способ 2 — f-string (самый популярный в production)
print(f"Мне {age} лет")

# Способ 3 — через запятую
print("Мне", age, "лет")

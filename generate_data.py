import csv
from faker import Faker


fake = Faker("ru_RU")
Faker.seed(1)


with open(
    "data/users.csv",
    "w",
    newline="",
    encoding="utf-8",
) as file:
    writer = csv.writer(file)

    writer.writerow(
        [
            "first_name",
            "last_name",
            "email",
            "postcode",
        ]
    )

    for _ in range(10):
        writer.writerow(
            [
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                fake.postcode(),
            ]
        )


print("Файл data/users.csv успешно создан.")
print("Количество пользователей: 10")
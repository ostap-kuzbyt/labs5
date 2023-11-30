class Smartphone:
    def __init__(self, model, price, mobile_numbers, storage_capacity, battery_capacity):
        self.model = model
        self.price = price
        self.mobile_numbers = mobile_numbers
        self.storage_capacity = storage_capacity
        self.battery_capacity = battery_capacity


class PhoneStore:
    def __init__(self):
        self.inventory = []

    def add_phone(self, smartphone):
        self.inventory.append(smartphone)

    def get_phone_price(self,phone):
        return phone.price

    def find_best_phone(self, max_budget):
        affordable_phones = [
            phone for phone in self.inventory if phone.price <= max_budget]
        sorted_phones = sorted(affordable_phones, key=self.get_phone_price)

        return sorted_phones


phone1 = Smartphone("Model A", 500, ["123-456-7890", "987-654-3210"], 64, 3000)
phone2 = Smartphone("Model B", 700, ["555-123-4567", "111-222-3333"], 128, 4000)
phone3 = Smartphone("Model C", 400, ["999-888-7777", "444-555-6666"], 32, 2500)

store = PhoneStore()
store.add_phone(phone1)
store.add_phone(phone2)
store.add_phone(phone3)

max_budget = 600
print(f'max budget = {max_budget}')
best_phones = store.find_best_phone(max_budget)


print("Phones within budget:")
for phone in best_phones:
    print(f"Model: {phone.model}, Price: {phone.price}, Storage: {phone.storage_capacity}GB, Battery: {phone.battery_capacity}mAh")

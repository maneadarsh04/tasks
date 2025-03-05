class audi:
  def __init__(self,car_name,engine_type):
    self.car_name=car_name
    self.engine_type=engine_type

  def car_details(self):
    print(f"Car name: {self.car_name}")
    print(f"Engine type: {self.engine_type}")

obj = audi

while True:
  print("1. R8\n2. A4\n3. Q7")
  car_choice = int(input("Enter your car choice: "))
  if car_choice > 3:
    print("Invalid choice")
    continue
  print("1. EV\n2. Petrol\n3. Diesel")
  engine_choice = int(input("Enter your engine choice: "))
  if engine_choice > 3:
    print("Invalid choice")
    continue
  if car_choice == 1 and engine_choice == 1:
    obj = audi("R8","EV")
    obj.car_details()
    break
  elif car_choice == 1 and engine_choice == 2:
    obj = audi("R8","Petrol")
    obj.car_details()
    break
  elif car_choice == 1 and engine_choice == 3:
    obj = audi("R8","Diesel")
    obj.car_details()
    break
  elif car_choice == 2 and engine_choice == 1:
    obj = audi("A4","EV")
    obj.car_details()
    break
  elif car_choice == 2 and engine_choice == 2:
    obj = audi("A4","Petrol")
    obj.car_details()
    break
  elif car_choice == 2 and engine_choice == 3:
    obj = audi("A4","Diesel")
    obj.car_details()
    break
  elif car_choice == 3 and engine_choice == 1:
    obj = audi("Q7","EV")
    obj.car_details()
    break
  elif car_choice == 3 and engine_choice == 2:
    obj = audi("Q7","Petrol")
    obj.car_details()
    break
  elif car_choice == 3 and engine_choice == 3:
    obj = audi("Q7","Diesel")
    obj.car_details()
    break
  else:
    print("Invalid choice")
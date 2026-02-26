class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis

    def sound(self):
        return "suara"
    

class Motorcycle(Vehicle):
    def __init__(self, merk, tahun_rilis, harga):
        super().__init__("Motor", merk, tahun_rilis)
        self.__price = harga
    
    def get_price(self):
        return self.__price
    
    def set_price(self, harga_baru):
        self.__price = harga_baru
        print(f"Harga Motor diubah menjadi: {harga_baru}")


class Car(Vehicle):
    def __init__(self, merk, tahun_rilis, harga):
        super().__init__("Mobil", merk, tahun_rilis)
        self.__price = harga

    def get_price(self):
        return self.__price
    
    def set_price(self, harga_baru):
        self.__price = harga_baru
        print(f"Harga Mobil diubah menjadi: {harga_baru}")


sepeda = Vehicle("Sepeda", "Polygon", 2025)
motor1 = Motorcycle("Yamaha", 2020, 20000000)
mobil1 = Car("Honda", 2021, 200000000)

print(sepeda.sound())

print(mobil1.get_price())
print(motor1.get_price())

motor1.set_price(18000000)
motor1.set_price(170000000)

print(mobil1.get_price())
print(motor1.get_price())
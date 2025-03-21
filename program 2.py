from abc import ABC, abstractmethod

class Gaji_Karyawan(ABC):
    @abstractmethod
    def gaji(self):
        pass
    @abstractmethod
    def pajak(self):
        pass
    @abstractmethod
    def gaji_bersih(self):
        pass

class Karyawan_Tetap(Gaji_Karyawan):
    def __init__(self, gaji_pokok, tunjangan, potongan_pajak):
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan
        self.potongan_pajak = potongan_pajak

    def gaji(self):
        return self.gaji_pokok + self.tunjangan
    
    def pajak(self):
        return (self.potongan_pajak/100) * self.gaji()
    
    def gaji_bersih(self):
        gaji_diterima = float(self.gaji() - self.pajak())
        return gaji_diterima
    
class Freelancer(Gaji_Karyawan):
    def __init__(self, tarif_per_jam, total_jam, potongan_pajak):
        self.tarif_per_jam = tarif_per_jam
        self.total_jam = total_jam
        self.potongan_pajak = potongan_pajak

    def gaji(self):
        return self.tarif_per_jam * self.total_jam
    
    def pajak(self):
        return (self.potongan_pajak/100) * self.gaji()
    
    def gaji_bersih(self):
        gaji_diterima = float(self.gaji() - self.pajak())
        return gaji_diterima

aldo = Karyawan_Tetap(2000000, 500000, 2)
ali = Freelancer(200000, 8, 2)

print("===== Karyawan Tetap =====")
print(f"Gaji pokok dan Tunjangan: Rp {aldo.gaji():,.2f}")
print("Potongan pajak:", aldo.potongan_pajak, "%" )
print(f"\nGaji Bersih => Rp {aldo.gaji_bersih():,.2f}")

print("\n===== Freelancer =====")
print(f"Upah harian: Rp {ali.gaji():,.2f}")
print("Potongan pajak:", ali.potongan_pajak, "%" )
print(f"\nGaji Bersih => Rp {ali.gaji_bersih():,.2f}")


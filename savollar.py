from file_handlers import file_writer

data = """
# 1) txt fayl o`quvchi va uni ichidagi so'zlarni sonni qaytaruvchi raqamni yozing. 

# 2) txt fayl o`quvchi va uni ichidagi so'zlarni eng kattasini qaytaruvchi kod yoizing. 

# 3) raqamlardan iborat list bor. Ushbu listni ichidagi raqamlarni o`shish holatiga ko`ra buzilganlik holatini topuvchi va o`sha buzilgan raqamni qaytaruvchi kod yozing 

# 4) sizda listni ichida ma`lumotlar bor, shularning ichida gmaillarni saralovchi kod yozing --- barcha javoblarni git-hubga yuklab repository linkini ERPGa yuklash
"""
file_writer('savollar.txt', data)
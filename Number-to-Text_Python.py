def number_to_thai_text(number):
    # Thai number words
    units = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    tens = ["", "สิบ", "ยี่สิบ", "สามสิบ", "สี่สิบ", "ห้าสิบ", "หกสิบ", "เจ็ดสิบ", "แปดสิบ", "เก้าสิบ"]
    places = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

    def num_to_text(num):
        if num == 0:
            return ""
        elif num < 0:
            return "ลบ" + num_to_text(-num)

        words = []
        digit = 0
        while num > 0:
            if digit == 6:  # switch to million place
                words.append("ล้าน")
                digit = 0
            n = num % 10
            if digit == 1 and n == 1:
                words.append("เอ็ด")
            elif digit == 1 and n == 2:
                words.append("ยี่")
            elif digit == 1 and n == 0:
                words.append(tens[0])
            elif digit > 0:
                words.append(units[n] + places[digit])
            else:
                words.append(units[n])
            num //= 10
            digit += 1

        words.reverse()
        return "".join(words)

    baht_text = num_to_text(int(number)) or "ศูนย์"
    satang = int(round((number - int(number)) * 100))
    
    if satang == 0:
        return baht_text + "บาทถ้วน"
    else:
        satang_text = num_to_text(satang)
        return baht_text + "บาท" + satang_text + "สตางค์"

# รับค่า input จากผู้ใช้
try:
    user_input = float(input("กรุณากรอกจำนวนเงิน: "))
    print(number_to_thai_text(user_input))
except ValueError:
    print("กรุณากรอกจำนวนเงินในรูปแบบที่ถูกต้อง")

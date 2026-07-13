# Unit Converter Project

# =====================================================
# 0. HEADING FUNCTION (used by every converter)
# =====================================================
def display_heading(title):
    print("=========================================")
    print(title)
    print("=========================================")


# =====================================================
# 1. LENGTH CONVERTER
# =====================================================
def length_converter():
    display_heading("LENGTH CONVERTER")

    meters = float(input("Enter meters: "))

    kilometers = meters / 1000
    centimeters = meters * 100
    millimeters = meters * 1000
    feet = meters * 3.28084
    inches = meters * 39.3701
    miles = meters * 0.000621371

    print("----------------------------")
    print(meters, "meters")
    print(round(kilometers, 5), "kilometers")
    print(round(centimeters, 2), "centimeters")
    print(round(millimeters, 2), "millimeters")
    print(round(feet, 2), "feet")
    print(round(inches, 2), "inches")
    print(round(miles, 5), "miles")
    print("----------------------------")


# =====================================================
# 2. WEIGHT CONVERTER
# =====================================================
def weight_converter():
    display_heading("WEIGHT CONVERTER")

    kilograms = float(input("Enter kilograms: "))

    grams = kilograms * 1000
    milligrams = kilograms * 1_000_000
    pounds = kilograms * 2.20462

    print("----------------------------")
    print("Kilograms  :", kilograms)
    print("Grams      :", round(grams, 2))
    print("Milligrams :", round(milligrams, 2))
    print("Pounds     :", round(pounds, 2))
    print("----------------------------")


# =====================================================
# 3. TEMPERATURE CONVERTER
# =====================================================
def temperature_converter():
    display_heading("TEMPERATURE CONVERTER")

    celsius = float(input("Enter Celsius: "))

    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15

    print("----------------------------")
    print("Celsius    :", celsius)
    print("Fahrenheit :", round(fahrenheit, 2))
    print("Kelvin     :", round(kelvin, 2))
    print("----------------------------")


# =====================================================
# 4. TIME CONVERTER
# =====================================================
def time_converter():
    display_heading("TIME CONVERTER")

    hours = float(input("Enter Hours: "))

    minutes = hours * 60
    seconds = hours * 3600

    print("----------------------------")
    print("Hours   :", hours)
    print("Minutes :", round(minutes, 2))
    print("Seconds :", round(seconds, 2))
    print("----------------------------")


# =====================================================
# BONUS 1: SPEED CONVERTER
# =====================================================
def speed_converter():
    display_heading("SPEED CONVERTER")

    kmh = float(input("Enter speed in km/h: "))

    ms = kmh / 3.6
    mph = kmh * 0.621371

    print("----------------------------")
    print("Km/h            :", kmh)
    print("Meters/second   :", round(ms, 2))
    print("Miles/hour      :", round(mph, 2))
    print("----------------------------")


# =====================================================
# BONUS 2: AREA CONVERTER
# =====================================================
def area_converter():
    display_heading("AREA CONVERTER")

    sq_meters = float(input("Enter area in square meters: "))

    sq_km = sq_meters / 1_000_000
    sq_feet = sq_meters * 10.7639

    print("----------------------------")
    print("Square meters    :", sq_meters)
    print("Square kilometers:", round(sq_km, 8))
    print("Square feet      :", round(sq_feet, 2))
    print("----------------------------")


# =====================================================
# BONUS 3: VOLUME CONVERTER
# =====================================================
def volume_converter():
    display_heading("VOLUME CONVERTER")

    litres = float(input("Enter volume in litres: "))

    millilitres = litres * 1000
    cubic_meters = litres / 1000

    print("----------------------------")
    print("Litres       :", litres)
    print("Millilitres  :", round(millilitres, 2))
    print("Cubic meters :", round(cubic_meters, 5))
    print("----------------------------")


# =====================================================
# BONUS 4: DATA STORAGE CONVERTER
# =====================================================
def data_storage_converter():
    display_heading("DATA STORAGE CONVERTER")

    gb = float(input("Enter size in GB: "))

    mb = gb * 1024
    kb = mb * 1024
    bytes_ = kb * 1024
    tb = gb / 1024

    print("----------------------------")
    print("GB    :", gb)
    print("MB    :", round(mb, 2))
    print("KB    :", round(kb, 2))
    print("Bytes :", round(bytes_, 2))
    print("TB    :", round(tb, 6))
    print("----------------------------")


# =====================================================
# MAIN MENU (just a printed banner for now --
# real menus with "if" come in a later lesson!)
# =====================================================
display_heading("UNIVERSAL UNIT CONVERTER")

print("1. Length Converter")
print("2. Weight Converter")
print("3. Temperature Converter")
print("4. Time Converter")
print("5. Speed Converter (bonus)")
print("6. Area Converter (bonus)")
print("7. Volume Converter (bonus)")
print("8. Data Storage Converter (bonus)")
print("=========================================")

# -----------------------------------------------------
# Since you don't know "if" statements yet, uncomment
# ONE function call below at a time to test it.
# (Remove the "#" from the start of the line to run it.)
# -----------------------------------------------------

length_converter()
weight_converter()
temperature_converter()
time_converter()
speed_converter()
area_converter()
volume_converter()
data_storage_converter()

print("Thank You!")
print("=========================================")
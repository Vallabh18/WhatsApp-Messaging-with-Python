import pywhatkit as kit

kit.add_driver_path('chromedriver.exe')
#here in local directory

kit.load_QRcode()
#to load the qr code that you need to scan

kit.sendwhatmsg('+91907*******','Hey Buddy!',11,30)
#phone number,message and time-hours,mins
#hours are in 24 hrs format.

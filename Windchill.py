# File: WindChill.py
# Student: Todd Sakai
# UT EID: tfs523
# Course Name: CS303E
# 
# Date: 9/15/25
# Description of Program: Takes the temperature in fahrenheit and the wind speed in miles per hour then gives back the calculated wind chill in fahrenheit and celcius

def main():
    f_t=float(input('Enter Fahrenheit temperature:'))
    mph_wspeed=float(input('Enter wind speed in miles per hour:'))
    f_wchill=(35.74 + 0.6215*f_t - 35.75*mph_wspeed**0.16 + 0.4275*f_t*mph_wspeed**0.16)
    c_t=(f_t - 32)*5/9
    kph_wspeed=(mph_wspeed*1.60934)
    c_wchill=(f_wchill - 32)*5/9

    print()
    print('Fahrenheit report')
    print(' ','Temperature:',format(f_t,'9.3f'),'\u00B0' + 'F')
    print(' ','Wind speed:',format(mph_wspeed,'9.3f'),'mph')
    print(' ','Wind chill:',format(f_wchill,'9.3f'),'\u00B0' + 'F')

    print()
    print('Celcius report')
    print(' ','Temperature:',format(c_t,'9.3f'),'\u00B0' + 'C')
    print(' ','Wind speed:',format(kph_wspeed,'9.3f'),'kph')
    print(' ','Wind chill:',format(c_wchill,'9.3f'),'\u00B0' + 'C')

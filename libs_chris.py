
## my library functions
##
## Created by: Chris
##


# simple function to fetch information from the internet
# 
def get_url(url):
    import requests

    r = requests.get(url)
    return r


# get RGB value for a HSV colour
def HSV2RGB(hue,sat=255,val=255):
      
    if hue >= 65536:
        hue %= 65536

    hue = (hue * 1530 + 32768) // 65536
    if hue < 510:
        b = 0
        if hue < 255:
            r = 255
            g = hue
        else:
            r = 510 - hue
            g = 255
    elif hue < 1020:
        r = 0
        if hue < 765:
            g = 255
            b = hue - 510
        else:
            g = 1020 - hue
            b = 255
    elif hue < 1530:
        g = 0
        if hue < 1275:
            r = hue - 1020
            b = 255
        else:
            r = 255
            b = 1530 - hue
    else:
        r = 255
        g = 0
        b = 0

    v1 = 1 + val
    s1 = 1 + sat
    s2 = 255 - sat

    r = ((((r * s1) >> 8) + s2) * v1) >> 8
    g = ((((g * s1) >> 8) + s2) * v1) >> 8
    b = ((((b * s1) >> 8) + s2) * v1) >> 8

    return r, g, b


# this code below is used to test any functions above.
# 
if __name__ == "__main__":
    print("testing:", __name__)
    response = get_url("http://www.bbc.co.uk")

    if response.status_code == 200:
        print("web page opened correctly")

        print("###### BBC Home page #######")
        print(response.text)
              


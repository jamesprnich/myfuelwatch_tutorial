
import itertools


def gen_fuelwatch_urls(fueltypes, regions):

    fuelwatch_urls = [
        "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={}&Region={}".format(*i)
        for i in itertools.product(fueltypes, regions)
    ]

    print("# of URLs to process: " + str(len(fuelwatch_urls)))
    return fuelwatch_urls


# ==Configuration Settings===========
# Fuelwatch API codes are located here: https://www.fuelwatch.wa.gov.au/fuelwatch/pages/public/contentholder.jspx?key=fuelwatchRSS.html
fueltypes = [11, 4, ]  # 11 = Brand Diesel
regions = [2, ]  # 2 = Broome

fuelwatch_urls = gen_fuelwatch_urls(fueltypes, regions)
print(fuelwatch_urls)


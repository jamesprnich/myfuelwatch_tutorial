
from lxml import objectify
import requests
import itertools
import datetime


def gen_fuelwatch_urls(fueltypes, regions, dates):

    # fuelwatch_urls = [
    #     "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={}&Region={}&Day={}".format(*i)
    #     for i in itertools.product(fueltypes, regions, dates)
    # ]
    #
    # print("# of URLs to process: " + str(len(fuelwatch_urls)))
    # return fuelwatch_urls

    fuelwatch_urls_list = [
        ("http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={}&Region={}&Day={}".format(*i), i[0])
        for i in itertools.product(fueltypes, regions, dates)
    ]

    print("# of URLs to process: " + str(len(fuelwatch_urls_list)))
    print("urls as tuple: " + str(fuelwatch_urls_list))
    return fuelwatch_urls_list  # [('url',1),('url2',2)]


def get_fueldata(fueltypes, regions, dates):

    fuelwatch_urls = gen_fuelwatch_urls(fueltypes, regions, dates)

    list_of_dicts = []

    for each_url in fuelwatch_urls:
        print(each_url[0])
        fuelprice_data = requests.get(each_url[0])

        root = objectify.fromstring(fuelprice_data.content)

        if hasattr(root.channel, 'item'):
            for each_item in root.channel.item:

                dict_data = {
                    'Price': each_item.price.text,
                    'Location': each_item.location.text,
                    'Address': each_item.address.text,
                    'Phone': each_item.phone.text,
                    'Brand': each_item.brand.text,
                    'Date': each_item.date.text,
                    'Fueltype': each_url[1]
                }

                list_of_dicts.append(dict_data)
    return list_of_dicts


# ==Configuration Settings===========
# Fuelwatch API codes are located here: https://www.fuelwatch.wa.gov.au/fuelwatch/pages/public/contentholder.jspx?key=fuelwatchRSS.html
fueltypes = [11, 4, 5, ]  # 11 = Brand Diesel
regions = [2, ]  # 2 = Broome
dates = ['18/04/2018', '19/04/2018']

# Call the function to get fuel data
list_of_dicts = get_fueldata(fueltypes, regions, dates)

list_of_dicts_sorted = sorted(list_of_dicts, key=lambda k: k['Price'], reverse=False)
print("Dict Sorted: " + str(list_of_dicts_sorted))

list_of_dicts_sorted = sorted(list_of_dicts, key=lambda k: k['Price'], reverse=True)
print("Dict Sorted (reversed): " + str(list_of_dicts_sorted))

# Gen HTML
table_content = ''

for each_row in list_of_dicts_sorted:
    # datetime.strptime(each_row['Date'], '%Y-%m-%d')

    if datetime.datetime.strptime(each_row['Date'], '%Y-%m-%d') > datetime.datetime.today():
        css_class = 'table-info'
    else:
        css_class = ''

    table_row = "<tr class='" + css_class + "'><td>{Price}</td><td>{Location}</td><td>{Address}</td><td>{Phone}</td><td>{Brand}</td><td>{Date}</td><td>{Fueltype}</td></tr>".format(**each_row)
    table_content = table_content + table_row

# Create contents of html page
html_content = """<html>
                  <head>
                      <title>Fuel Watch</title>
                        <script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous'></script>
                        <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css' integrity='sha256-LA89z+k9fjgMKQ/kq4OO2Mrf8VltYml/VES+Rg0fh20=' crossorigin='anonymous'>
                        <script src='https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js' integrity='sha256-5+02zu5UULQkO7w1GIr6vftCgMfFdZcAHeDtFnKZsBs=' crossorigin='anonymous'></script>
                     </head>
                  <body>
                      <h2>Fuel Prices For all metro regions</h2>
                       <table border = '1' class='table table-sm'>
                       <thead>
                              <tr>
                                 <th>Price</th>
                                 <th>Location</th>
                                 <th>Address</th>
                                 <th>Phone</th>
                                 <th>Brand</th>
                                 <th>Date</th>
                                 <th>FuelType</th>
                               </tr>
                         </thead>
                        <tbody>
                            {0}
                        </tbody>
                    </table>
                  </body>
              </html>""".format(table_content)

# Open File to create HTML file
# using "With"  statement , no need to close the file explictly
with open('fuelwatch_tutorial_v4_part1.html', 'w') as f:
    f.write(html_content)

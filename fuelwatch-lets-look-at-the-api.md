# Fuelwatch - Lets look at the API

### Fuelwatch Website

[https://www.fuelwatch.wa.gov.au](https://www.fuelwatch.wa.gov.au/)

### Fuelwatch API

Fuelwatch provide documentation on how to use their API [here](https://www.fuelwatch.wa.gov.au/fuelwatch/pages/public/contentholder.jspx?key=fuelwatchRSS.html). The Fuelwatch API returns data in [XML](untitled-1.md#xml) format.

### Fuelwatch API example result

You can test this out yourself. Open the link below in Google Chrome and see what you get as a result. It should look similar to the API Result below.

API url: [http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale&Surrounding=no](http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale&Surrounding=no)

{% code-tabs %}
{% code-tabs-item title="API Result" %}
```markup
<rss version="2.0">
    <channel>
        <title>FuelWatch Prices For Cloverdale</title>
        <ttl>720</ttl>
        <link>http://www.fuelwatch.wa.gov.au</link>
        <description>09/04/2018 - Cloverdale</description>
        <language>en-us</language>
        <copyright>Copyright 2005 FuelWatch. All Rights Reserved.</copyright>
        <lastBuildDate>
            Mon Apr 09 12:45:04 WST 2018Mon Apr 09 12:45:04 WST 2018
        </lastBuildDate>
        <image>
            <url>/fuelwatch/art/fuelwatch-logo.gif</url>
            <title>FuelWatch</title>
            <link>http://www.fuelwatch.wa.gov.au</link>
        </image>
        <item>
            <title>129.9: Coles Express Cloverdale</title>
            <description>
                Address: 223 Belmont Ave (Cnr Wright St), CLOVERDALE, Phone: (08) 9277 1660
            </description>
            <brand>Coles Express</brand>
            <date>2018-04-09</date>
            <price>129.9</price>
            <trading-name>Coles Express Cloverdale</trading-name>
            <location>CLOVERDALE</location>
            <address>223 Belmont Ave (Cnr Wright St)</address>
            <phone>(08) 9277 1660</phone>
            <latitude>-31.965057</latitude>
            <longitude>115.933164</longitude>
            <site-features>,</site-features>
        </item>
    </channel>
</rss>
```
{% endcode-tabs-item %}
{% endcode-tabs %}


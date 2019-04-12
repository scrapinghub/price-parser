# -*- coding: utf-8 -*-
"""
Currency information.

``CURRENCIES`` data is from https://github.com/StorePilot/coinify,
which is supposed to provide combined data from

* https://gist.github.com/Fluidbyte/2973986
* https://en.wikipedia.org/wiki/ISO_4217
* http://www.iotafinance.com/en/ISO-4217-Currency-Codes.html
* http://www.xe.com/symbols.php

Field meaning:

* s - currency main symbol
* n - currency name  (currently unused)
* sn - currency native symbol
* d - decimal digits (currently unused)
* r - rounding (currently unused)
* np - currency name, plural (currently unused)
* sn2 - other currency symbols

Some extra abbreviations are added to the list (they are set below
``CURRENCIES`` variable, scroll to the bottom).
"""
from typing import List, Dict
from itertools import chain


CURRENCIES: Dict[str, Dict] = {
    "AED": {
        "s": "AED",
        "n": "United Arab Emirates Dirham",
        "sn": "د.إ.‏",
        "d": 2,
        "r": 0,
        "np": "UAE dirhams"
    },
    "AFN": {
        "s": "Af",
        "n": "Afghan Afghani",
        "sn": "؋",
        "d": 0,
        "r": 0,
        "np": "Afghan Afghanis"
    },
    "ALL": {
        "s": "ALL",
        "n": "Albanian Lek",
        "sn": "Lek",
        "d": 0,
        "r": 0,
        "np": "Albanian lekë"
    },
    "AMD": {
        "s": "AMD",
        "n": "Armenian Dram",
        "sn": "դր.",
        "d": 0,
        "r": 0,
        "np": "Armenian drams"
    },
    "ANG": {
        "s": "ƒ",
        "n": "Netherlands Antilles Guilder",
        "sn": "ƒ",
        "d": 2,
        "r": 0,
        "np": "Netherlands Antilles Guilder"
    },
    "AOA": {
        "s": "Kz",
        "n": "Angolan kwanza",
        "sn": "Kz",
        "d": 2,
        "r": 0,
        "np": "Angolan kwanza"
    },
    "ARS": {
        "s": "AR$",
        "n": "Argentine Peso",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Argentine pesos"
    },
    "AUD": {
        "s": "AU$",
        "n": "Australian Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Australian dollars"
    },
    "AWG": {
        "s": "ƒ",
        "n": "Aruban Guilder",
        "sn": "ƒ",
        "d": 2,
        "r": 0,
        "np": "Aruban Guilders"
    },
    "AFL": {
        "s": "Afl.",
        "n": "Aruban Florin",
        "sn": "Afl.",
        "d": 2,
        "r": 0,
        "np": "Aruban Florins"
    },
    "AZN": {
        "s": "man.",
        "n": "Azerbaijani Manat",
        "sn": "ман.",
        "d": 2,
        "r": 0,
        "np": "Azerbaijani manats"
    },
    "BAM": {
        "s": "KM",
        "n": "Bosnia-Herzegovina Convertible Mark",
        "sn": "KM",
        "d": 2,
        "r": 0,
        "np": "Bosnia-Herzegovina convertible marks"
    },
    "BDT": {
        "s": "Tk",
        "n": "Bangladeshi Taka",
        "sn": "৳",
        "d": 2,
        "r": 0,
        "np": "Bangladeshi takas"
    },
    "BBD": {
        "s": "Bds$",
        "n": "Barbados dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Barbados dollar"
    },
    "BGN": {
        "s": "BGN",
        "n": "Bulgarian Lev",
        "sn": "лв.",
        "d": 2,
        "r": 0,
        "np": "Bulgarian leva"
    },
    "BHD": {
        "s": "BD",
        "n": "Bahraini Dinar",
        "sn": "د.ب.‏",
        "d": 3,
        "r": 0,
        "np": "Bahraini dinars"
    },
    "BIF": {
        "s": "FBu",
        "n": "Burundian Franc",
        "sn": "FBu",
        "d": 0,
        "r": 0,
        "np": "Burundian francs"
    },
    "BSD": {
        "s": "$",
        "n": "Bahamas Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Bahamas Dollar"
    },
    "BMD": {
        "s": "$",
        "n": "Bermuda Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Bermuda Dollars"
    },
    "BND": {
        "s": "BN$",
        "n": "Brunei Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Brunei dollars"
    },
    "BOB": {
        "s": "Bs",
        "n": "Bolivian Boliviano",
        "sn": "Bs",
        "d": 2,
        "r": 0,
        "np": "Bolivian bolivianos"
    },
    "BOV": {
        "s": "-",
        "n": "Bolivian Mvdol",
        "sn": "-",
        "d": 2,
        "r": 0,
        "np": "Bolivian Mvdol"
    },
    "BRL": {
        "s": "R$",
        "n": "Brazilian Real",
        "sn": "R$",
        "d": 2,
        "r": 0,
        "np": "Brazilian reals"
    },
    "BTN": {
        "s": "Nu.",
        "n": "Bhutanese ngultrum",
        "sn": "Nu.",
        "d": 2,
        "r": 0,
        "np": "Bhutanese ngultrum"
    },
    "BWP": {
        "s": "BWP",
        "n": "Botswanan Pula",
        "sn": "P",
        "d": 2,
        "r": 0,
        "np": "Botswanan pulas"
    },
    "BYN": {
        "s": "Br",
        "n": "Belarusian Ruble",
        "sn": "Br",
        "d": 0,
        "r": 0,
        "np": "Belarusian rubles"
    },
    "BZD": {
        "s": "BZ$",
        "n": "Belize Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Belize dollars"
    },
    "CAD": {
        "s": "CA$",
        "n": "Canadian Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Canadian dollars"
    },
    "CDF": {
        "s": "CDF",
        "n": "Congolese Franc",
        "sn": "FrCD",
        "d": 2,
        "r": 0,
        "np": "Congolese francs"
    },
    "CHE": {
        "s": "-",
        "n": "WIR Euro (complementary currency)",
        "sn": "-",
        "d": 2,
        "r": 0,
        "np": "WIR Euros (complementary currency)"
    },
    "CHF": {
        "s": "CHF",
        "n": "Swiss Franc",
        "sn": "CHF",
        "d": 2,
        "r": 0.05,
        "np": "Swiss francs"
    },
    "CHW": {
        "s": "-",
        "n": "WIR Franc (complementary currency)",
        "sn": "-",
        "d": 2,
        "r": 0,
        "np": "WIR Franc (complementary currency)"
    },
    "CLF": {
        "s": "UF",
        "n": "Unidad de Fomento (funds code)",
        "sn": "UF",
        "d": 4,
        "r": 0,
        "np": "Unidad de Fomento (funds code)"
    },
    "CLP": {
        "s": "CL$",
        "n": "Chilean Peso",
        "sn": "$",
        "d": 0,
        "r": 0,
        "np": "Chilean pesos"
    },
    "CNY": {
        "s": "CN¥",
        "n": "Chinese Yuan",
        "sn": "CN¥",
        "d": 2,
        "r": 0,
        "np": "Chinese yuan"
    },
    "COP": {
        "s": "CO$",
        "n": "Colombian Peso",
        "sn": "$",
        "d": 0,
        "r": 0,
        "np": "Colombian pesos"
    },
    "COU": {
        "s": "-",
        "n": "Unidad de Valor Real (UVR) (funds code)",
        "sn": "-",
        "d": 2,
        "r": 0,
        "np": "Unidad de Valor Real (UVR) (funds code)"
    },
    "CRC": {
        "s": "₡",
        "n": "Costa Rican Colón",
        "sn": "₡",
        "d": 0,
        "r": 0,
        "np": "Costa Rican colóns"
    },
    "CUC": {
        "s": "CUC$",
        "n": "Cuban convertible peso",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Cuban convertible pesos"
    },
    "CUP": {
        "s": "₱",
        "n": "Cuba Peso",
        "sn": "₱",
        "d": 0,
        "r": 0,
        "np": "Cuba Pesos"
    },
    "CVE": {
        "s": "CV$",
        "n": "Cape Verdean Escudo",
        "sn": "CV$",
        "d": 0,
        "r": 0,
        "np": "Cape Verdean escudos"
    },
    "CZK": {
        "s": "Kč",
        "n": "Czech Republic Koruna",
        "sn": "Kč",
        "d": 2,
        "r": 0,
        "np": "Czech Republic korunas"
    },
    "DJF": {
        "s": "Fdj",
        "n": "Djiboutian Franc",
        "sn": "Fdj",
        "d": 0,
        "r": 0,
        "np": "Djiboutian francs"
    },
    "DKK": {
        "s": "Dkr",
        "n": "Danish Krone",
        "sn": "kr",
        "d": 2,
        "r": 0,
        "np": "Danish kroner"
    },
    "DOP": {
        "s": "RD$",
        "n": "Dominican Peso",
        "sn": "RD$",
        "d": 2,
        "r": 0,
        "np": "Dominican pesos"
    },
    "DZD": {
        "s": "DA",
        "n": "Algerian Dinar",
        "sn": "د.ج.‏",
        "d": 2,
        "r": 0,
        "np": "Algerian dinars"
    },
    "EEK": {
        "s": "Ekr",
        "n": "Estonian Kroon",
        "sn": "kr",
        "d": 2,
        "r": 0,
        "np": "Estonian kroons"
    },
    "EGP": {
        "s": "EGP",
        "n": "Egyptian Pound",
        "sn": "ج.م.‏",
        "d": 2,
        "r": 0,
        "np": "Egyptian pounds"
    },
    "ERN": {
        "s": "Nfk",
        "n": "Eritrean Nakfa",
        "sn": "Nfk",
        "d": 2,
        "r": 0,
        "np": "Eritrean nakfas"
    },
    "ETB": {
        "s": "Br",
        "n": "Ethiopian Birr",
        "sn": "Br",
        "d": 2,
        "r": 0,
        "np": "Ethiopian birrs"
    },
    "EUR": {
        "s": "€",
        "n": "Euro",
        "sn": "€",
        "d": 2,
        "r": 0,
        "np": "euros"
    },
    "FJD": {
        "s": "$",
        "n": "Fiji Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Fiji Dollars"
    },
    "FKP": {
        "s": "£",
        "n": "Falkland Islands (Malvinas) Pound",
        "sn": "£",
        "d": 2,
        "r": 0,
        "np": "Falkland Islands (Malvinas) Pound"
    },
    "GBP": {
        "s": "£",
        "n": "British Pound Sterling",
        "sn": "£",
        "d": 2,
        "r": 0,
        "np": "British pounds sterling"
    },
    "GEL": {
        "s": "GEL",
        "n": "Georgian Lari",
        "sn": "GEL",
        "d": 2,
        "r": 0,
        "np": "Georgian laris"
    },
    "GGP": {
        "s": "£",
        "n": "Guernsey Pound",
        "sn": "£",
        "d": 2,
        "r": 0,
        "np": "Guernsey Pounds"
    },
    "GHS": {
        "s": "GH₵",
        "n": "Ghanaian Cedi",
        "sn": "GH₵",
        "d": 2,
        "r": 0,
        "np": "Ghanaian cedis"
    },
    "GIP": {
        "s": "£",
        "n": "Gibraltar Pound",
        "sn": "£",
        "d": 2,
        "r": 0,
        "np": "Gibraltar Pounds"
    },
    "GMD": {
        "s": "D",
        "n": "Gambian dalasi",
        "sn": "D",
        "d": 2,
        "r": 0,
        "np": "Gambian dalasi"
    },
    "GNF": {
        "s": "FG",
        "n": "Guinean Franc",
        "sn": "FG",
        "d": 0,
        "r": 0,
        "np": "Guinean francs"
    },
    "GTQ": {
        "s": "GTQ",
        "n": "Guatemalan Quetzal",
        "sn": "Q",
        "d": 2,
        "r": 0,
        "np": "Guatemalan quetzals"
    },
    "GYD": {
        "s": "$",
        "n": "Guyana Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Guyana Dollars"
    },
    "HKD": {
        "s": "HK$",
        "n": "Hong Kong Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Hong Kong dollars"
    },
    "HNL": {
        "s": "HNL",
        "n": "Honduran Lempira",
        "sn": "L",
        "d": 2,
        "r": 0,
        "np": "Honduran lempiras"
    },
    "HRK": {
        "s": "kn",
        "n": "Croatian Kuna",
        "sn": "kn",
        "d": 2,
        "r": 0,
        "np": "Croatian kunas"
    },
    "HTG": {
        "s": "G",
        "n": "Haitian gourde",
        "sn": "G",
        "d": 2,
        "r": 0,
        "np": "Haitian gourde"
    },
    "HUF": {
        "s": "Ft",
        "n": "Hungarian Forint",
        "sn": "Ft",
        "d": 0,
        "r": 0,
        "np": "Hungarian forints"
    },
    "IDR": {
        "s": "Rp",
        "n": "Indonesian Rupiah",
        "sn": "Rp",
        "d": 0,
        "r": 0,
        "np": "Indonesian rupiahs"
    },
    "ILS": {
        "s": "₪",
        "n": "Israeli New Sheqel",
        "sn": "₪",
        "d": 2,
        "r": 0,
        "np": "Israeli new sheqels"
    },
    "IMP": {
        "s": "£",
        "n": "Isle of Man Pound",
        "sn": "£",
        "d": 2,
        "r": 0,
        "np": "Isle of Man Pounds"
    },
    "INR": {
        "s": "Rs",
        "n": "Indian Rupee",
        "sn": "টকা",
        "d": 2,
        "r": 0,
        "np": "Indian rupees"
    },
    "IQD": {
        "s": "IQD",
        "n": "Iraqi Dinar",
        "sn": "د.ع.‏",
        "d": 3,
        "r": 0,
        "np": "Iraqi dinars"
    },
    "IRR": {
        "s": "IRR",
        "n": "Iranian Rial",
        "sn": "﷼",
        "d": 0,
        "r": 0,
        "np": "Iranian rials"
    },
    "ISK": {
        "s": "Ikr",
        "n": "Icelandic Króna",
        "sn": "kr",
        "d": 0,
        "r": 0,
        "np": "Icelandic krónur"
    },
    "JEP": {
        "s": "£",
        "n": "Jersey Pound",
        "sn": "£",
        "d": 2,
        "r": 0,
        "np": "Jersey Pounds"
    },
    "JMD": {
        "s": "J$",
        "n": "Jamaican Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Jamaican dollars"
    },
    "JOD": {
        "s": "JD",
        "n": "Jordanian Dinar",
        "sn": "د.أ.‏",
        "d": 3,
        "r": 0,
        "np": "Jordanian dinars"
    },
    "JPY": {
        "s": "¥",
        "n": "Japanese Yen",
        "sn": "￥",
        "d": 0,
        "r": 0,
        "np": "Japanese yen"
    },
    "KES": {
        "s": "Ksh",
        "n": "Kenyan Shilling",
        "sn": "Ksh",
        "d": 2,
        "r": 0,
        "np": "Kenyan shillings"
    },
    "KGS": {
        "s": "лв",
        "n": "Kyrgyzstan Som",
        "sn": "лв",
        "d": 2,
        "r": 0,
        "np": "Kyrgyzstan Som"
    },
    "KHR": {
        "s": "KHR",
        "n": "Cambodian Riel",
        "sn": "៛",
        "d": 2,
        "r": 0,
        "np": "Cambodian riels"
    },
    "KMF": {
        "s": "CF",
        "n": "Comorian Franc",
        "sn": "FC",
        "d": 0,
        "r": 0,
        "np": "Comorian francs"
    },
    "KPW": {
        "s": "₩",
        "n": "North Korean Won",
        "sn": "₩",
        "d": 0,
        "r": 0,
        "np": "North Korean Won"
    },
    "KRW": {
        "s": "₩",
        "n": "South Korean Won",
        "sn": "₩",
        "d": 0,
        "r": 0,
        "np": "South Korean won"
    },
    "KWD": {
        "s": "KD",
        "n": "Kuwaiti Dinar",
        "sn": "د.ك.‏",
        "d": 3,
        "r": 0,
        "np": "Kuwaiti dinars"
    },
    "KYD": {
        "s": "$",
        "n": "Cayman Islands Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Cayman Islands Dollars"
    },
    "KZT": {
        "s": "KZT",
        "n": "Kazakhstani Tenge",
        "sn": "тңг.",
        "d": 2,
        "r": 0,
        "np": "Kazakhstani tenges"
    },
    "LAK": {
        "s": "₭",
        "n": "Laos Kip",
        "sn": "₭",
        "d": 2,
        "r": 0,
        "np": "Laos Kip"
    },
    "LBP": {
        "s": "LB£",
        "n": "Lebanese Pound",
        "sn": "ل.ل.‏",
        "d": 0,
        "r": 0,
        "np": "Lebanese pounds"
    },
    "LKR": {
        "s": "SLRs",
        "n": "Sri Lankan Rupee",
        "sn": "SL Re",
        "d": 2,
        "r": 0,
        "np": "Sri Lankan rupees"
    },
    "LRD": {
        "s": "$",
        "n": "Liberia Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Liberia Dollars"
    },
    "LSL": {
        "s": "L",
        "n": "Lesotho loti",
        "sn": "L",
        "d": 2,
        "r": 0,
        "np": "Lesotho loti"
    },
    "LTL": {
        "s": "Lt",
        "n": "Lithuanian Litas",
        "sn": "Lt",
        "d": 2,
        "r": 0,
        "np": "Lithuanian litai"
    },
    "LVL": {
        "s": "Ls",
        "n": "Latvian Lats",
        "sn": "Ls",
        "d": 2,
        "r": 0,
        "np": "Latvian lati"
    },
    "LYD": {
        "s": "LD",
        "n": "Libyan Dinar",
        "sn": "د.ل.‏",
        "d": 3,
        "r": 0,
        "np": "Libyan dinars"
    },
    "MAD": {
        "s": "MAD",
        "n": "Moroccan Dirham",
        "sn": "د.م.‏",
        "d": 2,
        "r": 0,
        "np": "Moroccan dirhams"
    },
    "MDL": {
        "s": "MDL",
        "n": "Moldovan Leu",
        "sn": "MDL",
        "d": 2,
        "r": 0,
        "np": "Moldovan lei"
    },
    "MGA": {
        "s": "MGA",
        "n": "Malagasy Ariary",
        "sn": "MGA",
        "d": 0,
        "r": 0,
        "np": "Malagasy Ariaries"
    },
    "MKD": {
        "s": "MKD",
        "n": "Macedonian Denar",
        "sn": "MKD",
        "d": 2,
        "r": 0,
        "np": "Macedonian denari"
    },
    "MMK": {
        "s": "MMK",
        "n": "Myanma Kyat",
        "sn": "K",
        "d": 0,
        "r": 0,
        "np": "Myanma kyats"
    },
    "MNT": {
        "s": "₮",
        "n": "Mongolia Tughrik",
        "sn": "₮",
        "d": 2,
        "r": 0,
        "np": "Mongolia Tughrik"
    },
    "MOP": {
        "s": "MOP$",
        "n": "Macanese Pataca",
        "sn": "MOP$",
        "d": 2,
        "r": 0,
        "np": "Macanese patacas"
    },
    "MRO": {
        "s": "UM",
        "n": "Mauritanian ouguiya",
        "sn": "UM",
        "d": 1,
        "r": 0,
        "np": "Mauritanian ouguiya"
    },
    "MUR": {
        "s": "MURs",
        "n": "Mauritian Rupee",
        "sn": "MURs",
        "d": 0,
        "r": 0,
        "np": "Mauritian rupees"
    },
    "MVR": {
        "s": "MRf",
        "n": "Maldivian rufiyaa",
        "sn": "Rf",
        "d": 2,
        "r": 0,
        "np": "Maldivian rufiyaa"
    },
    "MWK": {
        "s": "MK",
        "n": "Malawian kwacha",
        "sn": "MK",
        "d": 2,
        "r": 0,
        "np": "Malawian kwacha"
    },
    "MXN": {
        "s": "MX$",
        "n": "Mexican Peso",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Mexican pesos"
    },
    "MXV": {
        "s": "-",
        "n": "Mexican Unidad de Inversion (UDI) (funds code)",
        "sn": "-",
        "d": 2,
        "r": 0,
        "np": "Mexican Unidad de Inversion (UDI) (funds code)"
    },
    "MYR": {
        "s": "RM",
        "n": "Malaysian Ringgit",
        "sn": "RM",
        "d": 2,
        "r": 0,
        "np": "Malaysian ringgits"
    },
    "MZN": {
        "s": "MTn",
        "n": "Mozambican Metical",
        "sn": "MTn",
        "d": 2,
        "r": 0,
        "np": "Mozambican meticals"
    },
    "NAD": {
        "s": "N$",
        "n": "Namibian Dollar",
        "sn": "N$",
        "d": 2,
        "r": 0,
        "np": "Namibian dollars"
    },
    "NGN": {
        "s": "₦",
        "n": "Nigerian Naira",
        "sn": "₦",
        "d": 2,
        "r": 0,
        "np": "Nigerian nairas"
    },
    "NIO": {
        "s": "C$",
        "n": "Nicaraguan Córdoba",
        "sn": "C$",
        "d": 2,
        "r": 0,
        "np": "Nicaraguan córdobas"
    },
    "NOK": {
        "s": "Nkr",
        "n": "Norwegian Krone",
        "sn": "kr",
        "d": 2,
        "r": 0,
        "np": "Norwegian kroner"
    },
    "NPR": {
        "s": "NPRs",
        "n": "Nepalese Rupee",
        "sn": "नेरू",
        "d": 2,
        "r": 0,
        "np": "Nepalese rupees"
    },
    "PRB": {
        "s": "руб",
        "n": "Transnistrian ruble",
        "sn": "руб",
        "d": 2,
        "r": 0,
        "np": "Transnistrian rubles"
    },
    "NZD": {
        "s": "NZ$",
        "n": "New Zealand Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "New Zealand dollars"
    },
    "OMR": {
        "s": "OMR",
        "n": "Omani Rial",
        "sn": "ر.ع.‏",
        "d": 3,
        "r": 0,
        "np": "Omani rials"
    },
    "PAB": {
        "s": "B/.",
        "n": "Panamanian Balboa",
        "sn": "B/.",
        "d": 2,
        "r": 0,
        "np": "Panamanian balboas"
    },
    "PEN": {
        "s": "S/.",
        "n": "Peruvian Nuevo Sol",
        "sn": "S/.",
        "d": 2,
        "r": 0,
        "np": "Peruvian nuevos soles"
    },
    "PGK": {
        "s": "K",
        "n": "Papua New Guinean kina",
        "sn": "K",
        "d": 2,
        "r": 0,
        "np": "Papua New Guinean kina"
    },
    "PHP": {
        "s": "₱",
        "n": "Philippine Peso",
        "sn": "₱",
        "d": 2,
        "r": 0,
        "np": "Philippine pesos"
    },
    "PKR": {
        "s": "PKRs",
        "n": "Pakistani Rupee",
        "sn": "₨",
        "d": 0,
        "r": 0,
        "np": "Pakistani rupees"
    },
    "PLN": {
        "s": "zł",
        "n": "Polish Zloty",
        "sn": "zł",
        "d": 2,
        "r": 0,
        "np": "Polish zlotys"
    },
    "PYG": {
        "s": "₲",
        "n": "Paraguayan Guarani",
        "sn": "₲",
        "d": 0,
        "r": 0,
        "np": "Paraguayan guaranis"
    },
    "QAR": {
        "s": "QR",
        "n": "Qatari Rial",
        "sn": "ر.ق.‏",
        "d": 2,
        "r": 0,
        "np": "Qatari rials"
    },
    "RON": {
        "s": "RON",
        "n": "Romanian Leu",
        "sn": "RON",
        "d": 2,
        "r": 0,
        "np": "Romanian lei"
    },
    "RSD": {
        "s": "din.",
        "n": "Serbian Dinar",
        "sn": "дин.",
        "d": 0,
        "r": 0,
        "np": "Serbian dinars"
    },
    "RUB": {
        "s": "RUB",
        "n": "Russian Ruble",
        "sn": "руб.",
        "d": 2,
        "r": 0,
        "np": "Russian rubles"
    },
    "RWF": {
        "s": "RWF",
        "n": "Rwandan Franc",
        "sn": "FR",
        "d": 0,
        "r": 0,
        "np": "Rwandan francs"
    },
    "SAR": {
        "s": "SR",
        "n": "Saudi Riyal",
        "sn": "ر.س.‏",
        "d": 2,
        "r": 0,
        "np": "Saudi riyals"
    },
    "SBD": {
        "s": "$",
        "n": "Solomon Islands Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Solomon Islands Dollars"
    },
    "SCR": {
        "s": "₨",
        "n": "Seychelles Rupee",
        "sn": "₨",
        "d": 2,
        "r": 0,
        "np": "Seychelles Rupees"
    },
    "SDG": {
        "s": "SDG",
        "n": "Sudanese Pound",
        "sn": "SDG",
        "d": 2,
        "r": 0,
        "np": "Sudanese pounds"
    },
    "SEK": {
        "s": "Skr",
        "n": "Swedish Krona",
        "sn": "kr",
        "d": 2,
        "r": 0,
        "np": "Swedish kronor"
    },
    "SGD": {
        "s": "S$",
        "n": "Singapore Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Singapore dollars"
    },
    "SHP": {
        "s": "£",
        "n": "Saint Helena Pound",
        "sn": "£",
        "d": 2,
        "r": 0,
        "np": "Saint Helena Pounds"
    },
    "SLL": {
        "s": "Le",
        "n": "Sierra Leonean leone",
        "sn": "Le",
        "d": 2,
        "r": 0,
        "np": "Sierra Leonean leone"
    },
    "SOS": {
        "s": "Ssh",
        "n": "Somali Shilling",
        "sn": "Ssh",
        "d": 0,
        "r": 0,
        "np": "Somali shillings"
    },
    "SRD": {
        "s": "$",
        "n": "Suriname Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Suriname Dollars"
    },
    "SSP": {
        "s": "SSP",
        "n": "South Sudanese pound",
        "sn": "SSP",
        "d": 2,
        "r": 0,
        "np": "South Sudanese pound"
    },
    "STD": {
        "s": "Db",
        "n": "São Tomé and Príncipe dobra",
        "sn": "Db",
        "d": 2,
        "r": 0,
        "np": "São Tomé and Príncipe dobra"
    },
    "SVC": {
        "s": "$",
        "n": "El Salvador Colon",
        "sn": "$",
        "d": 0,
        "r": 0,
        "np": "El Salvador Colon"
    },
    "SYP": {
        "s": "SY£",
        "n": "Syrian Pound",
        "sn": "ل.س.‏",
        "d": 0,
        "r": 0,
        "np": "Syrian pounds"
    },
    "SZL": {
        "s": "L",
        "n": "Swazi lilangeni",
        "sn": "L",
        "d": 2,
        "r": 0,
        "np": "Swazi lilangeni"
    },
    "THB": {
        "s": "฿",
        "n": "Thai Baht",
        "sn": "฿",
        "d": 2,
        "r": 0,
        "np": "Thai baht"
    },
    "TJS": {
        "s": "-",
        "n": "Tajikistani somoni",
        "sn": "-",
        "d": 2,
        "r": 0,
        "np": "Tajikistani somoni"
    },
    "TMT": {
        "s": "T",
        "n": "Turkmenistan manat",
        "sn": "T",
        "d": 2,
        "r": 0,
        "np": "Turkmenistan manat"
    },
    "TND": {
        "s": "DT",
        "n": "Tunisian Dinar",
        "sn": "د.ت.‏",
        "d": 3,
        "r": 0,
        "np": "Tunisian dinars"
    },
    "TOP": {
        "s": "T$",
        "n": "Tongan Paʻanga",
        "sn": "T$",
        "d": 2,
        "r": 0,
        "np": "Tongan paʻanga"
    },
    "TRY": {
        "s": "TL",
        "n": "Turkish Lira",
        "sn": "TL",
        "d": 2,
        "r": 0,
        "np": "Turkish Lira"
    },
    "TTD": {
        "s": "TT$",
        "n": "Trinidad and Tobago Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Trinidad and Tobago dollars"
    },
    "TVD": {
        "s": "$",
        "n": "Tuvalu Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Tuvalu Dollars"
    },
    "TWD": {
        "s": "NT$",
        "n": "New Taiwan Dollar",
        "sn": "NT$",
        "d": 2,
        "r": 0,
        "np": "New Taiwan dollars"
    },
    "TZS": {
        "s": "TSh",
        "n": "Tanzanian Shilling",
        "sn": "TSh",
        "d": 0,
        "r": 0,
        "np": "Tanzanian shillings"
    },
    "UAH": {
        "s": "₴",
        "n": "Ukrainian Hryvnia",
        "sn": "₴",
        "d": 2,
        "r": 0,
        "np": "Ukrainian hryvnias"
    },
    "UGX": {
        "s": "USh",
        "n": "Ugandan Shilling",
        "sn": "USh",
        "d": 0,
        "r": 0,
        "np": "Ugandan shillings"
    },
    "USD": {
        "s": "$",
        "n": "US Dollar",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "US dollars"
    },
    "USN": {
        "s": "$",
        "n": "United States dollar (next day) (funds code)",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "United States dollars (next day) (funds code)"
    },
    "UYI": {
        "s": "UYI",
        "n": "Uruguay Peso en Unidades Indexadas (URUIURUI) (funds code)",
        "sn": "UYI",
        "d": 0,
        "r": 0,
        "np": "Uruguay Peso en Unidades Indexadas (URUIURUI) (funds code)"
    },
    "UYU": {
        "s": "$U",
        "n": "Uruguayan Peso",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Uruguayan pesos"
    },
    "UZS": {
        "s": "UZS",
        "n": "Uzbekistan Som",
        "sn": "UZS",
        "d": 0,
        "r": 0,
        "np": "Uzbekistan som"
    },
    "VEF": {
        "s": "Bs.F.",
        "n": "Venezuelan Bolívar",
        "sn": "Bs.F.",
        "d": 2,
        "r": 0,
        "np": "Venezuelan bolívars"
    },
    "VND": {
        "s": "₫",
        "n": "Vietnamese Dong",
        "sn": "₫",
        "d": 0,
        "r": 0,
        "np": "Vietnamese dong"
    },
    "VUV": {
        "s": "VT",
        "n": "Vanuatu vatu",
        "sn": "VT",
        "d": 0,
        "r": 0,
        "np": "Vanuatu vatu"
    },
    "WST": {
        "s": "WS$",
        "n": "Samoan tala",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Samoan tala"
    },
    "XAF": {
        "s": "FCFA",
        "n": "CFA Franc BEAC",
        "sn": "FCFA",
        "d": 0,
        "r": 0,
        "np": "CFA francs BEAC"
    },
    "XAG": {
        "s": "XAG",
        "n": "Silver (one troy ounce)",
        "sn": "XAG",
        "d": 0,
        "r": 0,
        "np": "Silver (one troy ounce)"
    },
    "XAU": {
        "s": "XAU",
        "n": "Gold (one troy ounce)",
        "sn": "XAU",
        "d": 0,
        "r": 0,
        "np": "Gold (one troy ounce)"
    },
    "XBA": {
        "s": "XBA",
        "n": "European Composite Unit (EURCO) (bond market unit)",
        "sn": "XBA",
        "d": 0,
        "r": 0,
        "np": "European Composite Unit (EURCO) (bond market unit)"
    },
    "XBB": {
        "s": "XBB",
        "n": "European Monetary Unit (E.M.U.-6) (bond market unit)",
        "sn": "XBB",
        "d": 0,
        "r": 0,
        "np": "European Monetary Unit (E.M.U.-6) (bond market unit)"
    },
    "XBC": {
        "s": "XBC",
        "n": "European Unit of Account 9 (E.U.A.-9) (bond market unit)",
        "sn": "XBC",
        "d": 0,
        "r": 0,
        "np": "European Unit of Account 9 (E.U.A.-9) (bond market unit)"
    },
    "XBD": {
        "s": "XBD",
        "n": "European Unit of Account 17 (E.U.A.-17) (bond market unit)",
        "sn": "XBD",
        "d": 0,
        "r": 0,
        "np": "European Unit of Account 17 (E.U.A.-17) (bond market unit)"
    },
    "XCD": {
        "s": "$",
        "n": "East Caribbean Dollar",
        "sn": "$",
        "d": 0,
        "r": 0,
        "np": "East Caribbean Dollars"
    },
    "XDR": {
        "s": "XDR",
        "n": "Special drawing rights",
        "sn": "XDR",
        "d": 0,
        "r": 0,
        "np": "Special drawing rights"
    },
    "XOF": {
        "s": "CFA",
        "n": "CFA Franc BCEAO",
        "sn": "CFA",
        "d": 0,
        "r": 0,
        "np": "CFA francs BCEAO"
    },
    "XPD": {
        "s": "XPD",
        "n": "Palladium (one troy ounce)",
        "sn": "XPD",
        "d": 0,
        "r": 0,
        "np": "Palladium (one troy ounce)"
    },
    "XPF": {
        "s": "CFP",
        "n": "CFP franc (franc Pacifique)",
        "sn": "CFP",
        "d": 0,
        "r": 0,
        "np": "CFP franc (franc Pacifique)"
    },
    "XPT": {
        "s": "XPT",
        "n": "Platinum (one troy ounce)",
        "sn": "XPT",
        "d": 0,
        "r": 0,
        "np": "Platinum (one troy ounce)"
    },
    "XSU": {
        "s": "Sucre",
        "n": "SUCRE",
        "sn": "Sucre",
        "d": 0,
        "r": 0,
        "np": "SUCRE"
    },
    "XTS": {
        "s": "XTS",
        "n": "Code reserved for testing purposes",
        "sn": "XTS",
        "d": 0,
        "r": 0,
        "np": "Code reserved for testing purposes"
    },
    "XUA": {
        "s": "XUA",
        "n": "ADB Unit of Account",
        "sn": "XUA",
        "d": 0,
        "r": 0,
        "np": "ADB Unit of Account"
    },
    "XXX": {
        "s": "XXX",
        "n": "No currency",
        "sn": "XXX",
        "d": 0,
        "r": 0,
        "np": "No currency"
    },
    "YER": {
        "s": "YR",
        "n": "Yemeni Rial",
        "sn": "ر.ي.‏",
        "d": 0,
        "r": 0,
        "np": "Yemeni rials"
    },
    "ZAR": {
        "s": "R",
        "n": "South African Rand",
        "sn": "R",
        "d": 2,
        "r": 0,
        "np": "South African rand"
    },
    "ZMK": {
        "s": "ZK",
        "n": "Zambian Kwacha",
        "sn": "ZK",
        "d": 0,
        "r": 0,
        "np": "Zambian kwachas"
    },
    "ZMW": {
        "s": "ZK",
        "n": "Zambian kwacha",
        "sn": "ZK",
        "d": 2,
        "r": 0,
        "np": "Zambian kwacha"
    },
    "ZWD": {
        "s": "Z$",
        "n": "Zimbabwe Dollar",
        "sn": "Z$",
        "d": 2,
        "r": 0,
        "np": "Zimbabwe Dollars"
    },
    "ZWL": {
        "s": "$",
        "n": "Zimbabwean dollar A/10",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Zimbabwean dollars A/10"
    }
}

REPLACED_BY_EURO = {
    "ATS": {
        "s": "öS",
        "n": "Austrian schilling",
        "sn": "öS",
        "d": 2,
        "r": 0,
        "np": "Austrian schilling"
    },
    "BEF": {
        "s": "fr.",
        "n": "Belgian franc",
        "sn": "fr.",
        "d": 2,
        "r": 0,
        "np": "Belgian francs"
    },
    "CYP": {
        "s": "CYP",
        "n": "Cypriot pound",
        "sn": "£",
        "d": 2,
        "r": 0,
        "np": "Cypriot pounds"
    },
    "DEM": {
        "s": "DM",
        "n": "Deutsche Mark",
        "sn": "D-Mark",
        "d": 2,
        "r": 0,
        "np": "Deutsche marks"
    },
    "NLG": {
        "s": "fl.",
        "n": "Dutch guilder",
        "sn": "ƒ",
        "d": 2,
        "r": 0,
        "np": "Dutch guilders"
    },
    "EEK": {
        "s": "kr",
        "n": "Estonian kroon",
        "sn": "kroon",
        "d": 2,
        "r": 0,
        "np": "Estonian krooni"
    },
    "FIM": {
        "s": "FIM",
        "n": "Finnish markka",
        "sn": "mk.",
        "d": 2,
        "r": 0,
        "np": "Finnish markkaa"
    },
    "FRF": {
        "s": "F",
        "n": "French franc",
        "sn": "₣",
        "d": 2,
        "r": 0,
        "np": "French francs"
    },
    "GRD": {
        "s": "GRD",
        "n": "Greek drachma",
        "sn": "Δρχ.",
        "sn2": ["Δρ.", "₯"],
        "d": 2,
        "r": 0,
        "np": "Greek drachmae"
    },
    "IEP": {
        "s": "IR£",
        "n": "Irish pound",
        "sn": "£",
        "d": 2,
        "r": 0,
        "np": "Irish pounds"
    },
    "ITL": {
        "s": "L",
        "n": "Italian lira",
        "sn": "₤",
        "d": 0,
        "r": 0,
        "np": "Italian lire"
    },
    "LVL": {
        "s": "Ls",
        "n": "Latvian lats",
        "sn": "LVL",
        "d": 2,
        "r": 0,
        "np": "Latvian lati"
    },
    "LTL": {
        "s": "Lt",
        "n": "Lithuanian litas",
        "sn": "LTL",
        "sn2": ["litų"],
        "d": 2,
        "r": 0,
        "np": "Lithuanian litai"
    },
    "LUF": {
        "s": "F",
        "n": "Luxembourgish franc",
        "sn": "LUF",
        "d": 2,
        "r": 0,
        "np": "Luxembourgish francs"
    },
    "MTL": {
        "s": "Lm",
        "n": "Maltese lira",
        "sn": "₤",
        "d": 2,
        "r": 0,
        "np": "Maltese liri"
    },
    "PTE": {
        "s": "$",
        "n": "Portuguese escudo",
        "sn": "$",
        "d": 2,
        "r": 0,
        "np": "Portuguese escudos"
    },
    "SKK": {
        "s": "SKK",
        "n": "Slovak koruna",
        "sn": "Sk",
        "d": 2,
        "r": 0,
        "np": "Slovak Koruny"
    },
    "SIT": {
        "s": "SIT",
        "n": "Slovenian tolar",
        "sn": "SIT",
        "sn2": ["tolarjev"],
        "d": 2,
        "r": 0,
        "np": "Slovenian tolar"
    },
    "ESP": {
        "s": "Pta",
        "n": "Spanish peseta",
        "sn": "Ptas",
        "sn2": ["₧", "Pts", "Pt"],
        "d": 0,
        "r": 0,
        "np": "Spanish pesetas"
    },
    "VAL": {
        "s": "£",
        "n": "Vatican lira",
        "sn": "₤",
        "d": 0,
        "r": 0,
        "np": "Vatican liri"
    },
}

# updates
CURRENCIES.update(REPLACED_BY_EURO)
CURRENCIES["VND"]["sn2"] = ["đ"]
CURRENCIES["RON"]["sn2"] = ["lei", "leu", "Lei", "LEI"]
CURRENCIES["CHF"]["sn2"] = ["Fr."]
CURRENCIES["PLN"]["sn2"] = ["pln"]
CURRENCIES["INR"]["sn2"] = ["₹", "र"]
CURRENCIES["IRR"]["sn2"] = ["ریال"]


CURRENCY_CODES: List[str] = list(CURRENCIES.keys())
CURRENCY_SYMBOLS: List[str] = list({c['s'] for c in CURRENCIES.values()})
CURRENCY_NATIONAL_SYMBOLS: List[str] = list(
    {c['sn'] for c in CURRENCIES.values()} |
    set(chain.from_iterable(c['sn2'] for c in CURRENCIES.values()
                            if 'sn2' in c))
)

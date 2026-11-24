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
* sn - currency native symbol
* sn2 - other currency symbols

Some extra abbreviations are added to the list (they are set below
``CURRENCIES`` variable, scroll to the bottom).
"""

from __future__ import annotations

from itertools import chain
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    # typing.NotRequired requires Python 3.11
    from typing_extensions import NotRequired


class CurrencyInfo(TypedDict):
    s: str
    sn: str
    sn2: NotRequired[list[str]]


CURRENCIES: dict[str, CurrencyInfo] = {
    "AED": {
        "s": "AED",
        "sn": "د.إ.‏",
    },
    "AFN": {
        "s": "Af",
        "sn": "؋",
    },
    "ALL": {
        "s": "ALL",
        "sn": "Lek",
    },
    "AMD": {
        "s": "AMD",
        "sn": "դր.",
    },
    "ANG": {
        "s": "ƒ",
        "sn": "ƒ",
    },
    "AOA": {
        "s": "Kz",
        "sn": "Kz",
    },
    "ARS": {
        "s": "AR$",
        "sn": "$",
    },
    "AUD": {
        "s": "AU$",
        "sn": "$",
    },
    "AWG": {
        "s": "ƒ",
        "sn": "ƒ",
    },
    "AFL": {
        "s": "Afl.",
        "sn": "Afl.",
    },
    "AZN": {
        "s": "man.",
        "sn": "ман.",
    },
    "BAM": {
        "s": "KM",
        "sn": "KM",
    },
    "BDT": {
        "s": "Tk",
        "sn": "৳",
    },
    "BBD": {
        "s": "Bds$",
        "sn": "$",
    },
    "BGN": {
        "s": "BGN",
        "sn": "лв.",
    },
    "BHD": {
        "s": "BD",
        "sn": "د.ب.‏",
    },
    "BIF": {
        "s": "FBu",
        "sn": "FBu",
    },
    "BSD": {
        "s": "$",
        "sn": "$",
    },
    "BMD": {
        "s": "$",
        "sn": "$",
    },
    "BND": {
        "s": "BN$",
        "sn": "$",
    },
    "BOB": {
        "s": "Bs",
        "sn": "Bs",
    },
    "BOV": {
        "s": "-",
        "sn": "-",
    },
    "BRL": {
        "s": "R$",
        "sn": "R$",
    },
    "BTN": {
        "s": "Nu.",
        "sn": "Nu.",
    },
    "BWP": {
        "s": "BWP",
        "sn": "P",
    },
    "BYN": {
        "s": "Br",
        "sn": "Br",
    },
    "BZD": {
        "s": "BZ$",
        "sn": "$",
    },
    "CAD": {
        "s": "CA$",
        "sn": "$",
    },
    "CDF": {
        "s": "CDF",
        "sn": "FrCD",
    },
    "CHE": {
        "s": "-",
        "sn": "-",
    },
    "CHF": {
        "s": "CHF",
        "sn": "CHF",
    },
    "CHW": {
        "s": "-",
        "sn": "-",
    },
    "CLF": {
        "s": "UF",
        "sn": "UF",
    },
    "CLP": {
        "s": "CL$",
        "sn": "$",
    },
    "CNY": {
        "s": "CN¥",
        "sn": "CN¥",
    },
    "COP": {
        "s": "CO$",
        "sn": "$",
    },
    "COU": {
        "s": "-",
        "sn": "-",
    },
    "CRC": {
        "s": "₡",
        "sn": "₡",
    },
    "CUC": {
        "s": "CUC$",
        "sn": "$",
    },
    "CUP": {
        "s": "₱",
        "sn": "₱",
    },
    "CVE": {
        "s": "CV$",
        "sn": "CV$",
    },
    "CZK": {
        "s": "Kč",
        "sn": "Kč",
    },
    "DJF": {
        "s": "Fdj",
        "sn": "Fdj",
    },
    "DKK": {
        "s": "Dkr",
        "sn": "kr",
    },
    "DOP": {
        "s": "RD$",
        "sn": "RD$",
    },
    "DZD": {
        "s": "DA",
        "sn": "د.ج.‏",
    },
    "EEK": {
        "s": "Ekr",
        "sn": "kr",
    },
    "EGP": {
        "s": "EGP",
        "sn": "ج.م.‏",
    },
    "ERN": {
        "s": "Nfk",
        "sn": "Nfk",
    },
    "ETB": {
        "s": "Br",
        "sn": "Br",
    },
    "EUR": {"s": "€", "sn": "€"},
    "FJD": {
        "s": "$",
        "sn": "$",
    },
    "FKP": {
        "s": "£",
        "sn": "£",
    },
    "GBP": {
        "s": "£",
        "sn": "£",
    },
    "GEL": {
        "s": "GEL",
        "sn": "GEL",
    },
    "GGP": {
        "s": "£",
        "sn": "£",
    },
    "GHS": {
        "s": "GH₵",
        "sn": "GH₵",
    },
    "GIP": {
        "s": "£",
        "sn": "£",
    },
    "GMD": {
        "s": "D",
        "sn": "D",
    },
    "GNF": {
        "s": "FG",
        "sn": "FG",
    },
    "GTQ": {
        "s": "GTQ",
        "sn": "Q",
    },
    "GYD": {
        "s": "$",
        "sn": "$",
    },
    "HKD": {
        "s": "HK$",
        "sn": "$",
    },
    "HNL": {
        "s": "HNL",
        "sn": "L",
    },
    "HRK": {
        "s": "kn",
        "sn": "kn",
    },
    "HTG": {
        "s": "G",
        "sn": "G",
    },
    "HUF": {
        "s": "Ft",
        "sn": "Ft",
    },
    "IDR": {
        "s": "Rp",
        "sn": "Rp",
    },
    "ILS": {
        "s": "₪",
        "sn": "₪",
    },
    "IMP": {
        "s": "£",
        "sn": "£",
    },
    "INR": {
        "s": "Rs",
        "sn": "টকা",
    },
    "IQD": {
        "s": "IQD",
        "sn": "د.ع.‏",
    },
    "IRR": {
        "s": "IRR",
        "sn": "﷼",
    },
    "ISK": {
        "s": "Ikr",
        "sn": "kr",
    },
    "JEP": {
        "s": "£",
        "sn": "£",
    },
    "JMD": {
        "s": "J$",
        "sn": "$",
    },
    "JOD": {
        "s": "JD",
        "sn": "د.أ.‏",
    },
    "JPY": {
        "s": "¥",
        "sn": "￥",
        "sn2": ["円"],
    },
    "KES": {
        "s": "Ksh",
        "sn": "Ksh",
    },
    "KGS": {
        "s": "лв",
        "sn": "лв",
    },
    "KHR": {
        "s": "KHR",
        "sn": "៛",
    },
    "KMF": {
        "s": "CF",
        "sn": "FC",
    },
    "KPW": {
        "s": "₩",
        "sn": "원",
    },
    "KRW": {
        "s": "₩",
        "sn": "원",
    },
    "KWD": {
        "s": "KD",
        "sn": "د.ك.‏",
    },
    "KYD": {
        "s": "$",
        "sn": "$",
    },
    "KZT": {
        "s": "KZT",
        "sn": "тңг.",
    },
    "LAK": {
        "s": "₭",
        "sn": "₭",
    },
    "LBP": {
        "s": "LB£",
        "sn": "ل.ل.‏",
    },
    "LKR": {
        "s": "SLRs",
        "sn": "SL Re",
    },
    "LRD": {
        "s": "$",
        "sn": "$",
    },
    "LSL": {
        "s": "L",
        "sn": "L",
    },
    "LTL": {
        "s": "Lt",
        "sn": "Lt",
    },
    "LVL": {
        "s": "Ls",
        "sn": "Ls",
    },
    "LYD": {
        "s": "LD",
        "sn": "د.ل.‏",
    },
    "MAD": {
        "s": "MAD",
        "sn": "د.م.‏",
    },
    "MDL": {
        "s": "MDL",
        "sn": "MDL",
    },
    "MGA": {
        "s": "MGA",
        "sn": "MGA",
    },
    "MKD": {
        "s": "MKD",
        "sn": "MKD",
    },
    "MMK": {
        "s": "MMK",
        "sn": "K",
    },
    "MNT": {
        "s": "₮",
        "sn": "₮",
    },
    "MOP": {
        "s": "MOP$",
        "sn": "MOP$",
    },
    "MRO": {
        "s": "UM",
        "sn": "UM",
    },
    "MUR": {
        "s": "MURs",
        "sn": "MURs",
    },
    "MVR": {
        "s": "MRf",
        "sn": "Rf",
    },
    "MWK": {
        "s": "MK",
        "sn": "MK",
    },
    "MXN": {
        "s": "MX$",
        "sn": "$",
    },
    "MXV": {
        "s": "-",
        "sn": "-",
    },
    "MYR": {
        "s": "RM",
        "sn": "RM",
    },
    "MZN": {
        "s": "MTn",
        "sn": "MTn",
    },
    "NAD": {
        "s": "N$",
        "sn": "N$",
    },
    "NGN": {
        "s": "₦",
        "sn": "₦",
    },
    "NIO": {
        "s": "C$",
        "sn": "C$",
    },
    "NOK": {
        "s": "Nkr",
        "sn": "kr",
    },
    "NPR": {
        "s": "NPRs",
        "sn": "नेरू",
    },
    "PRB": {
        "s": "руб",
        "sn": "руб",
    },
    "NZD": {
        "s": "NZ$",
        "sn": "$",
    },
    "OMR": {
        "s": "OMR",
        "sn": "ر.ع.‏",
    },
    "PAB": {
        "s": "B/.",
        "sn": "B/.",
    },
    "PEN": {
        "s": "S/.",
        "sn": "S/.",
    },
    "PGK": {
        "s": "K",
        "sn": "K",
    },
    "PHP": {
        "s": "₱",
        "sn": "₱",
    },
    "PKR": {
        "s": "PKRs",
        "sn": "₨",
    },
    "PLN": {
        "s": "zł",
        "sn": "zł",
    },
    "PYG": {
        "s": "₲",
        "sn": "₲",
    },
    "QAR": {
        "s": "QR",
        "sn": "ر.ق.‏",
    },
    "RON": {
        "s": "RON",
        "sn": "RON",
    },
    "RSD": {
        "s": "din.",
        "sn": "дин.",
    },
    "RUB": {
        "s": "RUB",
        "sn": "руб.",
    },
    "RWF": {
        "s": "RWF",
        "sn": "FR",
    },
    "SAR": {
        "s": "SR",
        "sn": "ر.س.‏",
    },
    "SBD": {
        "s": "$",
        "sn": "$",
    },
    "SCR": {
        "s": "₨",
        "sn": "₨",
    },
    "SDG": {
        "s": "SDG",
        "sn": "SDG",
    },
    "SEK": {
        "s": "Skr",
        "sn": "kr",
    },
    "SGD": {
        "s": "S$",
        "sn": "$",
    },
    "SHP": {
        "s": "£",
        "sn": "£",
    },
    "SLL": {
        "s": "Le",
        "sn": "Le",
    },
    "SOS": {
        "s": "Ssh",
        "sn": "Ssh",
    },
    "SRD": {
        "s": "$",
        "sn": "$",
    },
    "SSP": {
        "s": "SSP",
        "sn": "SSP",
    },
    "STD": {
        "s": "Db",
        "sn": "Db",
    },
    "SVC": {
        "s": "$",
        "sn": "$",
    },
    "SYP": {
        "s": "SY£",
        "sn": "ل.س.‏",
    },
    "SZL": {
        "s": "L",
        "sn": "L",
    },
    "THB": {
        "s": "฿",
        "sn": "฿",
    },
    "TJS": {
        "s": "-",
        "sn": "-",
    },
    "TMT": {
        "s": "T",
        "sn": "T",
    },
    "TND": {
        "s": "DT",
        "sn": "د.ت.‏",
    },
    "TOP": {
        "s": "T$",
        "sn": "T$",
    },
    "TRY": {
        "s": "TL",
        "sn": "TL",
    },
    "TTD": {
        "s": "TT$",
        "sn": "$",
    },
    "TVD": {
        "s": "$",
        "sn": "$",
    },
    "TWD": {
        "s": "NT$",
        "sn": "NT$",
    },
    "TZS": {
        "s": "TSh",
        "sn": "TSh",
    },
    "UAH": {
        "s": "₴",
        "sn": "₴",
    },
    "UGX": {
        "s": "USh",
        "sn": "USh",
    },
    "USD": {
        "s": "$",
        "sn": "$",
    },
    "USN": {
        "s": "$",
        "sn": "$",
    },
    "UYI": {
        "s": "UYI",
        "sn": "UYI",
    },
    "UYU": {
        "s": "$U",
        "sn": "$",
    },
    "UZS": {
        "s": "UZS",
        "sn": "UZS",
    },
    "VEF": {
        "s": "Bs.F.",
        "sn": "Bs.F.",
    },
    "VND": {
        "s": "₫",
        "sn": "₫",
    },
    "VUV": {
        "s": "VT",
        "sn": "VT",
    },
    "WST": {
        "s": "WS$",
        "sn": "$",
    },
    "XAF": {
        "s": "FCFA",
        "sn": "FCFA",
    },
    "XAG": {
        "s": "XAG",
        "sn": "XAG",
    },
    "XAU": {
        "s": "XAU",
        "sn": "XAU",
    },
    "XBA": {
        "s": "XBA",
        "sn": "XBA",
    },
    "XBB": {
        "s": "XBB",
        "sn": "XBB",
    },
    "XBC": {
        "s": "XBC",
        "sn": "XBC",
    },
    "XBD": {
        "s": "XBD",
        "sn": "XBD",
    },
    "XCD": {
        "s": "$",
        "sn": "$",
    },
    "XDR": {
        "s": "XDR",
        "sn": "XDR",
    },
    "XOF": {
        "s": "CFA",
        "sn": "CFA",
    },
    "XPD": {
        "s": "XPD",
        "sn": "XPD",
    },
    "XPF": {
        "s": "CFP",
        "sn": "CFP",
    },
    "XPT": {
        "s": "XPT",
        "sn": "XPT",
    },
    "XSU": {
        "s": "Sucre",
        "sn": "Sucre",
    },
    "XTS": {
        "s": "XTS",
        "sn": "XTS",
    },
    "XUA": {
        "s": "XUA",
        "sn": "XUA",
    },
    "XXX": {
        "s": "XXX",
        "sn": "XXX",
    },
    "YER": {
        "s": "YR",
        "sn": "ر.ي.‏",
    },
    "ZAR": {
        "s": "R",
        "sn": "R",
    },
    "ZMK": {
        "s": "ZK",
        "sn": "ZK",
    },
    "ZMW": {
        "s": "ZK",
        "sn": "ZK",
    },
    "ZWD": {
        "s": "Z$",
        "sn": "Z$",
    },
    "ZWL": {
        "s": "$",
        "sn": "$",
    },
}


# Commonly used unofficial names.
# See also: https://en.wikipedia.org/wiki/ISO_4217#Unofficial_currency_codes
CURRENCIES["NTD"] = CURRENCIES["TWD"]
CURRENCIES["RMB"] = CURRENCIES["CNY"]


REPLACED_BY_EURO: dict[str, CurrencyInfo] = {
    "ATS": {
        "s": "öS",
        "sn": "öS",
    },
    "BEF": {
        "s": "fr.",
        "sn": "fr.",
    },
    "CYP": {
        "s": "CYP",
        "sn": "£",
    },
    "DEM": {
        "s": "DM",
        "sn": "D-Mark",
    },
    "NLG": {
        "s": "fl.",
        "sn": "ƒ",
    },
    "EEK": {
        "s": "kr",
        "sn": "kroon",
    },
    "FIM": {
        "s": "FIM",
        "sn": "mk.",
    },
    "FRF": {
        "s": "F",
        "sn": "₣",
    },
    "GRD": {
        "s": "GRD",
        "sn": "Δρχ.",
        "sn2": ["Δρ.", "₯"],
    },
    "IEP": {
        "s": "IR£",
        "sn": "£",
    },
    "ITL": {
        "s": "L",
        "sn": "₤",
    },
    "LVL": {
        "s": "Ls",
        "sn": "LVL",
    },
    "LTL": {
        "s": "Lt",
        "sn": "LTL",
        "sn2": ["litų"],
    },
    "LUF": {
        "s": "F",
        "sn": "LUF",
    },
    "MTL": {
        "s": "Lm",
        "sn": "₤",
    },
    "PTE": {
        "s": "$",
        "sn": "$",
    },
    "SKK": {
        "s": "SKK",
        "sn": "Sk",
    },
    "SIT": {
        "s": "SIT",
        "sn": "SIT",
        "sn2": ["tolarjev"],
    },
    "ESP": {
        "s": "Pta",
        "sn": "Ptas",
        "sn2": ["₧", "Pts", "Pt"],
    },
    "VAL": {
        "s": "£",
        "sn": "₤",
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


CURRENCY_CODES: list[str] = list(CURRENCIES.keys())
CURRENCY_SYMBOLS: list[str] = list({c["s"] for c in CURRENCIES.values()})
CURRENCY_NATIONAL_SYMBOLS: list[str] = list(
    {c["sn"] for c in CURRENCIES.values()}
    | set(chain.from_iterable(c["sn2"] for c in CURRENCIES.values() if "sn2" in c))
)

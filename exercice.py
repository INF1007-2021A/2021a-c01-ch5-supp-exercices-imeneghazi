#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	sous_total = 0
	for produit in data:
		sous_total += produit[1]*produit[2]
	taxes = sous_total*0.15
	total = sous_total+taxes
	affichage_nom = "{} \n".format(name)
	affichage_sous_total = "SOUS TOTAL {:>10.2f} $\n".format(sous_total)
	affichage_taxes = "TAXES {:>15.2f} $\n".format(taxes)
	affichage_total = "TOTAL {:>15.2f} $\n".format(total)
	return affichage_nom+affichage_sous_total+affichage_taxes+affichage_total


def format_number(number, num_decimal_digits):
	return ""

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))

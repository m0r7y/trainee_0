# -*- coding: UTF-8 -*-

# Python 3.x : Prove that you know python; API REST

# Attention les solutions à la dure vaudront 0 points !!!!!!!!.

# un api vient de retourner ces données :
api_response = [
    {
        'id': 1,
        'product_id': 155,
        'qty': 5,
    },
    {
        'id': 2,
        'product_id': 1000,
        'qty': 1,
    },
    {
        'id': 3,
        'product_id': 155,
        'qty': 2,
    },
    {
        'id': 4,
        'product_id': 155,
        'qty': 7,
    },
]

# l'on veut avoir la quantité de chaque produit
# output attendu [{'product_id': 1000, 'qty': 1}, {'product_id': 155, 'qty': 14}]
def groupByProduct(api_response):
    # your code
    # retourner l'output
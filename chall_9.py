# -*- coding: UTF-8 -*-

# Python 3.x : Prove that you know python

# Attention les solutions à la dure vaudront 0 points !!!!!!!!.

# Donner le code pour avoir le nom du jour :
# En langue française
# En langue anglaise
# Attention, selon la langue et région de votre système vous pouvez obtenir
# Une date en français ou une date en anglais par défaut
# Attention aussi au solution à la dure, si je vous dis d'ajouter une date en néerlandais
# Oserez vous encore utilisez un "if"
# Mais aujourd'hui nous nous contenterons des dates en français et en anglais

# parter de ce code
# avez-vous entendu de fonction setlocale
from datetime import datetime
datetime.now().strftime('%A')
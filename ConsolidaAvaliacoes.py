#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Processo de agregação e consolidação dos ficheiros individuais de avaliação,
# para a determinação da lista ordenada de atribuição de RVD's
#

import sys
from pt.bportugal.Avaliacoes.Consolidation import Consolidation

__author__ = 'Alexandre Carlos'
__version__ = "1.1"

if __name__ == '__main__':
    consolidation = Consolidation()

    sys.exit(consolidation.do_consolidation())
    #Consolidation(sys.argv))

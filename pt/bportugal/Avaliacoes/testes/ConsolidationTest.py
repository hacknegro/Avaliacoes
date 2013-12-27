#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
__author__ = 'Alexandre Carlos'

import unittest
from pt.bportugal.Avaliacoes.Consolidation import Consolidation

class ConsolidationTestCase(unittest.TestCase):

    def setUp(self):
        self.consolidation = Consolidation()

    def test_init(self):
        self.assertEqual(self.consolidation.worker_excel_file, r"C:\Users\KKU035\Documents\Dropbox\Gestão\Pessoal\Avaliações 2013\Avaliação\António Simões.xls")
        self.assertEqual(self.consolidation.worker, "António Simões")
        self.assertEqual(self.consolidation.global_assessment_excel_file, r"C:\Users\KKU035\Documents\Dropbox\Gestão\Pessoal\Avaliações 2013\Avaliação\AvaliaçõesGlobais.xls")
        self.assertEqual(self.consolidation.workers, ())
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

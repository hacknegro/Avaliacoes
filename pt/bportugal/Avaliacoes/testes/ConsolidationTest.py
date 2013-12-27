#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
__author__ = 'Alexandre Carlos'

import unittest
from pt.bportugal.Avaliacoes.Consolidation import *

class ConsolidationTestCase(unittest.TestCase):

    def setUp(self):
        self.consolidation = Consolidation()
        self.we = WorkerEvaluation(self.consolidation.worker_excel_file)

    def test_init(self):
        # self.assertEqual(self.consolidation.worker_excel_file, r"C:\Users\KKU035\Documents\Dropbox\Gestão\Pessoal\Avaliações 2013\Avaliação\António Simões.xls")
        self.assertEqual(self.consolidation.worker_excel_file, r"/home/alexandre/Documentos/Dropbox/Gestão/Pessoal/Avaliações 2013/Avaliação/António Simões.xls")
        self.assertEqual(self.consolidation.worker, "António Simões")
        # self.assertEqual(self.consolidation.global_assessment_excel_file, r"C:\Users\KKU035\Documents\Dropbox\Gestão\Pessoal\Avaliações 2013\Avaliação\AvaliaçõesGlobais.xls")
        self.assertEqual(self.consolidation.global_assessment_excel_file, r"/home/alexandre/Documentos/Dropbox/Gestão/Pessoal/Avaliações 2013/Avaliação/AvaliaçõesGlobais.xls")
        self.assertEqual(self.consolidation.workers, ())
        # self.assertEqual(True, False)

    def test_worker_evaluation (self):
        evaluation = self.we.getEvaluation()
        self.assertEqual(5.500, evaluation)

    def test_handle_worker(self):
        wk = self.consolidation.handle_worker(self.consolidation.worker)

        self.assertEqual("António Simões", wk.get_name())
        self.assertEqual(5.500, wk.get_assessment())

if __name__ == '__main__':
    unittest.main()

#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
__author__ = 'Alexandre Carlos'
__version__ = "1.0"

import unittest
from pt.bportugal.Avaliacoes.Consolidation import *


class ConsolidationTestCase(unittest.TestCase):

    reference_workers_files = ("António Simões.xls", "Cristina Coelho.xls", "João Carlos.xls",
                               "José Augusto.xls", "Luís Rio.xls", "Maria da Graça.xls", "Maria da Luz.xls", "Maria João.xls")
    reference_workers = ["António Simões", "Cristina Coelho", "João Carlos", "José Augusto",
                         "Luís Rio", "Maria da Graça", "Maria da Luz", "Maria João"]
    reference_workers_values =[5.500, 4.400, 5.300, 3.300, 5.550, 4.350, 4.200, 4.250]
    reference_global_excel_file = r"/home/alexandre/Documentos/Dropbox/Gestão/Pessoal/Avaliações 2013/" + \
                                  "Avaliação/AvaliaçõesGlobais.xls"
    reference_single_worker_name = "António Simões"
    reference_single_worker_value = 5.500

    def setUp(self):
        self.consolidation = Consolidation()

        # self.we = WorkerEvaluation(self.consolidation.worker_excel_file)

    def test_init(self):
        self.assertEqual(self.consolidation.config.worker_file_path, r"/home/alexandre/Documentos/Dropbox/Gestão/Pessoal/Avaliações 2013/Avaliação")
        self.assertEqual(self.consolidation.config.file_workers, self.reference_workers_files)
        self.assertEqual(self.consolidation.config.global_assessment_excel_file, self.reference_global_excel_file)


    def test_get_workers(self):
        self.consolidation.get_workers()

        self.assertEqual(self.consolidation.workers, self.reference_workers)

    def test_handle_single_worker(self):
        self.consolidation.get_workers()
        wk = self.consolidation.handle_worker(0)

        self.assertEqual(wk.get_name(), self.reference_single_worker_name)
        self.assertEqual(wk.get_assessment(), self.reference_single_worker_value)

    def test_handle_all_workers(self):
        self.consolidation.get_workers()

        for i in range(len(self.consolidation.workers)):
            wk = self.consolidation.handle_worker(i)

            self.assertEqual(wk.get_name(), self.reference_workers[i])
            self.assertEqual(wk.get_assessment(), self.reference_workers_values[i])

    def test_global_assessment(self):
        self.consolidation.get_workers()

        self.assertEqual(self.consolidation.global_assessment.worker_index, 1)

        wk = self.consolidation.handle_worker(0)
        self.consolidation.global_assessment.new_assessment(wk)
        self.assertEqual(self.consolidation.global_assessment.worker_index, 2)

        wk = self.consolidation.handle_worker(1)
        self.consolidation.global_assessment.new_assessment(wk)
        self.assertEqual(self.consolidation.global_assessment.worker_index, 3)


if __name__ == '__main__':
    unittest.main()

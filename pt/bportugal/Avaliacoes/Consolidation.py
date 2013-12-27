#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Processo de agregação e consolidação dos ficheiros individuais de avaliação,
# para a determinação da lista ordenada de atribuição de RVD's
#
__author__ = 'Alexandre Carlos'
__version__ = "0.1"

from xlrd import open_workbook
from xlwt import Workbook

class Worker(object):
    """
    """
    name = ""
    evaluation = 0

    def __init__(self, valor):
        self.name = valor

    def put_assessment (self, valor):
        self.evaluation = valor

    def get_name(self):
        return self.name

    def get_assessment(self):
        return self.evaluation

class WorkerEvaluation(object):
    """

    """

    def __init__(self, exel_file):
        self.worker_file = exel_file

    def getEvaluation(self):

        wb = open_workbook(self.worker_file)

        sheet = wb.sheet_by_name(u"Avaliação Global")

        # sheet.cell(row_index,col_index).value
        return sheet.cell(2,3).value


class Consolidation(object):
    """

    """

    def __init__(self):
        # self.worker_excel_file = r"C:\Users\KKU035\Documents\Dropbox\Gestão\Pessoal\Avaliações 2013\Avaliação\António Simões.xls"
        self.worker_excel_file = r"/home/alexandre/Documentos/Dropbox/Gestão/Pessoal/Avaliações 2013/Avaliação/António Simões.xls"
        self.worker = "António Simões"
        # self.global_assessment_excel_file = r"C:\Users\KKU035\Documents\Dropbox\Gestão\Pessoal\Avaliações 2013\Avaliação\AvaliaçõesGlobais.xls"
        self.global_assessment_excel_file = r"/home/alexandre/Documentos/Dropbox/Gestão/Pessoal/Avaliações 2013/Avaliação/AvaliaçõesGlobais.xls"
        self.workers = ()
        self.global_wb = Workbook(encoding='utf-8')

    def get_workers(self):
        self.workers = ("António Simões",)

    def handle_worker(self, nome):
        worker = Worker(nome)

        wk = WorkerEvaluation(self.worker_excel_file)

        worker.put_assessment(wk.getEvaluation())

        return worker

    def save_assessment(self, worker):

        worker_name = worker.get_name()

        print(worker_name)

        sheet2 = self.global_wb.add_sheet(u"Avaliação Global")
        sheet2.write(0,0,worker_name)
        sheet2.write(1,0,worker.get_assessment())

        self.global_wb.save(self.global_assessment_excel_file)

        return 10

    def do_consolidation(self):
        """

        @type self: object
        """
        self.get_workers()

        worker = self.handle_worker(self.workers[0])

        return self.save_assessment(worker)
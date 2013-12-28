#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Processo de agregação e consolidação dos ficheiros individuais de avaliação,
# para a determinação da lista ordenada de atribuição de RVD's
#
__author__ = 'Alexandre Carlos'
__version__ = "1.0"

from xlrd import open_workbook
from xlwt import Workbook
import os


class ConfigSetup (object):

    def __init__(self):
        # self.worker_file_path = r"C:\Users\KKU035\Documents\Dropbox\Gestão\Pessoal\Avaliações 2013\Avaliação"
        # self.global_assessment_excel_file = r"C:\Users\KKU035\Documents\Dropbox\Gestão\Pessoal\Avaliações 2013\" +\
        #                                     "Avaliação\AvaliaçõesGlobais.xls"

        self.worker_file_path = r"/home/alexandre/Documentos/Dropbox/Gestão/Pessoal/Avaliações 2013/Avaliação"
        self.global_assessment_excel_file = r"/home/alexandre/Documentos/Dropbox/Gestão/Pessoal/Avaliações 2013/" +\
                                            r"Avaliação/AvaliaçõesGlobais.xls"
        self.file_workers = ("António Simões.xls", "Cristina Coelho.xls", "João Carlos.xls", "José Augusto.xls",
                             "Luís Rio.xls", "Maria da Graça.xls", "Maria da Luz.xls", "Maria João.xls")


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


class GlobalAssessment (object):

    first_row = 0

    first_column = 0
    second_column = 1

    def __init__(self, global_assessment_filename):
        self.global_wb = Workbook(encoding='utf-8')
        self.worker_index = 1
        self.global_assessment_filename = global_assessment_filename
        self.global_assessment_sheet = self.global_wb.add_sheet(u"Avaliação Global")

        self.global_assessment_sheet.write(self.first_row, self.first_column, u"Avaliado")
        self.global_assessment_sheet.write(self.first_row, self.second_column, u"Avaliação")

        self.global_assessment_sheet.col(self.first_column).width = 256*20
        self.global_assessment_sheet.col(self.second_column).width = 256*10

    def new_assessment(self, worker):

        self.global_assessment_sheet.write(self.worker_index, self.first_column, worker.get_name())
        self.global_assessment_sheet.write(self.worker_index, self.second_column, worker.get_assessment())

        self.worker_index += 1

    def save_assessment(self):
        self.global_wb.save(self.global_assessment_filename)


class WorkerEvaluation(object):
    """

    """

    def __init__(self, exel_file):

        self.worker_file = exel_file

    def get_evaluation(self):
        """

        @rtype : float
        """
        wb = open_workbook(self.worker_file)

        sheet = wb.sheet_by_name(u"Avaliação Global")

        # sheet.cell(row_index,col_index).value
        return sheet.cell(2,3).value


class Consolidation(object):
    """

    """

    def __init__(self):

        self.config = ConfigSetup()
        self.workers = []
        self.global_assessment = GlobalAssessment(self.config.global_assessment_excel_file)


    def get_workers(self):

        for worker_file in self.config.file_workers:
            base, ext = os.path.splitext(worker_file)
            self.workers.append(base)

    def handle_worker(self, worker_index):
        """

        @rtype : Worker
        """

        worker = Worker(self.workers[worker_index])

        wk = WorkerEvaluation(os.path.join(self.config.worker_file_path, self.config.file_workers[worker_index]))

        worker.put_assessment(wk.get_evaluation())

        return worker

    def do_consolidation(self):
        """

        @type self: object
        """
        self.get_workers()

        for i in range(len(self.config.file_workers)):
            worker = self.handle_worker(i)
            self.global_assessment.new_assessment(worker)

        self.global_assessment.save_assessment()

        return
        # return self.save_assessment(worker)
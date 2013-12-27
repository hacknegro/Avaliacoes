#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Processo de agregação e consolidação dos ficheiros individuais de avaliação,
# para a determinação da lista ordenada de atribuição de RVD's
#
__author__ = 'Alexandre Carlos'


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


class Consolidation(object):
    """

    """

    def __init__(self):
        self.workerExcelFile = r"C:\Users\KKU035\Documents\Dropbox\Gestão\Pessoal\Avaliações 2013\Avaliação\António Simões.xls"
        self.worker = "António Simões"
        self.globalAssessmentExcelFile = r"C:\Users\KKU035\Documents\Dropbox\Gestão\Pessoal\Avaliações 2013\Avaliação\AvaliaçõesGlobais.xls"
        self.workers = ()

    def get_workers(self):
        self.workers = ("António Simões")


    def handle_worker(self, nome):
        worker = Worker(nome)

        worker.put_assessment(3)

        return worker


    def save_assessment(selfself, worker):

        return -88

    def do_consolidation(self):
        """

        @type self: object
        """
        self.get_workers()

        worker = self.handle_worker(self.workers[0])

        return self.save_assessment(worker)
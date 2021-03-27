import psutil as pu
import pyautogui as bot
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QTableWidgetItem

from mainFoo import fish_tank
from mainForm import Ui_MainForm  # импорт нашего сгенерированного файла

bot.FAILSAFE = True
bot.PAUSE = .2


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        self.f_lesh = 0
        self.f_gustera = 0
        self.f_beloglazka = 0
        self.f_ripus = 0
        self.f_korushka = 0
        self.f_rybec = 0
        self.f_sig = 0
        self.f_ludoga = 0
        self.f_shuka = 0
        self.f_big_shuka = 0
        self.f_sudak = 0
        self.f_big_sudak = 0
        self.f_ugor = 0
        self.f_losos = 0
        self.f_paliya = 0
        self.f_ludoznaya_paliya = 0
        self.f_krayznaya_paliya = 0
        self.f_osetr = 0


        self.count_fish = 0

        self.ripus_width = 0
        self.corushka_width = 0
        self.rybec_width = 0
        self.sig_width = 0
        self.ludoga_width = 0
        self.shuka_width = 0
        self.big_shuka_width = 0
        self.sudak_width = 0
        self.big_sudak_width = 0
        self.ugor_width = 0
        self.losos_width = 0
        self.paliya_width = 0
        self.ludoznaya_paliya_width = 0
        self.kryaznaya_paliya_width = 0
        self.osetr_width = 0

        self.setFixedSize(800, 600)

        self.ui.stopLesh.setVisible(False)
        self.ui.btnStopRipus.setVisible(False)
        self.ui.btnStopSig.setVisible(False)
        self.ui.btnStopShuka.setVisible(False)
        self.ui.btnStopSudak.setVisible(False)
        self.ui.btnStopUgor.setVisible(False)
        self.ui.btnStopLosos.setVisible(False)
        self.ui.btnStopPaliya.setVisible(False)
        self.ui.btnStopOsetr.setVisible(False)
        self.ui.startLesh.clicked.connect(self.start_timer_lesh)
        self.ui.stopLesh.clicked.connect(self.stop_timer_lesh)
        self.ui.btnStartRipus.clicked.connect(self.start_timer_ripus)
        self.ui.btnStopRipus.clicked.connect(self.stop_timer_ripus)
        self.ui.btnStartSig.clicked.connect(self.start_timer_sig)
        self.ui.btnStopSig.clicked.connect(self.stop_timer_sig)
        self.ui.btnStartShuka.clicked.connect(self.start_timer_shuka)
        self.ui.btnStopShuka.clicked.connect(self.stop_timer_shuka)
        self.ui.btnStartSudak.clicked.connect(self.start_timer_sudak)
        self.ui.btnStopSudak.clicked.connect(self.stop_timer_sudak)
        self.ui.btnStartUgor.clicked.connect(self.start_timer_ugor)
        self.ui.btnStopUgor.clicked.connect(self.stop_timer_ugor)
        self.ui.btnStartLosos.clicked.connect(self.start_timer_losos)
        self.ui.btnStopLosos.clicked.connect(self.stop_timer_losos)
        self.ui.btnStartPaliya.clicked.connect(self.start_timer_paliya)
        self.ui.btnStopPaliya.clicked.connect(self.stop_timer_paliya)
        self.ui.btnStartOsetr.clicked.connect(self.start_timer_osetr)
        self.ui.btnStopOsetr.clicked.connect(self.stop_timer_osetr)

        self.ui.tableLesh.setRowCount(9)
        self.ui.tableGustera.setRowCount(3)
        self.ui.tableBeloglazka.setRowCount(6)

        self.ui.tableRipus.setRowCount(200)
        self.ui.tableKorushka.setRowCount(200)

        # self.shortcutStart = QShortcut(QKeySequence("Alt+A"), self)
        # self.shortcutStart.activated.connect(self.start_Timer)

        # Таймер для вкладки Лещ
        self.timer_lesh = QTimer()
        self.timer_lesh.timeout.connect(self.main_loop_lesh)

        # Таймер для вкладки Рипус
        self.timer_ripus = QTimer()
        self.timer_ripus.timeout.connect(self.main_loop_ripus)

        # Таймер для вкладки Сиг
        self.timer_sig = QTimer()
        self.timer_sig.timeout.connect(self.main_loop_sig)

        # Таймер для вкладки Щука
        self.timer_shuka = QTimer()
        self.timer_shuka.timeout.connect(self.main_loop_shuka)

        # Таймер для вкладки Судак
        self.timer_sudak = QTimer()
        self.timer_sudak.timeout.connect(self.main_loop_sudak)

        # Таймер для вкладки Угорь
        self.timer_ugor = QTimer()
        self.timer_ugor.timeout.connect(self.main_loop_ugor)

        # Таймер для вкладки Лосось
        self.timer_losos = QTimer()
        self.timer_losos.timeout.connect(self.main_loop_losos)

        # Таймер для вкладки Палия
        self.timer_paliya = QTimer()
        self.timer_paliya.timeout.connect(self.main_loop_paliya)

        # Таймер для вкладки Осетр
        self.timer_osetr = QTimer()
        self.timer_osetr.timeout.connect(self.main_loop_osetr)

    # ---------------------------------- OSETR_____________________________________________
    def stop_timer_osetr(self):
        self.ui.tableOsetr.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.osetr_width = 0

        self.ui.tableOsetr.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdOsetr.display(str(self.count_fish))
        self.ui.tableOsetr.setRowCount(5)
        self.f_osetr = 0

        self.ui.btnStopPaliya.setVisible(False)
        self.ui.btnStartPaliya.setVisible(True)
        self.timer_paliya.stop()


    def start_timer_osetr(self):
        self.ui.tableOsetr.setRowCount(5)

        self.ui.tableOsetr.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.textBrowser_9.clear()
        self.ui.btnStopOsetr.setVisible(True)
        self.ui.btnStartOsetr.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_osetr.start(500)  # Запуск оснавного таймера

        else:
            self.timer_osetr.stop()
            bot.alert('Запустите рыбалку')
            self.ui.btnStartOsetr.setVisible(True)
            self.ui.btnStopOsetr.setVisible(False)


    def main_loop_osetr(self):
        # Основной цикл вылова (Палия)
        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))
            if width_f < 1000 and width_f == int(width_f):
                pass
            else:
                width_f *= 1000

            if str(ulov[0]) == 'Атлантический Осетр' and width_f >= 200000 and self.f_osetr < 5:
                self.ui.tableOsetr.setItem(self.f_osetr, 0, QTableWidgetItem("Атлантический Осетр"))
                self.ui.tableOsetr.setItem(self.f_osetr, 1, QTableWidgetItem(str(int(width_f))))
                self.f_osetr += 1
            if self.f_osetr > 4:
                self.ui.tableOsetr.setStyleSheet("background-color: rgb(0, 170, 0);")


            self.count_fish += 1
            self.ui.textBrowser_9.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdOsetr.display(str(self.count_fish))

        except:
            pass


    # ---------------------------------- END OSETR_________________________________________

    # ---------------------------------- PALIYA_____________________________________________
    def stop_timer_paliya(self):
        self.ui.tablePaliya.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableLudoznayaPaliya.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableKryazhevayaPaliya.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.paliya_width = 0
        self.ludoznaya_paliya_width = 0
        self.kryaznaya_paliya_width = 0

        self.ui.tablePaliya.setRowCount(0)
        self.ui.tableLudoznayaPaliya.setRowCount(0)
        self.ui.tableKryazhevayaPaliya.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdPaliya.display(str(self.count_fish))
        self.ui.tablePaliya.setRowCount(4)
        self.ui.tableLudoznayaPaliya.setRowCount(3)
        self.ui.tableKryazhevayaPaliya.setRowCount(2)
        self.f_paliya = 0
        self.f_ludoznaya_paliya = 0
        self.f_krayznaya_paliya = 0

        self.ui.btnStopPaliya.setVisible(False)
        self.ui.btnStartPaliya.setVisible(True)
        self.timer_paliya.stop()

    def start_timer_paliya(self):
        self.ui.tablePaliya.setRowCount(4)
        self.ui.tableLudoznayaPaliya.setRowCount(3)
        self.ui.tableKryazhevayaPaliya.setRowCount(2)

        self.ui.tablePaliya.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableLudoznayaPaliya.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableKryazhevayaPaliya.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.textBrowser_8.clear()
        self.ui.btnStopPaliya.setVisible(True)
        self.ui.btnStartPaliya.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_paliya.start(500)  # Запуск оснавного таймера

        else:
            self.timer_paliya.stop()
            bot.alert('Запустите рыбалку')
            self.ui.btnStartPaliya.setVisible(True)
            self.ui.btnStopPaliya.setVisible(False)


    def main_loop_paliya(self):
        # Основной цикл вылова (Палия)
        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))
            if width_f < 1000 and width_f == int(width_f):
                pass
            else:
                width_f *= 1000

            if str(ulov[0]) == 'Палия' and width_f >= 2000 and self.f_paliya < 4:
                self.ui.tablePaliya.setItem(self.f_paliya, 0, QTableWidgetItem("Палия"))
                self.ui.tablePaliya.setItem(self.f_paliya, 1, QTableWidgetItem(str(int(width_f))))
                self.f_paliya += 1
            if self.f_paliya > 3:
                self.ui.tablePaliya.setStyleSheet("background-color: rgb(0, 170, 0);")

            if str(ulov[0]) == 'Лудожная палия' and width_f >= 2500 and self.f_ludoznaya_paliya < 3:
                self.ui.tableLudoznayaPaliya.setItem(self.f_ludoznaya_paliya, 0, QTableWidgetItem("Лудожная палия"))
                self.ui.tableLudoznayaPaliya.setItem(self.f_ludoznaya_paliya, 1, QTableWidgetItem(str(int(width_f))))
                self.f_ludoznaya_paliya += 1
            if self.f_ludoznaya_paliya > 2:
                self.ui.tableLudoznayaPaliya.setStyleSheet("background-color: rgb(0, 170, 0);")

            if str(ulov[0]) == 'Кряжевая палия' and width_f >= 1500 and self.f_krayznaya_paliya < 2:
                self.ui.tableKryazhevayaPaliya.setItem(self.f_krayznaya_paliya, 0, QTableWidgetItem("Кряжевая палия"))
                self.ui.tableKryazhevayaPaliya.setItem(self.f_krayznaya_paliya, 1, QTableWidgetItem(str(int(width_f))))
                self.f_krayznaya_paliya += 1
            if self.f_krayznaya_paliya > 1:
                self.ui.tableKryazhevayaPaliya.setStyleSheet("background-color: rgb(0, 170, 0);")

            self.count_fish += 1
            self.ui.textBrowser_8.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdPaliya.display(str(self.count_fish))

        except:
            pass


    # ---------------------------------END PALIYA___________________________________________

    # ---------------------------------- LOSOS_____________________________________________
    def stop_timer_losos(self):
        self.ui.tableLosos.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ugor_width = 0

        self.ui.tableLosos.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdLosos.display(str(self.count_fish))
        self.ui.tableLosos.setRowCount(5)
        self.f_losos = 0

        self.ui.btnStopLosos.setVisible(False)
        self.ui.btnStartLosos.setVisible(True)
        self.timer_losos.stop()


    def start_timer_losos(self):
        self.ui.tableLosos.setRowCount(5)
        self.ui.tableLosos.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.textBrowser_7.clear()
        self.ui.btnStopLosos.setVisible(True)
        self.ui.btnStartLosos.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_losos.start(500)  # Запуск оснавного таймера

        else:
            self.timer_losos.stop()
            bot.alert('Запустите рыбалку')
            self.ui.btnStartLosos.setVisible(True)
            self.ui.btnStopLosos.setVisible(False)


    def main_loop_losos(self):
        # Основной цикл вылова (Лосось)
        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))
            if width_f < 1000 and width_f == int(width_f):
                pass
            else:
                width_f *= 1000

            if str(ulov[0]) == 'Лосось' and width_f >= 15000 and self.f_ugor < 5:
                self.ui.tableLosos.setItem(self.f_losos, 0, QTableWidgetItem("Лосось"))
                self.ui.tableLosos.setItem(self.f_losos, 1, QTableWidgetItem(str(int(width_f))))
                self.f_losos += 1
            if self.f_losos > 4:
                self.ui.tableLosos.setStyleSheet("background-color: rgb(0, 170, 0);")

            self.count_fish += 1
            self.ui.textBrowser_7.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdLosos.display(str(self.count_fish))

        except:
            pass

    # ---------------------------------- END LOSOS_____________________________________________


    # ---------------------------------- UGOR_____________________________________________
    def stop_timer_ugor(self):
        self.ui.tableUgor.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ugor_width = 0

        self.ui.tableUgor.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdUgor.display(str(self.count_fish))
        self.ui.tableUgor.setRowCount(5)
        self.f_ugor = 0

        self.ui.btnStopUgor.setVisible(False)
        self.ui.btnStartUgor.setVisible(True)
        self.timer_ugor.stop()

    def start_timer_ugor(self):
        self.ui.tableUgor.setRowCount(5)
        self.ui.tableUgor.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.textBrowser_6.clear()
        self.ui.btnStopUgor.setVisible(True)
        self.ui.btnStartUgor.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_ugor.start(500)  # Запуск оснавного таймера

        else:
            self.timer_ugor.stop()
            bot.alert('Запустите рыбалку')
            self.ui.btnStartUgor.setVisible(True)
            self.ui.btnStopUgor.setVisible(False)

    def main_loop_ugor(self):
        # Основной цикл вылова (Угорь)
        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))
            if width_f < 100:
                width_f *= 1000

            if str(ulov[0]) == 'Угорь' and (7000 >= width_f >= 5000) and self.f_ugor < 5:
                self.ui.tableUgor.setItem(self.f_ugor, 0, QTableWidgetItem('Угорь'))
                self.ui.tableUgor.setItem(self.f_ugor, 1, QTableWidgetItem(str(int(width_f))))
                self.f_ugor += 1
            if self.f_ugor > 4:
                self.ui.tableUgor.setStyleSheet("background-color: rgb(0, 170, 0);")

            self.count_fish += 1
            self.ui.textBrowser_6.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdUgor.display(str(self.count_fish))

        except:
            pass


    # ---------------------------------- END UGOR_________________________________________


    # ---------------------------------- SUDAK_____________________________________________

    def stop_timer_sudak(self):
        self.ui.tableSudak.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableBigSudak.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.sudak_width = 0
        self.big_sudak_width = 0

        self.ui.tableSudak.setRowCount(0)
        self.ui.tableBigSudak.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdSudak.display(str(self.count_fish))
        self.ui.tableSudak.setRowCount(5)
        self.ui.tableBigSudak.setRowCount(1)
        self.f_sudak = 0
        self.f_big_sudak = 0

        self.ui.btnStopSudak.setVisible(False)
        self.ui.btnStartSudak.setVisible(True)
        self.timer_sudak.stop()

    def start_timer_sudak(self):
        self.ui.tableSudak.setRowCount(5)
        self.ui.tableBigSudak.setRowCount(1)
        self.ui.tableSudak.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableBigSudak.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.textBrowser_5.clear()
        self.ui.btnStopSudak.setVisible(True)
        self.ui.btnStartSudak.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_sudak.start(500)  # Запуск оснавного таймера

        else:
            self.timer_sudak.stop()
            bot.alert('Запустите рыбалку')
            self.ui.btnStartSudak.setVisible(True)
            self.ui.btnStopSudak.setVisible(False)

    def main_loop_sudak(self):
        # Основной цикл вылова (Судак)
        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))
            if width_f < 1000 and width_f == int(width_f):
                pass
            else:
                width_f *= 1000

            if str(ulov[0]) == 'Судак' and width_f >= 9000 and self.f_sudak < 5:
                self.ui.tableSudak.setItem(self.f_sudak, 0, QTableWidgetItem('Судак'))
                self.ui.tableSudak.setItem(self.f_sudak, 1, QTableWidgetItem(str(int(width_f))))
                self.f_sudak += 1
            if self.f_sudak > 4:
                self.ui.tableSudak.setStyleSheet("background-color: rgb(0, 170, 0);")

            if str(ulov[0]) == 'Глубинный судак' and self.f_shuka < 1:
                self.ui.tableBigSudak.setItem(self.f_big_sudak, 0, QTableWidgetItem('Глубинный судак'))
                self.ui.tableBigSudak.setItem(self.f_big_sudak, 1, QTableWidgetItem(str(int(width_f))))
                self.f_big_sudak += 1
            if self.f_big_sudak > 0:
                self.ui.tableBigSudak.setStyleSheet("background-color: rgb(0, 170, 0);")

            self.count_fish += 1
            self.ui.textBrowser_5.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdSudak.display(str(self.count_fish))

        except:
            pass

    # ------------------------------- END SUDAK_____________________________________________


    # ---------------------------------- SHUKA_____________________________________________


    def stop_timer_shuka(self):
        self.ui.tableShuka.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableBigShuka.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.shuka_width = 0
        self.big_shuka_width = 0

        self.ui.tableShuka.setRowCount(0)
        self.ui.tableBigShuka.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdShuka.display(str(self.count_fish))
        self.ui.tableShuka.setRowCount(5)
        self.ui.tableBigShuka.setRowCount(1)
        self.f_shuka = 0
        self.f_big_shuka = 0

        self.ui.btnStopShuka.setVisible(False)
        self.ui.btnStartShuka.setVisible(True)
        self.timer_shuka.stop()

    def start_timer_shuka(self):
        self.ui.tableShuka.setRowCount(5)
        self.ui.tableBigShuka.setRowCount(1)
        self.ui.tableShuka.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableBigShuka.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.textBrowser_4.clear()
        self.ui.btnStopShuka.setVisible(True)
        self.ui.btnStartShuka.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_shuka.start(500)  # Запуск оснавного таймера

        else:
            self.timer_shuka.stop()
            bot.alert('Запустите рыбалку')
            self.ui.btnStartShuka.setVisible(True)
            self.ui.btnStopShuka.setVisible(False)

    def main_loop_shuka(self):
        # Основной цикл вылова (Щука)
        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))
            if width_f < 1000 and width_f == int(width_f):
                pass
            else:
                width_f *= 1000

            if str(ulov[0]) == 'Щука' and width_f >= 15000 and self.f_shuka < 5:
                self.ui.tableShuka.setItem(self.f_shuka, 0, QTableWidgetItem('Щука'))
                self.ui.tableShuka.setItem(self.f_shuka, 1, QTableWidgetItem(str(int(width_f))))
                self.f_shuka += 1
            if self.f_shuka > 4:
                self.ui.tableShuka.setStyleSheet("background-color: rgb(0, 170, 0);")

            if str(ulov[0]) == 'Глубинная щука' and self.f_shuka < 1:
                self.ui.tableBigShuka.setItem(self.f_big_shuka, 0, QTableWidgetItem('Глубинная щука'))
                self.ui.tableBigShuka.setItem(self.f_big_shuka, 1, QTableWidgetItem(str(int(width_f))))
                self.f_big_shuka += 1
            if self.f_big_shuka > 0:
                self.ui.tableBigShuka.setStyleSheet("background-color: rgb(0, 170, 0);")

            self.count_fish += 1
            self.ui.textBrowser_4.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdShuka.display(str(self.count_fish))

        except:
            pass


    # ---------------------------------- END SHUKA_________________________________________

    # ---------------------------------- SIG_______________________________________________

    def start_timer_sig(self):
        self.ui.tableRybec.setRowCount(8)
        self.ui.tableSig.setRowCount(8)
        self.ui.tableLudoga.setRowCount(8)
        self.ui.tableRybec.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableSig.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableLudoga.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.textBrowser_3.clear()
        self.ui.btnStopSig.setVisible(True)
        self.ui.btnStartSig.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_sig.start(500)  # Запуск оснавного таймера

        else:
            self.timer_sig.stop()
            bot.alert('Запустите рыбалку')
            self.ui.btnStartSig.setVisible(True)
            self.ui.btnStopSig.setVisible(False)

    def stop_timer_sig(self):
        self.ui.tableRybec.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableSig.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableLudoga.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.rybec_width = 0
        self.sig_width = 0

        self.ui.tableRybec.setRowCount(0)
        self.ui.tableSig.setRowCount(0)
        self.ui.tableLudoga.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdSig.display(str(self.count_fish))
        self.ui.tableRybec.setRowCount(8)
        self.ui.tableSig.setRowCount(8)
        self.ui.tableLudoga.setRowCount(8)
        self.f_rybec = 0
        self.f_sig = 0
        self.f_ludoga = 0

        self.ui.btnStopSig.setVisible(False)
        self.ui.btnStartSig.setVisible(True)
        self.timer_sig.stop()

    def main_loop_sig(self):
        # Основной цикл вылова (Рипус)
        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))
            if width_f < 1000 and width_f == int(width_f):
                pass
            else:
                width_f *= 1000

            if str(ulov[0]) == 'Рыбец' and width_f >= 250 and self.f_rybec < 8:
                self.ui.tableRybec.setItem(self.f_rybec, 0, QTableWidgetItem('Рыбец'))
                self.ui.tableRybec.setItem(self.f_rybec, 1, QTableWidgetItem(str(int(width_f))))
                self.f_rybec += 1
            if self.f_rybec > 7:
                self.ui.tableRybec.setStyleSheet("background-color: rgb(0, 170, 0);")

            if str(ulov[0]) == 'Сиг' and width_f >= 3000 and self.f_rybec < 8:
                self.ui.tableSig.setItem(self.f_sig, 0, QTableWidgetItem('Сиг'))
                self.ui.tableSig.setItem(self.f_sig, 1, QTableWidgetItem(str(int(width_f))))
                self.f_sig += 1
            if self.f_sig > 7:
                self.ui.tableSig.setStyleSheet("background-color: rgb(0, 170, 0);")

            if str(ulov[0]) == 'Лудога' and width_f >= 350 and self.f_rybec < 8:
                self.ui.tableLudoga.setItem(self.f_ludoga, 0, QTableWidgetItem('Лудога'))
                self.ui.tableLudoga.setItem(self.f_ludoga, 1, QTableWidgetItem(str(int(width_f))))
                self.f_ludoga += 1
            if self.f_ludoga > 7:
                self.ui.tableLudoga.setStyleSheet("background-color: rgb(0, 170, 0);")

            self.count_fish += 1
            self.ui.textBrowser_3.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdSig.display(str(self.count_fish))
        except:
            pass

    # ---------------------------------- END SIG_____________________________________________

    # ---------------------------------- RIPUS_____________________________________________
    def start_timer_ripus(self):
        self.ui.tableRipus.setRowCount(200)
        self.ui.tableKorushka.setRowCount(200)
        self.ui.tableRipus.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableKorushka.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.textBrowser_2.clear()
        self.ui.btnStopRipus.setVisible(True)
        self.ui.btnStartRipus.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_ripus.start(600)  # Запуск оснавного таймера

        else:
            self.timer_ripus.stop()
            bot.alert('Запустите рыбалку')
            self.ui.btnStartRipus.setVisible(True)
            self.ui.btnStopRipus.setVisible(False)

    def stop_timer_ripus(self):
        self.ui.tableRipus.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableKorushka.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ripus_width = 0
        self.ui.lcdR.display(str(self.ripus_width))
        self.corushka_width = 0
        self.ui.lcdK.display(str(self.corushka_width))
        self.ui.tableRipus.setRowCount(0)
        self.ui.tableKorushka.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdRipus.display(str(self.count_fish))
        self.ui.tableRipus.setRowCount(200)
        self.ui.tableKorushka.setRowCount(200)
        self.f_ripus = 0
        self.f_korushka = 0
        self.ui.btnStopRipus.setVisible(False)
        self.ui.btnStartRipus.setVisible(True)
        self.timer_ripus.stop()

    def main_loop_ripus(self):
        # Основной цикл вылова (Рипус)
        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))
            if width_f < 1000 and width_f == int(width_f):
                pass
            else:
                width_f *= 1000

            if str(ulov[0]) == 'Рипус':
                self.ui.tableRipus.setItem(self.f_ripus, 0, QTableWidgetItem('Рипус'))
                self.ui.tableRipus.setItem(self.f_ripus, 1, QTableWidgetItem(str(width_f)))
                self.f_ripus += 1
                self.ripus_width += width_f

            if str(ulov[0]) == 'Корюшка':
                self.ui.tableKorushka.setItem(self.f_korushka, 0, QTableWidgetItem('Корюшка'))
                self.ui.tableKorushka.setItem(self.f_korushka, 1, QTableWidgetItem(str(width_f)))
                self.f_korushka += 1
                self.corushka_width += width_f

            self.ui.lcdR.display(str(self.ripus_width))
            self.ui.lcdK.display(str(self.corushka_width))

            if self.ripus_width >= 15000:
                self.ui.tableRipus.setStyleSheet("background-color: rgb(0, 170, 0);")
            if self.corushka_width >= 5000:
                self.ui.tableKorushka.setStyleSheet("background-color: rgb(0, 170, 0);")

            self.count_fish += 1
            self.ui.textBrowser_2.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdRipus.display(str(self.count_fish))
        except:
            pass

    # ---------------------------------- END RIPUS_____________________________________________

    # --------------------------------------1 TAB----------------------------------------------

    def stop_timer_lesh(self):
        self.ui.tableLesh.setRowCount(0)
        self.ui.tableGustera.setRowCount(0)
        self.ui.tableBeloglazka.setRowCount(0)
        self.count_fish = 0
        self.ui.lcdLesh.display(str(self.count_fish))

        self.ui.tableLesh.setRowCount(9)
        self.ui.tableGustera.setRowCount(3)
        self.ui.tableBeloglazka.setRowCount(6)

        self.f_lesh = 0
        self.f_gustera = 0
        self.f_beloglazka = 0
        self.ui.stopLesh.setVisible(False)
        self.ui.startLesh.setVisible(True)
        self.timer_lesh.stop()

    def start_timer_lesh(self):
        self.ui.tableLesh.setRowCount(9)
        self.ui.tableGustera.setRowCount(3)
        self.ui.tableBeloglazka.setRowCount(6)
        self.ui.tableLesh.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableGustera.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ui.tableBeloglazka.setStyleSheet("background-color: rgb(170, 170, 127);")

        self.ui.textBrowser.clear()
        self.ui.stopLesh.setVisible(True)
        self.ui.startLesh.setVisible(False)
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer_lesh.start(600)  # Запуск оснавного таймера

        else:
            self.timer_lesh.stop()
            bot.alert('Запустите рыбалку')
            self.ui.startLesh.setVisible(True)
            self.ui.stopLesh.setVisible(False)

    def main_loop_lesh(self):

        # Основной цикл вылова (Лещ)

        try:
            ulov = fish_tank()
            width_f = float(ulov[1].split()[1].replace(',', '.'))
            if width_f < 1000 and width_f == int(width_f):
                pass
            else:
                width_f *= 1000

            """Если лещ"""
            if str(ulov[0]) == 'Лещ' and width_f >= 5000 and self.f_lesh < 9:
                self.ui.tableLesh.setItem(self.f_lesh, 0, QTableWidgetItem('Лещ'))
                self.ui.tableLesh.setItem(self.f_lesh, 1, QTableWidgetItem(str(width_f)))
                self.f_lesh += 1

            """Если Густера"""
            if str(ulov[0]) == 'Густера' and width_f >= 300 and self.f_gustera < 4:
                self.ui.tableGustera.setItem(self.f_gustera, 0, QTableWidgetItem('Густера'))
                self.ui.tableGustera.setItem(self.f_gustera, 1, QTableWidgetItem(str(width_f)))
                self.f_gustera += 1

            """Если Белоглазка"""
            if str(ulov[0]) == 'Белоглазка' and width_f >= 250 and self.f_beloglazka < 7:
                self.ui.tableBeloglazka.setItem(self.f_beloglazka, 0, QTableWidgetItem('Белоглазка'))
                self.ui.tableBeloglazka.setItem(self.f_beloglazka, 1, QTableWidgetItem(str(width_f)))
                self.f_beloglazka += 1
            self.count_fish += 1
            self.ui.textBrowser.append(f'{ulov[0]}, {ulov[1]}')
            self.ui.lcdLesh.display(str(self.count_fish))

            if self.f_lesh > 8:
                self.ui.tableLesh.setStyleSheet("background-color: rgb(0, 170, 0);")
            if self.f_gustera > 2:
                self.ui.tableGustera.setStyleSheet("background-color: rgb(0, 170, 0);")

            if self.f_beloglazka > 5:
                self.ui.tableBeloglazka.setStyleSheet("background-color: rgb(0, 170, 0);")

            if self.f_lesh > 8 and self.f_gustera > 2 and self.f_beloglazka > 5:
                self.timer_lesh.stop()
        #  ------------------------------------------- END 1 TAB --------------------------------------------------------------

        except:
            pass

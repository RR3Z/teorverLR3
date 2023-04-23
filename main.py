import math
import sys
import re
from mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QListWidgetItem
from PySide6.QtCore import Slot, Signal
from calculatingFunctions import bernulli, bernulliPolynom, muavLaplasLib, FormulaType
from qpixmapCreator import mathTex_to_QPixmap
class calculatingType:
    bernuli = 0
    polynom = 1
    integral = 2

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        qpixmap = mathTex_to_QPixmap(r"$\frac{-b\pm\sqrt{b^2-4ac}}{2a}$", 20)
        self.ui.photoBernuliFirstFormulaType1.setPixmap(qpixmap)
        
        #Соединяем сигнал кнопки bernuliBtn со слотом setPages с параметром 1
        self.ui.bernuliBtn.clicked.connect(lambda: self.setPages(2))
        self.ui.integralBtn.clicked.connect(lambda: self.setPages(1))
        self.ui.polynomBtn.clicked.connect(lambda: self.setPages(0))

        
        #Соединяем сигнал кнопки calculateBtn со слотом calculate
        self.ui.calculateBernuliBtn.clicked.connect(lambda: self.calculate(calculatingType.bernuli))
        self.ui.calculatePolynomBtn.clicked.connect(lambda: self.calculate(calculatingType.polynom))
        self.ui.calculateIntegralBtn.clicked.connect(lambda: self.calculate(calculatingType.integral))

      

    @Slot()
    def setPages(self, pageIndex):
        if self.ui.mainWidget.currentIndex() == 2 and pageIndex == 1:
            buffer = self.ui.bernuliParamsLine.text()
            self.ui.nNumberLine.setText(buffer)
        if self.ui.mainWidget.currentIndex() == 1 and pageIndex == 2:
            buffer = self.ui.nNumberLine.text()
            self.ui.bernuliParamsLine.setText(buffer)
               
        self.ui.mainWidget.setCurrentIndex(pageIndex)
       

    @Slot()
    def calculate(self, type : calculatingType):
        
        if type == calculatingType.bernuli:
            #Преобразуем строку в набор чисел число с плавающей точкой
            string = self.ui.bernuliParamsLine.text()
            params = re.findall(r"[-+]?\d*\.\d+|\d+", string)
            result = 0
            
            if self.ui.bernuliFormulaType.currentRow() == -1:
                result = "Выберите формулу"
            else:
                formula = FormulaType(self.ui.bernuliFormulaType.currentRow())
                if (len(params) != 4 and formula == FormulaType.INTERVAL) or (len(params) != 3 and (formula == FormulaType.EQUALITY or formula == FormulaType.LOWER or formula == FormulaType.HIGHEREQUAL)):
                    result = "Неверное количество параметров"
                else:
                    if len(params) == 3:
                        params.append(0)
                    if int(params[1]) < max(int(params[2]), int(params[3])):
                        result = "Введено неверное значение, n должно быть больше m1 и m2"
                    elif float(params[0]) > 1 or float(params[0]) < 0:
                        result = "Введено неверное значение, p должно быть в диапазоне от 0 до 1"
                    else:
                        result = bernulli(float(params[0]), int(params[1]), int(params[2]), int(params[3]), FormulaType(self.ui.bernuliFormulaType.currentRow()))
                        result = round(result, 5)
                    
            self.ui.bernuliAnswerLine.setText(str(result))
        elif type == calculatingType.polynom:
            n = int(self.ui.nParamLine.text())
            
            m = re.findall(r"[-+]?\d*\.\d+|\d+", self.ui.mParamsLine.text())
            p = re.findall(r"[-+]?\d*\.\d+|\d+", self.ui.pParamsLine.text())
            m = list(map(int, m))
            p = list(map(float, p))
            #Добавить ограничения с выводом ошибок
            if len(m) != len(p):
                result = "Неверное количество параметров"
            elif len(m) == 0:
                result = "Введите хотя бы один параметр"
            #Провека, что сумма всех m = n
            elif sum(m) != n:
                result = "Введено неверное значение, сумма всех m должна быть равна n"
            #Проверка, что все p в диапазоне от 0 до 1
            elif any(x > 1 or x < 0 for x in p):
                result = "Введено неверное значение, p должно быть в диапазоне от 0 до 1"
            else:
                result = bernulliPolynom(n, p, m)
                result = round(result, 5)
            
            self.ui.polynomAnswerLine.setText(str(result))
        elif type == calculatingType.integral:
            params = re.findall(r"[-+]?\d*\.\d+|\d+", self.ui.nNumberLine.text())
            if len(params) != 4:
                result = "Неверное количество параметров"
            else:
                n = int(params[1])
                p = float(params[0])
                m1 = int(params[2])
                m2 = int(params[3])
                if p > 1 or p < 0:
                    result = "Введено неверное значение, p должно быть в диапазоне от 0 до 1"
                elif m1 > m2:
                    result = "Введено неверное значение, m1 должно быть меньше m2"
                elif n < m2:
                    result = "Введено неверное значение, n должно быть больше m2"
                elif m1 < 0:
                    result = "Введено неверное значение, m1 должно быть больше 0"
                else:
                    resultArray = muavLaplasLib(n,m1, m2, p)
                    result = round(resultArray[0], 5)
                    x1 = resultArray[1]
                    x2 = resultArray[2]
                    self.ui.x1ResultLabel.setText(str(round(x1, 5)))
                    self.ui.x2ResultLabel.setText(str(round(x2, 5)))
                
            self.ui.integralAnswerLine.setText(str(result))
        
        
    
    
    



if __name__ == "__main__":
    app = QApplication()
    window = MainWindow() 
    window.show()
    sys.exit(app.exec())
    



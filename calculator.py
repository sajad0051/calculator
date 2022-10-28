
from PySide6.QtWidgets import QWidget,QApplication
from PySide6.QtUiTools import QUiLoader
from functools import partial
class calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.loader=QUiLoader()
        self.ui=self.loader.load('from.ui')
        self.ui.btn0.clicked.connect(partial(self.number,'0'))
        self.ui.btn1.clicked.connect(partial(self.number,'1'))
        self.ui.btn2.clicked.connect(partial(self.number,'2'))
        self.ui.btn3.clicked.connect(partial(self.number,'3'))
        self.ui.btn4.clicked.connect(partial(self.number,'4'))
        self.ui.btn5.clicked.connect(partial(self.number,'5'))
        self.ui.btn6.clicked.connect(partial(self.number,'6'))
        self.ui.btn7.clicked.connect(partial(self.number,'7'))
        self.ui.btn8.clicked.connect(partial(self.number,'8'))
        self.ui.btn9.clicked.connect(partial(self.number,'9'))
        self.ui.btn_sum.clicked.connect(partial(self.op,'+'))
        self.ui.btn_tg.clicked.connect(partial(self.ogh,'/'))
        self.ui.btn_taf.clicked.connect(partial(self.ot,'-'))
        self.ui.btn_zarb.clicked.connect(partial(self.oz,'*'))
        self.ui.btn_n.clicked.connect(partial(self.os,'.'))
        self.ui.btn_c.clicked.connect(partial(self.c))
        self.ui.btn_eq.clicked.connect(self.eq)
        self.ui.btn_eq.clicked.connect(self.eg)
        self.ui.btn_eq.clicked.connect(self.et)
        self.ui.btn_eq.clicked.connect(self.ez)
        
        self.ui.show()

    def number(self,num):
        txt=self.ui.lbl.text()
        self.ui.lbl.setText(txt+num)

    def os(self,num):
        txt=self.ui.lbl.text()
        if num =='.':
            for t in txt:
                if t=='.':
                    break
            else:
                self.ui.lbl.setText(txt+num)
        else:
            self.ui.lbl.setText(txt+num)
                


    def op(self,operator):
        if self.op != '':
            self.eq()
        self.num1=self.ui.lbl.text()
        self.op=operator
        self.ui.lbl.setText('')
    def eq(self):
        self.num2=self.ui.lbl.text()
        if self.op == '+':
            self.num1=float(self.num1)+float(self.num2)
            self.op=''
            self.ui.lbl.setText(str(self.num1))

    def ot(self,operator):
        if self.ot != '':
            self.et()
        self.num1=self.ui.lbl.text()
        self.ot=operator
        self.ui.lbl.setText('')

    def et(self):
        self.num2=self.ui.lbl.text()
        if self.ot == '-':
            self.num1=float(self.num1)-float(self.num2)
            self.ot=''
            self.ui.lbl.setText(str(self.num1))

    def oz(self,operator):
        if self.oz != '':
            self.ez()
        self.num1=self.ui.lbl.text()
        self.oz=operator
        self.ui.lbl.setText('')

    def ez(self):
        self.num2=self.ui.lbl.text()
        if self.oz == '*':
            self.num3=float(self.num1)*float(self.num2)
            self.oz=''
            self.ui.lbl.setText(str(self.num3))

    def ogh(self,operator):
        if self.ogh != '':
            self.eg()
        self.num7=self.ui.lbl.text()
        self.ogh=operator
        self.ui.lbl.setText('')

    def eg(self):
        self.num8=self.ui.lbl.text()
        if self.ogh == '/':
            self.num7=float(self.num7)/float(self.num8)
            self.ogh=''
            self.ui.lbl.setText(str(self.num7))
    def c(self):
        self.ui.lbl.setText('')

        


app=QApplication([])
main=calculator()
app.exit(app.exec())
test=False

from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
import sys, os,AI
import re
version="1.2"
app = QApplication(sys.argv)
konto_fenster = []

def Konto(name):
    mon = 0
    ordner_liste = [f for f in os.listdir("Kontos") if os.path.isdir(os.path.join("Kontos", f))]
    windowa = QWidget()
    windowa.setWindowTitle("MoneyTracker - " + name)
    
    konto_fenster.append(windowa)

    al=[]
    bl=[]
    cl=[]
    di={}
    dicc={}

    def Find(name):
        al=[]
        bl=[]
        cl=[]
        mon=0
        
        with open("Kontos/"+name+"/his.txt","r",encoding="utf-8") as f:
            his_txt=f.readlines()

        for i in his_txt:
            i=i.strip()
            if i=="":
                continue
            typee,numm,namee,kontoo,datummzeit=i.split(" ")
            datumm,zeitt=datummzeit.split("-")

            if typee=="+":
                mon=mon+float(numm)
                nameee="+$"+numm+" "+namee+"  "+datumm+" "+zeitt
                di[nameee]=i.split(" ")
                al.append(nameee)
                cl.append(nameee)
                
            elif typee=="-":
                mon=mon-float(numm)
                nameee="-$"+numm+" "+namee+"  "+datumm+" "+zeitt
                di[nameee]=i.split(" ")
                al.append(nameee)
                cl.append(nameee)
                
            elif typee=="<":
                mon=mon-float(numm)
                nameee="-$"+numm+" "+name+">"+kontoo+"  "+namee+"  "+datumm+" "+zeitt
                di[nameee]=i.split(" ")
                al.append(nameee)
                cl.append(nameee)
                
            elif typee==">":
                mon=mon+float(numm)
                nameee="+$"+numm+" "+kontoo+">"+name+"  "+namee+"  "+datumm+" "+zeitt
                di[nameee]=i.split(" ")
                al.append(nameee)
                cl.append(nameee)
                
            elif typee=="a":
                mon=mon-float(numm)
                nameee="-$"+numm+" lent  "+namee+"  "+datumm+" "+zeitt
                di[nameee]=i.split(" ")
                dicc[namee]=nameee
                al.append(nameee)
                bl.append(nameee)
                
            elif typee=="aa":
                aaa=dicc[namee]
                index = al.index(aaa)
                al[index] = aaa+" (Returned on "+datumm+" "+zeitt+")"
                index = bl.index(aaa)
                bl[index] = aaa+" (Returned on "+datumm+" "+zeitt+")"
                
            elif typee=="b":
                mon=mon+float(numm)
                nameee="+$"+numm+" borrowed  "+namee+"  "+datumm+" "+zeitt
                di[nameee]=i.split(" ")
                dicc[namee]=nameee
                al.append(nameee)
                bl.append(nameee)
                
            elif typee=="bb":
                aaa=dicc[namee]
                index = al.index(aaa)
                al[index] = aaa+" (Returned on "+datumm+" "+zeitt+")"
                index = bl.index(aaa)
                bl[index] = aaa+" (Returned on "+datumm+" "+zeitt+")"
                
            else:
                nameee="Error! text:"+i
                al.append(nameee)
                bl.append(nameee)
                cl.append(nameee)
        
        al.reverse()
        bl.reverse()
        cl.reverse()

        return al,bl,cl,mon
    def suchen(text):
        
        alsn = []
        blsn = []
        clsn = []
        hasht=""

        if "#" in text:
            hasht=text.split("#")

            for i in al:
                for ii in hasht:
                    f=True
                    if ii.lower() in i.lower():
                        continue
                    f=False
                    break
                if f:
                    alsn.append(i)

            for i in bl:
                for ii in hasht:
                    f=True
                    if ii.lower() in i.lower():
                        continue
                    f=False
                    break
                if f:
                    blsn.append(i)

            for i in cl:
                for ii in hasht:
                    f=True
                    if ii.lower() in i.lower():
                        continue
                    f=False
                    break
                if f:
                    clsn.append(i)

        else:
            for i in al:
                if text.lower() in i.lower():
                    alsn.append(i)

            for i in bl:
                if text.lower() in i.lower():
                    blsn.append(i)

            for i in cl:
                if text.lower() in i.lower():
                    clsn.append(i)

        a.clear()
        a.addItems(alsn)

        b.clear()
        b.addItems(blsn)

        c.clear()
        c.addItems(clsn)


    def Ch(text):
        nonlocal al, bl, cl, mon, name
        name=text
        windowa.setWindowTitle("MoneyTracker - " + text)

        al,bl,cl,mon=Find(text)

        a.clear()
        a.addItems(al)

        b.clear()
        b.addItems(bl)

        c.clear()
        c.addItems(cl)

        label.setText(f"Money: {mon:.2f} $")


    def add():

        allll=[
            "Income",
            "Expense",
            "Transfer (Incoming)",
            "Transfer (Outgoing)",
            "Lend Money",
            "Borrow Money"
        ]

        dialog = QDialog(windowa)
        dialog.setWindowTitle("MoneyTracker - Add")

        layout = QVBoxLayout(dialog)

        seiten = QStackedWidget()


        # Page 1
        seite1 = QWidget()
        l1 = QVBoxLayout(seite1)

        nameentry1 = QLineEdit()
        nameentry1.setPlaceholderText("Name")
        l1.addWidget(nameentry1)

        geldentry1 = QDoubleSpinBox()
        geldentry1.setDecimals(2)
        geldentry1.setRange(0, 1000000000)
        geldentry1.setPrefix("$+ ")
        geldentry1.setSingleStep(0.01)
        l1.addWidget(geldentry1)

        datumentry1 = QDateEdit()
        datumentry1.setDate(QDate.currentDate())
        datumentry1.setDisplayFormat("dd.MM.yyyy")
        datumentry1.setCalendarPopup(True)
        l1.addWidget(datumentry1)

        zeitentry1 = QTimeEdit()
        zeitentry1.setTime(QTime.currentTime())
        zeitentry1.setDisplayFormat("HH:mm")
        l1.addWidget(zeitentry1)

        seiten.addWidget(seite1)



        # Page 2
        seite2 = QWidget()
        l2 = QVBoxLayout(seite2)

        nameentry2 = QLineEdit()
        nameentry2.setPlaceholderText("Name")
        l2.addWidget(nameentry2)

        geldentry2 = QDoubleSpinBox()
        geldentry2.setDecimals(2)
        geldentry2.setRange(0, 1000000000)
        geldentry2.setPrefix("$- ")
        geldentry2.setSingleStep(0.01)
        l2.addWidget(geldentry2)

        datumentry2 = QDateEdit()
        datumentry2.setDate(QDate.currentDate())
        datumentry2.setDisplayFormat("dd.MM.yyyy")
        datumentry2.setCalendarPopup(True)
        l2.addWidget(datumentry2)

        zeitentry2 = QTimeEdit()
        zeitentry2.setTime(QTime.currentTime())
        zeitentry2.setDisplayFormat("HH:mm")
        l2.addWidget(zeitentry2)

        seiten.addWidget(seite2)
        seite3 = QWidget()
        l3 = QVBoxLayout(seite3)

        nameentry3 = QLineEdit()
        nameentry3.setPlaceholderText("Name")
        l3.addWidget(nameentry3)

        geldentry3 = QDoubleSpinBox()
        geldentry3.setDecimals(2)
        geldentry3.setRange(0, 1000000000)
        geldentry3.setPrefix("$+ ")
        geldentry3.setSingleStep(0.01)
        l3.addWidget(geldentry3)

        datumentry3 = QDateEdit()
        datumentry3.setDate(QDate.currentDate())
        datumentry3.setDisplayFormat("dd.MM.yyyy")
        datumentry3.setCalendarPopup(True)
        l3.addWidget(datumentry3)

        zeitentry3 = QTimeEdit()
        zeitentry3.setTime(QTime.currentTime())
        zeitentry3.setDisplayFormat("HH:mm")
        l3.addWidget(zeitentry3)

        l3.addWidget(QLabel("From:"))

        konto3 = QComboBox()
        konto3.addItems(ordner_liste)
        l3.addWidget(konto3)

        seiten.addWidget(seite3)


        seite4 = QWidget()
        l4 = QVBoxLayout(seite4)

        nameentry4 = QLineEdit()
        nameentry4.setPlaceholderText("Name")
        l4.addWidget(nameentry4)

        geldentry4 = QDoubleSpinBox()
        geldentry4.setDecimals(2)
        geldentry4.setRange(0, 1000000000)
        geldentry4.setPrefix("$- ")
        geldentry4.setSingleStep(0.01)
        l4.addWidget(geldentry4)

        datumentry4 = QDateEdit()
        datumentry4.setDate(QDate.currentDate())
        datumentry4.setDisplayFormat("dd.MM.yyyy")
        datumentry4.setCalendarPopup(True)
        l4.addWidget(datumentry4)

        zeitentry4 = QTimeEdit()
        zeitentry4.setTime(QTime.currentTime())
        zeitentry4.setDisplayFormat("HH:mm")
        l4.addWidget(zeitentry4)

        l4.addWidget(QLabel("To:"))

        konto4 = QComboBox()
        konto4.addItems(ordner_liste)
        l4.addWidget(konto4)

        seiten.addWidget(seite4)
        
        seite5 = QWidget()
        l5 = QVBoxLayout(seite5)

        nameentry5 = QLineEdit()
        nameentry5.setPlaceholderText("Name")
        l5.addWidget(nameentry5)

        geldentry5 = QDoubleSpinBox()
        geldentry5.setDecimals(2)
        geldentry5.setRange(0, 1000000000)
        geldentry5.setPrefix("$- ")
        geldentry5.setSingleStep(0.01)
        l5.addWidget(geldentry5)

        datumentry5 = QDateEdit()
        datumentry5.setDate(QDate.currentDate())
        datumentry5.setDisplayFormat("dd.MM.yyyy")
        datumentry5.setCalendarPopup(True)
        l5.addWidget(datumentry5)

        zeitentry5 = QTimeEdit()
        zeitentry5.setTime(QTime.currentTime())
        zeitentry5.setDisplayFormat("HH:mm")
        l5.addWidget(zeitentry5)

        seiten.addWidget(seite5)
        
        
        seite6 = QWidget()
        l6 = QVBoxLayout(seite6)

        nameentry6 = QLineEdit()
        nameentry6.setPlaceholderText("Name")
        l6.addWidget(nameentry6)

        geldentry6 = QDoubleSpinBox()
        geldentry6.setDecimals(2)
        geldentry6.setRange(0, 1000000000)
        geldentry6.setPrefix("$+ ")
        geldentry6.setSingleStep(0.01)
        l6.addWidget(geldentry6)

        datumentry6 = QDateEdit()
        datumentry6.setDate(QDate.currentDate())
        datumentry6.setDisplayFormat("dd.MM.yyyy")
        datumentry6.setCalendarPopup(True)
        l6.addWidget(datumentry6)

        zeitentry6 = QTimeEdit()
        zeitentry6.setTime(QTime.currentTime())
        zeitentry6.setDisplayFormat("HH:mm")
        l6.addWidget(zeitentry6)

        seiten.addWidget(seite6)

        def Chh(text):
            index = allll.index(text)
            print(index)
            seiten.setCurrentIndex(index)


        layout.addWidget(QLabel("Select Type: "))

        amd = QComboBox()
        amd.addItems(allll)
        amd.currentTextChanged.connect(Chh)
        layout.addWidget(amd)

        seiten.setCurrentIndex(0)

        layout.addWidget(seiten)
        def addd():
            t = amd.currentText()
            
            if t=="Income":
                text="+ "+str(geldentry1.value())+" "+nameentry1.text()+" - "+datumentry1.text()+"-"+zeitentry1.text()
            
            elif t=="Expense":
                text="- "+str(geldentry2.value())+" "+nameentry2.text()+" - "+datumentry2.text()+"-"+zeitentry2.text()
            
            elif t=="Transfer (Incoming)":
                with open("Kontos/"+konto3.currentText()+"/his.txt","a",encoding="utf-8") as f:
                    print("Kontos/"+konto3.currentText()+"/his.txt",name)
                    f.write("\n< "+str(geldentry3.value())+" "+nameentry3.text()+" "+name+" "+datumentry3.text()+"-"+zeitentry3.text())
                text="> "+str(geldentry3.value())+" "+nameentry3.text()+" "+konto3.currentText()+" "+datumentry3.text()+"-"+zeitentry3.text()
            
            elif t=="Transfer (Outgoing)":
                with open("Kontos/"+konto4.currentText()+"/his.txt","a",encoding="utf-8") as f:
                    f.write("\n> "+str(geldentry4.value())+" "+nameentry4.text()+" "+name+" "+datumentry4.text()+"-"+zeitentry4.text())
                text="< "+str(geldentry4.value())+" "+nameentry4.text()+" "+konto4.currentText()+" "+datumentry4.text()+"-"+zeitentry4.text()
            
            elif t=="Lend Money":
                text="a "+str(geldentry5.value())+" "+nameentry5.text()+" - "+datumentry5.text()+"-"+zeitentry5.text()
                
            elif t=="Borrow Money":
                text="b "+str(geldentry6.value())+" "+nameentry6.text()+" - "+datumentry6.text()+"-"+zeitentry6.text()
            else:
                print("Error: "+t)
            
            with open("Kontos/"+name+"/his.txt","a",encoding="utf-8") as f:
                f.write("\n"+text)
            dialog.close()
            Ch(name)
        buttona = QPushButton("Add")
        buttona.clicked.connect(addd)
        layout.addWidget(buttona)


        buttonaa = QPushButton("Cancel")
        buttonaa.clicked.connect(dialog.close)
        layout.addWidget(buttonaa)
        
        dialog.exec()
        
    def edit():
        for i in [a.currentItem(),b.currentItem(),c.currentItem()]:
            if i==None:
                continue
            tx=i.text()
            
        print(tx)
        l=di[tx]
        typee=l[0]
        inte=l[1]
        namee=l[2]
        kontoe=l[3]
        datumzeite=l[4]
        datume,zeite=datumzeite.split("-")
        allll=[
            "Income",
            "Expense",
            "Transfer (Incoming)",
            "Transfer (Outgoing)",
            "Lend Money",
            "Borrow Money"
        ]

        dialog = QDialog(windowa)
        dialog.setWindowTitle("MoneyTracker - Edit")

        layout = QVBoxLayout(dialog)

        seiten = QStackedWidget()


        # Page 1
        seite1 = QWidget()
        l1 = QVBoxLayout(seite1)

        nameentry1 = QLineEdit()
        nameentry1.setPlaceholderText("Name")
        l1.addWidget(nameentry1)

        geldentry1 = QDoubleSpinBox()
        geldentry1.setDecimals(2)
        geldentry1.setRange(0, 1000000000)
        geldentry1.setPrefix("$+ ")
        geldentry1.setSingleStep(0.01)
        l1.addWidget(geldentry1)

        datumentry1 = QDateEdit()
        datumentry1.setDate(QDate.currentDate())
        datumentry1.setDisplayFormat("dd.MM.yyyy")
        datumentry1.setCalendarPopup(True)
        l1.addWidget(datumentry1)

        zeitentry1 = QTimeEdit()
        zeitentry1.setTime(QTime.currentTime())
        zeitentry1.setDisplayFormat("HH:mm")
        l1.addWidget(zeitentry1)

        seiten.addWidget(seite1)



        # Page 2
        seite2 = QWidget()
        l2 = QVBoxLayout(seite2)

        nameentry2 = QLineEdit()
        nameentry2.setPlaceholderText("Name")
        l2.addWidget(nameentry2)

        geldentry2 = QDoubleSpinBox()
        geldentry2.setDecimals(2)
        geldentry2.setRange(0, 1000000000)
        geldentry2.setPrefix("$- ")
        geldentry2.setSingleStep(0.01)
        l2.addWidget(geldentry2)

        datumentry2 = QDateEdit()
        datumentry2.setDate(QDate.currentDate())
        datumentry2.setDisplayFormat("dd.MM.yyyy")
        datumentry2.setCalendarPopup(True)
        l2.addWidget(datumentry2)

        zeitentry2 = QTimeEdit()
        zeitentry2.setTime(QTime.currentTime())
        zeitentry2.setDisplayFormat("HH:mm")
        l2.addWidget(zeitentry2)

        seiten.addWidget(seite2)
        seite3 = QWidget()
        l3 = QVBoxLayout(seite3)

        nameentry3 = QLineEdit()
        nameentry3.setPlaceholderText("Name")
        l3.addWidget(nameentry3)

        geldentry3 = QDoubleSpinBox()
        geldentry3.setDecimals(2)
        geldentry3.setRange(0, 1000000000)
        geldentry3.setPrefix("$+ ")
        geldentry3.setSingleStep(0.01)
        l3.addWidget(geldentry3)

        datumentry3 = QDateEdit()
        datumentry3.setDate(QDate.currentDate())
        datumentry3.setDisplayFormat("dd.MM.yyyy")
        datumentry3.setCalendarPopup(True)
        l3.addWidget(datumentry3)

        zeitentry3 = QTimeEdit()
        zeitentry3.setTime(QTime.currentTime())
        zeitentry3.setDisplayFormat("HH:mm")
        l3.addWidget(zeitentry3)

        l3.addWidget(QLabel("From:"))

        konto3 = QComboBox()
        konto3.addItems(ordner_liste)
        l3.addWidget(konto3)

        seiten.addWidget(seite3)


        seite4 = QWidget()
        l4 = QVBoxLayout(seite4)

        nameentry4 = QLineEdit()
        nameentry4.setPlaceholderText("Name")
        l4.addWidget(nameentry4)

        geldentry4 = QDoubleSpinBox()
        geldentry4.setDecimals(2)
        geldentry4.setRange(0, 1000000000)
        geldentry4.setPrefix("$- ")
        geldentry4.setSingleStep(0.01)
        l4.addWidget(geldentry4)

        datumentry4 = QDateEdit()
        datumentry4.setDate(QDate.currentDate())
        datumentry4.setDisplayFormat("dd.MM.yyyy")
        datumentry4.setCalendarPopup(True)
        l4.addWidget(datumentry4)

        zeitentry4 = QTimeEdit()
        zeitentry4.setTime(QTime.currentTime())
        zeitentry4.setDisplayFormat("HH:mm")
        l4.addWidget(zeitentry4)

        l4.addWidget(QLabel("To:"))

        konto4 = QComboBox()
        konto4.addItems(ordner_liste)
        l4.addWidget(konto4)

        seiten.addWidget(seite4)
        
        seite5 = QWidget()
        l5 = QVBoxLayout(seite5)

        nameentry5 = QLineEdit()
        nameentry5.setPlaceholderText("Name")
        l5.addWidget(nameentry5)

        geldentry5 = QDoubleSpinBox()
        geldentry5.setDecimals(2)
        geldentry5.setRange(0, 1000000000)
        geldentry5.setPrefix("$- ")
        geldentry5.setSingleStep(0.01)
        l5.addWidget(geldentry5)

        datumentry5 = QDateEdit()
        datumentry5.setDate(QDate.currentDate())
        datumentry5.setDisplayFormat("dd.MM.yyyy")
        datumentry5.setCalendarPopup(True)
        l5.addWidget(datumentry5)

        zeitentry5 = QTimeEdit()
        zeitentry5.setTime(QTime.currentTime())
        zeitentry5.setDisplayFormat("HH:mm")
        l5.addWidget(zeitentry5)

        seiten.addWidget(seite5)
        
        
        seite6 = QWidget()
        l6 = QVBoxLayout(seite6)

        nameentry6 = QLineEdit()
        nameentry6.setPlaceholderText("Name")
        l6.addWidget(nameentry6)

        geldentry6 = QDoubleSpinBox()
        geldentry6.setDecimals(2)
        geldentry6.setRange(0, 1000000000)
        geldentry6.setPrefix("$+ ")
        geldentry6.setSingleStep(0.01)
        l6.addWidget(geldentry6)

        datumentry6 = QDateEdit()
        datumentry6.setDate(QDate.currentDate())
        datumentry6.setDisplayFormat("dd.MM.yyyy")
        datumentry6.setCalendarPopup(True)
        l6.addWidget(datumentry6)

        zeitentry6 = QTimeEdit()
        zeitentry6.setTime(QTime.currentTime())
        zeitentry6.setDisplayFormat("HH:mm")
        l6.addWidget(zeitentry6)

        seiten.addWidget(seite6)

        

        des=False
        
        if typee=="+":
            seiten.setCurrentIndex(0)
            nameentry1.setText(namee)
            geldentry1.setValue(float(inte))
            datumentry1.setDate(QDate.fromString(datume, "dd.MM.yyyy"))
            zeitentry1.setTime(QTime.fromString(zeite, "HH:mm"))
            t="Income"
        elif typee=="-":
            seiten.setCurrentIndex(1)
            nameentry2.setText(namee)
            geldentry2.setValue(float(inte))
            datumentry2.setDate(QDate.fromString(datume, "dd.MM.yyyy"))
            zeitentry2.setTime(QTime.fromString(zeite, "HH:mm"))
            t="Expense"
        elif typee==">":
            return
            des=True
            dialog.close()
            seiten.setCurrentIndex(2)
            nameentry3.setText(namee)
            geldentry3.setValue(float(inte))
            datumentry3.setDate(QDate.fromString(datume, "dd.MM.yyyy"))
            zeitentry3.setTime(QTime.fromString(zeite, "HH:mm"))
            konto3.setCurrentText(kontoe)
            t="Transfer (Incoming)"
        elif typee=="<":
            return
            des=True
            dialog.close()
            seiten.setCurrentIndex(3)
            nameentry4.setText(namee)
            geldentry4.setValue(float(inte))
            datumentry4.setDate(QDate.fromString(datume, "dd.MM.yyyy"))
            zeitentry4.setTime(QTime.fromString(zeite, "HH:mm"))
            konto4.setCurrentText(kontoe)
            t="Transfer (Outgoing)"
        elif typee=="a":
            seiten.setCurrentIndex(4)
            nameentry5.setText(namee)
            geldentry5.setValue(float(inte))
            datumentry5.setDate(QDate.fromString(datume, "dd.MM.yyyy"))
            zeitentry5.setTime(QTime.fromString(zeite, "HH:mm"))
            t="Lend Money"
        elif typee=="b":
            seiten.setCurrentIndex(5)
            nameentry6.setText(namee)
            geldentry6.setValue(float(inte))
            datumentry6.setDate(QDate.fromString(datume, "dd.MM.yyyy"))
            zeitentry6.setTime(QTime.fromString(zeite, "HH:mm"))
            t="Borrow Money"
        layout.addWidget(seiten)
        def addd():
            
            
            if t=="Income":
                text="+ "+str(geldentry1.value())+" "+nameentry1.text()+" - "+datumentry1.text()+"-"+zeitentry1.text()
            
            elif t=="Expense":
                text="- "+str(geldentry2.value())+" "+nameentry2.text()+" - "+datumentry2.text()+"-"+zeitentry2.text()
            
            elif t=="Transfer (Incoming)":
                with open("Kontos/"+konto3.currentText()+"/his.txt","a",encoding="utf-8") as f:
                    print("Kontos/"+konto3.currentText()+"/his.txt",name)
                    f.write("\n< "+str(geldentry3.value())+" "+nameentry3.text()+" "+name+" "+datumentry3.text()+"-"+zeitentry3.text())
                text="> "+str(geldentry3.value())+" "+nameentry3.text()+" "+konto3.currentText()+" "+datumentry3.text()+"-"+zeitentry3.text()
            
            elif t=="Transfer (Outgoing)":
                with open("Kontos/"+konto4.currentText()+"/his.txt","a",encoding="utf-8") as f:
                    f.write("\n> "+str(geldentry4.value())+" "+nameentry4.text()+" "+name+" "+datumentry4.text()+"-"+zeitentry4.text())
                text="< "+str(geldentry4.value())+" "+nameentry4.text()+" "+konto4.currentText()+" "+datumentry4.text()+"-"+zeitentry4.text()
            
            elif t=="Lend Money":
                text="a "+str(geldentry5.value())+" "+nameentry5.text()+" - "+datumentry5.text()+"-"+zeitentry5.text()
                
            elif t=="Borrow Money":
                text="b "+str(geldentry6.value())+" "+nameentry6.text()+" - "+datumentry6.text()+"-"+zeitentry6.text()
            else:
                print("Error: "+t)
            
            with open("Kontos/"+name+"/his.txt","r",encoding="utf-8") as f:
                tt=f.read()
            original = " ".join(di[tx])
            tt=tt.replace(original,text)
            with open("Kontos/"+name+"/his.txt","w",encoding="utf-8") as f:
                f.write(tt)
            dialog.close()
            Ch(name)
        buttona = QPushButton("Save")
        buttona.clicked.connect(addd)
        layout.addWidget(buttona)

        
        buttonaa = QPushButton("Cancel")
        buttonaa.clicked.connect(dialog.close)
        layout.addWidget(buttonaa)
        
        
        
        dialog.exec()
        
    def dell():
        for i in [a.currentItem(),b.currentItem(),c.currentItem()]:
            if i==None:
                continue
            tx=i.text()
        
        with open("Kontos/"+name+"/his.txt","r",encoding="utf-8") as f:
            tt=f.read()
        original = " ".join(di[tx])
        tt=tt.replace(original,"")
        with open("Kontos/"+name+"/his.txt","w",encoding="utf-8") as f:
            f.write(tt)
        Ch(name)
    al, bl, cl, mon=Find(name)
    windowa.setWindowIcon(QIcon("icon.ico"))

    main_layout = QHBoxLayout()

    links = QVBoxLayout()
    mitte = QVBoxLayout()
    rechts = QVBoxLayout()


    mein_dropdown = QComboBox()

    for i in [f for f in os.listdir("Kontos") if os.path.isdir(os.path.join("Kontos", f))]:
        mein_dropdown.addItem(i)

    mein_dropdown.setFixedHeight(35)
    mein_dropdown.currentTextChanged.connect(Ch)
    
    links.addWidget(mein_dropdown)


    a=QListWidget()
    a.addItems(al)
    links.addWidget(a)


    buttona = QPushButton("Add")
    buttona.clicked.connect(add)
    links.addWidget(buttona)

    
    label = QLabel(f"Money: {mon:.2f} $")
    label.setStyleSheet("font-size: 20pt;")
    mitte.addWidget(label, alignment=Qt.AlignCenter)

    
    b=QListWidget()
    b.addItems(bl)
    mitte.addWidget(b)
    
    buttonb = QPushButton("Edit")
    buttonb.clicked.connect(edit)
    mitte.addWidget(buttonb)

    eingabe = QLineEdit()
    eingabe.setPlaceholderText("Search")
    eingabe.setFixedHeight(35)
    eingabe.textChanged.connect(lambda:suchen(eingabe.text()))

    rechts.addWidget(eingabe)


    c=QListWidget()
    c.addItems(cl)
    rechts.addWidget(c)

    buttonc = QPushButton("Del")
    buttonc.clicked.connect(dell)
    rechts.addWidget(buttonc)

    def auswahl_geaendert(aktive_liste):
        for liste in (a, b, c):
            if liste != aktive_liste:
                liste.blockSignals(True)
                liste.setCurrentRow(-1)
                liste.clearSelection()
                liste.blockSignals(False)


    a.itemSelectionChanged.connect(lambda: auswahl_geaendert(a))
    b.itemSelectionChanged.connect(lambda: auswahl_geaendert(b))
    c.itemSelectionChanged.connect(lambda: auswahl_geaendert(c))


    main_layout.addLayout(links)
    main_layout.addLayout(mitte)
    main_layout.addLayout(rechts)
    
    mein_dropdown.setCurrentText(name)
    
    windowa.setLayout(main_layout)
    windowa.show()
def Main():
    fenstera=None
    def AIA():
        global fenstera
        def senden():
            text = eingabe.text()

            if text:
                label = QLabel("Du:\n" + text)
                label.setWordWrap(True)
                label.setStyleSheet("""
                    background:#25D366;
                    border-radius:10px;
                    padding:8px;
                """)

                item = QListWidgetItem(chat)
                item.setSizeHint(label.sizeHint())

                chat.addItem(item)
                chat.setItemWidget(item, label)

                eingabe.clear()                
                
                
                texta=AI.ask(text)
                
                textal=texta.split("\n")
                muster = r"\{.+,.+,.+,.+,.+,.+\}"
                for i in textal:
                    i=i.strip()
                    
                    if re.fullmatch(muster, i):
                        i=i.replace("{","").replace("}","")
                        konto,ty,me,na,zk,datetime=i.split(",")
                        with open("Kontos/"+konto+"/his.txt","a",encoding="utf-8")as f:
                            f.write(f"\n{ty} {me} {na} {zk} {datetime}")
                        texta=texta.replace(i,f"(Added a transaction in {konto})")
                label = QLabel("MoneyAI:\n" + texta)
                label.setWordWrap(True)
                label.setStyleSheet("""
                    background:#ffffff;
                    border-radius:10px;
                    padding:8px;
                """)
                
                item = QListWidgetItem(chat)
                item.setSizeHint(label.sizeHint())

                chat.addItem(item)
                chat.setItemWidget(item, label)
                
                eingabe.clear()
                with open("aichat.txt","a",encoding="utf-8") as f:
                    f.write(f"\n User: {text} \nMoneyAI: {texta}\n")
        fenstera = QWidget()
        fenstera.setWindowTitle("MoneyTracker - MoneyAI")
        fenstera.resize(800, 500)
        fenstera.setWindowIcon(QIcon("icon.ico"))

        
        haupt = QHBoxLayout(fenstera)


        




        
        rechts = QVBoxLayout()


        chat = QListWidget()
        chat.setStyleSheet("""
        QListWidget {
            background:#efeae2;
            border:none;
            font-size:16px;
        }
        """)

        rechts.addWidget(chat)


        
                
        

        unten = QHBoxLayout()

        eingabe = QLineEdit()
        eingabe.setPlaceholderText("Send message...")

        button = QPushButton("Send")
        button.clicked.connect(senden)


        unten.addWidget(eingabe)
        unten.addWidget(button)

        rechts.addLayout(unten)


        haupt.addLayout(rechts)


        fenstera.setStyleSheet("""
        QPushButton {
            background:#25D366;
            color:white;
            border-radius:10px;
            padding:8px;
        }

        QLineEdit {
            border:1px solid gray;
            border-radius:10px;
            padding:8px;
        }
        """)

        
    
        fenstera.show()
    def New_A():
        def c():
            name=eingabe.text()
            os.makedirs("Kontos/"+name ,exist_ok=True)

            with open("Kontos/"+name+"/his.txt", "w", encoding="utf-8") as datei:
                datei.write("")
            list_widget.addItem(name)
            dialog.accept()
        dialog = QDialog(window)
        dialog.setWindowTitle("MoneyTracker - Create new Account")

        eingabe = QLineEdit()
        eingabe.setPlaceholderText("Name")
        button = QPushButton("Create")

        button.clicked.connect(c)

        layout = QVBoxLayout()
        layout.addWidget(eingabe)
        layout.addWidget(button)

        dialog.setLayout(layout)

        dialog.exec()
    window.setWindowTitle("MoneyTracker "+version)
    window.setWindowIcon(QIcon("icon.ico"))

    layout = QVBoxLayout()

    ordner_liste = [
        f for f in os.listdir("Kontos") 
        if os.path.isdir(os.path.join("Kontos", f))
    ]

    print(ordner_liste)
    
    label = QLabel("Welcome MoneyAI!!!!")
    label.setStyleSheet("color: green;")

    layout.addWidget(label,alignment=Qt.AlignCenter)
    
    list_widget = QListWidget()
    list_widget.addItems(ordner_liste)

    layout.addWidget(list_widget)


    btn = QPushButton("Open")
    btn.clicked.connect(lambda: Konto(list_widget.currentItem().text()))
    
    btn1 = QPushButton("Create new Account")
    btn1.clicked.connect(New_A)
    
    btn2 = QPushButton("MoneyAI")
    btn2.clicked.connect(AIA)
    
    layout.addWidget(btn)
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    
    window.setLayout(layout)
    window.show()





with open("aichat.txt","w") as f:
    f.write("")
window = QWidget()

Main()

sys.exit(app.exec())
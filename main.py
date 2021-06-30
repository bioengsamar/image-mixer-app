from PyQt5 import QtWidgets
from mixer import Ui_MainWindow 
from  PyQt5.QtWidgets  import QFileDialog,QMessageBox
from PyQt5.QtGui import QPixmap,QImage
import numpy as np
import sys
from imageModel import ImageModel
from modesEnum import Modes
import logging

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mix3=np.array([])
        self.ui.comboBox_3.currentTextChanged.connect(self.mixer)
        self.ui.comboBox_4.currentTextChanged.connect(self.mixer)
        self.ui.comboBox_5.currentTextChanged.connect(self.mixer)
        self.ui.comboBox_6.currentTextChanged.connect(self.mixer)
        self.ui.comboBox_7.currentIndexChanged.connect(self.mixer)
        self.ui.horizontalSlider_2.valueChanged['int'].connect(self.mixer)
        self.ui.horizontalSlider.valueChanged['int'].connect(self.mixer)
        
        
    def load(self):
        global image_1
        self.image1 = QFileDialog.getOpenFileName(self, 'Open file','',' *.jpg *.png')[0]
        image_1 = QPixmap(self.image1)
        self.ui.label.setPixmap(QPixmap(image_1.scaled(250,250)))
        logging.debug('{}'.format(self.image1))
        logging.debug('{}'.format(self.ui.button1))
        
    def load2(self):
        self.image2 = QFileDialog.getOpenFileName(self, 'Open file','',' *.jpg *.png')[0]
        image_2= QPixmap(self.image2)
        self.ui.label_2.setPixmap(QPixmap(image_2.scaled(250,250)))
        logging.debug('{}'.format(self.image2))
        if image_2.size()!= image_1.size():
            QMessageBox.about(self, "Warning!", "not the same size")
        logging.debug('{}'.format(self.ui.button2))
            
    def fourier_image1(self):
        if self.ui.comboBox.currentIndex()==1:
            magnitude=ImageModel(self.image1).magnitude.astype(np.uint8)
            img_mag=QImage(magnitude,magnitude.shape[1],magnitude.shape[0],QImage.Format_Grayscale8)
            self.ui.label_3.setPixmap(QPixmap(img_mag.scaled(250,250)))
        if self.ui.comboBox.currentIndex()==2:
             real=ImageModel(self.image1).real.astype(np.uint8)
             img_real=QImage(real,real.shape[1],real.shape[0],QImage.Format_Grayscale8)
             self.ui.label_3.setPixmap(QPixmap(img_real.scaled(250,250)))
             
        if self.ui.comboBox.currentIndex()==3:
            imaginary=ImageModel(self.image1).imaginary.astype(np.uint8)
            img_imag=QImage(imaginary,imaginary.shape[1],imaginary.shape[0],QImage.Format_Grayscale8)
            self.ui.label_3.setPixmap(QPixmap(img_imag.scaled(250,250)))
            
        if self.ui.comboBox.currentIndex()==4:
            phase=ImageModel(self.image1).phase.astype(np.uint8)
            img_phase=QImage(phase,phase.shape[1],phase.shape[0],QImage.Format_Grayscale8)
            self.ui.label_3.setPixmap(QPixmap(img_phase.scaled(250,250)))
            
        logging.debug('{}'.format(self.ui.comboBox))
            
    def fourier_image2(self):
        if self.ui.comboBox_2.currentIndex()==1:
            magnitude=ImageModel(self.image2).magnitude.astype(np.uint8)
            img_mag_2=QImage(magnitude,magnitude.shape[1],magnitude.shape[0],QImage.Format_Grayscale8)
            self.ui.label_4.setPixmap(QPixmap(img_mag_2.scaled(250,250)))
        if self.ui.comboBox_2.currentIndex()==2:
            real=ImageModel(self.image2).real.astype(np.uint8)
            img_real_2=QImage(real,real.shape[1],real.shape[0],QImage.Format_Grayscale8)
            self.ui.label_4.setPixmap(QPixmap(img_real_2.scaled(250,250)))
            
        if self.ui.comboBox_2.currentIndex()==3:
            imaginary=ImageModel(self.image2).imaginary.astype(np.uint8)
            img_imag_2=QImage(imaginary,imaginary.shape[1],imaginary.shape[0],QImage.Format_Grayscale8)
            self.ui.label_4.setPixmap(QPixmap(img_imag_2.scaled(250,250)))
        
        if self.ui.comboBox_2.currentIndex()==4:
            phase=ImageModel(self.image2).phase.astype(np.uint8)
            img_phase_2=QImage(phase,phase.shape[1],phase.shape[0],QImage.Format_Grayscale8)
            self.ui.label_4.setPixmap(QPixmap(img_phase_2.scaled(250,250)))
        logging.debug('{}'.format(self.ui.comboBox_2))
        
       
    def mixer(self):
       value1=self.ui.horizontalSlider.value()
       if self.ui.comboBox_3.currentText()=='output 1' :
           if self.ui.comboBox_4.currentText()=='image 1' or 'image 2':
                if self.ui.comboBox_6.currentText()=='real':
                   self.ui.comboBox_7.view().setRowHidden(0,True)
                   self.ui.comboBox_7.view().setRowHidden(1,False)
                   self.ui.comboBox_7.view().setRowHidden(2,True)
                   self.ui.comboBox_7.view().setRowHidden(3,True)
                if self.ui.comboBox_6.currentText()=='imaginary':
                   self.ui.comboBox_7.view().setRowHidden(0,False)
                   self.ui.comboBox_7.view().setRowHidden(1,True)
                   self.ui.comboBox_7.view().setRowHidden(2,True)
                   self.ui.comboBox_7.view().setRowHidden(3,True)
                if self.ui.comboBox_6.currentText()=='magnitude':
                   self.ui.comboBox_7.view().setRowHidden(0,True)
                   self.ui.comboBox_7.view().setRowHidden(1,True)
                   self.ui.comboBox_7.view().setRowHidden(2,True)
                   self.ui.comboBox_7.view().setRowHidden(3,False)
                if self.ui.comboBox_6.currentText()=='phase':
                   self.ui.comboBox_7.view().setRowHidden(0,True)
                   self.ui.comboBox_7.view().setRowHidden(1,True)
                   self.ui.comboBox_7.view().setRowHidden(2,False)
                   self.ui.comboBox_7.view().setRowHidden(3,True)
                    
                if self.ui.comboBox_5.currentText()=='image 2':
                    if self.ui.comboBox_7.currentText()=='imaginary':
                        if self.ui.comboBox_4.currentText()=='image 1':
                            self.ui.horizontalSlider_2.setValue(100-value1)
                            mix=ImageModel(self.image1).mix(ImageModel(self.image2),value1/100,Modes.realAndImaginary).astype(np.uint8)
                        else:
                            self.ui.horizontalSlider_2.setValue(100-value1)
                            mix=ImageModel(self.image2).mix(ImageModel(self.image2),value1/100,Modes.realAndImaginary).astype(np.uint8)
                    if self.ui.comboBox_7.currentIndex()==0: #real part
                        if self.ui.comboBox_4.currentText()=='image 1':
                            self.ui.horizontalSlider_2.setValue(100-value1)
                            mix=ImageModel(self.image2).mix(ImageModel(self.image1),value1/100,Modes.realAndImaginary).astype(np.uint8)
                        else:
                            self.ui.horizontalSlider_2.setValue(100-value1)
                            mix=ImageModel(self.image2).mix(ImageModel(self.image2),value1/100,Modes.realAndImaginary).astype(np.uint8)
                    if self.ui.comboBox_7.currentText()=='phase':
                        if self.ui.comboBox_4.currentText()=='image 1':
                            self.ui.horizontalSlider_2.setValue(100-value1)
                            mix=ImageModel(self.image1).mix(ImageModel(self.image2),value1/100,Modes.magnitudeAndPhase).astype(np.uint8)
                        else:
                            self.ui.horizontalSlider_2.setValue(100-value1)
                            mix=ImageModel(self.image2).mix(ImageModel(self.image2),value1/100,Modes.magnitudeAndPhase).astype(np.uint8)
                    if self.ui.comboBox_7.currentText()=='magnitude':
                        if self.ui.comboBox_4.currentText()=='image 1':
                            self.ui.horizontalSlider_2.setValue(100-value1)
                            mix=ImageModel(self.image2).mix(ImageModel(self.image1),value1/100,Modes.magnitudeAndPhase).astype(np.uint8)
                        else:
                            self.ui.horizontalSlider_2.setValue(100-value1)
                            mix=ImageModel(self.image2).mix(ImageModel(self.image2),value1/100,Modes.magnitudeAndPhase).astype(np.uint8)
                    mix=QImage(mix,mix.shape[1],mix.shape[0],QImage.Format_Grayscale8)
                    self.ui.label_8.setPixmap(QPixmap(mix.scaled(350,350)))
                        
                else:
                    if self.ui.comboBox_7.currentText()=='imaginary':
                        self.ui.horizontalSlider_2.setValue(100-value1)
                        mix=ImageModel(self.image1).mix(ImageModel(self.image1),value1/100,Modes.realAndImaginary).astype(np.uint8)
                        mix=QImage(mix,mix.shape[1],mix.shape[0],QImage.Format_Grayscale8)
                        self.ui.label_8.setPixmap(QPixmap(mix.scaled(350,350)))
                    if self.ui.comboBox_7.currentIndex()==0: #real part
                        self.ui.horizontalSlider_2.setValue(100-value1)
                        mix=ImageModel(self.image1).mix(ImageModel(self.image1),value1/100,Modes.realAndImaginary).astype(np.uint8)
                        mix=QImage(mix,mix.shape[1],mix.shape[0],QImage.Format_Grayscale8)
                        self.ui.label_8.setPixmap(QPixmap(mix.scaled(350,350)))
                    if self.ui.comboBox_7.currentText()=='phase': 
                        self.ui.horizontalSlider_2.setValue(100-value1)
                        mix=ImageModel(self.image1).mix(ImageModel(self.image1),value1/100,Modes.magnitudeAndPhase).astype(np.uint8).astype(np.uint8)
                        mix=QImage(mix,mix.shape[1],mix.shape[0],QImage.Format_Grayscale8)
                        self.ui.label_8.setPixmap(QPixmap(mix.scaled(350,350)))
                    if self.ui.comboBox_7.currentText()=='magnitude': 
                        self.ui.horizontalSlider_2.setValue(100-value1)
                        mix=ImageModel(self.image1).mix(ImageModel(self.image1),value1/100,Modes.magnitudeAndPhase).astype(np.uint8)
                        mix=QImage(mix,mix.shape[1],mix.shape[0],QImage.Format_Grayscale8)
                        self.ui.label_8.setPixmap(QPixmap(mix.scaled(350,350)))
                    
       else: 
            if self.ui.comboBox_4.currentText()=='image 1' or 'image 2' :
                if self.ui.comboBox_6.currentText()=='real':
                   self.ui.comboBox_7.view().setRowHidden(0,True)
                   self.ui.comboBox_7.view().setRowHidden(1,False)
                   self.ui.comboBox_7.view().setRowHidden(2,True)
                   self.ui.comboBox_7.view().setRowHidden(3,True)
                if self.ui.comboBox_6.currentText()=='imaginary':
                   self.ui.comboBox_7.view().setRowHidden(0,False)
                   self.ui.comboBox_7.view().setRowHidden(1,True)
                   self.ui.comboBox_7.view().setRowHidden(2,True)
                   self.ui.comboBox_7.view().setRowHidden(3,True)
                if self.ui.comboBox_6.currentText()=='magnitude':
                   self.ui.comboBox_7.view().setRowHidden(0,True)
                   self.ui.comboBox_7.view().setRowHidden(1,True)
                   self.ui.comboBox_7.view().setRowHidden(2,True)
                   self.ui.comboBox_7.view().setRowHidden(3,False)
                if self.ui.comboBox_6.currentText()=='phase':
                   self.ui.comboBox_7.view().setRowHidden(0,True)
                   self.ui.comboBox_7.view().setRowHidden(1,True)
                   self.ui.comboBox_7.view().setRowHidden(2,False)
                   self.ui.comboBox_7.view().setRowHidden(3,True)
                  
                if self.ui.comboBox_5.currentText()=='image 2' :
                    if self.ui.comboBox_7.currentText()=='imaginary':
                       if self.ui.comboBox_4.currentText()=='image 1':
                           self.ui.horizontalSlider_2.setValue(100-value1)
                           mix=ImageModel(self.image1).mix(ImageModel(self.image2),value1/100,Modes.realAndImaginary).astype(np.uint8)
                       else:
                           self.ui.horizontalSlider_2.setValue(100-value1)
                           mix=ImageModel(self.image2).mix(ImageModel(self.image2),value1/100,Modes.realAndImaginary).astype(np.uint8)
                    if self.ui.comboBox_7.currentIndex()==0: #real part
                       if self.ui.comboBox_4.currentText()=='image 1':
                           self.ui.horizontalSlider_2.setValue(100-value1)
                           mix=ImageModel(self.image2).mix(ImageModel(self.image1),value1/100,Modes.realAndImaginary).astype(np.uint8)
                       else:
                           self.ui.horizontalSlider_2.setValue(100-value1)
                           mix=ImageModel(self.image2).mix(ImageModel(self.image2),value1/100,Modes.realAndImaginary).astype(np.uint8)
                    if self.ui.comboBox_7.currentText()=='phase': 
                        if self.ui.comboBox_4.currentText()=='image 1':
                            self.ui.horizontalSlider_2.setValue(100-value1)
                            mix=ImageModel(self.image1).mix(ImageModel(self.image2),value1/100,Modes.magnitudeAndPhase).astype(np.uint8)
                        else:
                            self.ui.horizontalSlider_2.setValue(100-value1)
                            mix=ImageModel(self.image2).mix(ImageModel(self.image2),value1/100,Modes.magnitudeAndPhase).astype(np.uint8)
                    if self.ui.comboBox_7.currentText()=='magnitude':
                        if self.ui.comboBox_4.currentText()=='image 1':
                            self.ui.horizontalSlider_2.setValue(100-value1)
                            mix=ImageModel(self.image2).mix(ImageModel(self.image1),value1/100,Modes.magnitudeAndPhase).astype(np.uint8)
                        else:
                            self.ui.horizontalSlider_2.setValue(100-value1)
                            mix=ImageModel(self.image2).mix(ImageModel(self.image2),value1/100,Modes.magnitudeAndPhase).astype(np.uint8)
                        
                    mix=QImage(mix,mix.shape[1],mix.shape[0],QImage.Format_Grayscale8)
                    self.ui.label_9.setPixmap(QPixmap(mix.scaled(350,350)))
                    
                else:
                    if self.ui.comboBox_7.currentText()=='imaginary':
                        self.ui.horizontalSlider_2.setValue(100-value1)
                        mix=ImageModel(self.image1).mix(ImageModel(self.image1),value1/100,Modes.realAndImaginary).astype(np.uint8)
                        mix=QImage(mix,mix.shape[1],mix.shape[0],QImage.Format_Grayscale8)
                        self.ui.label_9.setPixmap(QPixmap(mix.scaled(350,350)))
                    if self.ui.comboBox_7.currentIndex()==0: #real part
                        self.ui.horizontalSlider_2.setValue(100-value1)
                        mix=ImageModel(self.image1).mix(ImageModel(self.image1),value1/100,Modes.realAndImaginary).astype(np.uint8)
                        mix=QImage(mix,mix.shape[1],mix.shape[0],QImage.Format_Grayscale8)
                        self.ui.label_9.setPixmap(QPixmap(mix.scaled(350,350)))
                    if self.ui.comboBox_7.currentText()=='phase': 
                        self.ui.horizontalSlider_2.setValue(100-value1)
                        mix=ImageModel(self.image1).mix(ImageModel(self.image1),value1/100,Modes.magnitudeAndPhase).astype(np.uint8).astype(np.uint8)
                        mix=QImage(mix,mix.shape[1],mix.shape[0],QImage.Format_Grayscale8)
                        self.ui.label_9.setPixmap(QPixmap(mix.scaled(350,350)))
                    if self.ui.comboBox_7.currentText()=='magnitude': 
                        self.ui.horizontalSlider_2.setValue(100-value1)
                        mix=ImageModel(self.image1).mix(ImageModel(self.image1),value1/100,Modes.magnitudeAndPhase).astype(np.uint8)
                        mix=QImage(mix,mix.shape[1],mix.shape[0],QImage.Format_Grayscale8)
                        self.ui.label_9.setPixmap(QPixmap(mix.scaled(350,350)))
                        
    def reset(self):
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider_2.setValue(0)
        self.ui.comboBox_3.setCurrentIndex(0)
        self.ui.comboBox_4.setCurrentIndex(0)
        self.ui.comboBox_5.setCurrentIndex(0)
        self.ui.comboBox_6.setCurrentIndex(0)
        self.ui.comboBox_7.setCurrentIndex(0)
        self.ui.label_8.clear()
        self.ui.label_9.clear()
        logging.debug('{}'.format(self.ui.pushButton))

def main():
    logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
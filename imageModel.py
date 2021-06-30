from modesEnum import Modes
import numpy as np
import cv2
class ImageModel():


    def __init__(self, imgPath:str):
       
        self.imgByte =cv2.imread(imgPath,0)
        self.dft = np.fft.fft2(self.imgByte)
        self.real =np.real(self.dft)
        self.imaginary =np.imag(self.dft)
        self.magnitude =np.abs(self.dft)
        self.phase =np.angle(self.dft)
        
        
        
    
    def mix(self, imageToBeMixed: 'ImageModel', magnitudeOrRealRatio: float, mode: 'Modes') -> np.ndarray:
        """
        a function that takes ImageModel object mag ratio, phase ration and
        return the magnitude of ifft of the mix
        return type ---> 2D numpy array
        please Add whatever functions realted to the image data in this file
        """
        if mode==Modes.magnitudeAndPhase:
            mix=np.multiply(magnitudeOrRealRatio*self.magnitude,(1-magnitudeOrRealRatio)*np.exp(1j*imageToBeMixed.phase))
            mix=np.real(np.fft.ifft2(mix))
            self.mix=np.abs(mix)
            return self.mix
    
        if mode==Modes.realAndImaginary:
            a=magnitudeOrRealRatio*self.real
            b=(1-magnitudeOrRealRatio)*imageToBeMixed.imaginary
            mix=a+b*1j
            mix=np.fft.ifft2(mix)
            self.mix=np.abs(mix)
            return self.mix
        
   
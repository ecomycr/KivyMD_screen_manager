# -*- coding: utf-8 -*-

import kivy
import os

#grafics
from kivy.config import Config
Config.set("graphics","width","340")
Config.set("graphics","hight","640")

#mods
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.uix.button import MDFillRoundFlatIconButton

from kivymd.uix.button import MDRectangleFlatIconButton


from kivy.uix.screenmanager import ScreenManager, Screen
		
class Madre(ScreenManager):
    def __init__(self,**kwargs):
        super(Madre,self).__init__()
        
        self.ScreenUno = ScreenUno(self)
        self.ScreenDos = ScreenDos(self)
        self.ScreenTres = ScreenTres(self)
        
        self.Menu = Menu(self)
        
        
        wid= Screen (name='menu')
        wid.add_widget(self.Menu)
        self.add_widget(wid)
        
        wid = Screen (name = 'uno')
        wid.add_widget(self.ScreenUno)
        self.add_widget(wid)
        
        wid = Screen (name = 'dos')
        wid.add_widget(self.ScreenDos)
        self.add_widget(wid)
        
        wid = Screen (name = 'tres')
        wid.add_widget(self.ScreenTres)
        self.add_widget(wid)
        
        
        self.go_menu()
        
    def go_screenUno(self):
    	self.current = 'uno'
    
    def go_screenDos(self):
    	self.current = 'dos'
    
    def go_screenTres(self):
    	self.current = 'tres'
    
    def go_menu(self):
    	self.current= 'menu'
	


class ScreenUno(BoxLayout):
	def __init__(self, madre,**kwargs):
		super(ScreenUno, self).__init__()
		self.madre = madre
	
	def go_menu(self):
		self.madre.go_menu()

class ScreenDos(BoxLayout):
	def __init__(self,madre,**kwargs):
		super(ScreenDos,self).__init__()
		self.madre = madre
	
	def go_menu(self):
		self.madre.go_menu()
		
class ScreenTres(BoxLayout):
	def __init__(self,madre, **kwargs):
		super(ScreenTres,self).__init__()
		self.madre = madre
	
	def go_menu(self):
		self.madre.go_menu()
		

class Menu(BoxLayout):
	def __init__(self, madre, **kwargs):
		super(Menu,self).__init__()
		self.madre = madre
	
	def go_sc1(self):
		self.madre.go_screenUno()
	
	def go_sc2(self):
		self.madre.go_screenDos()
	
	def go_sc3(self):
		self.madre.go_screenTres()



class MainApp(MDApp):
    def build(self):
        return Madre()
        
if __name__ == '__main__':
    MainApp().run()

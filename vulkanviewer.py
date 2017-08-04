import tkinter as tk
import itertools
from tkinter import ttk 
from tkinter import scrolledtext
import subprocess
import os

def Vulkan(tab2):

	
	# Creating Tabs for different Features

	#Creating Feature Tab
	os.system("vulkaninfo > vulkaninfo.txt")

	tabcontrol = ttk.Notebook(tab2, padding=10)
	FeatureTab = ttk.Frame(tabcontrol)
	tabcontrol.add(FeatureTab, text="Features")
	tabcontrol.grid(column=0,row=1)

 	#Creating Extensions Tab

	LimitsTab = ttk.Frame(tabcontrol)
	tabcontrol.add(LimitsTab,text = "Limits")
	tabcontrol.grid(column=0,row=1)

	ExtensionsTab = ttk.Frame(tabcontrol)
	tabcontrol.add(ExtensionsTab,text = "Extensions")
	tabcontrol.grid(column=0,row=1)

	def Features(i,j):

		frame2 = ttk.LabelFrame(FeatureTab, text="Device Features")
		frame2.grid(column=0,row=1)

		FS = scrolledtext.ScrolledText(frame2, width=100,height=30,bg="LIGHT GRAY")
		FS.grid(column=0,row=1)

		os.system("cat vulkaninfo.txt | awk '/VkPhysicalDeviceFeatures:/{flag=1; next}/Format Properties:/{flag=0} flag' | sort | awk '/==/{flag=1; next} flag' > Features.txt")

		with open("Features.txt","r") as file1:
			for line in itertools.islice(file1,i,None,j):
				FS.insert('insert',line)

		FS.configure(foreground="BLUE")	
	radvar = tk.IntVar()

	def Limits():
		
		frame3 = ttk.LabelFrame(LimitsTab, text="Device Limits")
		frame3.grid(column=0,row=0)


		DL = scrolledtext.ScrolledText(frame3,width=100,height=30,bg="LIGHT GRAY")
		DL.grid(column=0,row=1)
		GPU = radvar.get()
		if GPU == 0 :
			os.system("cat vulkaninfo.txt | awk '/GPU0/{flag=1;next}/VkPhysicalDeviceSparseProperties:/{flag=0}flag'| awk '/--/{flag=1 ; next} flag' | sort > VKDlimits.txt")
		elif GPU == 1 :
			os.system("cat vulkaninfo.txt | awk '/GPU1/{flag=1;next}/VkPhysicalDeviceSparseProperties:/{flag=0}flag'| awk '/--/{flag=1 ; next} flag' | sort > VKDlimits.txt")

		with open("VKDlimits.txt","r") as file1:
			for line in file1:
				DL.insert('insert',line)

		DL.configure(foreground="BLUE")		

	def Extensions():
		frame4 = ttk.LabelFrame(ExtensionsTab, text="Device Extension ")
		frame4.grid(column=0,row=0)


		ES = scrolledtext.ScrolledText(frame4,width=100,height=30,bg="LIGHT GRAY")
		ES.grid(column=0,row=1)
		GPU = radvar.get()
		if GPU == 0 :
			os.system("cat vulkaninfo.txt | awk '/GPU0/{flag=1;next}/VkQueueFamilyProperties/{flag=0}flag'|awk '/Device Extensions/{flag=1; next}/VkQueueFamilyProperties/{flag=0} flag' | grep VK_ | sort > VKDExtensions.txt")
		elif GPU == 1 :
			os.system("cat vulkaninfo.txt | awk '/GPU1/{flag=1;next}/VkQueueFamilyProperties/{flag=0}flag'|awk '/Device Extensions/{flag=1; next}/VkQueueFamilyProperties/{flag=0} flag'| grep VK_ |sort > VKDExtensions.txt")

		with open("VKDExtensions.txt","r") as file1:
			count = len(file1.readlines())
			frame4.configure(text = count)
			file1.seek(0,0)
			for line in file1:
				ES.insert('insert',line)

		ES.configure(foreground="BLUE")

	def radcall():
		radsel= radvar.get()
		print(radsel)
		if radsel == 0:
			Features(1,2)
			Limits()
			Extensions()
		if radsel == 1:
			Features(0,2)
			Limits()
			Extensions()
		if radsel == 5:
			Features(0,1)
			Limits()
			Extensions()




	frame1 = ttk.LabelFrame(tab2,text="")
	frame1.grid(column=0,row=0)
	os.system("cat vulkaninfo.txt | grep '^GPU id' | grep GPU > GPU.txt")

	with open("GPU.txt","r") as file2:
		count=len(file2.readlines())
		list = []
		file2.seek(0,0)
		for line in file2:
			list.append(line)

	DS = ttk.Label(frame1, text="Select Device :")
	DS.grid(column=0,row=0, padx=100, pady=10)
	if len(list) > 1:
		for i in range(len(list)):
			GPU = tk.Radiobutton(frame1,text=list[i], variable=radvar,value=i,command=radcall)
			GPU.grid(column=1,row=i,sticky=tk.W)
			if i == 0:
				GPU.invoke()
	else:
		GPU = tk.Radiobutton(frame1,text=list[0], variable=radvar,value=5,command=radcall)
		GPU.grid(column=1,row=0,sticky=tk.W)
		GPU.invoke()
	



	


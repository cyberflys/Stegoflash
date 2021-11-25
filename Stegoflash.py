"""	
	Stegoflash v1.0a
		stego tool used to hide messages in .jpeg, .png , .mp3 ...

			by suibex
				24. Nov. 21.

		All rights reserved.
"""
"""
	Patch Notes:

		Version 1.0a:
			By suibex

		-Built main function
		-Added full support for PNG,JPEG.
		-Half working: mp3, mp4 ....
		-didn't fix pycrypto error(need to add encryption and decryption)

"""

import os,sys,io
#from Crypto.Cipher import AES
import base64

class Stegoflash():

	def __init__(self):
		"""
			User Guidance:
					-h  (HIDE)
					-r (READ)
					-e (extract)
					-en (encrypt)
					-de (decrypt)

		"""
		
		if len(sys.argv) > 1:
			if sys.argv[1] == "-h":
				self.hide(sys.argv[2],sys.argv[3])

			if sys.argv[1] == "-r":
				data = self.read(sys.argv[2])
				print(data)
			if sys.argv[1] == "-e":
				self.extract(sys.argv[2],sys.argv[3])
			if sys.argv == "-en":
				self.encrypt(sys.argv[2],sys.argv[3],sys.argv[4])
			if sys.argv == "-en":
				self.decrypt(sys.argv[2],sys.argv[3])

		else:
			print("""
************** HELP **************
List of commands available to use: 

🔵 -h  {filename} { text or file} - specify when hiding text/ file data into file.
🔵 -r  {filename} - read embedded data (NOT ACTUAL IMAGE DATA!)
🔵 -e {filename} {name of file where to save data} - use when extracting data from image to another file
🔵 -en {filename} {key} - used to encrypt secret data in file , and make it more secure. ( NEED TO SPECIFY A 🔑)
🔵 -de {filename} {key} - used to decrypt secret data in file , and output it to the screen.
				
	have a nice day,	
		suibex. 💎

***** END OF HELP SECTION *****
""")
		exit(1)

	def hide(self,file,data):

		if "." in data:
			print("***RULE CHANGED***\nFile specified instead of data.")
			o = open(data,"rb")
			da = o.read()
			

			with open(file,"ab") as f:
				f.write(da)
				
			print("Message hidden. 🔒")
		else:
			with open(file,"ab") as f:
				f.write(data.encode())
				
			print("Message hidden. 🔒")


	def read(self,file):
	
		
		if ".jpg" or ".jpeg" or ".JPG" or ".JPEG" in file:
			with open(file,"rb") as f:
				content = f.read()
				offset = content.index(bytes.fromhex("FFD9"))
				f.seek(offset + 2)
				return f.read()

		elif ".png" or ".PNG" in file:
			with open(file,"rb") as f:
				content = f.read()
				offset = content.index(bytes.fromhex("6082"))
				f.seek(offset +2 )
				
				return f.read()

			
		else:
			
			with open(file,"rb") as f:
				f.seek(0,2)
				return f.read()

	def extract(self,file,extension):
		
		filedata = self.read(file)	

		o1 = open(extension,"wb")
		o1.write(filedata)
		o1.close()
		print("Extraction completed... 🔓 ")
		
		
		
	"""
	def encrypt(self,file,key):
		print("Encrypting...")
		print("Decrypting...")
		
		if ".jpg " or ".jpeg " or ".JPG" or ".JPEG"  in file:
			da = open(file,"rb")
			f = da.read()
			offset = f.index(bytes.fromhex("FFD9"))
			da.seek(offset+2 )
			cont = da.read()

			key = self._pad(key)
			data = self._pad(cont)
			cipher = AES.new(key,AES.MODE_ECB)
			text = base64.b64encode(data)
			dec = cipher.encrypt(text)
			print(f"Encrypted data: \n{ dec} ")

			
			
		if ".png " or ".PNG " in file:
			da = open(file,"rb")
			f = da.read()
			offset = f.index(bytes.fromhex("6082"))
			da.seek(offset+2)
			cont = da.read()

			key = self._pad(key)
			data = self._pad(cont)
			cipher = AES.new(key,AES.MODE_ECB)
			text = base64.b64encode(data)
			dec = cipher.encrypt(text)
			print(f"Encrypted data: \n{ dec} ")

	

	def decrypt(self,file,key1):
		print("Decrypting...")

		if ".jpg " or ".jpeg " or ".JPG" or ".JPEG"  in file:
			da = open(file,"rb")
			f = da.read()
			offset = f.index(bytes.fromhex("FFD9"))
			da.seek(offset+2)
			cont = da.read()

			key = self._pad(key1)
			data = self._pad(cont)
			cipher = AES.new(key,AES.MODE_ECB)
			text = base64.b64decode(data)
			dec = cipher.decrypt(text)
			datasave = str(self._unpad(dec),'utf-8')

			o  = open(file,"wb")
			o.write(datasave)
			o.close()
			print("Files written.")
		if ".png " or ".PNG " in file:
			da = open(file,"rb")
			f = da.read()
			offset = f.index(bytes.fromhex("6082"))
			da.seek(offset+2)
			cont = da.read()

			key = self._pad(key1)
			data =self. _pad()
			cipher = AES.new(key,AES.MODE_ECB)
			text = base64.b64decode(data)
			dec = cipher.decrypt(text)
			datasave = str(self._unpad(dec),'utf-8')

			o  = open(file,"wb")
			o.write(datasave)
			o.close()
			print("Files written.")
	def _unpad(self,s):
		return s[:-ord(s[len(s)-1:])]
	def _pad(self,s):
		return s + (16 - len(s) % 16) * chr(16 - len(s) %16)

	"""


stegoflash = Stegoflash()
stegoflash.__init__()
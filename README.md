# Stegoflash🔑
Stegoflash is a tool for hiding messages,files.. etc in JPEG and PNG files!
<br>Our goal is to make stegonography fun.</br>
<br>Tool is based on Python3.</br>
<br>Now on more important stuff.😁</br>

<h2>How to setup it? </h2>

	
	Just install Python3,and no fuss!🦾
	After that install pycrypto with: 
	pip3 install pycrypto

<h2>How to do i stego my stuff?? </h2>
<h3>Easy.</h3>
    
    Run with: python3 Stegoflash.py {and then commands specified below}
    
    
    🔵 -h  {filename} { text or file} - specify when hiding text/ file data into file,
  
    🔵 -r  {filename} - read embedded data (NOT ACTUAL IMAGE DATA!)
     
    🔵 -e {filename} {name of file where to save data} - use when extracting data from image to another file
    
    🔵 -en {filename} {key} - used to encrypt secret data in file , and make it more secure. ( NEED TO SPECIFY A 🔑) ( STILL IN REALLY BETA PHASE)
      
    🔵 -de {filename} {key} - used to decrypt secret data in file , and output it to the screen. ( STILL IN REALLY BETA PHASE)
    
    
    
<h2>Example:</h2>


![ad](https://user-images.githubusercontent.com/62068607/143486369-f8daaa10-8f4d-44c6-9bf8-e046d7156047.png)





<h2>Changelog:</h2>


<h3>Version 1.0a</h3>
	
	
		Built main function
		Added full support for PNG,JPEG.
		didn't fix pycrypto error(need to add encryption and decryption)
   
    

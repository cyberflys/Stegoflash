# Stegoflash
Stegoflash is a tool for hiding messages,files.. etc in JPEG and PNG files!
<br>Our goal is to make stegonography fun.</br>
<br>Tool is based on Python3. </br>
<br>Now on more important stuff.</br>

<h2>How to do i stego my stuff?? </h2>
<h3>Easy.</h3>
    
    🔵 -h  {filename} { text or file} - specify when hiding text/ file data into file,
  
    🔵 -r  {filename} - read embedded data (NOT ACTUAL IMAGE DATA!)
     
    🔵 -e {filename} {name of file where to save data} - use when extracting data from image to another file
    
    🔵 -en {filename} {key} - used to encrypt secret data in file , and make it more secure. ( NEED TO SPECIFY A 🔑)
      
    🔵 -de {filename} {key} - used to decrypt secret data in file , and output it to the screen.
    
    
    
<h2>Example:</h2>
![1231](https://user-images.githubusercontent.com/62068607/143486215-54b9564b-db5a-434e-936e-2af264d50f99.png)


<h2>Patch Notes:</h2>


<h3>Version 1.0a</h3>
	

		Built main function
		Added full support for PNG,JPEG.
		Half working: mp3, mp4 ....
		didn't fix pycrypto error(need to add encryption and decryption)
   
    

# Function to rename multiple files 
import os 
  
PATH = "C:\Users\HP EliteBook 8470p\Documents\Coding\AmiArt.com\resized-logos"
def main(): 
    i = 0
      
    for filename in os.listdir(PATH): 
        dst ="logo" + str(i) + ".jpeg"
        src = PATH + filename 
        dst = PATH + dst 
          
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
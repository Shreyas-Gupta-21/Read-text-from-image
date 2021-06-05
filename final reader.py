# read text from image
from PIL import Image
import pytesseract
image = Image.open('med1.jpeg')
pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"
txt = pytesseract.image_to_string(image)
print(txt)

Med = { 'Crocin' : ['Algina', 'Cipmol','Dolo','Paracip', 'Febrex'] ,
 'Remdesivir' : ['Dexamethasone','FabiFlu '],
'Ecospirin' : ['Sprin', 'Aspidot','CV sprin'] ,
'Cetzine' : ['Sizon', 'Cetriver','Okacet'] ,
'Zincovit' : ['Zinconia', 'New Celin','A to Z NS'] ,
'Demisone' : ['Dexona', 'Decdan','Wymesone'] ,
'Wincold' : ['Flu-4-XN', 'Saczine-Cold','Fluban', 'Helcet plus' ] ,
'Aciloc' : ['Zinemac', 'Ranitas','Rafilon', 'Zynol'] ,
'Omez Capsule' : ['Omesec 20', 'Omecip Capsule','Promisec'],
'Razo 20' : ['Cyra', 'Rabid','Pepcia 20', 'Raboni'],
'Brufen' : ['IBUFLAMAR', 'Bruriff','ALFAM', 'Maxofen'],
'Azithromycin' : ['Zithrozem', 'Zady','Azax'],
'Betnesol' : ['Cortil', 'Betaken','Betapen', 'Cortibet'],
'Ciprobid' : ['Ciprokind', 'Alciflox','Ceepro', 'Ciplox'],
'Catef O' : ['Cefaxime O', 'Neeflox O','Surgicef O', 'Pelflix O'],
}

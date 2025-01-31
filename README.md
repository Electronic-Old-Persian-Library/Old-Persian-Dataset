# Raw dataset for Old Persian cuneiform


Dear contributors, please be aware that cuneiform are different. For instance, the most popular are Elamite, Babylonian and Old Persian; we are working on Old Persian in this project. Below you can see the differences:

![types of cuneiform](https://github.com/Electronic-Old-Persian-Library/Old-Persian-Dataset/assets/74653444/2e84ae6b-f3fa-40c0-aa71-a3a125c0f040)

(Photo is taken from national museum of Iran, the gold plate of king Darius, DPh)

## Data structure:

/imagedata/

     /source/
            /king/
               source_king_001.jpg
            
      #example:
      
      /behistun/
           /darius_1/
               behistun_darius_1_001.jpg
          
/textdata/
            
      
      /eng_transcription_to_english/
           /metadata/
           eng_transcription_to_english_001.json
           
      /eng_transliteration_to_english/
           /metadata/
           eng_transliteration_to_english_001.json
           
      /single/
          /metadata/
          /eng_transliteration/
                eng_transliteration_001.json

                  
       # "single" refers to text data that are just a text without translation 
      
Translating Old Persian language has some methods, for example, transliteration and transcription. Below you can see an example to know the difference between them:

![transliteration_transcription](https://github.com/Electronic-Persian-Old-Library/Persian-Old-Dataset/assets/74653444/a0a1692e-6740-46ac-8167-e9acb7324fec)


            
## Metadata 

For each directory a "source.metadata.csv" file is provided to see the information of data. 

Explanation about metadata columns:

imagedata:

source: The source that I have taken data from.

abbreviation: The name of inscription 

location: The main discovered location of that inscription.

translation: 1: if I have the translation of that inscription, 0: if I have not.

collection: The palace of storing that inscription at this current time.

artifact_id : artifact_id from CDLI reference 

asset_number: asset_number from british museum collection

museum_number: museum_number from british museum collection

--------------------------------------

textdata: 

abbreviation: The name of inscription 

reference: The reference that I have taken data from.

location: The main discovered location of that inscription 

image: 1: if I have the image of that inscription, 0: if I have not.

artifact_id : artifact_id from CDLI reference 

## References

- [Livius.org](https://www.livius.org/sources/content/achaemenid-royal-inscriptions/)


- [British Museum collection](https://www.britishmuseum.org/collection/)


- [Wikipedia](https://en.wikipedia.org/wiki/Achaemenid_royal_inscriptions)
  

- [Cuneiform Digital Library Initiative (CDLI)](https://cdli.mpiwg-berlin.mpg.de/)



- [Book: The Inscriptions in Old Persian Cuneiform of the Achaemenian Emperors by
Ralph Norman Sharp](https://drive.google.com/file/d/1iqo0i3cyfN_DNho3xIwp1S4BAvdB70CQ/view?usp=sharing)


- Personal photography from national museum of Iran and Takht-e-Jamshid (Persepolis)




## Glossary



Behistun:بیستون

Susa:شوش

Persepolis:پرسپولیس(تخت جمشید)

Elamite:ایلامی

Babylonian:بابِلی

Cyrus:کوروش

Xerxes:خشایار

Artaxerxes:اردشیر

𐎠𐎢𐎼𐎶𐏀𐎡𐎠:اهورامزدا

## LICENSE
This repository is under [CC-BY-NC](https://github.com/Electronic-Old-Persian-Library/Old-Persian-Dataset/blob/main/LICENSE-CC-BY-NC) license and any commercial use is prohibited.



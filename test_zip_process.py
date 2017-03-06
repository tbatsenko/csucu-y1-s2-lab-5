from zip_processor import ZipProcessor
from zip_replace import ZipReplace
from scale_zip import ScaleZip

print("Enter the word, which will be replaced:")
word_to_replace = input()
print("Enter the word, which will replace the word you entered:")
word_to_replace_with = input()
zipreplace = ZipReplace(word_to_replace, word_to_replace_with)
print("Enter the full name of zip (with .zip in the end):")
zip_name = input()
ZipProcessor(zip_name, zipreplace).process_zip()

zipscale = ScaleZip()
ZipProcessor("test_img.zip", zipscale).process_zip()

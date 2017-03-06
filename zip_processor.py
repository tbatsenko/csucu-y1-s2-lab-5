import os
import shutil
import zipfile


class ZipProcessor:
    def __init__(self, zipname, processor):
        """
        called when initing a new instance of ZipProcessor class
        creates attributes zipname, temp_directory and processor
        """
        self.zipname = zipname
        self.temp_directory = "unzipped-{}".format(zipname[:-4])
        self.processor = processor

    def _full_filename(self, filename):
        """
        returns full path to the file
        """
        return os.path.join(self.temp_directory, filename)

    def process_zip(self):
        """
        unzips the given zip, calls processor's method process and zips
        processed files back
        """
        self.unzip_files()
        self.processor.process(self)
        self.zip_files()

    def unzip_files(self):
        """
        unzips files of given zip called 'zipname'
        """
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()

    def zip_files(self):
        """
        zips files of given zip called 'zipname'
        """
        file = zipfile.ZipFile(self.zipname, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
            shutil.rmtree(self.temp_directory)

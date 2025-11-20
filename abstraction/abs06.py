from abc import ABC,abstractmethod

class Storage:
    @abstractmethod
    def save(self,file):
        pass
    @abstractmethod
    def load(self,filename):
        pass

class LocalStorage(Storage):
    def save(self,file):
        print(f"{file} is Saved in LocalStorage")
    def load(self,filename):
        print(f"{filename} is loading in LocalStorage ")
class S3Storage(Storage):
    def save(self,file):
        print(f"{file} is Saved in S3Storage")
    def load(self,filename):
        print(f"{filename} is loading in S3Storage ")
class GoogleCloudStorage(Storage):
    def save(self,file):
        print(f"{file} is Saved in GoogleCloudStorage")
    def load(self,filename):
        print(f"{filename} is loading in GoogleCloudStorage")

def check(s:Storage,file):
    s.save(file)
    s.load(file)

g=GoogleCloudStorage()
check(g,"photo.jpg")
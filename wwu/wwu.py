import requests, urllib.request, os
from sys import platform

if platform == "linux" or platform == "linux2": op = "linux"
elif platform == "win32": op = "win"
elif platform == "darwin": op = "mac"

class client():
    def __init__(self, base_folder, version_url, current_version, *files):
        self.files = []
        for file in files: self.files.append(file)
        self.current_version = current_version
        self.version = requests.get(version_url).text
        self.base_folder = base_folder
        
    def check(self):
        if self.current_version == self.version: return False
        else: return True
            
    def download(self, folder=None, log=True, launch_after=None):
        if folder is None: pass
        else: 
            folder2 = folder.split("/")
            for i in range(len(folder2)):
                if not os.path.exists(folder2[i]): os.mkdir(folder2[i])
                os.chdir(folder2[i])
            folder = "/".join(folder2)
        dir = os.getcwd()
        
        for file in self.files:
            file_name = file.split("/")[-1]
            if op == "win": file_split = file.split("\\")[-1]
            else: file_split = file.split("/")[-1]
            
            if file_split.split("/")[-2] == self.base_folder: 
                try:
                    urllib.request.urlretrieve(file, f"{dir}/{file_name}")
                    if log: print(f"Downloaded {file_name} into {dir}")
                except Exception as e:
                    raise Exception(f"[WWU] Failed to download {file_name}: ", e)    
            else:
                A = file_split.split(self.base_folder)[-1]
                if A.startswith("/"): A = A[1:]
                A2 = A.split("/")[0]
                
                if not os.path.exists(A2): os.mkdir(A2)
                os.chdir(A2)
                urllib.request.urlretrieve(file, os.getcwd() + "/" + file_name)
                if log: print(f"Downloaded {file_name} into {os.getcwd()}")
                os.chdir(dir)

        if launch_after is not None:
            if op == "linux": os.system(f"python3 {launch_after}")
            elif op == "win": os.system(f"python {launch_after}")
            elif op == "mac": os.system(f"python3 {launch_after}")
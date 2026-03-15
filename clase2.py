""" PROGRAMA PARA GUARDAR DATOS DE MI PC
"""

import platform, socket
from pathlib import Path

FILE_PATH = Path("pc_info.txt")



def guardar_pc_info():
    
    pc_data = "======== INFO DE PC ========\n"
    pc_data += "SISTEMA OPERATIVO: " + platform.system() + "\n" + platform.version() + "\n"
    pc_data += "ARQUITECTURA: " + platform.architecture()[0] + "\n"
    pc_data += "NOMBRE DE LA MAQUINA: " + socket.gethostname() + "\n"
    pc_data += "PROCESADOR: " + platform.processor() + "\n"
    pc_data += "HOSTNAME: " + socket.gethostname() + "\n"
    pc_data += "IP ADDRESS: " + socket.gethostbyname(socket.gethostname()) + "\n"
        
    with open(FILE_PATH, "w") as pc_file:
        pc_file.write(pc_data)
    
    print("INFO DE PC GUARDADA EN pc_info.txt")

def leer_pc_info():
    try:
        with open(FILE_PATH, "r") as pc_file:
            pc_info = pc_file.read()
            print(pc_info)
    except FileNotFoundError:
        print("EL ARCHIVO pc_info.txt NO EXISTE. PRIMERO DEBES GUARDAR LA INFO DE LA PC.")
    
if __name__ == "__main__":
    guardar_pc_info()
    leer_pc_info()
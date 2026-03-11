""" PROGRAMA PARA GUARDAR DATOS DE MI PC
"""

import platform, socket

def guardar_pc_info():
    
    pc_data = "======== INFO DE PC ========\n"
    pc_data += "SISTEMA OPERATIVO: " + platform.system() + "\n" + platform.version() + "\n"
    pc_data += "ARQUITECTURA: " + platform.architecture()[0] + "\n"
    pc_data += "NOMBRE DE LA MAQUINA: " + socket.gethostname() + "\n"
    pc_data += "PROCESADOR: " + platform.processor() + "\n"
    pc_data += "HOSTNAME: " + socket.gethostname() + "\n"
    pc_data += "IP ADDRESS: " + socket.gethostbyname(socket.gethostname()) + "\n"
        
    pc_file = open("pc_info.txt", "w")
    pc_file.write(pc_data)
    pc_file.close()
    
    print("INFO DE PC GUARDADA EN pc_info.txt")

def leer_pc_info():
    try:
        pc_file = open("pc_info.txt", "r")
        pc_data = pc_file.read()
        print(pc_data)
        pc_file.close()
    except FileNotFoundError:
        print("EL ARCHIVO pc_info.txt NO EXISTE. PRIMERO DEBES GUARDAR LA INFO DE LA PC.")
    
if __name__ == "__main__":
    guardar_pc_info()
    leer_pc_info()
import socket
import subprocess
#import os        # libreria per i comandi shell

address = ""
port = 15000

def ricevi_comandi(conn, s):
    while True:
        richiesta = conn.recv(4096)
        risposta = subprocess.run(richiesta.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        data = risposta.stdout + risposta.stderr
        conn.send(data)
        #if richiesta.decode().lower() == "shutdown":               # spegnimento computer al comando shutdown
                #s.close()
                #os.system("sudo shutdown -h now")
                #break
        print(richiesta.decode())
        s.close()
        sub_server((address, port))
        break
        

def sub_server(indirizzo, backlog=1):
    try:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(indirizzo)
        s.listen(backlog)
        print("Server in ascolto...")
    except socket.error as errore:
        print(f"Qualcosa e' andato storto... \n{errore}")
        print("Sto tentando di reinizializzare il Server...")
        sub_server(indirizzo, backlog=1) # richiamo funzione
    conn, indirizzo_client = s.accept()
    print(f"Connessione Server - Client stabilita: {indirizzo_client}")
    ricevi_comandi(conn, s)

if __name__ == "__main__":
    sub_server((address, port)) # lasciando vuoto mantiene l'ip del dispositivo

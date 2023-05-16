import socket
import sys

def invia_comandi(s):
    while True:
        comando = input("-> ")
        s.send(comando.encode())  # invio dati
        data = s.recv(4096)
        print("Sto chiudendo la connessione con il Server")
        s.close()
        sys.exit()

def conn_sub_server(indirizzo_server):
    try:
        s = socket.socket()             # Creazione socket client
        s.connect(indirizzo_server)     # connessione server
        print(f"Connessione al Server: {indirizzo_server} stabilita")
    except socket.error as errore:
        print(f"Qualcosa è andato storto \n{errore}")
        sys.exit()
    while True:
        invia_comandi(s)

if __name__ == "__main__":
    conn_sub_server(("192.168.1.92", 15000))     # la porta deve essere maggiore di 1000 perchè quelle sotto sono di sistema
                                                  # ipconfig -> trovare l'ip su linux "inet 192.168"

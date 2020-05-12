"""
Server ECHO UDP 
"""
import socket

ip = '127.0.0.1'
porta = 2512

#creazione del socket TCP IPv4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind del server per esporlo sulla rete
server.bind((ip, porta))   

#comunicazione dei dati del server all'utente
print(f"\nIl Server è online \t {ip}:{porta}")

#attesa di una connessione
server.listen()
#accettazione delle eventuali connessioni
connessione, indirizzo_client = server.accept()

while(True):
    #lettura dei dati inviati dall'utente
    data = connessione.recv(4096)  

    #controllo del comando di chiusura
    if(data.decode() == "close()"):
        break

    #comunicazione dei dati del calcolo all'utente
    print(str(indirizzo_client) + ": \t" + data.decode())    

    #restituisco il risultato al client
    connessione.sendall(data)

#chiusura del socket
server.close()

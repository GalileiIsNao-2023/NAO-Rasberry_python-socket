# NAO-Raspberry Socket in Python
Il socket è stato creato interamente in python senza alcuna dipendenza in modo da essere gestito senza alcun problema sia dal NAO che dal Raspberry.

## 🖥️Raspberry
Il rasberry è in grado di lanciare il programma in background al momento dell'accensione grazie al comando `python3 ./home/pi/Desktop/sub_serverTCP.py` all'interno del file di configurazione `./etc/rc.local`
```
_PI=$(hostname -I) || true
if [ "$_IP" ]; then
  print "My IP address is %s\n" "$_IP"
fi
python3 /home/pi/Desktop/sub_serverTCP.py
exit 0
```
**⚠️Attenzione!**
Quando il programma sarà in esecuzione la porta del dospitivo non sarà più utilizzabile.

## 🤖NAO
Il socket è ideato in modo da scollegarsi dopo ogni richiesta fatta da client, per poi tornare in ascolto fino alla prossima richiesta del NAO.

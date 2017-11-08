process_monitor

Conjunto de três arquivos que se destina a monitorar o estouro de processo winbind.

Meu servidor tinha o problema de estourar o processo do winbind, tornando mapeamentos do samba server indisponíveis.

Então acabei tendo a idéia de criar esse aplicativo, que verifica quando o winbind estoura e automaticamente mata o processo winbindd, impedindo assim que o serviço fique indisponível.

1. process_cron.py
Agendar no cron.

2. process_final.py
Responsável em matar o processo winbindd. Colocar em algum local com permissão de execução.

3. process
init linux (init.d)

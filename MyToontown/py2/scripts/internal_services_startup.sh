cd ~/Documents/MyToontown/py2

export MAX_CHANNELS=999999
export STATE_SERVER=4002
export ASTRON_IP=127.0.0.1:7199
export EVENT_LOGGER_IP=127.0.0.1:7197
export DISTRICT_NAME=Super Shore
export BASE_CHANNEL=401000000

#rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
#set /P PPYTHON_PATH=<PPYTHON_PATH

ppython -m toontown.ai.ServiceStart --base-channel 401000000 --max-channels 999999 --stateserver 4002 --astron-ip 127.0.0.1:7199 --eventlogger-ip 127.0.0.1:7197 --district-name 'Super Shore'

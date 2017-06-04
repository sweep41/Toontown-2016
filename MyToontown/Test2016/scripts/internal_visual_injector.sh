cd ~/Documents/MyToontown/Test2016

export ttiUsername=username
export ttiPassword=password
export TTI_PLAYCOOKIE=sweep
export TTI_GAMESERVER=Superserver.3d-game.com

#rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
#set /P PPYTHON_PATH=<PPYTHON_PATH

echo _______________________________
echo Toontown is starting. Please be
echo patient, as the length of this
echo process is based on your computer.
echo ________________________________

ppython -m toontown.toonbase.ToontownStartWithInjector
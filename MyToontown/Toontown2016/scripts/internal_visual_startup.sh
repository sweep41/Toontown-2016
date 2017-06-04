cd ~/Documents/MyToontown/Toontown2016

export ttiUsername=username
export ttiPassword=password

echo -n 'Username: '
read username

export TTI_PLAYCOOKIE=$username
export TTI_GAMESERVER=127.0.0.1

#rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
#set /P PPYTHON_PATH=<PPYTHON_PATH

echo _______________________________
echo Toontown is starting. Please be
echo patient, as the length of this
echo process is based on your computer.
echo ________________________________

ppython -m toontown.toonbase.ToontownStart
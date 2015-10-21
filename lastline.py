import os
def GetLastNLines(self, n, fileName):
    """
    Name:           Get LastNLines
    Description:        Gets last n lines using Unix tail
    Output:         returns last n lines of a file
    Keyword argument:
    n -- number of last lines to return
    filename -- Name of the file you need to tail into
    """
    p=subprocess.Popen(['tail','-n',str(n),self.__fileName], stdout=subprocess.PIPE)
    soutput,sinput=p.communicate()
    return soutput
for line in GetLastNLines('tail',50,'/var/log/messages').split('\n'):
    print line

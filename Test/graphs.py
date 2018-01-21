from Test.models import *

import matplotlib.pyplot as plt

# KD and WL Graph

def graph(user, time_slot):
    """
    Pass in class with Stat info
    """

    x = Stat.objects.filter(char_inst__char_id=user)
    x.get('time_stamp')
    y = Stat.objects.filter(char_inst__char_id=user)
    y.get()



    plt.plot(x, y)
    plt.plot([0.0, scale*10.0],[1.0,1.0])
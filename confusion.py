
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

def confusion_matrix_graphic(array):
    df_cm = pd.DataFrame(array, index = [i for i in 'AB'],
                      columns = [i for i in 'AB'])
    plt.figure(figsize = (10,7))
    sn.heatmap(df_cm, annot=True)
    # Display matrix
    plt.matshow(array)
    plt.show()

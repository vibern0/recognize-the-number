import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
#
import convert

def build_matrix_array(matrix, desired_results, obtained_results):
    for position in range(0, len(desired_results)):
        # print(desired_results[position])
        #
        desired = convert.convert_binary_to_int(desired_results[position])
        obtained = convert.convert_binary_to_int(obtained_results[position])
        #
        # print('>>>>>>>>>>>', desired, obtained, desired_results[position], obtained_results[position])
        matrix[desired][obtained] = matrix[desired][obtained] + 1

    return matrix

def confusion_matrix_graphic(array):
    df_cm = pd.DataFrame(array, index = [i for i in 'ABCDE'],
                      columns = [i for i in 'ABCDE'])
    plt.figure(figsize = (10,7))
    sn.heatmap(df_cm, annot=True)
    # Display matrix
    plt.matshow(array)
    plt.show()

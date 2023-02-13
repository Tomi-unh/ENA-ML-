# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 17:12:56 2023

@author: may7e
"""


"""
This creates a pickle file that combines all the CDF files of the ENA temperature maps data. The pickle file is a
dictionary with the handle being the datetime of the each timestep in the CDF file.
"""

import glob
import pickle 
import spacepy.pycdf as cdf

def cdf_to_pickle(path, filename):
    """
    

    Parameters
    ----------
    path : String
        path to the files being converted into a pickle.
    filename : String
        filename of the pickle file being created.

    Returns: Pickle file.    
    -------
    """
    
    data_dic = {}
    for file in glob.glob(path + '\\*'):
        data = cdf.CDF(file)
        time = data['Epoch'][:]
        temp_data = data['Ion_Temperature'][:]
        
        for i in range(len(time)):
            data_dic[time[i]] = temp_data[i]
        
        with open(filename , 'wb') as pickle_file:
            pickle.dump(data_dic, pickle_file)
            # del data_dic
        


def main(path, filename):
    cdf_to_pickle(path, filename)
        
        
        
if __name__ == '__main__':
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
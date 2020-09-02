from pathlib import Path
import pandas as pd 
import tensorflow as tf 
import numpy as np 


def open_files():
    
    files = []
    df = []
    data_folder = Path('C:/Users/Papalexandropoulos/Desktop/General/FakeNewsNet/NewDataset/')
    buzz_true = data_folder / 'BuzzFeed_real_news_content.csv'
    buzz_fake = data_folder / 'BuzzFeed_fake_news_content.csv'
    poli_true = data_folder / 'PolitiFact_real_news_content.csv'
    poli_fake = data_folder / 'PolitiFact_fake_news_content.csv'
    
    files.append(buzz_true)
    files.append(buzz_fake)
    files.append(poli_true)
    files.append(poli_fake)

    for i in range(len(files)):
        if not files[i].exists():
            print('The file dont exist on the current folder')
        else:
            df.append(pd.read_csv(files[i]))

    return files, df 

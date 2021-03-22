import pickle

def load(file_path):
    with open(file_path, 'rb') as pf:
        dataset = pickle.load(pf)
    return dataset

def save(file_path, dataset):
    with open(file_path, 'wb') as pf:
        pickle.dump(dataset, pf)

import pandas as pd


pathDict = {
    'originalCsv' : r'../data/data_set.csv',
    'finalCsv' : r'../data/final_data_with_scores.csv'
}

def score_calculator(row):
    '''
        Calculates the score of a given row using the formula provided and x1-x5 values

        Parameters:
            row - The row from a dataframe for which the score needs to be calculated
        Returns:
            score - The score for the row
    '''

    x1, x2, x3, x4, x5 = row[-5:]
    score = 0.717*x1 + 0.847*x2 + 3.107*x3 + 0.420*x4 + 0.998*x5

    return score



if __name__ == '__main__':
    dataframe = pd.read_csv(pathDict['originalCsv'])

    scoreList = list()
    for i, row in dataframe.iterrows():
        scoreList.append(score_calculator(row))
    
    scoreList = pd.DataFrame(scoreList, columns = ['Score'])

    finalDF = pd.concat([dataframe, scoreList], axis = 1)
    finalDF.to_csv(pathDict['finalCsv'])
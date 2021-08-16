import pandas as pd


def mainf():
    df = pd.read_excel("ReportCard/DummyData.xlsx")
    df = df[df['Unnamed: 0'] == 1]
    df = df.reset_index()
    candidate_df = df
    CandidateName = candidate_df['Unnamed: 4'][1]
    RegistrationNumber = candidate_df['Unnamed: 5'][1]
    Grade = candidate_df['Unnamed: 6'][1]
    NameofSchool = candidate_df['Unnamed: 7'][1]
    Gender = candidate_df['Unnamed: 8'][1]
    Address = candidate_df['Unnamed: 10'][1] + \
        "/"+candidate_df['Unnamed: 12'][1]
    DateofBirth = str(candidate_df['Unnamed: 9'][1]).split()[0]
    DateofTest = candidate_df['Unnamed: 11'][1]
    ScoreData = candidate_df[['Unnamed: 13', 'Unnamed: 14',
                              'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18']].to_numpy()
    FinalResult = candidate_df['Unnamed: 19'][1]
    PossibleScore = candidate_df['Unnamed: 17'].sum()
    candidate_df['Unnamed: 18'] = pd.to_numeric(
        candidate_df['Unnamed: 18'])
    OverallScore = candidate_df["Unnamed: 18"].sum()

    # making dict and passing to html using jinja
    template_var = {"CandidateName": CandidateName,
                    "RegistrationNumber": RegistrationNumber,
                    "Grade": Grade,
                    "NameofSchool": NameofSchool,
                    "Gender": Gender,
                    "Address": Address,
                    "DateofBirth": DateofBirth,
                    "DateofTest": DateofTest,
                    "FinalResult": FinalResult,
                    "ScoreData": ScoreData,
                    "PossibleScore": PossibleScore,
                    "OverallScore": OverallScore}
    return template_var

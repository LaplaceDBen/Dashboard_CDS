# Test-Space für ein Paar Versuche; Raphael

import pandas as pd
from IPython.display import display
import plotly.graph_objects as go


df = pd.read_csv(r'.\Summer-Olympic-medals-1976-to-2008.csv', encoding="utf-8")

#A46
def A46(df):
    df1 = df.copy()

    print("\nSortieren des Olympia-Datensatzes nach Land, Jahr und Sportart.\nWenn Sie die Suche bei einem Kriterium nicht einschränken möchten, drücken Sie einfach Enter.\n")
    inputLand = input("Geben Sie ein, nach welchem Land Sie sortieren möchten: ")
    inputJahr = input("Geben Sie ein, nach welchem Jahr Sie sortieren möchten: ")
    inputSportart = input("Geben Sie ein, nach welcher Sportart Sie sortieren möchten: ")
    print("\nSortiere nach folgenden Kriterien:",inputLand, inputJahr,inputSportart,"\n")

    if inputLand in df['Country'].values:
        df1 = df1[df.Country == inputLand]
    else:
        print(inputLand,"ist nicht vorhanden\n")
    if inputJahr.isdigit():
        if int(inputJahr) in df['Year'].values:
            df1 = df1[df1.Year == int(inputJahr)]
        else:
            print(inputJahr,"ist nicht vorhanden\n")
    else:
        print(inputJahr,"ist keine Zahl.\n")
    if inputSportart in df['Sport'].values:
        df1 = df1[df1.Sport == inputSportart]
    else:
        print(inputSportart,"ist nicht vorhanden\n")

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'right')
    pd.set_option('display.precision', 3)

    if not df1.empty:
        display(df1)
    else:
        print("Mit diesen Kriterien gibt es keine Resultate\n")

    return df1

#A46 ausführen: nächste Zeile auskommentieren
#A46(df)

#Beispiel: Land - Switzerland; Jahr - 1976, Sportart - Equestrian

# _______________________________________________

#A47
def A47(df):
    df2 = df.copy()

    eingabe = input("Geben Sie ein paar Buchstaben ein: ")
    print("\nIhre Eingabe: ",eingabe)

    liste = []
    for i in range(len(df2.Athlete)):
        liste.append(True)

    for i in range(len(eingabe)):
        df2[i] = pd.DataFrame(df2['Athlete'].str.contains(eingabe[i],case=False))
    for j in range(len(df2.Athlete)):
        for k in range(len(eingabe)):
            if df2[k][j] == False:
                liste[j] = False

    df2['NameCheck'] = pd.DataFrame(liste)
    df2 = df2[df2.NameCheck == True]
    df2=df2.dropna()

    print("\nMit Ihrer eingabe wurden",len(df2.NameCheck),"Athleten gefunden!\n\n")

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'right')
    pd.set_option('display.precision', 3)
    display(df2['Athlete'])

    return df2

#A47 ausführen: nächste Zeile auskommentieren
#A47(df)

#Beispiel: CHRISTIAN (Gross-/Kleinschreibung wird nicht beachtet.
#Erstes Resultat vom Beispiel: WITSCHAS-ACKERMANN, Rosemarie
#Resultat: Erfolgreich, denn es sind alle Buchstaben von 'CHRISTIAN' enthalten.
#Da jegliche Kombination der Buchstaben gültig ist, gibt es immer extrem viele Resultate.

# _______________________________________________

#A48
def A48(df):
    df3 = df.copy()
    df3 = df3.dropna()
    df3 = df3.drop(columns=['City','Year','Sport','Discipline','Event','Athlete','Gender','Country_Code','Event_gender'])

    eingabe2 = input("Geben Sie das Land ein, nach dem Sie filtern möchten: ")
    print("\nIhre Auswahl:",eingabe2,"\n")
    df3 = df3[df3.Country == eingabe2]

    total = len(df3)
    gold = len(df3[df3["Medal"]=='Gold'])
    silver = len(df3[df3["Medal"]=='Silver'])
    bronze = len(df3[df3["Medal"]=='Bronze'])

    print("Anzahl Medallien insgesamt:",total)
    print("Anzahl Gold-Medallien:",gold)
    print("Anzahl Silber-Medallien:",silver)
    print("Anzahl Bronze-Medallien:",bronze)

    # result = df3['Medal'].value_counts() (Übersicht)

    return total, gold, silver, bronze

#A48 ausführen: nächste Zeile auskommentieren
#A48(df)

#Beispiel: Switzerland
# _______________________________________________
#A49
#separat

# _______________________________________________

#A50
#Wir führen Anpassungen am Code vom Aufgabenblatt 9 durch, um die Matrix besser zu sortieren
#Sortierung ist mit Kommentar markiert
#Visualisierung wurde separat abgespeichert, siehe PDF

#Aufgabe 42
def A_42(df):
    df_m = df.groupby(['Country']).size().reset_index(name='counts')
    m= df_m.sort_values(by=['counts'], ascending=False)
    print(m.head(10))
    return m

#A_42(df)

def A_43(df):
    df_cd = df.groupby(['Country','Sport']).size().reset_index(name='counts')
    cd = df_cd.sort_values(by=['Country','Sport'], ascending=True)
    print(cd)
    return cd
#A_43(df)

#Aufgabe 44

def A_50(df):
    country = A_42(df)
    cd_df = A_43(df)
    country = country.rename(columns={'counts': 'counts_all'})
    ratio_df = country.merge(cd_df, how='left', left_on='Country', right_on='Country')
    ratio_df['normalized']= ratio_df['counts']/ ratio_df['counts_all']
    final_df = ratio_df.sort_values(by=['Country','Sport'], ascending=True)
    final_df = final_df.sort_values(['normalized','Sport']) #!!!NEU: Sortiert nach der Normalisierung
    print(final_df.head())
    print(final_df)

    fig = go.Figure(data=go.Heatmap(
        z=final_df['normalized'], x=final_df['Country'],y=final_df['Sport'],hoverongaps=False))
    fig.write_html("file.html")
    fig.show()
    return fig

#Aufgabe 50:
A_50(df)
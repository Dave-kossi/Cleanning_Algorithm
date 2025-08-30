import pandas as pd
import os

def charger_fichier(fichier):
    extension = os.path.splitext(fichier)[1]
    
    if extension == ".csv":
        df = pd.read_csv(fichier)
    elif extension in [".xls", ".xlsx"]:
        df = pd.read_excel(fichier)
    elif extension == ".json":
        df = pd.read_json(fichier)
    else:
        raise ValueError("Format de fichier non supporté.")
    
    print(f"✅ Fichier chargé : {fichier} ({df.shape[0]} lignes, {df.shape[1]} colonnes)")
    return df

def nettoyer_donnees(df):
    df = df.copy()
    print("\n🔍 Nettoyage de base en cours...")

    # Suppression des doublons
    avant = df.shape[0]
    df = df.drop_duplicates()
    print(f" - Doublons supprimés : {avant - df.shape[0]}")

    # Valeurs manquantes
    print("\n - Valeurs manquantes détectées :")
    print(df.isnull().sum()[df.isnull().sum() > 0])

    # Remplissage simple des colonnes numériques
    for col in df.select_dtypes(include='number').columns:
        df[col].fillna(df[col].mean(), inplace=True)
    
    df.dropna(how='all', inplace=True)
    return df

def generer_rapport_simple(df, nom_fichier="rapport_diagnostic.txt", seuil_nan=0.95):
    lignes = []
    total_rows = df.shape[0]

    lignes.append("=== RAPPORT DE DIAGNOSTIC ===\n")
    lignes.append(f"Nombre de lignes : {total_rows}")
    lignes.append(f"Nombre de colonnes : {df.shape[1]}\n")

    # Doublons
    nb_doublons = df.duplicated().sum()
    lignes.append(f"🔁 Doublons : {nb_doublons} lignes ({nb_doublons / total_rows:.2%})\n")

    # Valeurs manquantes
    lignes.append("=== Valeurs manquantes par colonne ===")
    missing = df.isnull().sum()
    for col in df.columns:
        if missing[col] > 0:
            lignes.append(f"{col}: {missing[col]} valeurs manquantes ({missing[col] / total_rows:.2%})")

    # Colonnes constantes
    lignes.append("\n=== Colonnes constantes ===")
    constantes = [col for col in df.columns if df[col].nunique(dropna=False) <= 1]
    if constantes:
        for col in constantes:
            lignes.append(f"{col}: constante")
    else:
        lignes.append("Aucune")

    # Colonnes avec trop de NaN
    lignes.append("\n=== Colonnes avec trop de NaN (> {:.0f}%) ===".format(seuil_nan*100))
    for col in df.columns:
        ratio_nan = df[col].isnull().mean()
        if ratio_nan > seuil_nan:
            lignes.append(f"{col}: {ratio_nan:.2%} de NaN")

    # Colonnes avec types incohérents
    lignes.append("\n=== Colonnes texte avec types mélangés ===")
    for col in df.select_dtypes(include='object'):
        types = df[col].dropna().apply(type).value_counts()
        if len(types) > 1:
            lignes.append(f"{col}: types mélangés {dict(types)}")

    # Statistiques générales
    lignes.append("\n=== Aperçu statistique ===")
    lignes.append(df.describe(include='all').to_string())

    # Écriture du fichier
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes))

    print(f"\n✅ Rapport de diagnostic généré : {nom_fichier}")

def sauvegarder_donnees(df, nom_fichier="data_nettoyee.csv"):
    df.to_csv(nom_fichier, index=False)
    print(f"\n✅ Données nettoyées sauvegardées dans : {nom_fichier}")

# --- Utilisation ---
if __name__ == "__main__":
    chemin_fichier = "Online Retail.xlsx"   # À modifier selon ton fichier
    df = charger_fichier(chemin_fichier)
    generer_rapport_simple(df)
    df_nettoye = nettoyer_donnees(df)
    sauvegarder_donnees(df_nettoye)

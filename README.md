# Cleanning_Algorithm
# 🧹 Nettoyage intelligent de données avec Python

## 📌 Objectif du projet

Ce projet propose un **script Python automatisé** pour **charger, diagnostiquer, nettoyer intelligemment et sauvegarder** un jeu de données. Il est idéal pour les data analysts, data scientists ou toute personne manipulant des fichiers contenant des incohérences, doublons ou valeurs manquantes.

## 🚀 Fonctionnalités principales

- ✅ **Chargement universel** : supporte `.csv`, `.xlsx` et `.json`
- 🔍 **Diagnostic complet** :
  - Doublons
  - Valeurs manquantes
  - Colonnes constantes ou incohérentes
  - Types mélangés dans les colonnes texte
  - Colonnes avec trop de NaN
- 🧠 **Nettoyage automatique** :
  - Normalisation des chaînes de caractères
  - Tentative de conversion en numérique ou datetime
  - Imputation des valeurs manquantes
  - Suppression des lignes/colonnes entièrement vides
- 📊 **Rapport de diagnostic généré en `.txt`**
- 💾 **Sauvegarde des données nettoyées**

## 🛠️ Utilisation

### 1. Remplacer le nom de fichier dans le script :
```python
chemin_fichier = "Data.csv"  # Remplacez par le nom de votre fichier
et exécuter l'algorithme par:
'''python Cleanning_Algo.py'''
 Résultats obtenus :
rapport_diagnostic.txt : rapport complet du fichier original

data_nettoyee.csv : jeu de données prêt pour l’analyse ou la modélisation

📂 Organisation du script
charger_fichier() : charge le fichier selon son format

corriger_formats() : corrige et homogénéise les formats

nettoyer_donnees_intelligemment() : pipeline de nettoyage automatique

generer_rapport_simple() : génère un rapport de qualité des données

sauvegarder_donnees() : exporte le fichier nettoyé

📌 Exemple d’application
Ce script peut être intégré :

À une pipeline de data ingestion

Dans un projet de data science ou machine learning

Pour auditer la qualité des données dans des fichiers clients ou CRM

Dans un outil low-code ou interface utilisateur Gradio/Streamlit

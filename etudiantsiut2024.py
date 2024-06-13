import streamlit as st
import pyodbc
def create_conn():
  conn= pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-O4KS14V\\SQLEXPRESS;'
    'DATABASE=etudiants;'
    'UID=alken;'
    'PWD=#kenne*dy*27#;'
    'Trusted_Connection=no;' # Utilisez l'authentification windows
  )
  return conn
# inserer les donnees dans la table eleve
def insert_data(nom,prenom,matricule,filliere ,salle):
  conn=create_conn()
  cursor=conn.cursor()
  query="INSERT INTO eleve (nom,prenom,matricule,filliere,salle) VALUES(?,?,?,?,?)"
  cursor.execute(query,(nom,prenom,matricule,filliere,salle))
  conn.commit()
  conn.close()
  
 #creer l'interface utilisateur de streamlit
def create_ui():
  st.title("formulaire d'inscription des etudiants")
  nom=st.text_input("Nom")
  prenom=st.text_input("prenom")
  matricule=st.text_input("Matricule")
  filliere=st.selectbox("Fillier",["informatique","Mathematiques","Physique","chimie"])
  salle=st.text_input("salle")

  if st.button("soumettre"):
    insert_data(nom,prenom,matricule,filliere,salle)
    st.success("les donnees ont ete inseree avec succes dans la base de donnees.")
create_ui()    
  

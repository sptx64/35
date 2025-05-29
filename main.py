import streamlit as st
import random

# Liste des défis
defis = [
    "Tant que ton verre est plein tu n'as pas le droit de le poser, le garder en main tout le temps",
    "A chaque fois que tu finis ton verre tu dois dire 'on est bien là'",
    "A chaque fois que tu arrives dans un nouveau bar tu dois dire 'Paquito?'",
    "A chaque fois que tu rentres dans un nouveau bar tu dois dire 'heeeyyyy'",
    "Tu dois être le premier à rentrer dans le bar, peut importe les conséquences",
    "Tu dois demander où sont les toilettes dans chaque bar, et ne pas y aller",
    "À chaque fois que quelqu'un dit 'bon allé' tu dois faire un tour sur toi même, discrètement",
    "Tu dois partir le dernier de chaque bar et dire 'on n'attend pas Patrick ?'",
    "Quand on te demande ce que tu prends demande s'ils ont du lillet, dire 'c'est moins sucré' puis demander une bière finalement",
    "Quand tu rentres dans un nouveau bar, demande aux serveurs 'où sont les toilettes ?'. Ne pas y aller.",
    "Demander dans chaque bar à quelqu'un : 'c'est toi qui déménage ce weekend ?'",
    "Quand tu finis ta bière dire 'encore une que les allemands n'auront pas'",
    "Dans chaque bar dire 'ah la bière était meilleure dans le bar d'avant'",
    "Avant de t'asseoir tu dois faire un squat.",
    "Dans chaque nouveau bar défier quelqu'un au bras de fer",
    "Dans chaque bar défier quelqu'un à la bataille de pouce",
    "Trouver Alice, dans chaque bar lui dire 'attention Alice, ça glisse 🤙'",
    "A chaque fois qu'on trinque, dire 'cul sec ?'",
    "Dans tous les bars faire au moins une référence à la coupe du monde 98",
    "Progressivement, deviner le signe astrologique de tout le monde dans la soirée. 'Tu serais pas scorpion toi' et trouver des arguments pour dire que ça se voit",
    "#jacquesbashing à chaque fois que Jacques parle être hyper impressionné : 'Wow' / 'Mais nonnn' / 'C'est incroyable'",
    "#jacquesbashing à chaque fois que Jacques t'adresse la parole, se lever et s'en aller.",
    "Tu dois changer de place à chaque fois que tu entends le mot anniversaire. Ça fonctionne aussi bien debout qu'assis.",
    "Tu dois discrètement pointer du doigt tout le monde quand tu parles",
    "A partir de maintenant tu rigoles comme dans un texto : utilises les acronymes lol, mdr, ptdr à la place",
    "Quand tu es assis tu dois mimer tous les mouvements de Manu, tout le temps.",
    "Tu es le Jacques de la soirée, sois pessimiste, dis qu'on n'y arrivera jamais, dire que ça aurait été mieux avec plus d'organisation, etc..."
]

# Titre de l'application
st.title("Défi de la Soirée 🎉")

# Bouton pour tirer un défi au hasard
if st.button("Tirer un défi"):
    defi_choisi = random.choice(defis)
    st.success(defi_choisi)
    st.balloons()

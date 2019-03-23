# **Guessless Project**

## Membres :
* Maher LAAROUSSI (maher.laaroussi@gmail.com) [MaherLRS](https://github.com/maherlaaroussi "maherlaaroussi")
* Aboubakr CHOUTTA (achoutta@gmail.com)  [aboubakrCH](https://github.com/aboubakrCH "aboubakrCH")
* Hamid OUFKIR (hamid.oufkir@yahoo.com) [HamidOuF](https://github.com/HamidOuF "HamidOuF")
* Othmane MCHOUAT (mchouat.o@gmail.com)  [othmaneMCHOUAT](https://github.com/othmaneMCHOUAT "othmaneMCHOUAT")


## Nom du produit IoT : Guessless

![alt text](https://github.com/institut-galilee/guessless/blob/master/docs/Design.png)

## C'est quoi guessless ?

Une table connectée à mettre partout dans la maison, qui permet de reconnaitre n'importe quel objet en cas de trou de mémoire.  
Dans la cuisine, elle vous fournira toute information essentielle sur un aliment pour ainsi manger plus sainement.  
Envie d'avoir une description détaillée sur un objet ? posez-le sur la table !

## Comment ça marche ?

Le principe est simple, il suffit de poser un objet sur la surface plexiglass au dessus du panneau LED pour que la table commence sa détéction, une animation vous le notifiera. Une fois la reconnaissance terminée, le résultat s'affichera sur l'écran se trouvant à coté du panneau.  
Vous pourrez afficher plus d'information en appuyant sur le bouton "Plus" de l'écran.


## Est-ce que ça marche ?

Pour l'instant, le projet est en cours de conception mais on vous tiendra au courant de son avancement.

## Dans le futur ?

Plusieurs améliorations sont prévues pour notre table comme la reconnaissance vocale, la comparaison de deux aliments et l'apairage avec un smartphone.


## Help ?
### Comment lancer l'application ?
L'application, pour l'instant, se situe dans le répertoire `tensorflow/models/research/object_detection/`.


## Aspet technique :

### Reconnaissance d'objet : Tensorflow
Tensorflow a été compilé depuis le code source a cause des problèmes renconré en l'installant avec la commande `sudo pip3 install tensorflow`.  

### Interface graphique de l'application : PyQt5
L'application qui permet de controller la table sera codé avec la librairie PyQt5 en Python.

  
## Composants :

* Matrix LED RGB 64x32 Panel
* Raspberry Pi Zero WH
* Raspberry Pi Zero 3 B+
* 1x Caméra Raspberry Pi
* 2x Power supply (Raspberry & LED Panel)
* Câbles & fils
* Plaque Plexiglass
* Balance
* 2x Haut-Parleurs
* Touchscreen display 7"

## Crédits :
* http://blog.deconinck.info/post/2016/12/19/A-Dirt-Cheap-F-Awesome-Led-Table (L'origine de notre projet)
* https://www.youtube.com/watch?v=npZ-8Nj1YwY (Mise en place de ProtoBuffer, OpenCV et Tensorflow sur un Raspberry)
* https://github.com/EdjeElectronics (Compréhension de comment Tensorflow fonctionne)

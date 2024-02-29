document.addEventListener('DOMContentLoaded', function() {
    var selectFournisseur = document.getElementById('id_fournisseur');
    var divAutreFournisseur = document.getElementById('nouveauFournisseur');

    selectFournisseur.addEventListener('change', function() {
        // Vérifiez si l'option "Autre ..." est sélectionnée
        if(this.value === '45') {
            divAutreFournisseur.style.display = 'block'; // Affichez le champ pour entrer un nouveau nom
        } else {
            console.log("ok");
            divAutreFournisseur.style.display = 'none'; // Cachez-le sinon
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var selectFournisseur = document.getElementById('id_atelier');
    var divAutreFournisseur = document.getElementById('nouveauAtelier');

    selectFournisseur.addEventListener('change', function() {
        // Vérifiez si l'option "Autre ..." est sélectionnée
        if(this.value === '14') {
            divAutreFournisseur.style.display = 'block'; // Affichez le champ pour entrer un nouveau nom
        } else {
            divAutreFournisseur.style.display = 'none'; // Cachez-le sinon
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var selectFournisseur = document.getElementById('id_fournisseur_actionneur');
    var divAutreFournisseur = document.getElementById('nouveauFournisseurActionneur');

    selectFournisseur.addEventListener('change', function() {
        // Vérifiez si l'option "Autre ..." est sélectionnée
        if(this.value === '45') {
            divAutreFournisseur.style.display = 'block'; // Affichez le champ pour entrer un nouveau nom
        } else {
            console.log("ok");
            divAutreFournisseur.style.display = 'none'; // Cachez-le sinon
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var selectFournisseur = document.getElementById('id_fournisseur_positionneur');
    var divAutreFournisseur = document.getElementById('nouveauFournisseurPositionneur');

    selectFournisseur.addEventListener('change', function() {
        // Vérifiez si l'option "Autre ..." est sélectionnée
        if(this.value === '45') {
            divAutreFournisseur.style.display = 'block'; // Affichez le champ pour entrer un nouveau nom
        } else {
            console.log("ok");
            divAutreFournisseur.style.display = 'none'; // Cachez-le sinon
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    var selectFournisseur = document.getElementById('presence_positionneur');
    var divAutreFournisseur = document.getElementById('infoPositionneur');

    // Fonction pour ajuster l'affichage de divAutreFournisseur en fonction de la sélection
    function ajusterAffichage() {
        if(selectFournisseur.value === '1') {
            divAutreFournisseur.style.display = 'block'; // Affichez le champ pour entrer un nouveau nom
        } else {
            divAutreFournisseur.style.display = 'none'; // Cachez-le sinon
        }
    }

    // Ajoutez un écouteur d'événement pour gérer le changement de sélection
    selectFournisseur.addEventListener('change', ajusterAffichage);

    // Appelez ajusterAffichage() pour définir l'affichage initial correctement
    ajusterAffichage();
});


document.addEventListener('DOMContentLoaded', function() {
    var selectFournisseur = document.getElementById('infoRevisionBIS');
    var divAutreFournisseur = document.getElementById('tempsRevision');

    // Fonction pour ajuster l'affichage de divAutreFournisseur en fonction de la sélection
    function ajusterAffichage() {
        if(selectFournisseur.value === '1') {
            divAutreFournisseur.style.display = 'block'; // Affichez le champ pour entrer un nouveau nom
        } else {
            divAutreFournisseur.style.display = 'none'; // Cachez-le sinon
        }
    }

    // Ajoutez un écouteur d'événement pour gérer le changement de sélection
    selectFournisseur.addEventListener('change', ajusterAffichage);

    // Appelez ajusterAffichage() pour définir l'affichage initial correctement
    ajusterAffichage();
});
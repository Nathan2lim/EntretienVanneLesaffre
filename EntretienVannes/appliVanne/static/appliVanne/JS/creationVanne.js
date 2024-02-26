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
    document.getElementById('presence_positionneur').addEventListener('change', function() {
        var infoDiv = document.getElementById('infoPositionneur');
        if (this.value === '1') {
            infoDiv.style.display = 'block'; // Afficher
        } else {
            infoDiv.style.display = 'none'; // Cacher
        }
    });
});


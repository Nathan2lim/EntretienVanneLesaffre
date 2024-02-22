document.addEventListener('DOMContentLoaded', function() {
    var selectFournisseur = document.getElementById('fournisseur');
    var divAutreFournisseur = document.getElementById('nouveauFournisseur');

    selectFournisseur.addEventListener('change', function() {
        // Vérifiez si l'option "Autre ..." est sélectionnée
        if(this.value === 'autre') {
            divAutreFournisseur.style.display = 'block'; // Affichez le champ pour entrer un nouveau nom
        } else {
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


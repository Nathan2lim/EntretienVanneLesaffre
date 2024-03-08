document.addEventListener('DOMContentLoaded', function() {
    // Sélectionne toutes les lignes du corps du tableau pour ajouter un écouteur d'événements
    var rows = document.querySelectorAll('.table tbody tr');
    
    rows.forEach(function(row) {
      row.addEventListener('click', function() {
        // Récupère l'URL de détail de la vanne depuis le data attribute ou le contenu de la cellule
        var vanneId = this.cells[0].textContent; // Supposons que l'ID de la vanne est dans la première cellule
        var detailUrl = '/vanne/' + vanneId + '/detail'; // Construit l'URL de détail

        // Redirige le navigateur vers l'URL de détail de la vanne
        window.location.href = detailUrl;
      });
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    // Cible uniquement les lignes du tableau avec la classe "historique-modifications"
    var rows = document.querySelectorAll('.historique-modifications tbody tr');
  
    rows.forEach(function(row) {
      row.addEventListener('click', function() {
        // L'ID de la vanne se trouve dans la deuxième cellule (index 1)
        var vanneId = this.cells[1].textContent.trim();
        var detailUrl = '/vanne/' + vanneId + '/detail'; // Construit l'URL de détail
        window.location.href = detailUrl; // Redirige vers l'URL de détail
      });
    });
  });
  
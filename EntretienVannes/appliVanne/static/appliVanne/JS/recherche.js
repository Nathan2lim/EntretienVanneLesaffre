


$(document).ready(function() {
    $('#searchInput').keyup(function() {
        var searchTerm = $(this).val();
        $.ajax({
            type: 'GET',
            url: '{% url 'dump' %}',
            data: {
                term: searchTerm
            },
            dataType: 'json', // Assure-toi d'ajouter cette ligne pour que jQuery parse le JSON automatiquement
            success: function(response) {
                displayResults(response);
            }
        });
    });

    function displayResults(response) {
        var tableBody = $('#vannesContainer');
        tableBody.empty();
        
        if (response.results.length === 0) {
            // Si aucun résultat n'est trouvé, affichez un message
            var noResultsRow = '<tr><td colspan="8">Aucun résultat</td></tr>';
            tableBody.append(noResultsRow);
        }
        else
        {
            response.results.forEach(function(result) {
                var deleteRecoverLink;
                var deleteRecoverText;
                
                if (parseInt(result.en_service_vanne) === 1) {
                    deleteRecoverLink = "/delete";
                    deleteRecoverText = "DELETE";
                    //console.log("del");
                } else {
                    deleteRecoverLink = "/recover";
                    deleteRecoverText = "RECOVER";
                    //console.log("reco");
                }
                
                var row = '<tr>' +
                    '<td>' + result.id_vanne + '</td>' +
                    '<td>' + result.id_atelier__nom_atelier + '</td>' +
                    '<td>' + result.repere_vanne + '</td>' +
                    '<td>' + result.affectation_vanne + '</td>' +
                    '<td>' + result.type_vannes + '</td>' +
                    '<td>' + result.voir_en + '</td>' +
                    '<td>' + result.id_positionneur__fonctionnement_positionneur__description_type_positionneur + '</td>' +
                    '<td>' + 
                        '<a class="detdel"  href="/vanne/' + result.id_vanne + '/detail">DETAIL / </a>' +
                        '<a class="detdel"  href="/vanne/' + result.id_vanne + deleteRecoverLink + '">' + deleteRecoverText + '</a>' +
                    '</td>'+
                    '</tr>';
                    
                    
                tableBody.append(row);
            });
        }
    }
    
    
});


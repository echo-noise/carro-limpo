var ctx = document.getElementById("estatisticasChart");
// Puxar as infos do DB e exibir no yValues
var yValues = [1, 1, 50, 50, 0];
    var productsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Serviços", "Clientes", "Faturamento", "Receita", "Gasto"],
            datasets: [{
                label: "",   
                data: yValues,        
                backgroundColor: [
                    '#008CFF',
                    '#003968',
                    '#000000',
                    '#035e12',
                    '#ff0000'
                ],
            }]
        },
        options: {
            responsive: false,
            legend: {display: false},
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
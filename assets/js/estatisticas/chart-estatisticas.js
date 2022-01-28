function chart(value1, value2, value3, value4) {
    var ctx = document.getElementById("estatisticasChart");
    // Puxar as infos do DB e exibir no yValues
    var yValues = [value1, value2, value3, value4];
        var productsChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ["Serviços", "Clientes", "Faturamento",  "Gasto"],
                datasets: [{
                    label: "",
                    data: yValues,
                    backgroundColor: [
                        '#008CFF',
                        '#003968',
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
}
function plotG(x_values,y_values){
    const ctx = document.getElementById('myChart');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: x_values,
            datasets: [{
                label: '# of Votes',
                data: y_values,
                borderWidth: 1
            }]
        },
        options: {
            animation: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
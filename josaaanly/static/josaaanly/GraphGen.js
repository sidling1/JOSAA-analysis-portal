const ctx = document.getElementById('myChart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 9, 3, 5, 2, 3],
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
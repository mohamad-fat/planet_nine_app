var ctx = document.getElementById('bar-chart').getContext('2d');
var barChart = new Chart(ctx, {
    type:'bar',
    data: {
        labels: {{ labels | safe }},
        datasets: [
            {
                data: {{ values | safe }},
                label: 'predicted',
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(153, 102, 255, 0.2)',],
                borderColor: [
                    'rgb(255, 99, 132)',
                    'rgb(54, 162, 235)',,
                    'rgb(153, 102, 255)'],
                borderWidth: 1
            }
        ],
    },
    options: {
        scales: {
            y: {
                suggestedMin: 0,
                suggestedMax: 1,
                title: {
                    display: true,
                    text: 'probability'
                }
            }
        },
        plugins: {
            title: {
                display: true,
                text: 'Top three predictions'
                // padding: {
                //     top: 10,
                //     bottom: 30
                // }
            }
    }
    }
});
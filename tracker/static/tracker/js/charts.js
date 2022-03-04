const data = {
    labels: labels,
    datasets: datasets
};

const config = {
    type: 'line',
    data: data,
    options: {}
};

const myChart = new Chart(
    document.getElementById('chart'),
    config
);
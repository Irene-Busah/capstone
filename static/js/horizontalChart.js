document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('consumptionRegionChart').getContext('2d');
    var consumptionRegionChart = new Chart(ctx, {
        type: 'bar', // Use 'bar' for horizontal bar chart and control direction with indexAxis
        data: {
            labels: [], // This will be the list of regions
            datasets: [{
                label: '',
                data: [],
                backgroundColor: '#B8E716',
                borderColor: '#B8E716',
                borderWidth: 1,
                barThickness: 50,
                borderRadius: 8,
            }]
        },
        options: {
            indexAxis: 'y', // Makes the chart horizontal
            scales: {
                x: { // Configures the horizontal axis
                    grid: {
                        display: false // Hides the grid lines for the x-axis
                    },
                    beginAtZero: true // Starts the scale at zero
                },
                y: { // Configures the vertical axis (categories)
                    grid: {
                        display: false // Hides the grid lines for the y-axis
                    },
                    barPercentage: 0.8, // Sets the thickness of the bars
                    categoryPercentage: 1.0 // Sets the spacing between categories
                }
            },
            plugins: {
                legend: {
                    display: false // Hides the legend
                }
            }
        }

    });

    function updateChartWithData() {
        fetch('/api/frequently-consumed-by-region/')
            .then(response => response.json())
            .then(data => {
                // Extract unique regions
                const regions = [...new Set(data.map(item => item['store__region__name']))];

                // Map each region to its total quantity by summing up the quantities for that region
                const quantities = regions.map(region => {
                    return data.filter(item => item['store__region__name'] === region)
                        .reduce((acc, curr) => acc + curr['total_quantity'], 0);
                });

                // Update the chart
                consumptionRegionChart.data.labels = regions;
                consumptionRegionChart.data.datasets[0].data = quantities;
                consumptionRegionChart.update();
            })
            .catch(error => console.error('Error fetching frequently consumed data:', error));
    }

    // Populate the chart with data
    updateChartWithData();
});

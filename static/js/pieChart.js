document.addEventListener('DOMContentLoaded', function () {
    const yearSelect = document.querySelector('#year');
    let foodExpirationChart;

    function fetchDataAndDrawChart() {
        fetch('/api/expired-products-by-category/')
            .then(response => response.json())
            .then(data => {
                const selectedYear = yearSelect.value;
                const yearData = data[selectedYear] || [];

                if (yearData.length === 0) {
                    // If there's no data for the selected year, hide the chart and display a message
                    document.getElementById('foodExpirationChart').style.display = 'none';
                    document.getElementById('legend-container').innerHTML = '<p style="font-weight: bold; color: red; text-align: center;">No data available for this year.</p>';
                    return;
                }


                // Ensure the chart canvas is visible
                document.getElementById('foodExpirationChart').style.display = '';

                // Process the data to fit Chart.js structure
                const labels = yearData.map(item => item.category_name);
                const percentages = yearData.map(item => item.percentage);
                const totalExpired = yearData.reduce((sum, item) => sum + item.total_expired, 0);

                if (foodExpirationChart) {
                    // If a chart instance exists, destroy it before creating a new one
                    foodExpirationChart.destroy();
                }

                // Create a new chart instance
                const ctx = document.getElementById('foodExpirationChart').getContext('2d');
                foodExpirationChart = new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: labels,
                        datasets: [{
                            data: percentages,
                            backgroundColor: ['#03974A', '#FFB800', '#CAF9E0', '#B8E716'],
                            borderColor: ['#fff'],
                            borderWidth: 1,
                            hoverOffset: 8,
                            borderRadius: 8,
                        }]
                    },
                    options: {
                        cutout: '70%',
                        responsive: true,
                        plugins: {
                            legend: {
                                display: false
                            },
                            title: {
                                display: false
                            },
                            tooltip: {
                                enabled: true
                            }
                        },
                        elements: {
                            arc: {
                                hoverOffset: 120
                            }
                        }
                    },
                    plugins: [{
                        afterDraw: function (chart) {
                            let ctx = chart.ctx;
                            let width = chart.width;
                            let height = chart.height;
                            ctx.textAlign = 'center';
                            ctx.textBaseline = 'middle';
                            ctx.font = 'bold 1.2em Urbanist';
                            ctx.fillStyle = '#000';
                            ctx.fillText(totalExpired.toLocaleString(), width / 2, height / 2 - 10);
                            ctx.font = '0.8em Urbanist';
                            ctx.fillStyle = '#9C9A9A';
                            ctx.fillText('Products', width / 2, height / 2 + 20);
                        }
                    }]
                });

                // Update the legend
                updateLegend(labels, foodExpirationChart.data.datasets[0].backgroundColor);
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    function updateLegend(labels, colors) {
        const legendContainer = document.getElementById('legend-container');
        const legendItems = labels.map((label, index) => {
            return `
            <div class="legend-item">
                <span class="legend-color" style="background-color: ${colors[index]};"></span>
                <span class="legend-label">${label}</span>
            </div>
            `;
        }).join('');
        legendContainer.innerHTML = legendItems;
    }

    // Initialize the chart with the default selected year's data
    fetchDataAndDrawChart();

    // Event listener for year change in the dropdown
    yearSelect.addEventListener('change', fetchDataAndDrawChart);
});

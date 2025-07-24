document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById("sentimentChart").getContext("2d");

    const sentimentCounts = JSON.parse(document.getElementById("sentiment-data").textContent);

    const chart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Positive", "Negative", "Neutral"],
            datasets: [{
                label: "Sentiment Count",
                data: [
                    sentimentCounts.Positive || 0,
                    sentimentCounts.Negative || 0,
                    sentimentCounts.Neutral || 0
                ],
                backgroundColor: [
                    "rgba(75, 192, 192, 0.6)",
                    "rgba(255, 99, 132, 0.6)",
                    "rgba(201, 203, 207, 0.6)"
                ],
                borderColor: [
                    "rgba(75, 192, 192, 1)",
                    "rgba(255, 99, 132, 1)",
                    "rgba(201, 203, 207, 1)"
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: { stepSize: 1 }
                }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });
});

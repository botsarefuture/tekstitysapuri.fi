document.addEventListener("DOMContentLoaded", function() {
    const donutChart = document.querySelector(".donut-chart");
    const donutText = document.querySelector(".donut-percent");
  
    // Hae prosentti HTML-attribuutista
    const percent = parseInt(donutChart.getAttribute("data-percent"));
  
    // Laske kulma asteina
    const angle = (360 * percent) / 100;
  
    // Aseta kulma donitsimittariin
    donutChart.style.transform = `rotate(${angle}deg)`;
  
    // Aseta prosenttiluku tekstikenttään
    donutText.innerText = `${percent}%`;
  });
  
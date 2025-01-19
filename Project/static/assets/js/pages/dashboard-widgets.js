// Widget Stacked Column Chart
const widgetStackedColumn = {
  series: [
    {
      name: "PRODUCT A",
      data: [150, 180, 240, 270, 200, 180, 200, 220, 200, 230, 290, 200],
    },
    {
      name: "PRODUCT B",
      data: [200, 180, 240, 270, 200, 180, 200, 220, 200, 230, 290, 200],
    },
    {
      name: "PRODUCT C",
      data: [150, 180, 240, 270, 200, 180, 200, 220, 200, 230, 290, 200],
    },
  ],
  chart: {
    type: "bar",
    height: 260,
    stacked: true,
    toolbar: {
      show: false,
    },
    zoom: {
      enabled: false,
    },
  },
  dataLabels: {
    enabled: false,
  },
  colors: ["#FFA305", "#66CC33", "#795DED"],
  legend: {
    show: false,
  },
  responsive: [
    {
      breakpoint: 480,
      options: {
        legend: {
          position: "bottom",
          offsetX: -10,
          offsetY: 0,
        },
      },
    },
  ],
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: "30%",
      endingShape: "rounded",
    },
  },
  grid: {
    borderColor: "#EEE",
  },
  xaxis: {
    axisTicks: {
      show: false,
    },
    categories: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "June",
      "July",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
  },
  yaxis: {
    min: 100,
    max: 1000,
    tickAmount: 5,
    labels: {
      formatter: (val) => val,
    },
  },
  fill: {
    opacity: 1,
  },
};

// Initialize the charts
const widgetStackedChart = new ApexCharts(
  document.querySelector("#widgetStackedColumn"),
  widgetStackedColumn
);
widgetStackedChart.render();

// Widget Pie Donut Chart
const widgetPieDonut = {
  series: [20, 20, 20, 20],
  chart: {
    width: "100%",
    height: "100%",
    type: "donut",
  },
  legend: {
    show: false,
  },
  colors: ["#D9FF47", "#A57CFD", "#EAE1FF", "#FFEEE7"],
  dataLabels: {
    enabled: false,
  },
  stroke: {
    show: false,
  },
  plotOptions: {
    pie: {
      donut: {
        size: "48%",
        background: "#fff",
        labels: {
          show: true,
          name: {
            show: false,
          },
          value: {
            show: true,
            fontSize: "16px",
            fontWeight: 700,
            color: "#251F47",
            offsetY: 7,
            formatter: function (val) {
              return val + "%";
            },
          },
          total: {
            show: true,
            formatter: function (w) {
              const seriesTotal = w.globals.seriesTotals.reduce(
                (a, b) => a + b,
                0
              );
              return seriesTotal + "%";
            },
          },
        },
      },
    },
  },
  responsive: [
    {
      breakpoint: 375,
      options: {
        chart: {
          width: "100%",
          height: "100%",
        },
        legend: {
          show: false,
        },
      },
    },
  ],
};

// Initialize the Pie Donut Charts
const pieDonutchart1 = new ApexCharts(
  document.querySelector("#pieDonutchart1"),
  widgetPieDonut
);
pieDonutchart1.render();

const pieDonutchart2 = new ApexCharts(
  document.querySelector("#pieDonutchart2"),
  widgetPieDonut
);
pieDonutchart2.render();

const pieDonutchart3 = new ApexCharts(
  document.querySelector("#pieDonutchart3"),
  widgetPieDonut
);
pieDonutchart3.render();

// Widget Spline Area Chart
const doubleSplineArea = {
  series: [
    {
      name: "series1",
      data: [10, 25, 15, 30, 20, 40, 30, 60, 70, 50, 90, 100],
    },
    {
      name: "series2",
      data: [10, 20, 40, 20, 50, 40, 60, 40, 50, 80, 60, 90],
    },
  ],
  chart: {
    height: 300,
    type: "area",
    toolbar: {
      show: false,
    },
    zoom: {
      enabled: false,
    },
  },
  dataLabels: {
    enabled: false,
  },
  legend: {
    show: false,
  },
  fill: {
    opacity: 0,
    type: "solid",
  },
  grid: {
    borderColor: "#EEE",
  },
  stroke: {
    show: true,
    curve: "smooth",
    lineCap: "butt",
    colors: ["#9C84F4", "#F9D34D"],
    width: 2.5,
    dashArray: 0,
  },
  xaxis: {
    axisTicks: {
      show: false,
    },
    categories: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "June",
      "July",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
  },
  yaxis: {
    min: 10,
    max: 100,
    tickAmount: 5,
    labels: {
      formatter: (val) => val + "%",
    },
  },
  tooltip: {
    y: {
      formatter: (val) => {
        return val + "%";
      },
    },
  },
};

// Initialize the Spline Area Charts
const doubleAreaChart = new ApexCharts(
  document.querySelector("#doubleSplineArea"),
  doubleSplineArea
);
doubleAreaChart.render();

// Widget Single Spline Area Chart
const widgetSplineArea = {
  series: [
    {
      name: "series1",
      data: [10, 25, 20, 30, 20, 40, 30, 50, 40, 70, 60, 100],
    },
  ],
  chart: {
    height: 300,
    type: "area",
    toolbar: {
      show: false,
    },
    zoom: {
      enabled: false,
    },
  },
  dataLabels: {
    enabled: false,
  },
  legend: {
    show: false,
  },
  fill: {
    type: "gradient",
    gradient: {
      shadeIntensity: 1,
      opacityFrom: 0.2,
      opacityTo: 0.6,
    },
  },
  grid: {
    borderColor: "#EEE",
  },
  stroke: {
    show: true,
    curve: "smooth",
    lineCap: "butt",
    colors: ["#23C965"],
    width: 2.5,
    dashArray: 0,
  },
  xaxis: {
    axisTicks: {
      show: false,
    },
    categories: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "June",
      "July",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
  },
  yaxis: {
    min: 10,
    max: 100,
    tickAmount: 5,
    labels: {
      formatter: (val) => val + "%",
    },
  },
  tooltip: {
    x: {
      show: true,
    },
    y: {
      format: "dd MMM",
      formatter: (val) => {
        return val + "%";
      },
    },
  },
};

// Initialize the Spline Area Charts
const widgetAreaChart = new ApexCharts(
  document.querySelector("#widgetSplineArea"),
  widgetSplineArea
);
widgetAreaChart.render();

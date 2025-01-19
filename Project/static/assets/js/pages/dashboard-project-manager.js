// CALENDER
document.addEventListener("DOMContentLoaded", () => {
  const inlineCalender = document.querySelector("#inline_calendar_input");
  inlineCalender.flatpickr({
    inline: true,
    mode: "range",
  });
  console.log(inlineCalender.value);
  inlineCalender.nextElementSibling.style.boxShadow = "none";
  inlineCalender.nextElementSibling.style.backgroundColor = "transparent";
});

// PROJECT STATUS PIE CHART
const projectStatusOptions = {
  series: [70, 20, 10],
  chart: {
    type: "pie",
    height: 230,
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  responsive: [
    {
      breakpoint: 1800,
      options: {
        chart: {
          height: 180,
        },
      },
    },
    {
      breakpoint: 1536,
      options: {
        chart: {
          height: 230,
        },
      },
    },
  ],

  labels: ["Active Project", "Pending Project", "Review Project"],
  colors: ["#795DED", "#B39EF9", "#F2ECFE"],
  legend: {
    show: false,
    position: "bottom",
    offsetY: 0,
    markers: {
      width: 7,
      height: 7,
      radius: 99,
      offsetX: -3,
      offsetY: -1,
    },
    itemMargin: {
      horizontal: 10,
    },
  },
  theme: {
    monochrome: {
      enabled: false,
    },
  },
  plotOptions: {
    pie: {
      expandOnClick: false,
      size: 1000,
    },
  },
  stroke: {
    show: false,
  },
  dataLabels: {
    enabled: false,
  },
};

const projectStatus = new ApexCharts(
  document.querySelector("#projectStatus"),
  projectStatusOptions
);
projectStatus.render();

// TOTAL TASK SEMI DONUT CHART
const totalTaskOptions = {
  series: [80, 90, 100],
  chart: {
    type: "radialBar",
    width: "100%",
    height: 300,
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  responsive: [
    {
      breakpoint: 1800,
      options: {
        chart: {
          height: 200,
        },
      },
    },
    {
      breakpoint: 1536,
      options: {
        chart: {
          height: 300,
        },
      },
    },
  ],
  colors: ["#795DED", "#B39EF9", "#F2ECFE"],
  plotOptions: {
    radialBar: {
      inverseOrder: true,
      startAngle: -90,
      endAngle: 90,
      track: {
        startAngle: -90,
        endAngle: 90,
        background: "transparent",
        margin: -0.5,
      },
      dataLabels: {
        value: {
          fontFamily: "inherit",
          fontSize: "12px",
          color: "#555",
          offsetY: -30,
          formatter: function (val) {
            return val + "%";
          },
        },
        name: {
          fontFamily: "inherit",
          fontSize: "12px",
          fontWeight: 400,
          color: "#555",
          offsetY: 5,
        },
        total: {
          show: true,
          label: "Average Task",
          fontFamily: "inherit",
          fontSize: "12px",
          color: "#555",
          fontWeight: 400,
          formatter: function (w) {
            return (
              w.globals.seriesTotals.reduce((a, b) => {
                return a + b;
              }, 0) /
                w.globals.series.length +
              "%"
            );
          },
        },
      },
    },
  },
  stroke: {
    lineCap: "round",
  },
  labels: ["Active task", "Pending task", "Reivew task"],
};

const totalTask = new ApexCharts(
  document.querySelector("#total-task-chart"),
  totalTaskOptions
);
totalTask.render();

// FINANCE STATUS CHART
const financeStatusOptions = {
  series: [90, 80, 70],
  chart: {
    type: "radialBar",
    height: 230,
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  responsive: [
    {
      breakpoint: 1800,
      options: {
        chart: {
          height: 180,
        },
      },
    },
    {
      breakpoint: 1536,
      options: {
        chart: {
          height: 230,
        },
      },
    },
  ],
  colors: ["#795DED", "#66CC33", "#FFA305"],
  plotOptions: {
    radialBar: {
      track: {
        background: ["#795DED", "#66CC33", "#FFA305"],
        opacity: 0.1,
        margin: 6,
      },
      dataLabels: {
        showOn: "always",
        name: {
          fontSize: "14px",
          fontWeight: 500,
          offsetY: -2,
          show: true,
        },
        value: {
          show: true,
          fontSize: "12px",
          color: "#555",
          offsetY: 2,
          formatter: function (val) {
            return val + "%";
          },
        },
      },
      barLabels: {
        enabled: true,
      },
    },
  },
  stroke: {
    lineCap: "round",
  },
  labels: ["Average", "Active", "Lowest"],
};

var financeStatusChart = new ApexCharts(
  document.querySelector("#finance-status-chart"),
  financeStatusOptions
);
financeStatusChart.render();

// TASK OVERVIEW CHART
const taskOverviewOptions = {
  series: [
    {
      name: "Today",
      data: [25, 15, 25, 10, 8, 25, 10, 15, 5, 10],
    },
  ],
  chart: {
    type: "bar",
    width: "100%",
    height: 400,
    toolbar: {
      show: false,
    },
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  plotOptions: {
    bar: {
      horizontal: false,
      borderRadius: 15,
      columnWidth: 30,
      colors: {
        backgroundBarColors: ["#F9F6FF"],
        backgroundBarRadius: 10,
      },
    },
  },
  responsive: [
    {
      breakpoint: 640,
      options: {
        plotOptions: {
          bar: {
            borderRadius: 5,
            columnWidth: 10,
          },
        },
      },
    },
  ],
  dataLabels: {
    enabled: false,
  },
  grid: {
    borderColor: "#f3f3f3",
  },
  stroke: {
    show: false,
  },
  yaxis: {
    min: 0,
    max: 30,
    stepSize: 5,
    tickAmount: 6,
    labels: {
      formatter: (val) => val + "k",
    },
  },
  xaxis: {
    type: "datetime",
    categories: [
      "01/01/2024 GMT",
      "01/02/2024 GMT",
      "01/03/2024 GMT",
      "01/04/2024 GMT",
      "01/05/2024 GMT",
      "01/06/2024 GMT",
      "01/07/2024 GMT",
      "01/08/2024 GMT",
      "01/09/2024 GMT",
      "01/10/2024 GMT",
    ],
  },
  fill: {
    colors: ["#795DED"],
    opacity: 1,
  },
  tooltip: {
    y: {
      formatter: (val) => {
        return val + "k";
      },
    },
  },
};

const taskOverviewChart = new ApexCharts(
  document.querySelector("#taskOverview"),
  taskOverviewOptions
);
taskOverviewChart.render();

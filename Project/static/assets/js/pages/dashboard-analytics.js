// Total Revenue
const conversionOneOptions = {
  series: [
    {
      name: "Revenue",
      data: [5, 30, 10, 25, 11, 30, 15, 28, 33],
    },
  ],
  chart: {
    type: "area",
    height: 70,
    sparkline: {
      enabled: true,
    },
    zoom: {
      autoScaleYaxis: true,
    },
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  colors: ["#795DED"],
  stroke: {
    width: 1.2,
    curve: "smooth",
  },
  tooltip: {
    enabled: true,
    x: {
      show: false,
    },
    y: {
      title: {
        formatter: function (seriesName) {
          return "";
        },
      },
    },
    marker: {
      show: false,
    },
  },
  fill: {
    type: "gradient",
    gradient: {
      opacityFrom: 0.5,
      opacityTo: 0.2,
      stops: [0, 60],
    },
  },
};
const conversionOneChart = new ApexCharts(
  document.querySelector("#conversionOne"),
  conversionOneOptions
);
conversionOneChart.render();

// Total Enrollment
var conversionTwoOptions = {
  series: [
    {
      name: "Enroll",
      data: [5, 30, 10, 25, 11, 30, 15, 28, 33],
    },
  ],
  chart: {
    type: "area",
    height: 70,
    sparkline: {
      enabled: true,
    },
    zoom: {
      autoScaleYaxis: true,
    },
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  colors: ["#FF4626"],
  stroke: {
    width: 1.2,
    curve: "smooth",
  },
  tooltip: {
    enabled: true,
    x: {
      show: false,
    },
    y: {
      title: {
        formatter: function (seriesName) {
          return "";
        },
      },
    },
    marker: {
      show: false,
    },
  },
  fill: {
    type: "gradient",
    gradient: {
      opacityFrom: 0.5,
      opacityTo: 0.2,
      stops: [0, 60],
    },
  },
};
var conversionTwoChart = new ApexCharts(
  document.querySelector("#conversionTwo"),
  conversionTwoOptions
);
conversionTwoChart.render();

// Total Courses
var conversionThreeOptions = {
  series: [
    {
      name: "Course",
      data: [5, 30, 10, 25, 11, 30, 15, 28, 33],
    },
  ],
  chart: {
    type: "area",
    height: 70,
    sparkline: {
      enabled: true,
    },
    zoom: {
      autoScaleYaxis: true,
    },
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  colors: ["#795DED"],
  stroke: {
    width: 1.2,
    curve: "smooth",
  },
  tooltip: {
    enabled: true,
    x: {
      show: false,
    },
    y: {
      title: {
        formatter: function (seriesName) {
          return "";
        },
      },
    },
    marker: {
      show: false,
    },
  },
  fill: {
    type: "gradient",
    gradient: {
      opacityFrom: 0.5,
      opacityTo: 0.2,
      stops: [0, 60],
    },
  },
};
var conversionThreeChart = new ApexCharts(
  document.querySelector("#conversionThree"),
  conversionThreeOptions
);
conversionThreeChart.render();

// Analytic Overview Chart
const analyticOverviewOptions = {
  chart: {
    height: 400,
    width: "100%",
    stacked: true,
    toolbar: {
      show: false,
    },
    theme: {
      mode: "dark", // enables dark mode in ApexCharts
    },
    zoom: {
      autoScaleYaxis: true,
    },
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  series: [
    {
      name: "Total Visitor",
      type: "area",
      color: "#F2ECFE",
      data: [
        {
          x: "01-01-2023 GMT",
          y: 3.4,
        },
        {
          x: "01-05-2023 GMT",
          y: 7.0,
        },
        {
          x: "01-10-2023 GMT",
          y: 3.1,
        },
        {
          x: "01-15-2023 GMT",
          y: 6.0,
        },
        {
          x: "01-20-2023 GMT",
          y: 4.0,
        },
        {
          x: "01-25-2023 GMT",
          y: 8.0,
        },
        {
          x: "01-30-2023 GMT",
          y: 6.0,
        },
      ],
      zIndex: 30.0,
    },
    {
      name: "Impression",
      type: "line",
      data: [
        {
          x: "01-01-2023 GMT",
          y: 0,
        },
        {
          x: "01-05-2023 GMT",
          y: 6.0,
        },
        {
          x: "01-10-2023 GMT",
          y: 2.1,
        },
        {
          x: "01-15-2023 GMT",
          y: 5.0,
        },
        {
          x: "01-20-2023 GMT",
          y: 3.0,
        },
        {
          x: "01-25-2023 GMT",
          y: 7.0,
        },
        {
          x: "01-30-2023 GMT",
          y: 5.0,
        },
      ],
      zIndex: 10.0,
    },
  ],
  xaxis: {
    type: "datetime",
    min: new Date("01 Jan 2023").getTime(),
  },
  yaxis: {
    min: 0.5,
    max: 10.0,
    tickAmount: 2,
    decimalsInFloat: false,
    labels: {
      formatter: (val) => val + "k",
    },
  },
  grid: {
    borderColor: "#EEE",
  },
  dataLabels: {
    enabled: false,
  },
  stroke: {
    show: true,
    curve: "smooth",
    colors: ["none", "#795DED"],
    width: 2,
  },
  markers: {
    size: 5,
    colors: ["transparent", "#795DED"],
    strokeColors: "transparent",
    hover: {
      sizeOffset: 0,
    },
  },
  legend: {
    position: "top",
    horizontalAlign: "left",
    offsetY: 0,
    markers: {
      width: 7,
      height: 7,
      radius: 99,
      fillColors: ["#F2ECFE", "#795DED"],
      offsetX: -3,
      offsetY: -1,
    },
    itemMargin: {
      horizontal: 10,
    },
  },
  tooltip: {
    y: {
      formatter: (val) => {
        return val + "k";
      },
      title: {
        formatter: (sn) => "",
      },
    },
    marker: {
      show: false,
    },
  },
};

const analyticOverviewChart = new ApexCharts(
  document.querySelector("#analytic-overview-chart"),
  analyticOverviewOptions
);
analyticOverviewChart.render();

// Active User Chart
var activeUserOptions = {
  chart: {
    height: "auto",
    // stacked: true,
    toolbar: {
      show: false,
    },
    zoom: {
      autoScaleYaxis: true,
    },
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  series: [
    {
      name: "Desktop",
      type: "area",
      color: "#F2ECFE",
      data: [
        {
          x: "01-01-2024 GMT",
          y: 0,
        },
        {
          x: "01-05-2024 GMT",
          y: 25,
        },
        {
          x: "01-10-2024 GMT",
          y: 50,
        },
        {
          x: "01-15-2024 GMT",
          y: 70,
        },
        {
          x: "01-20-2024 GMT",
          y: 90,
        },
      ],
    },
    {
      name: "Mobile",
      type: "area",
      color: "#B39EF9",
      data: [
        {
          x: "01-01-2024 GMT",
          y: 0,
        },
        {
          x: "01-05-2024 GMT",
          y: 20,
        },
        {
          x: "01-10-2024 GMT",
          y: 30,
        },
        {
          x: "01-15-2024 GMT",
          y: 40,
        },
        {
          x: "01-20-2024 GMT",
          y: 50,
        },
      ],
    },
    {
      name: "Tablet",
      type: "area",
      color: "#795DED",
      data: [
        {
          x: "01-01-2024 GMT",
          y: 0,
        },
        {
          x: "01-05-2024 GMT",
          y: 10,
        },
        {
          x: "01-10-2024 GMT",
          y: 15,
        },
        {
          x: "01-15-2024 GMT",
          y: 20,
        },
        {
          x: "01-20-2024 GMT",
          y: 25,
        },
      ],
    },
  ],
  xaxis: {
    type: "datetime",
    min: new Date("01 Jan 2024").getTime(),
  },
  yaxis: {
    min: 0,
    max: 100,
    tickAmount: 4,
    decimalsInFloat: false,
    opposite: true,
    labels: {
      formatter: (val) => val + "%",
    },
  },
  grid: {
    show: false,
  },
  dataLabels: {
    enabled: false,
  },
  stroke: {
    show: false,
    curve: "straight",
  },
  legend: {
    show: true,
    formatter: function (seriesName, opts) {
      return [
        seriesName,
        opts.w.globals.series[opts.seriesIndex].slice(-1) + "%",
      ];
    },
    position: "top",
    horizontalAlign: "left",
    offsetY: 0,
    markers: {
      width: 7,
      height: 7,
      radius: 99,
      offsetX: -3,
      offsetY: -1,
    },
    itemMargin: {
      horizontal: 5,
    },
  },
  tooltip: {
    y: {
      formatter: (val) => {
        return val + "%";
      },
      title: {
        formatter: (sn) => "",
      },
    },
    marker: {
      show: false,
    },
  },
};

const activeUserChart = new ApexCharts(
  document.querySelector("#active-user-chart"),
  activeUserOptions
);
activeUserChart.render();

// Browser Session Chart
const browserSessionOptions = {
  series: [55, 40, 5],
  chart: {
    width: "100%",
    height: "auto",
    type: "pie",
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  labels: ["Chrome", "Mozilla", "Other"],
  colors: ["#795DED", "#B39EF9", "#F2ECFE"],
  legend: {
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
      dataLabels: {
        offset: -10,
        minAngleToShowLabel: 10,
      },
    },
  },
  stroke: {
    show: false,
  },
};

const browserSessionChart = new ApexCharts(
  document.querySelector("#browser-session-chart"),
  browserSessionOptions
);
browserSessionChart.render();

// Views Per Minutes Chart
var options = {
  chart: {
    height: 150,
    type: "bar",
    toolbar: {
      show: false,
    },
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  series: [
    {
      name: "views per minute",
      data: [55, 30, 70, 45, 25, 30, 50, 82, 30],
      color: "#795DED",
    },
  ],
  grid: {
    show: false,
  },
  plotOptions: {
    bar: {
      borderRadius: 10,
      columnWidth: "80%",
      barHeight: "100%",
      dataLabels: {
        position: "top",
      },
      colors: {
        backgroundBarColors: ["#F2ECFE"],
        backgroundBarRadius: 10,
      },
    },
  },
  dataLabels: {
    enabled: false,
    offsetY: "100%",
    style: {
      fontSize: "12px",
      colors: ["#999999"],
    },
  },
  xaxis: {
    categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"],
    labels: {
      show: false,
    },
    axisBorder: {
      show: false,
    },
    axisTicks: {
      show: false,
    },
  },
  yaxis: {},
  yaxis: {
    min: 0,
    max: 100,
    tickAmount: 5,
    decimalsInFloat: false,
    labels: {
      show: false,
      formatter: (val) => val + "k",
    },
  },
  tooltip: {
    y: {
      formatter: (val) => {
        return val + "k";
      },
      title: {
        formatter: (sn) => "",
      },
    },
    marker: {
      show: false,
    },
  },
};

var chart = new ApexCharts(
  document.querySelector("#views-browser-perminute-chart"),
  options
);
chart.render();

// Source Breakdown Chart
const SourceBreakdownChartOptions = {
  series: [55, 40, 5],
  chart: {
    width: "100%",
    height: "auto",
    type: "pie",
    events: {
      mounted: (chart) => {
        chart.windowResizeHandler();
      },
    },
  },
  labels: ["Reddit", "Quora", "Youtube"],
  colors: ["#795DED", "#B39EF9", "#a58bd9"],
  legend: {
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
      dataLabels: {
        offset: -10,
        minAngleToShowLabel: 10,
      },
    },
  },
  stroke: {
    show: false,
  },
};

const SourceBreakdownChart = new ApexCharts(
  document.querySelector("#source-breakdown-chart"),
  SourceBreakdownChartOptions
);
SourceBreakdownChart.render();

// Users By Country
const markers = [
  {
    name: "Russia",
    coords: [55.75, 37.61],
  },
  {
    name: "Canada",
    coords: [56.1304, -106.3468],
  },
  {
    name: "Singapore",
    coords: [1.3, 103.8],
  },
];
new jsVectorMap({
  selector: "#customer-country-chart",
  map: "world_merc",
  markersSelectable: true,
  // zoomOnScroll: false,
  zoomButtons: false,
  labels: {
    markers: {
      render: function (marker) {
        return marker.name;
      },
    },
  },
  markers: markers,
  markerStyle: {
    initial: {
      image: "assets/images/icons/location.svg",
    },
  },
  regionStyle: {
    initial: {
      fill: "#F4ECFF",
      stroke: "#B39EF9",
      strokeWidth: 1,
      fillOpacity: 1,
    },
  },
  onMarkerSelected(index, isSelected, selectedMarkers) {
    console.log(index, isSelected, selectedMarkers);
  },
});
